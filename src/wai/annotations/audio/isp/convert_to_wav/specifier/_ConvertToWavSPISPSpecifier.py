from typing import Type, Tuple

from wai.annotations.core.component import ProcessorComponent
from wai.annotations.core.domain import DomainSpecifier
from wai.annotations.core.specifier import ProcessorStageSpecifier


class ConvertToWavSPISPSpecifier(ProcessorStageSpecifier):
    """
    Converts mp3/flac/ogg to wav for audio classification.
    """
    @classmethod
    def description(cls) -> str:
        return "Converts mp3/flac/ogg to wav for audio classification."

    @classmethod
    def domain_transfer_function(
            cls,
            input_domain: Type[DomainSpecifier]
    ) -> Type[DomainSpecifier]:
        from wai.annotations.domain.audio.speech import SpeechDomainSpecifier
        if input_domain is SpeechDomainSpecifier:
            return input_domain
        else:
            raise Exception(
                f"ConvertToWavSPISPSpecifier only handles the following domains: "
                f"{SpeechDomainSpecifier.name()}"
            )

    @classmethod
    def components(cls) -> Tuple[Type[ProcessorComponent]]:
        from wai.annotations.audio.isp.convert_to_wav.component import ConvertToWav
        return ConvertToWav,
