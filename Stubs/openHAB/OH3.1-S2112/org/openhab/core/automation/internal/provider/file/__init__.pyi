import java.io
import java.lang
import java.util
import org.openhab.core.automation.parser
import org.openhab.core.automation.template
import org.openhab.core.automation.type
import org.openhab.core.common.registry
import org.openhab.core.service
import typing


_AbstractFileProvider__E = typing.TypeVar('_AbstractFileProvider__E')  # <E>
class AbstractFileProvider(org.openhab.core.common.registry.Provider[_AbstractFileProvider__E], typing.Generic[_AbstractFileProvider__E]):
    """
    Java class 'org.openhab.core.automation.internal.provider.file.AbstractFileProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.common.registry.Provider
    
      Constructors:
        * AbstractFileProvider(java.lang.String)
    
    """
    def __init__(self, root: java.lang.String): ...
    def activate(self, config: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def addParser(self, parser: org.openhab.core.automation.parser.Parser[_AbstractFileProvider__E], properties: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> None: ...
    def addProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[_AbstractFileProvider__E]) -> None: ...
    def deactivate(self) -> None: ...
    def importResources(self, file: java.io.File) -> None: ...
    def modified(self, config: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def removeParser(self, parser: org.openhab.core.automation.parser.Parser[_AbstractFileProvider__E], properties: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> None: ...
    def removeProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[_AbstractFileProvider__E]) -> None: ...
    def removeResources(self, file: java.io.File) -> None: ...

class AutomationWatchService(org.openhab.core.service.AbstractWatchService):
    """
    Java class 'org.openhab.core.automation.internal.provider.file.AutomationWatchService'
    
        Extends:
            org.openhab.core.service.AbstractWatchService
    
      Constructors:
        * AutomationWatchService(org.openhab.core.automation.internal.provider.file.AbstractFileProvider, java.lang.String)
    
    """
    def __init__(self, provider: AbstractFileProvider, watchingDir: java.lang.String): ...

class WatchServiceUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.internal.provider.file.WatchServiceUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * WatchServiceUtil()
    
    """
    def __init__(self): ...
    @classmethod
    def deactivateWatchService(cls, watchingDir: java.lang.String, provider: AbstractFileProvider) -> None: ...
    @classmethod
    def initializeWatchService(cls, watchingDir: java.lang.String, provider: AbstractFileProvider) -> None: ...

class ModuleTypeFileProvider(AbstractFileProvider[org.openhab.core.automation.type.ModuleType], org.openhab.core.automation.type.ModuleTypeProvider):
    """
    Java class 'org.openhab.core.automation.internal.provider.file.ModuleTypeFileProvider'
    
        Extends:
            org.openhab.core.automation.internal.provider.file.AbstractFileProvider
    
        Interfaces:
            org.openhab.core.automation.type.ModuleTypeProvider
    
      Constructors:
        * ModuleTypeFileProvider()
    
    """
    def __init__(self): ...
    def getAll(self) -> java.util.Collection[org.openhab.core.automation.type.ModuleType]: ...
    _getModuleType__T = typing.TypeVar('_getModuleType__T', bound=org.openhab.core.automation.type.ModuleType)  # <T>
    def getModuleType(self, UID: java.lang.String, locale: java.util.Locale) -> _getModuleType__T: ...
    _getModuleTypes__T = typing.TypeVar('_getModuleTypes__T', bound=org.openhab.core.automation.type.ModuleType)  # <T>
    def getModuleTypes(self, locale: java.util.Locale) -> java.util.Collection[_getModuleTypes__T]: ...

class TemplateFileProvider(AbstractFileProvider[org.openhab.core.automation.template.RuleTemplate], org.openhab.core.automation.template.RuleTemplateProvider):
    """
    Java class 'org.openhab.core.automation.internal.provider.file.TemplateFileProvider'
    
        Extends:
            org.openhab.core.automation.internal.provider.file.AbstractFileProvider
    
        Interfaces:
            org.openhab.core.automation.template.RuleTemplateProvider
    
      Constructors:
        * TemplateFileProvider()
    
    """
    def __init__(self): ...
    def getAll(self) -> java.util.Collection[org.openhab.core.automation.template.RuleTemplate]: ...
    @typing.overload
    def getTemplate(self, UID: java.lang.String, locale: java.util.Locale) -> org.openhab.core.automation.template.RuleTemplate: ...
    @typing.overload
    def getTemplate(self, string: java.lang.String, locale: java.util.Locale) -> org.openhab.core.automation.template.Template: ...
    def getTemplates(self, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.automation.template.RuleTemplate]: ...

class ModuleTypeFileProviderWatcher(ModuleTypeFileProvider):
    """
    Java class 'org.openhab.core.automation.internal.provider.file.ModuleTypeFileProviderWatcher'
    
        Extends:
            org.openhab.core.automation.internal.provider.file.ModuleTypeFileProvider
    
      Constructors:
        * ModuleTypeFileProviderWatcher()
    
    """
    def __init__(self): ...
    def addParser(self, parser: org.openhab.core.automation.parser.Parser[org.openhab.core.automation.type.ModuleType], properties: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> None: ...
    def removeParser(self, parser: org.openhab.core.automation.parser.Parser[org.openhab.core.automation.type.ModuleType], properties: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> None: ...

class TemplateFileProviderWatcher(TemplateFileProvider):
    """
    Java class 'org.openhab.core.automation.internal.provider.file.TemplateFileProviderWatcher'
    
        Extends:
            org.openhab.core.automation.internal.provider.file.TemplateFileProvider
    
      Constructors:
        * TemplateFileProviderWatcher()
    
    """
    def __init__(self): ...
    def addParser(self, parser: org.openhab.core.automation.parser.Parser[org.openhab.core.automation.template.RuleTemplate], properties: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> None: ...
    def removeParser(self, parser: org.openhab.core.automation.parser.Parser[org.openhab.core.automation.template.RuleTemplate], properties: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> None: ...
