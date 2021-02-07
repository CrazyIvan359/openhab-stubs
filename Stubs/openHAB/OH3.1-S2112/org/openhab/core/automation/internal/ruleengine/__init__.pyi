import java.lang
import java.util
import org.openhab.core.automation
import org.openhab.core.automation.handler
import org.openhab.core.automation.internal
import typing


_WrappedModule__M = typing.TypeVar('_WrappedModule__M', bound=org.openhab.core.automation.Module)  # <M>
_WrappedModule__H = typing.TypeVar('_WrappedModule__H', bound=org.openhab.core.automation.handler.ModuleHandler)  # <H>
class WrappedModule(java.lang.Object, typing.Generic[_WrappedModule__M, _WrappedModule__H]):
    """
    Java class 'org.openhab.core.automation.internal.ruleengine.WrappedModule'
    
        Extends:
            java.lang.Object
    
    """
    def getModuleHandler(self) -> _WrappedModule__H: ...
    def setModuleHandler(self, handler: _WrappedModule__H) -> None: ...
    def unwrap(self) -> _WrappedModule__M: ...

class WrappedRule(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.internal.ruleengine.WrappedRule'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * WrappedRule(org.openhab.core.automation.Rule)
    
    """
    def __init__(self, rule: org.openhab.core.automation.Rule): ...
    def getActions(self) -> java.util.List['WrappedAction']: ...
    def getConditions(self) -> java.util.List['WrappedCondition']: ...
    def getModules(self) -> java.util.List[WrappedModule[org.openhab.core.automation.Module, org.openhab.core.automation.handler.ModuleHandler]]: ...
    def getStatusInfo(self) -> org.openhab.core.automation.RuleStatusInfo: ...
    def getTriggers(self) -> java.util.List['WrappedTrigger']: ...
    def getUID(self) -> java.lang.String: ...
    def setStatusInfo(self, statusInfo: org.openhab.core.automation.RuleStatusInfo) -> None: ...
    def unwrap(self) -> org.openhab.core.automation.Rule: ...

class WrappedAction(WrappedModule[org.openhab.core.automation.Action, org.openhab.core.automation.handler.ActionHandler]):
    """
    Java class 'org.openhab.core.automation.internal.ruleengine.WrappedAction'
    
        Extends:
            org.openhab.core.automation.internal.ruleengine.WrappedModule
    
      Constructors:
        * WrappedAction(org.openhab.core.automation.Action)
    
    """
    def __init__(self, action: org.openhab.core.automation.Action): ...
    def getConnections(self) -> java.util.Set[org.openhab.core.automation.internal.Connection]: ...
    def getInputs(self) -> java.util.Map[java.lang.String, java.lang.String]: ...
    def setConnections(self, connections: java.util.Set[org.openhab.core.automation.internal.Connection]) -> None: ...
    def setInputs(self, inputs: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> None: ...

class WrappedCondition(WrappedModule[org.openhab.core.automation.Condition, org.openhab.core.automation.handler.ConditionHandler]):
    """
    Java class 'org.openhab.core.automation.internal.ruleengine.WrappedCondition'
    
        Extends:
            org.openhab.core.automation.internal.ruleengine.WrappedModule
    
      Constructors:
        * WrappedCondition(org.openhab.core.automation.Condition)
    
    """
    def __init__(self, condition: org.openhab.core.automation.Condition): ...
    def getConnections(self) -> java.util.Set[org.openhab.core.automation.internal.Connection]: ...
    def getInputs(self) -> java.util.Map[java.lang.String, java.lang.String]: ...
    def setConnections(self, connections: java.util.Set[org.openhab.core.automation.internal.Connection]) -> None: ...
    def setInputs(self, inputs: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> None: ...

class WrappedTrigger(WrappedModule[org.openhab.core.automation.Trigger, org.openhab.core.automation.handler.TriggerHandler]):
    """
    Java class 'org.openhab.core.automation.internal.ruleengine.WrappedTrigger'
    
        Extends:
            org.openhab.core.automation.internal.ruleengine.WrappedModule
    
      Constructors:
        * WrappedTrigger(org.openhab.core.automation.Trigger)
    
    """
    def __init__(self, trigger: org.openhab.core.automation.Trigger): ...
