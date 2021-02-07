import java.lang
import java.util
import org.openhab.core.automation
import org.openhab.core.automation.handler
import org.openhab.core.automation.internal
import org.openhab.core.automation.type
import typing


_AbstractCompositeModuleHandler__M = typing.TypeVar('_AbstractCompositeModuleHandler__M', bound=org.openhab.core.automation.Module)  # <M>
_AbstractCompositeModuleHandler__MT = typing.TypeVar('_AbstractCompositeModuleHandler__MT', bound=org.openhab.core.automation.type.ModuleType)  # <MT>
_AbstractCompositeModuleHandler__H = typing.TypeVar('_AbstractCompositeModuleHandler__H', bound=org.openhab.core.automation.handler.ModuleHandler)  # <H>
class AbstractCompositeModuleHandler(org.openhab.core.automation.handler.ModuleHandler, typing.Generic[_AbstractCompositeModuleHandler__M, _AbstractCompositeModuleHandler__MT, _AbstractCompositeModuleHandler__H]):
    """
    Java class 'org.openhab.core.automation.internal.composite.AbstractCompositeModuleHandler'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.handler.ModuleHandler
    
      Constructors:
        * AbstractCompositeModuleHandler(org.openhab.core.automation.Module, org.openhab.core.automation.type.ModuleType, java.util.LinkedHashMap)
    
    """
    def __init__(self, module: _AbstractCompositeModuleHandler__M, moduleType: _AbstractCompositeModuleHandler__MT, mapModuleToHandler: java.util.LinkedHashMap[_AbstractCompositeModuleHandler__M, _AbstractCompositeModuleHandler__H]): ...
    def dispose(self) -> None: ...
    def setCallback(self, callback: org.openhab.core.automation.ModuleHandlerCallback) -> None: ...

class CompositeModuleHandlerFactory(org.openhab.core.automation.handler.BaseModuleHandlerFactory):
    """
    Java class 'org.openhab.core.automation.internal.composite.CompositeModuleHandlerFactory'
    
        Extends:
            org.openhab.core.automation.handler.BaseModuleHandlerFactory
    
        Interfaces:
            org.openhab.core.automation.handler.ModuleHandlerFactory
    
      Constructors:
        * CompositeModuleHandlerFactory(org.openhab.core.automation.type.ModuleTypeRegistry, org.openhab.core.automation.internal.RuleEngineImpl)
    
    """
    def __init__(self, mtRegistry: org.openhab.core.automation.type.ModuleTypeRegistry, re: org.openhab.core.automation.internal.RuleEngineImpl): ...
    def deactivate(self) -> None: ...
    def getTypes(self) -> java.util.Collection[java.lang.String]: ...
    def internalCreate(self, module: org.openhab.core.automation.Module, ruleUID: java.lang.String) -> org.openhab.core.automation.handler.ModuleHandler: ...
    def ungetHandler(self, module: org.openhab.core.automation.Module, childModulePrefix: java.lang.String, handler: org.openhab.core.automation.handler.ModuleHandler) -> None: ...

class CompositeActionHandler(AbstractCompositeModuleHandler[org.openhab.core.automation.Action, org.openhab.core.automation.type.CompositeActionType, org.openhab.core.automation.handler.ActionHandler], org.openhab.core.automation.handler.ActionHandler):
    """
    Java class 'org.openhab.core.automation.internal.composite.CompositeActionHandler'
    
        Extends:
            org.openhab.core.automation.internal.composite.AbstractCompositeModuleHandler
    
        Interfaces:
            org.openhab.core.automation.handler.ActionHandler
    
      Constructors:
        * CompositeActionHandler(org.openhab.core.automation.Action, org.openhab.core.automation.type.CompositeActionType, java.util.LinkedHashMap, java.lang.String)
    
      Attributes:
        REFERENCE (java.lang.String): final static field
    
    """
    REFERENCE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, action: org.openhab.core.automation.Action, mt: org.openhab.core.automation.type.CompositeActionType, mapModuleToHandler: java.util.LinkedHashMap[org.openhab.core.automation.Action, org.openhab.core.automation.handler.ActionHandler], ruleUID: java.lang.String): ...
    def execute(self, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> java.util.Map[java.lang.String, typing.Any]: ...

class CompositeConditionHandler(AbstractCompositeModuleHandler[org.openhab.core.automation.Condition, org.openhab.core.automation.type.CompositeConditionType, org.openhab.core.automation.handler.ConditionHandler], org.openhab.core.automation.handler.ConditionHandler):
    """
    Java class 'org.openhab.core.automation.internal.composite.CompositeConditionHandler'
    
        Extends:
            org.openhab.core.automation.internal.composite.AbstractCompositeModuleHandler
    
        Interfaces:
            org.openhab.core.automation.handler.ConditionHandler
    
      Constructors:
        * CompositeConditionHandler(org.openhab.core.automation.Condition, org.openhab.core.automation.type.CompositeConditionType, java.util.LinkedHashMap, java.lang.String)
    
    """
    def __init__(self, condition: org.openhab.core.automation.Condition, mt: org.openhab.core.automation.type.CompositeConditionType, mapModuleToHandler: java.util.LinkedHashMap[org.openhab.core.automation.Condition, org.openhab.core.automation.handler.ConditionHandler], ruleUID: java.lang.String): ...
    def isSatisfied(self, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> bool: ...

class CompositeTriggerHandler(AbstractCompositeModuleHandler[org.openhab.core.automation.Trigger, org.openhab.core.automation.type.CompositeTriggerType, org.openhab.core.automation.handler.TriggerHandler], org.openhab.core.automation.handler.TriggerHandler, org.openhab.core.automation.handler.TriggerHandlerCallback):
    """
    Java class 'org.openhab.core.automation.internal.composite.CompositeTriggerHandler'
    
        Extends:
            org.openhab.core.automation.internal.composite.AbstractCompositeModuleHandler
    
        Interfaces:
            org.openhab.core.automation.handler.TriggerHandler,
            org.openhab.core.automation.handler.TriggerHandlerCallback
    
      Constructors:
        * CompositeTriggerHandler(org.openhab.core.automation.Trigger, org.openhab.core.automation.type.CompositeTriggerType, java.util.LinkedHashMap, java.lang.String)
    
    """
    def __init__(self, trigger: org.openhab.core.automation.Trigger, mt: org.openhab.core.automation.type.CompositeTriggerType, mapModuleToHandler: java.util.LinkedHashMap[org.openhab.core.automation.Trigger, org.openhab.core.automation.handler.TriggerHandler], ruleUID: java.lang.String): ...
    def dispose(self) -> None: ...
    def getStatus(self, ruleUID: java.lang.String) -> org.openhab.core.automation.RuleStatus: ...
    def getStatusInfo(self, ruleUID: java.lang.String) -> org.openhab.core.automation.RuleStatusInfo: ...
    def isEnabled(self, ruleUID: java.lang.String) -> bool: ...
    @typing.overload
    def runNow(self, uid: java.lang.String) -> None: ...
    @typing.overload
    def runNow(self, uid: java.lang.String, considerConditions: bool, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def setCallback(self, callback: org.openhab.core.automation.ModuleHandlerCallback) -> None: ...
    def setEnabled(self, uid: java.lang.String, isEnabled: bool) -> None: ...
    def triggered(self, trigger: org.openhab.core.automation.Trigger, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
