import librosa

from wai.common.cli.options import TypedOption, FlagOption
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

    verbose: bool = FlagOption(
        "-v", "--verbose",
        help="whether to output some debugging output"
    )

    def process_element(
            self,
            element: AudioInstance,
            then: ThenFunction[AudioInstance],
            done: DoneFunction
    ):
        data, sample_rate = element.data.audio_data
        if self.verbose:
            self.logger.info("before resample: %s" % str(data.shape))
        data = librosa.resample(data, orig_sr=sample_rate, target_sr=self.sample_rate)
        if self.verbose:
            self.logger.info("after resample: %s" % str(data.shape))
        audio = Audio(element.data.filename, format=AudioFormat.WAV, sample_rate=self.sample_rate, audio_data=(data, self.sample_rate))
        then(element.__class__(audio, element.annotations))
