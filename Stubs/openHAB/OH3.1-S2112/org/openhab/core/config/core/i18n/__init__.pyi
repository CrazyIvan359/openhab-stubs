import java.lang
import java.net
import java.util
import org.openhab.core.config.core
import org.openhab.core.i18n
import org.osgi.framework
import typing


class ConfigI18nLocalizationService(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.i18n.ConfigI18nLocalizationService'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConfigI18nLocalizationService(org.openhab.core.i18n.TranslationProvider)
    
    """
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    def getLocalizedConfigDescription(self, bundle: org.osgi.framework.Bundle, configDescription: org.openhab.core.config.core.ConfigDescription, locale: java.util.Locale) -> org.openhab.core.config.core.ConfigDescription: ...
    @typing.overload
    def getLocalizedConfigDescriptionGroup(self, bundle: org.osgi.framework.Bundle, configDescriptionURI: java.net.URI, group: org.openhab.core.config.core.ConfigDescriptionParameterGroup, locale: java.util.Locale) -> org.openhab.core.config.core.ConfigDescriptionParameterGroup: ...
    @typing.overload
    def getLocalizedConfigDescriptionGroup(self, bundle: org.osgi.framework.Bundle, configDescription: org.openhab.core.config.core.ConfigDescription, group: org.openhab.core.config.core.ConfigDescriptionParameterGroup, locale: java.util.Locale) -> org.openhab.core.config.core.ConfigDescriptionParameterGroup: ...
    @typing.overload
    def getLocalizedConfigDescriptionParameter(self, bundle: org.osgi.framework.Bundle, configDescriptionURI: java.net.URI, parameter: org.openhab.core.config.core.ConfigDescriptionParameter, locale: java.util.Locale) -> org.openhab.core.config.core.ConfigDescriptionParameter: ...
    @typing.overload
    def getLocalizedConfigDescriptionParameter(self, bundle: org.osgi.framework.Bundle, configDescription: org.openhab.core.config.core.ConfigDescription, parameter: org.openhab.core.config.core.ConfigDescriptionParameter, locale: java.util.Locale) -> org.openhab.core.config.core.ConfigDescriptionParameter: ...
    def getLocalizedOptions(self, originalOptions: java.util.List[org.openhab.core.config.core.ParameterOption], bundle: org.osgi.framework.Bundle, configDescriptionURI: java.net.URI, parameterName: java.lang.String, locale: java.util.Locale) -> java.util.List[org.openhab.core.config.core.ParameterOption]: ...
