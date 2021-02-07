import java.lang
import java.net
import java.util
import org.openhab.core.config.core
import org.openhab.core.config.core.validation
import typing


class ConfigDescriptionParameterValidator(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.internal.validation.ConfigDescriptionParameterValidator'
    
    """
    def validate(self, parameter: org.openhab.core.config.core.ConfigDescriptionParameter, value: typing.Any) -> org.openhab.core.config.core.validation.ConfigValidationMessage: ...

class ConfigDescriptionParameterValidatorFactory(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.internal.validation.ConfigDescriptionParameterValidatorFactory'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def createMinMaxValidator(cls) -> ConfigDescriptionParameterValidator: ...
    @classmethod
    def createPatternValidator(cls) -> ConfigDescriptionParameterValidator: ...
    @classmethod
    def createRequiredValidator(cls) -> ConfigDescriptionParameterValidator: ...
    @classmethod
    def createTypeValidator(cls) -> ConfigDescriptionParameterValidator: ...

class ConfigDescriptionValidatorImpl(org.openhab.core.config.core.validation.ConfigDescriptionValidator):
    """
    Java class 'org.openhab.core.config.core.internal.validation.ConfigDescriptionValidatorImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.core.validation.ConfigDescriptionValid
            ator
    
      Constructors:
        * ConfigDescriptionValidatorImpl()
    
    """
    def __init__(self): ...
    def validate(self, configurationParameters: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]], configDescriptionURI: java.net.URI) -> None: ...
