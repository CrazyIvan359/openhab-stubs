import java.lang
import java.util
import org.openhab.core.automation.handler
import org.openhab.core.automation.module.script


class ScriptModuleHandlerFactory(org.openhab.core.automation.handler.BaseModuleHandlerFactory):
    """
    Java class 'org.openhab.core.automation.module.script.internal.factory.ScriptModuleHandlerFactory'
    
        Extends:
            org.openhab.core.automation.handler.BaseModuleHandlerFactory
    
      Constructors:
        * ScriptModuleHandlerFactory()
    
    """
    def __init__(self): ...
    def getTypes(self) -> java.util.Collection[java.lang.String]: ...
    def setScriptEngineManager(self, scriptEngineManager: org.openhab.core.automation.module.script.ScriptEngineManager) -> None: ...
    def unsetScriptEngineManager(self, scriptEngineManager: org.openhab.core.automation.module.script.ScriptEngineManager) -> None: ...
