import librosa

from wai.common.cli.options import TypedOption
from wai.annotations.core.component import ProcessorComponent
from wai.annotations.core.stream import ThenFunction, DoneFunction
from wai.annotations.core.stream.util import RequiresNoFinalisation
from wai.annotations.domain.audio import AudioInstance, Audio, AudioFormat


class ResampleAudio(
    RequiresNoFinalisation,
    ProcessorComponent[AudioInstance, AudioInstance]
):
    """
    Stream processor to resample audio.
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
        data, sample_rate = element.data.audio_data
        data = librosa.resample(data, orig_sr=sample_rate, target_sr=self.sample_rate)
        audio = Audio(element.data.filename, format=AudioFormat.WAV, sample_rate=self.sample_rate, audio_data=(data, self.sample_rate))
        then(element.__class__(audio, element.annotations))
