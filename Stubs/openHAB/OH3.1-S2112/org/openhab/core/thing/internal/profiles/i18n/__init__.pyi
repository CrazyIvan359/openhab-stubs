import java.lang
import java.util
import org.openhab.core.i18n
import org.openhab.core.thing.profiles
import org.osgi.framework


class ProfileI18nUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.internal.profiles.i18n.ProfileI18nUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ProfileI18nUtil(org.openhab.core.i18n.TranslationProvider)
    
    """
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    def getProfileLabel(self, bundle: org.osgi.framework.Bundle, profileTypeUID: org.openhab.core.thing.profiles.ProfileTypeUID, defaultLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
