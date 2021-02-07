import java.lang
import java.net
import java.util
import org.openhab.core.config.core
import org.openhab.core.i18n
import org.osgi.framework


class ConfigDescriptionGroupI18nUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.internal.i18n.ConfigDescriptionGroupI18nUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConfigDescriptionGroupI18nUtil(org.openhab.core.i18n.TranslationProvider)
    
    """
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    def getGroupDescription(self, bundle: org.osgi.framework.Bundle, configDescriptionURI: java.net.URI, groupName: java.lang.String, defaultDescription: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getGroupLabel(self, bundle: org.osgi.framework.Bundle, configDescriptionURI: java.net.URI, groupName: java.lang.String, defaultLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...

class ConfigDescriptionI18nUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.internal.i18n.ConfigDescriptionI18nUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConfigDescriptionI18nUtil(org.openhab.core.i18n.TranslationProvider)
    
    """
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    def getParameterDescription(self, bundle: org.osgi.framework.Bundle, configDescriptionURI: java.net.URI, parameterName: java.lang.String, defaultDescription: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getParameterLabel(self, bundle: org.osgi.framework.Bundle, configDescriptionURI: java.net.URI, parameterName: java.lang.String, defaultLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getParameterOptionLabel(self, bundle: org.osgi.framework.Bundle, configDescriptionURI: java.net.URI, parameterName: java.lang.String, optionValue: java.lang.String, defaultOptionLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getParameterPattern(self, bundle: org.osgi.framework.Bundle, configDescriptionURI: java.net.URI, parameterName: java.lang.String, defaultPattern: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getParameterUnitLabel(self, bundle: org.osgi.framework.Bundle, configDescriptionURI: java.net.URI, parameterName: java.lang.String, unit: java.lang.String, defaultUnitLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...

class I18nConfigOptionsProvider(org.openhab.core.config.core.ConfigOptionProvider):
    """
    Java class 'org.openhab.core.config.core.internal.i18n.I18nConfigOptionsProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.core.ConfigOptionProvider
    
      Constructors:
        * I18nConfigOptionsProvider()
    
    """
    def __init__(self): ...
    def getParameterOptions(self, uri: java.net.URI, param: java.lang.String, context: java.lang.String, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.config.core.ParameterOption]: ...
