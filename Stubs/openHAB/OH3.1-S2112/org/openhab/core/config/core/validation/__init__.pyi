import java.lang
import java.net
import java.util
import org.openhab.core.i18n
import org.osgi.framework
import typing


class ConfigDescriptionValidator(java.lang.Object):
    """
    public interface ConfigDescriptionValidator
    
        The :class:`~org.openhab.core.config.core.validation.ConfigDescriptionValidator` validates a given set of
        :class:`~org.openhab.core.config.core.Configuration` parameters against a given
        :class:`~org.openhab.core.config.core.ConfigDescription` URI. So it can be used as a static pre-validation to avoid that
        the configuration of an entity is updated with parameters which do not match with the declarations in the configuration
        description. If the validator detects one or more mismatches then a
        :class:`~org.openhab.core.config.core.validation.ConfigValidationException` is thrown.
    
    
    """
    def validate(self, configurationParameters: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]], configDescriptionURI: java.net.URI) -> None: ...

class ConfigValidationException(java.lang.RuntimeException):
    """
    Java class 'org.openhab.core.config.core.validation.ConfigValidationException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * ConfigValidationException(org.osgi.framework.Bundle, org.openhab.core.i18n.TranslationProvider, java.util.Collection)
    
    """
    def __init__(self, bundle: org.osgi.framework.Bundle, translationProvider: org.openhab.core.i18n.TranslationProvider, configValidationMessages: typing.Union[java.util.Collection['ConfigValidationMessage'], typing.Sequence['ConfigValidationMessage']]): ...
    @typing.overload
    def getValidationMessages(self) -> java.util.Map[java.lang.String, java.lang.String]: ...
    @typing.overload
    def getValidationMessages(self, locale: java.util.Locale) -> java.util.Map[java.lang.String, java.lang.String]: ...

class ConfigValidationMessage(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.validation.ConfigValidationMessage'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConfigValidationMessage(java.lang.String, java.lang.String, java.lang.String)
        * ConfigValidationMessage(java.lang.String, java.lang.String, java.lang.String, java.lang.Object[])
    
      Attributes:
        parameterName (java.lang.String): final field
        defaultMessage (java.lang.String): final field
        messageKey (java.lang.String): final field
        content ([Ljava.lang.Object;): final field
    
    """
    parameterName: java.lang.String = ...
    defaultMessage: java.lang.String = ...
    messageKey: java.lang.String = ...
    content: typing.List[typing.Any] = ...
    @typing.overload
    def __init__(self, parameterName: java.lang.String, defaultMessage: java.lang.String, messageKey: java.lang.String): ...
    @typing.overload
    def __init__(self, parameterName: java.lang.String, defaultMessage: java.lang.String, messageKey: java.lang.String, content: typing.List[typing.Any]): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
