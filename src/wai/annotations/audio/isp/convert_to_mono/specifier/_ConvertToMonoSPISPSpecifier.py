from typing import Type, Tuple

from wai.annotations.core.component import ProcessorComponent
from wai.annotations.core.domain import DomainSpecifier
from wai.annotations.core.specifier import ProcessorStageSpecifier


class ConvertToMonoSPISPSpecifier(ProcessorStageSpecifier):
    """
    Converts audio files to mono (speech domain).
    """
    @classmethod
    def description(cls) -> str:
        return "Converts audio files to mono (speech domain)"

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
                f"ConvertToMonoSPISPSpecifier only handles the following domains: "
                f"{SpeechDomainSpecifier.name()}"
            )

    @classmethod
    def components(cls) -> Tuple[Type[ProcessorComponent]]:
        from wai.annotations.audio.isp.convert_to_mono.component import ConvertToMono
        return ConvertToMono,