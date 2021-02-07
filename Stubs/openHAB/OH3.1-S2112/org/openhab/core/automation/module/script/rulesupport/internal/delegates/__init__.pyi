import java.lang
import java.util
import org.openhab.core.automation
import org.openhab.core.automation.handler
import org.openhab.core.automation.module.script.rulesupport.shared.simple
import typing


class SimpleActionHandlerDelegate(org.openhab.core.automation.handler.BaseActionModuleHandler):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.internal.delegates.SimpleActionHandlerDelegate'
    
        Extends:
            org.openhab.core.automation.handler.BaseActionModuleHandler
    
      Constructors:
        * SimpleActionHandlerDelegate(org.openhab.core.automation.Action, org.openhab.core.automation.module.script.rulesupport.shared.simple.SimpleActionHandler)
    
    """
    def __init__(self, module: org.openhab.core.automation.Action, actionHandler: org.openhab.core.automation.module.script.rulesupport.shared.simple.SimpleActionHandler): ...
    def dispose(self) -> None: ...
    def execute(self, inputs: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> java.util.Map[java.lang.String, typing.Any]: ...

class SimpleConditionHandlerDelegate(org.openhab.core.automation.handler.BaseConditionModuleHandler):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.internal.delegates.SimpleConditionHandlerDelegate'
    
        Extends:
            org.openhab.core.automation.handler.BaseConditionModuleHandler
    
      Constructors:
        * SimpleConditionHandlerDelegate(org.openhab.core.automation.Condition, org.openhab.core.automation.module.script.rulesupport.shared.simple.SimpleConditionHandler)
    
    """
    def __init__(self, condition: org.openhab.core.automation.Condition, scriptedHandler: org.openhab.core.automation.module.script.rulesupport.shared.simple.SimpleConditionHandler): ...
    def dispose(self) -> None: ...
    def isSatisfied(self, inputs: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> bool: ...

class SimpleTriggerHandlerCallbackDelegate(org.openhab.core.automation.module.script.rulesupport.shared.simple.SimpleTriggerHandlerCallback):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.internal.delegates.SimpleTriggerHandlerCallbackDelegate'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.module.script.rulesupport.shared.s
            imple.SimpleTriggerHandlerCallback
    
      Constructors:
        * SimpleTriggerHandlerCallbackDelegate(org.openhab.core.automation.Trigger, org.openhab.core.automation.handler.TriggerHandlerCallback)
    
    """
    def __init__(self, trigger: org.openhab.core.automation.Trigger, callback: org.openhab.core.automation.handler.TriggerHandlerCallback): ...
    def getStatus(self, ruleUID: java.lang.String) -> org.openhab.core.automation.RuleStatus: ...
    def getStatusInfo(self, ruleUID: java.lang.String) -> org.openhab.core.automation.RuleStatusInfo: ...
    def isEnabled(self, ruleUID: java.lang.String) -> bool: ...
    @typing.overload
    def runNow(self, uid: java.lang.String) -> None: ...
    @typing.overload
    def runNow(self, uid: java.lang.String, considerConditions: bool, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def setEnabled(self, uid: java.lang.String, isEnabled: bool) -> None: ...
    @typing.overload
    def triggered(self, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    @typing.overload
    def triggered(self, trigger: org.openhab.core.automation.Trigger, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...

class SimpleTriggerHandlerDelegate(org.openhab.core.automation.handler.BaseTriggerModuleHandler):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.internal.delegates.SimpleTriggerHandlerDelegate'
    
        Extends:
            org.openhab.core.automation.handler.BaseTriggerModuleHandler
    
      Constructors:
        * SimpleTriggerHandlerDelegate(org.openhab.core.automation.Trigger, org.openhab.core.automation.module.script.rulesupport.shared.simple.SimpleTriggerHandler)
    
    """
    def __init__(self, module: org.openhab.core.automation.Trigger, triggerHandler: org.openhab.core.automation.module.script.rulesupport.shared.simple.SimpleTriggerHandler): ...
    def dispose(self) -> None: ...
    def setCallback(self, callback: org.openhab.core.automation.ModuleHandlerCallback) -> None: ...
