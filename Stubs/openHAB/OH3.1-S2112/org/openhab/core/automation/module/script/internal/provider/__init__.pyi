import java.lang
import java.util
import org.openhab.core.automation.module.script
import org.openhab.core.automation.type
import org.openhab.core.common.registry


class ScriptModuleTypeProvider(org.openhab.core.automation.type.ModuleTypeProvider):
    """
    Java class 'org.openhab.core.automation.module.script.internal.provider.ScriptModuleTypeProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.type.ModuleTypeProvider
    
      Constructors:
        * ScriptModuleTypeProvider()
    
    """
    def __init__(self): ...
    def addProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[org.openhab.core.automation.type.ModuleType]) -> None: ...
    def getAll(self) -> java.util.Collection[org.openhab.core.automation.type.ModuleType]: ...
    def getModuleType(self, UID: java.lang.String, locale: java.util.Locale) -> org.openhab.core.automation.type.ModuleType: ...
    def getModuleTypes(self, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.automation.type.ModuleType]: ...
    def removeProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[org.openhab.core.automation.type.ModuleType]) -> None: ...
    def setScriptEngineFactory(self, engineFactory: org.openhab.core.automation.module.script.ScriptEngineFactory) -> None: ...
    def unsetScriptEngineFactory(self, engineFactory: org.openhab.core.automation.module.script.ScriptEngineFactory) -> None: ...
