import java.lang
import java.util
import org.openhab.core.automation.type
import org.osgi.framework


class ModuleTypeI18nService(java.lang.Object):
    """
    @NonNullByDefault public interface ModuleTypeI18nService
    
        Interface for a service that offer i18n functionality
    
    
    """
    def getModuleTypePerLocale(self, defModuleType: org.openhab.core.automation.type.ModuleType, locale: java.util.Locale, bundle: org.osgi.framework.Bundle) -> org.openhab.core.automation.type.ModuleType: ...
