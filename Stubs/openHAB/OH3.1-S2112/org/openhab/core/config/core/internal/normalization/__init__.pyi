import java.lang
import org.openhab.core.config.core
import typing


class Normalizer(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.internal.normalization.Normalizer'
    
    """
    def normalize(self, value: typing.Any) -> typing.Any: ...

class NormalizerFactory(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.internal.normalization.NormalizerFactory'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def getNormalizer(cls, configDescriptionParameter: org.openhab.core.config.core.ConfigDescriptionParameter) -> Normalizer: ...
