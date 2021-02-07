import java.lang
import java.util
import org.openhab.core.automation
import org.openhab.core.automation.module.provider.i18n
import org.openhab.core.automation.template
import org.openhab.core.automation.type
import org.openhab.core.common.registry
import org.openhab.core.config.core.i18n
import org.openhab.core.i18n
import org.osgi.framework
import org.osgi.util.tracker
import typing


_AbstractResourceBundleProvider__E = typing.TypeVar('_AbstractResourceBundleProvider__E')  # <E>
class AbstractResourceBundleProvider(java.lang.Object, typing.Generic[_AbstractResourceBundleProvider__E]):
    """
    Java class 'org.openhab.core.automation.internal.provider.AbstractResourceBundleProvider'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * AbstractResourceBundleProvider(java.lang.String)
    
    """
    def __init__(self, path: java.lang.String): ...

_AutomationResourceBundlesEventQueue__E = typing.TypeVar('_AutomationResourceBundlesEventQueue__E')  # <E>
class AutomationResourceBundlesEventQueue(java.lang.Runnable, typing.Generic[_AutomationResourceBundlesEventQueue__E]):
    """
    Java class 'org.openhab.core.automation.internal.provider.AutomationResourceBundlesEventQueue'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.lang.Runnable
    
      Constructors:
        * AutomationResourceBundlesEventQueue(org.openhab.core.automation.internal.provider.AbstractResourceBundleProvider)
    
    """
    def __init__(self, provider: AbstractResourceBundleProvider[_AutomationResourceBundlesEventQueue__E]): ...
    def run(self) -> None: ...
    def stop(self) -> None: ...

class AutomationResourceBundlesTracker(org.osgi.util.tracker.BundleTrackerCustomizer[org.osgi.framework.Bundle]):
    """
    Java class 'org.openhab.core.automation.internal.provider.AutomationResourceBundlesTracker'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.osgi.util.tracker.BundleTrackerCustomizer
    
      Constructors:
        * AutomationResourceBundlesTracker()
    
    """
    def __init__(self): ...
    @typing.overload
    def addingBundle(self, bundle: org.osgi.framework.Bundle, bundleEvent: org.osgi.framework.BundleEvent) -> typing.Any: ...
    @typing.overload
    def addingBundle(self, bundle: org.osgi.framework.Bundle, event: org.osgi.framework.BundleEvent) -> org.osgi.framework.Bundle: ...
    @typing.overload
    def modifiedBundle(self, bundle: org.osgi.framework.Bundle, bundleEvent: org.osgi.framework.BundleEvent, object: typing.Any) -> None: ...
    @typing.overload
    def modifiedBundle(self, bundle: org.osgi.framework.Bundle, event: org.osgi.framework.BundleEvent, object: org.osgi.framework.Bundle) -> None: ...
    @typing.overload
    def removedBundle(self, bundle: org.osgi.framework.Bundle, bundleEvent: org.osgi.framework.BundleEvent, object: typing.Any) -> None: ...
    @typing.overload
    def removedBundle(self, bundle: org.osgi.framework.Bundle, event: org.osgi.framework.BundleEvent, object: org.osgi.framework.Bundle) -> None: ...

class HostFragmentMappingUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.internal.provider.HostFragmentMappingUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * HostFragmentMappingUtil()
    
    """
    def __init__(self): ...

class Vendor(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.internal.provider.Vendor'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Vendor(java.lang.String)
        * Vendor(java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, nameversion: java.lang.String): ...
    @typing.overload
    def __init__(self, name: java.lang.String, version: java.lang.String): ...
    def count(self) -> int: ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getVendorID(self) -> java.lang.String: ...
    def getVendorSymbolicName(self) -> java.lang.String: ...
    def getVendorVersion(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def setVendorVersion(self, version: java.lang.String) -> None: ...
    def toString(self) -> java.lang.String: ...

class ModuleTypeResourceBundleProvider(AbstractResourceBundleProvider[org.openhab.core.automation.type.ModuleType], org.openhab.core.automation.type.ModuleTypeProvider):
    """
    Java class 'org.openhab.core.automation.internal.provider.ModuleTypeResourceBundleProvider'
    
        Extends:
            org.openhab.core.automation.internal.provider.AbstractResourceBundleProvider
    
        Interfaces:
            org.openhab.core.automation.type.ModuleTypeProvider
    
      Constructors:
        * ModuleTypeResourceBundleProvider(org.openhab.core.automation.module.provider.i18n.ModuleTypeI18nService)
    
    """
    def __init__(self, moduleTypeI18nService: org.openhab.core.automation.module.provider.i18n.ModuleTypeI18nService): ...
    def addProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[org.openhab.core.automation.type.ModuleType]) -> None: ...
    def getAll(self) -> java.util.Collection[org.openhab.core.automation.type.ModuleType]: ...
    _getModuleType__T = typing.TypeVar('_getModuleType__T', bound=org.openhab.core.automation.type.ModuleType)  # <T>
    def getModuleType(self, UID: java.lang.String, locale: java.util.Locale) -> _getModuleType__T: ...
    def getModuleTypes(self, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.automation.type.ModuleType]: ...
    def removeProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[org.openhab.core.automation.type.ModuleType]) -> None: ...

class RuleResourceBundleImporter(AbstractResourceBundleProvider[org.openhab.core.automation.Rule]):
    """
    Java class 'org.openhab.core.automation.internal.provider.RuleResourceBundleImporter'
    
        Extends:
            org.openhab.core.automation.internal.provider.AbstractResourceBundleProvider
    
      Constructors:
        * RuleResourceBundleImporter()
    
    """
    def __init__(self): ...
    def deactivate(self) -> None: ...

class TemplateResourceBundleProvider(AbstractResourceBundleProvider[org.openhab.core.automation.template.RuleTemplate], org.openhab.core.automation.template.RuleTemplateProvider):
    """
    Java class 'org.openhab.core.automation.internal.provider.TemplateResourceBundleProvider'
    
        Extends:
            org.openhab.core.automation.internal.provider.AbstractResourceBundleProvider
    
        Interfaces:
            org.openhab.core.automation.template.RuleTemplateProvider
    
      Constructors:
        * TemplateResourceBundleProvider(org.openhab.core.config.core.i18n.ConfigI18nLocalizationService, org.openhab.core.i18n.TranslationProvider)
    
    """
    def __init__(self, configI18nService: org.openhab.core.config.core.i18n.ConfigI18nLocalizationService, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    def addProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[org.openhab.core.automation.template.RuleTemplate]) -> None: ...
    def getAll(self) -> java.util.Collection[org.openhab.core.automation.template.RuleTemplate]: ...
    @typing.overload
    def getTemplate(self, UID: java.lang.String, locale: java.util.Locale) -> org.openhab.core.automation.template.RuleTemplate: ...
    @typing.overload
    def getTemplate(self, string: java.lang.String, locale: java.util.Locale) -> org.openhab.core.automation.template.Template: ...
    def getTemplates(self, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.automation.template.RuleTemplate]: ...
    def removeProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[org.openhab.core.automation.template.RuleTemplate]) -> None: ...
