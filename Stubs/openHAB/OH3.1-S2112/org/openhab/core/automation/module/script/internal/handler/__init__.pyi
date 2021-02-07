import java.lang
import java.util
import org.openhab.core.automation
import org.openhab.core.automation.handler
import org.openhab.core.automation.module.script
import typing


_AbstractScriptModuleHandler__T = typing.TypeVar('_AbstractScriptModuleHandler__T', bound=org.openhab.core.automation.Module)  # <T>
class AbstractScriptModuleHandler(org.openhab.core.automation.handler.BaseModuleHandler[_AbstractScriptModuleHandler__T], typing.Generic[_AbstractScriptModuleHandler__T]):
    """
    Java class 'org.openhab.core.automation.module.script.internal.handler.AbstractScriptModuleHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseModuleHandler
    
      Constructors:
        * AbstractScriptModuleHandler(org.openhab.core.automation.Module, java.lang.String, org.openhab.core.automation.module.script.ScriptEngineManager)
    
      Attributes:
        SCRIPT_TYPE (java.lang.String): final static field
        SCRIPT (java.lang.String): final static field
    
    """
    SCRIPT_TYPE: typing.ClassVar[java.lang.String] = ...
    SCRIPT: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: _AbstractScriptModuleHandler__T, ruleUID: java.lang.String, scriptEngineManager: org.openhab.core.automation.module.script.ScriptEngineManager): ...
    def dispose(self) -> None: ...

class ScriptActionHandler(AbstractScriptModuleHandler[org.openhab.core.automation.Action], org.openhab.core.automation.handler.ActionHandler):
    """
    Java class 'org.openhab.core.automation.module.script.internal.handler.ScriptActionHandler'
    
        Extends:
            org.openhab.core.automation.module.script.internal.handler.AbstractScriptModuleHandler
    
        Interfaces:
            org.openhab.core.automation.handler.ActionHandler
    
      Constructors:
        * ScriptActionHandler(org.openhab.core.automation.Action, java.lang.String, org.openhab.core.automation.module.script.ScriptEngineManager)
    
      Attributes:
        TYPE_ID (java.lang.String): final static field
    
    """
    TYPE_ID: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Action, ruleUID: java.lang.String, scriptEngineManager: org.openhab.core.automation.module.script.ScriptEngineManager): ...
    def dispose(self) -> None: ...
    def execute(self, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> java.util.Map[java.lang.String, typing.Any]: ...

class ScriptConditionHandler(AbstractScriptModuleHandler[org.openhab.core.automation.Condition], org.openhab.core.automation.handler.ConditionHandler):
    """
    Java class 'org.openhab.core.automation.module.script.internal.handler.ScriptConditionHandler'
    
        Extends:
            org.openhab.core.automation.module.script.internal.handler.AbstractScriptModuleHandler
    
        Interfaces:
            org.openhab.core.automation.handler.ConditionHandler
    
      Constructors:
        * ScriptConditionHandler(org.openhab.core.automation.Condition, java.lang.String, org.openhab.core.automation.module.script.ScriptEngineManager)
    
      Attributes:
        TYPE_ID (java.lang.String): final static field
    
    """
    TYPE_ID: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Condition, ruleUID: java.lang.String, scriptEngineManager: org.openhab.core.automation.module.script.ScriptEngineManager): ...
    def isSatisfied(self, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> bool: ...
