import java.lang
import java.util
import org.openhab.core.i18n
import org.osgi.framework


class BindingI18nUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.binding.internal.i18n.BindingI18nUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * BindingI18nUtil(org.openhab.core.i18n.TranslationProvider)
    
    """
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    def getDescription(self, bundle: org.osgi.framework.Bundle, bindingId: java.lang.String, defaultDescription: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getName(self, bundle: org.osgi.framework.Bundle, bindingId: java.lang.String, defaultLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
