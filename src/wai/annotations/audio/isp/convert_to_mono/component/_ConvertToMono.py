import os
import librosa
import soundfile
from io import BytesIO

from wai.common.cli.options import TypedOption
from wai.annotations.core.component import ProcessorComponent
from wai.annotations.core.stream import ThenFunction, DoneFunction
from wai.annotations.core.stream.util import RequiresNoFinalisation
from wai.annotations.domain.audio import AudioInstance, Audio
from wai.annotations.audio.core import SUPPORTED_AUDIO_EXT


class ConvertToMono(
    RequiresNoFinalisation,
    ProcessorComponent[AudioInstance, AudioInstance]
):
    """
    Stream processor to turn audio into mono.
    """

    sample_rate: int = TypedOption(
        "-s", "--sample-rate",
        type=int,
        default=22050,
        help="the sample rate to use for the audio data."
    )

    def process_element(
            self,
            element: AudioInstance,
            then: ThenFunction[AudioInstance],
            done: DoneFunction
    ):
        ext = os.path.splitext(element.data.filename.lower())[1]
        if ext in SUPPORTED_AUDIO_EXT:
            data, sample_rate = librosa.load(BytesIO(element.data.data), sr=self.sample_rate)
            data = librosa.to_mono(data)
            bytes = BytesIO()
            soundfile.write(bytes, data, sample_rate, format="WAV")
            bytes.seek(0)
            audio = Audio(element.data.filename, bytes.read())
            then(element.__class__(audio, element.annotations))
        else:
            raise Exception("Unknown audio file format (%s): %s" % (element.data.filename, ext))
