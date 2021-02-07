import java.lang
import java.util
import org
import org.openhab.core.automation
import org.openhab.core.automation.template
import org.openhab.core.automation.type
import org.openhab.core.config.core
import org.slf4j
import typing


class ConfigurationNormalizer(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.util.ConfigurationNormalizer'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConfigurationNormalizer()
    
    """
    def __init__(self): ...
    @classmethod
    def getConfigDescriptionMap(cls, configDesc: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]) -> java.util.Map[java.lang.String, org.openhab.core.config.core.ConfigDescriptionParameter]: ...
    @classmethod
    def normalizeConfiguration(cls, configuration: org.openhab.core.config.core.Configuration, configDescriptionMap: typing.Union[java.util.Map[java.lang.String, org.openhab.core.config.core.ConfigDescriptionParameter], typing.Mapping[java.lang.String, org.openhab.core.config.core.ConfigDescriptionParameter]]) -> None: ...
    _normalizeModuleConfigurations__T = typing.TypeVar('_normalizeModuleConfigurations__T', bound=org.openhab.core.automation.Module)  # <T>
    @classmethod
    def normalizeModuleConfigurations(cls, modules: java.util.List[_normalizeModuleConfigurations__T], mtRegistry: org.openhab.core.automation.type.ModuleTypeRegistry) -> None: ...

_ModuleBuilder__B = typing.TypeVar('_ModuleBuilder__B', bound='ModuleBuilder')  # <B>
_ModuleBuilder__T = typing.TypeVar('_ModuleBuilder__T', bound=org.openhab.core.automation.Module)  # <T>
class ModuleBuilder(java.lang.Object, typing.Generic[_ModuleBuilder__B, _ModuleBuilder__T]):
    """
    Java class 'org.openhab.core.automation.util.ModuleBuilder'
    
        Extends:
            java.lang.Object
    
    """
    def build(self) -> _ModuleBuilder__T: ...
    _create__B = typing.TypeVar('_create__B', bound='ModuleBuilder')  # <B>
    _create__T = typing.TypeVar('_create__T', bound=org.openhab.core.automation.Module)  # <T>
    @classmethod
    def create(cls, module: org.openhab.core.automation.Module) -> 'ModuleBuilder'[_create__B, _create__T]: ...
    @classmethod
    @typing.overload
    def createAction(cls) -> 'ActionBuilder': ...
    @classmethod
    @typing.overload
    def createAction(cls, action: org.openhab.core.automation.Action) -> 'ActionBuilder': ...
    @classmethod
    @typing.overload
    def createCondition(cls) -> 'ConditionBuilder': ...
    @classmethod
    @typing.overload
    def createCondition(cls, condition: org.openhab.core.automation.Condition) -> 'ConditionBuilder': ...
    @classmethod
    @typing.overload
    def createTrigger(cls) -> 'TriggerBuilder': ...
    @classmethod
    @typing.overload
    def createTrigger(cls, trigger: org.openhab.core.automation.Trigger) -> 'TriggerBuilder': ...
    def withConfiguration(self, configuration: org.openhab.core.config.core.Configuration) -> _ModuleBuilder__B: ...
    def withDescription(self, description: java.lang.String) -> _ModuleBuilder__B: ...
    def withId(self, id: java.lang.String) -> _ModuleBuilder__B: ...
    def withLabel(self, label: java.lang.String) -> _ModuleBuilder__B: ...
    def withTypeUID(self, typeUID: java.lang.String) -> _ModuleBuilder__B: ...

class ReferenceResolver(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.util.ReferenceResolver'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ReferenceResolver()
    
    """
    def __init__(self): ...
    @classmethod
    def getCompositeChildContext(cls, module: org.openhab.core.automation.Module, compositeContext: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> java.util.Map[java.lang.String, typing.Any]: ...
    @classmethod
    def getNextRefToken(cls, ref: java.lang.String, startIndex: int) -> int: ...
    @classmethod
    def resolveComplexDataReference(cls, object: typing.Any, tokens: typing.List[java.lang.String]) -> typing.Any: ...
    @classmethod
    def resolveReference(cls, reference: java.lang.String, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> typing.Any: ...
    @classmethod
    def splitReferenceToTokens(cls, reference: java.lang.String) -> typing.List[java.lang.String]: ...
    @classmethod
    def updateConfiguration(cls, config: org.openhab.core.config.core.Configuration, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]], logger: org.slf4j.Logger) -> None: ...

class RuleBuilder(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.util.RuleBuilder'
    
        Extends:
            java.lang.Object
    
    """
    def build(self) -> org.openhab.core.automation.Rule: ...
    @classmethod
    @typing.overload
    def create(cls, ruleId: java.lang.String) -> 'RuleBuilder': ...
    @classmethod
    @typing.overload
    def create(cls, r: org.openhab.core.automation.Rule) -> 'RuleBuilder': ...
    @classmethod
    @typing.overload
    def create(cls, template: org.openhab.core.automation.template.RuleTemplate, uid: java.lang.String, name: java.lang.String, configuration: org.openhab.core.config.core.Configuration, visibility: org.openhab.core.automation.Visibility) -> 'RuleBuilder': ...
    @typing.overload
    def withActions(self, actions: java.util.List[org.openhab.core.automation.Action]) -> 'RuleBuilder': ...
    @typing.overload
    def withActions(self, actions: typing.List[org.openhab.core.automation.Action]) -> 'RuleBuilder': ...
    @typing.overload
    def withConditions(self, conditions: java.util.List[org.openhab.core.automation.Condition]) -> 'RuleBuilder': ...
    @typing.overload
    def withConditions(self, conditions: typing.List[org.openhab.core.automation.Condition]) -> 'RuleBuilder': ...
    def withConfiguration(self, ruleConfiguration: org.openhab.core.config.core.Configuration) -> 'RuleBuilder': ...
    def withConfigurationDescriptions(self, configDescs: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]) -> 'RuleBuilder': ...
    def withDescription(self, description: java.lang.String) -> 'RuleBuilder': ...
    def withName(self, name: java.lang.String) -> 'RuleBuilder': ...
    @typing.overload
    def withTags(self, tags: typing.List[java.lang.String]) -> 'RuleBuilder': ...
    @typing.overload
    def withTags(self, tags: java.util.Set[java.lang.String]) -> 'RuleBuilder': ...
    def withTemplateUID(self, uid: java.lang.String) -> 'RuleBuilder': ...
    @typing.overload
    def withTriggers(self, triggers: java.util.List[org.openhab.core.automation.Trigger]) -> 'RuleBuilder': ...
    @typing.overload
    def withTriggers(self, triggers: typing.List[org.openhab.core.automation.Trigger]) -> 'RuleBuilder': ...
    def withVisibility(self, visibility: org.openhab.core.automation.Visibility) -> 'RuleBuilder': ...

class ActionBuilder(ModuleBuilder[org.openhab.core.automation.util.ActionBuilder, org.openhab.core.automation.Action]):
    """
    Java class 'org.openhab.core.automation.util.ActionBuilder'
    
        Extends:
            org.openhab.core.automation.util.ModuleBuilder
    
    """
    @typing.overload
    def build(self) -> org.openhab.core.automation.Action: ...
    @typing.overload
    def build(self) -> org.openhab.core.automation.Module: ...
    @classmethod
    @typing.overload
    def create(cls) -> 'ActionBuilder': ...
    @classmethod
    @typing.overload
    def create(cls, action: org.openhab.core.automation.Action) -> 'ActionBuilder': ...
    _create_2__B = typing.TypeVar('_create_2__B', bound=ModuleBuilder)  # <B>
    _create_2__T = typing.TypeVar('_create_2__T', bound=org.openhab.core.automation.Module)  # <T>
    @classmethod
    @typing.overload
    def create(cls, module: org.openhab.core.automation.Module) -> ModuleBuilder[_create_2__B, _create_2__T]: ...
    def withInputs(self, inputs: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> 'ActionBuilder': ...

class ConditionBuilder(ModuleBuilder[org.openhab.core.automation.util.ConditionBuilder, org.openhab.core.automation.Condition]):
    """
    Java class 'org.openhab.core.automation.util.ConditionBuilder'
    
        Extends:
            org.openhab.core.automation.util.ModuleBuilder
    
    """
    @typing.overload
    def build(self) -> org.openhab.core.automation.Condition: ...
    @typing.overload
    def build(self) -> org.openhab.core.automation.Module: ...
    @classmethod
    @typing.overload
    def create(cls) -> 'ConditionBuilder': ...
    @classmethod
    @typing.overload
    def create(cls, condition: org.openhab.core.automation.Condition) -> 'ConditionBuilder': ...
    _create_2__B = typing.TypeVar('_create_2__B', bound=ModuleBuilder)  # <B>
    _create_2__T = typing.TypeVar('_create_2__T', bound=org.openhab.core.automation.Module)  # <T>
    @classmethod
    @typing.overload
    def create(cls, module: org.openhab.core.automation.Module) -> ModuleBuilder[_create_2__B, _create_2__T]: ...
    def withInputs(self, inputs: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> 'ConditionBuilder': ...

class TriggerBuilder(ModuleBuilder[org.openhab.core.automation.util.TriggerBuilder, org.openhab.core.automation.Trigger]):
    """
    Java class 'org.openhab.core.automation.util.TriggerBuilder'
    
        Extends:
            org.openhab.core.automation.util.ModuleBuilder
    
    """
    @typing.overload
    def build(self) -> org.openhab.core.automation.Module: ...
    @typing.overload
    def build(self) -> org.openhab.core.automation.Trigger: ...
    _create_0__B = typing.TypeVar('_create_0__B', bound=ModuleBuilder)  # <B>
    _create_0__T = typing.TypeVar('_create_0__T', bound=org.openhab.core.automation.Module)  # <T>
    @classmethod
    @typing.overload
    def create(cls, module: org.openhab.core.automation.Module) -> ModuleBuilder[_create_0__B, _create_0__T]: ...
    @classmethod
    @typing.overload
    def create(cls) -> 'TriggerBuilder': ...
    @classmethod
    @typing.overload
    def create(cls, trigger: org.openhab.core.automation.Trigger) -> 'TriggerBuilder': ...
