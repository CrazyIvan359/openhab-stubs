import java.lang
import java.util
import org.openhab.core.binding
import org.openhab.core.i18n
import org.osgi.framework


class BindingI18nLocalizationService(java.lang.Object):
    """
    Java class 'org.openhab.core.binding.i18n.BindingI18nLocalizationService'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * BindingI18nLocalizationService(org.openhab.core.i18n.TranslationProvider)
    
    """
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    def createLocalizedBindingInfo(self, bundle: org.osgi.framework.Bundle, bindingInfo: org.openhab.core.binding.BindingInfo, locale: java.util.Locale) -> org.openhab.core.binding.BindingInfo: ...
