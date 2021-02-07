import java.lang
import java.util
import org.openhab.core.automation
import org.openhab.core.automation.handler
import org.openhab.core.automation.module.script.rulesupport.shared
import org.openhab.core.config.core
import typing


class SimpleActionHandler(org.openhab.core.automation.module.script.rulesupport.shared.ScriptedHandler):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.shared.simple.SimpleActionHandler'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.module.script.rulesupport.shared.S
            criptedHandler
    
      Constructors:
        * SimpleActionHandler()
    
    """
    def __init__(self): ...
    def execute(self, module: org.openhab.core.automation.Action, inputs: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> typing.Any: ...
    def init(self, module: org.openhab.core.automation.Action) -> None: ...

class SimpleConditionHandler(org.openhab.core.automation.module.script.rulesupport.shared.ScriptedHandler):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.shared.simple.SimpleConditionHandler'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.module.script.rulesupport.shared.S
            criptedHandler
    
      Constructors:
        * SimpleConditionHandler()
    
    """
    def __init__(self): ...
    def init(self, condition: org.openhab.core.automation.Condition) -> None: ...
    def isSatisfied(self, condition: org.openhab.core.automation.Condition, inputs: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> bool: ...

class SimpleRuleActionHandler(java.lang.Object):
    """
    public interface SimpleRuleActionHandler
    
    
    
    """
    def execute(self, module: org.openhab.core.automation.Action, inputs: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> typing.Any: ...

class SimpleTriggerHandler(org.openhab.core.automation.module.script.rulesupport.shared.ScriptedHandler):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.shared.simple.SimpleTriggerHandler'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.module.script.rulesupport.shared.S
            criptedHandler
    
      Constructors:
        * SimpleTriggerHandler()
    
    """
    def __init__(self): ...
    def init(self, module: org.openhab.core.automation.Trigger) -> None: ...
    def setRuleEngineCallback(self, module: org.openhab.core.automation.Trigger, ruleCallback: 'SimpleTriggerHandlerCallback') -> None: ...

class SimpleTriggerHandlerCallback(org.openhab.core.automation.handler.TriggerHandlerCallback):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.shared.simple.SimpleTriggerHandlerCallback'
    
        Interfaces:
            org.openhab.core.automation.handler.TriggerHandlerCallback
    
    """
    @typing.overload
    def triggered(self, trigger: org.openhab.core.automation.Trigger, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    @typing.overload
    def triggered(self, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...

class SimpleRule(org.openhab.core.automation.Rule, SimpleRuleActionHandler):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.shared.simple.SimpleRule'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.Rule, org.openhab.core.automation.
            module.script.rulesupport.shared.simple.SimpleRuleActionHandle
            r
    
      Constructors:
        * SimpleRule()
    
    """
    def __init__(self): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getActions(self) -> java.util.List[org.openhab.core.automation.Action]: ...
    def getConditions(self) -> java.util.List[org.openhab.core.automation.Condition]: ...
    def getConfiguration(self) -> org.openhab.core.config.core.Configuration: ...
    def getConfigurationDescriptions(self) -> java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]: ...
    def getDescription(self) -> java.lang.String: ...
    @typing.overload
    def getModules(self) -> java.util.List[org.openhab.core.automation.Module]: ...
    _getModules_1__T = typing.TypeVar('_getModules_1__T', bound=org.openhab.core.automation.Module)  # <T>
    @typing.overload
    def getModules(self, moduleClazz: typing.Type[_getModules_1__T]) -> java.util.List[_getModules_1__T]: ...
    def getName(self) -> java.lang.String: ...
    def getTags(self) -> java.util.Set[java.lang.String]: ...
    def getTemplateUID(self) -> java.lang.String: ...
    def getTriggers(self) -> java.util.List[org.openhab.core.automation.Trigger]: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    @typing.overload
    def getUID(self) -> java.lang.String: ...
    def getVisibility(self) -> org.openhab.core.automation.Visibility: ...
    def hashCode(self) -> int: ...
    def setActions(self, actions: java.util.List[org.openhab.core.automation.Action]) -> None: ...
    def setConditions(self, conditions: java.util.List[org.openhab.core.automation.Condition]) -> None: ...
    def setConfiguration(self, ruleConfiguration: org.openhab.core.config.core.Configuration) -> None: ...
    def setConfigurationDescriptions(self, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]) -> None: ...
    def setDescription(self, ruleDescription: java.lang.String) -> None: ...
    def setName(self, ruleName: java.lang.String) -> None: ...
    def setTags(self, ruleTags: java.util.Set[java.lang.String]) -> None: ...
    def setTemplateUID(self, templateUID: java.lang.String) -> None: ...
    def setTriggers(self, triggers: java.util.List[org.openhab.core.automation.Trigger]) -> None: ...
    def setVisibility(self, visibility: org.openhab.core.automation.Visibility) -> None: ...

class SimpleRuleActionHandlerDelegate(SimpleActionHandler):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.shared.simple.SimpleRuleActionHandlerDelegate'
    
        Extends:
            org.openhab.core.automation.module.script.rulesupport.shared.simple.SimpleActionHandler
    
      Constructors:
        * SimpleRuleActionHandlerDelegate(org.openhab.core.automation.module.script.rulesupport.shared.simple.SimpleRuleActionHandler)
    
    """
    def __init__(self, handler: SimpleRuleActionHandler): ...
    def execute(self, module: org.openhab.core.automation.Action, inputs: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> typing.Any: ...
