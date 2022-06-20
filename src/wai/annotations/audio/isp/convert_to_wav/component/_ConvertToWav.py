import os
import librosa
import soundfile
import tempfile
import time
from io import BytesIO

from wai.common.cli.options import TypedOption
from wai.annotations.core.component import ProcessorComponent
from wai.annotations.core.stream import ThenFunction, DoneFunction
from wai.annotations.core.stream.util import RequiresNoFinalisation
from wai.annotations.domain.audio import AudioInstance, Audio


class ConvertToWav(
    RequiresNoFinalisation,
    ProcessorComponent[AudioInstance, AudioInstance]
):
    """
    Stream processor which converts mp3/flac/ogg to wav.
    """

    sample_rate: int = TypedOption(
        "-s", "--sample-rate",
        type=int,
        default=22050,
        help="the sample rate to use for the WAV data."
    )

    def process_element(
            self,
            element: AudioInstance,
            then: ThenFunction[AudioInstance],
            done: DoneFunction
    ):
        ext = os.path.splitext(element.data.filename.lower())[1]
        filename_new = os.path.splitext(element.data.filename)[0] + ".wav"
        if ext == ".mp3":
            filename_tmp = os.path.join(tempfile.gettempdir(), "waiann-%d.mp3" % round(time.time()))
            with open(filename_tmp, "wb") as fp:
                fp.write(element.data.data)
                fp.close()
            data, sample_rate = librosa.load(filename_tmp, sr=self.sample_rate)
            bytes = BytesIO()
            soundfile.write(bytes, data, sample_rate, format="WAV")
            bytes.seek(0)
            audio = Audio(filename_new, bytes.read())
            then(element.__class__(audio, element.annotations))
        elif ext in [".flac", ".ogg"]:
            data, sample_rate = librosa.load(BytesIO(element.data.data), sr=self.sample_rate)
            bytes = BytesIO()
            soundfile.write(bytes, data, sample_rate, format="WAV")
            bytes.seek(0)
            audio = Audio(filename_new, bytes.read())
            then(element.__class__(audio, element.annotations))
        else:
            then(element)
