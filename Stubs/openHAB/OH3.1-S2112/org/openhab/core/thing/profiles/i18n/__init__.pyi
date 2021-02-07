import java.lang
import java.util
import org.openhab.core.i18n
import org.openhab.core.thing.profiles
import org.osgi.framework


class ProfileTypeI18nLocalizationService(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.profiles.i18n.ProfileTypeI18nLocalizationService'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ProfileTypeI18nLocalizationService(org.openhab.core.i18n.TranslationProvider)
    
    """
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    def createLocalizedProfileType(self, bundle: org.osgi.framework.Bundle, profileType: org.openhab.core.thing.profiles.ProfileType, locale: java.util.Locale) -> org.openhab.core.thing.profiles.ProfileType: ...
