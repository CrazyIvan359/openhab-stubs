import java.lang
import java.util
import org.openhab.core.automation
import org.openhab.core.common.registry
import org.openhab.core.config.core
import typing


class Input(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.type.Input'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Input(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.util.Set, boolean, java.lang.String, java.lang.String)
        * Input(java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, name: java.lang.String, type: java.lang.String): ...
    @typing.overload
    def __init__(self, name: java.lang.String, type: java.lang.String, label: java.lang.String, description: java.lang.String, tags: java.util.Set[java.lang.String], required: bool, reference: java.lang.String, defaultValue: java.lang.String): ...
    def getDefaultValue(self) -> java.lang.String: ...
    def getDescription(self) -> java.lang.String: ...
    def getLabel(self) -> java.lang.String: ...
    def getName(self) -> java.lang.String: ...
    def getReference(self) -> java.lang.String: ...
    def getTags(self) -> java.util.Set[java.lang.String]: ...
    def getType(self) -> java.lang.String: ...
    def isRequired(self) -> bool: ...
    def toString(self) -> java.lang.String: ...

class ModuleType(org.openhab.core.common.registry.Identifiable[java.lang.String]):
    """
    Java class 'org.openhab.core.automation.type.ModuleType'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.common.registry.Identifiable
    
      Constructors:
        * ModuleType(java.lang.String, java.util.List)
        * ModuleType(java.lang.String, java.util.List, java.lang.String, java.lang.String, java.util.Set, org.openhab.core.automation.Visibility)
    
    """
    @typing.overload
    def __init__(self, UID: java.lang.String, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]): ...
    @typing.overload
    def __init__(self, UID: java.lang.String, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter], label: java.lang.String, description: java.lang.String, tags: java.util.Set[java.lang.String], visibility: org.openhab.core.automation.Visibility): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getConfigurationDescriptions(self) -> java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]: ...
    def getDescription(self) -> java.lang.String: ...
    def getLabel(self) -> java.lang.String: ...
    def getTags(self) -> java.util.Set[java.lang.String]: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    @typing.overload
    def getUID(self) -> java.lang.String: ...
    def getVisibility(self) -> org.openhab.core.automation.Visibility: ...
    def hashCode(self) -> int: ...

class ModuleTypeProvider(org.openhab.core.common.registry.Provider[ModuleType]):
    """
    @NonNullByDefault public interface ModuleTypeProvider extends org.openhab.core.common.registry.Provider<:class:`~org.openhab.core.automation.type.ModuleType`>
    
        This interface has to be implemented by all providers of :class:`~org.openhab.core.automation.type.ModuleType`s. The
        :class:`~org.openhab.core.automation.type.ModuleTypeRegistry` uses it to get access to available
        :class:`~org.openhab.core.automation.type.ModuleType`s.
    
    
    """
    _getModuleType__T = typing.TypeVar('_getModuleType__T', bound=ModuleType)  # <T>
    def getModuleType(self, UID: java.lang.String, locale: java.util.Locale) -> _getModuleType__T: ...
    _getModuleTypes__T = typing.TypeVar('_getModuleTypes__T', bound=ModuleType)  # <T>
    def getModuleTypes(self, locale: java.util.Locale) -> java.util.Collection[_getModuleTypes__T]: ...

class ModuleTypeRegistry(org.openhab.core.common.registry.Registry[ModuleType, java.lang.String]):
    """
    @NonNullByDefault public interface ModuleTypeRegistry extends org.openhab.core.common.registry.Registry<:class:`~org.openhab.core.automation.type.ModuleType`,​:class:`~org.openhab.core.automation.type.https:.docs.oracle.com.en.java.javase.11.docs.api.java.base.java.lang.String?is`>
    
        This interface provides functionality to get available :class:`~org.openhab.core.automation.type.ModuleType`s. The
        module types can be returned localized depending on locale parameter. When it is not specified or there is no such
        localization resources the returned module type is localized with default locale.
    
    
    """
    _get_0__T = typing.TypeVar('_get_0__T', bound=ModuleType)  # <T>
    @typing.overload
    def get(self, moduleTypeUID: java.lang.String, locale: java.util.Locale) -> _get_0__T: ...
    @typing.overload
    def get(self, key: typing.Any) -> org.openhab.core.common.registry.Identifiable: ...
    @typing.overload
    def getActions(self, tags: typing.List[java.lang.String]) -> java.util.Collection['ActionType']: ...
    @typing.overload
    def getActions(self, locale: java.util.Locale, tags: typing.List[java.lang.String]) -> java.util.Collection['ActionType']: ...
    _getByTag_0__T = typing.TypeVar('_getByTag_0__T', bound=ModuleType)  # <T>
    @typing.overload
    def getByTag(self, moduleTypeTag: java.lang.String) -> java.util.Collection[_getByTag_0__T]: ...
    _getByTag_1__T = typing.TypeVar('_getByTag_1__T', bound=ModuleType)  # <T>
    @typing.overload
    def getByTag(self, moduleTypeTag: java.lang.String, locale: java.util.Locale) -> java.util.Collection[_getByTag_1__T]: ...
    _getByTags_0__T = typing.TypeVar('_getByTags_0__T', bound=ModuleType)  # <T>
    @typing.overload
    def getByTags(self, tags: typing.List[java.lang.String]) -> java.util.Collection[_getByTags_0__T]: ...
    _getByTags_1__T = typing.TypeVar('_getByTags_1__T', bound=ModuleType)  # <T>
    @typing.overload
    def getByTags(self, locale: java.util.Locale, tags: typing.List[java.lang.String]) -> java.util.Collection[_getByTags_1__T]: ...
    @typing.overload
    def getConditions(self, tags: typing.List[java.lang.String]) -> java.util.Collection['ConditionType']: ...
    @typing.overload
    def getConditions(self, locale: java.util.Locale, tags: typing.List[java.lang.String]) -> java.util.Collection['ConditionType']: ...
    @typing.overload
    def getTriggers(self, tags: typing.List[java.lang.String]) -> java.util.Collection['TriggerType']: ...
    @typing.overload
    def getTriggers(self, locale: java.util.Locale, tags: typing.List[java.lang.String]) -> java.util.Collection['TriggerType']: ...

class Output(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.type.Output'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Output(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.util.Set, java.lang.String, java.lang.String)
        * Output(java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, name: java.lang.String, type: java.lang.String): ...
    @typing.overload
    def __init__(self, name: java.lang.String, type: java.lang.String, label: java.lang.String, description: java.lang.String, tags: java.util.Set[java.lang.String], reference: java.lang.String, defaultValue: java.lang.String): ...
    def getDefaultValue(self) -> java.lang.String: ...
    def getDescription(self) -> java.lang.String: ...
    def getLabel(self) -> java.lang.String: ...
    def getName(self) -> java.lang.String: ...
    def getReference(self) -> java.lang.String: ...
    def getTags(self) -> java.util.Set[java.lang.String]: ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ActionType(ModuleType):
    """
    Java class 'org.openhab.core.automation.type.ActionType'
    
        Extends:
            org.openhab.core.automation.type.ModuleType
    
      Constructors:
        * ActionType(java.lang.String, java.util.List, java.lang.String, java.lang.String, java.util.Set, org.openhab.core.automation.Visibility, java.util.List, java.util.List)
        * ActionType(java.lang.String, java.util.List, java.util.List, java.util.List)
        * ActionType(java.lang.String, java.util.List, java.util.List)
    
    """
    @typing.overload
    def __init__(self, UID: java.lang.String, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter], label: java.lang.String, description: java.lang.String, tags: java.util.Set[java.lang.String], visibility: org.openhab.core.automation.Visibility, inputs: java.util.List[Input], outputs: java.util.List[Output]): ...
    @typing.overload
    def __init__(self, UID: java.lang.String, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter], inputs: java.util.List[Input]): ...
    @typing.overload
    def __init__(self, UID: java.lang.String, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter], inputs: java.util.List[Input], outputs: java.util.List[Output]): ...
    def getInputs(self) -> java.util.List[Input]: ...
    def getOutputs(self) -> java.util.List[Output]: ...

class ConditionType(ModuleType):
    """
    Java class 'org.openhab.core.automation.type.ConditionType'
    
        Extends:
            org.openhab.core.automation.type.ModuleType
    
      Constructors:
        * ConditionType(java.lang.String, java.util.List, java.util.List)
        * ConditionType(java.lang.String, java.util.List, java.lang.String, java.lang.String, java.util.Set, org.openhab.core.automation.Visibility, java.util.List)
    
    """
    @typing.overload
    def __init__(self, UID: java.lang.String, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter], label: java.lang.String, description: java.lang.String, tags: java.util.Set[java.lang.String], visibility: org.openhab.core.automation.Visibility, inputs: java.util.List[Input]): ...
    @typing.overload
    def __init__(self, UID: java.lang.String, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter], inputs: java.util.List[Input]): ...
    def getInputs(self) -> java.util.List[Input]: ...

class TriggerType(ModuleType):
    """
    Java class 'org.openhab.core.automation.type.TriggerType'
    
        Extends:
            org.openhab.core.automation.type.ModuleType
    
      Constructors:
        * TriggerType(java.lang.String, java.util.List, java.util.List)
        * TriggerType(java.lang.String, java.util.List, java.lang.String, java.lang.String, java.util.Set, org.openhab.core.automation.Visibility, java.util.List)
    
    """
    @typing.overload
    def __init__(self, UID: java.lang.String, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter], label: java.lang.String, description: java.lang.String, tags: java.util.Set[java.lang.String], visibility: org.openhab.core.automation.Visibility, outputs: java.util.List[Output]): ...
    @typing.overload
    def __init__(self, UID: java.lang.String, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter], outputs: java.util.List[Output]): ...
    def getOutputs(self) -> java.util.List[Output]: ...

class CompositeActionType(ActionType):
    """
    Java class 'org.openhab.core.automation.type.CompositeActionType'
    
        Extends:
            org.openhab.core.automation.type.ActionType
    
      Constructors:
        * CompositeActionType(java.lang.String, java.util.List, java.util.List, java.util.List, java.util.List)
        * CompositeActionType(java.lang.String, java.util.List, java.lang.String, java.lang.String, java.util.Set, org.openhab.core.automation.Visibility, java.util.List, java.util.List, java.util.List)
    
    """
    @typing.overload
    def __init__(self, UID: java.lang.String, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter], label: java.lang.String, description: java.lang.String, tags: java.util.Set[java.lang.String], visibility: org.openhab.core.automation.Visibility, inputs: java.util.List[Input], outputs: java.util.List[Output], children: java.util.List[org.openhab.core.automation.Action]): ...
    @typing.overload
    def __init__(self, UID: java.lang.String, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter], inputs: java.util.List[Input], outputs: java.util.List[Output], children: java.util.List[org.openhab.core.automation.Action]): ...
    def getChildren(self) -> java.util.List[org.openhab.core.automation.Action]: ...

class CompositeConditionType(ConditionType):
    """
    Java class 'org.openhab.core.automation.type.CompositeConditionType'
    
        Extends:
            org.openhab.core.automation.type.ConditionType
    
      Constructors:
        * CompositeConditionType(java.lang.String, java.util.List, java.util.List, java.util.List)
        * CompositeConditionType(java.lang.String, java.util.List, java.lang.String, java.lang.String, java.util.Set, org.openhab.core.automation.Visibility, java.util.List, java.util.List)
    
    """
    @typing.overload
    def __init__(self, UID: java.lang.String, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter], label: java.lang.String, description: java.lang.String, tags: java.util.Set[java.lang.String], visibility: org.openhab.core.automation.Visibility, inputs: java.util.List[Input], children: java.util.List[org.openhab.core.automation.Condition]): ...
    @typing.overload
    def __init__(self, UID: java.lang.String, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter], inputs: java.util.List[Input], children: java.util.List[org.openhab.core.automation.Condition]): ...
    def getChildren(self) -> java.util.List[org.openhab.core.automation.Condition]: ...

class CompositeTriggerType(TriggerType):
    """
    Java class 'org.openhab.core.automation.type.CompositeTriggerType'
    
        Extends:
            org.openhab.core.automation.type.TriggerType
    
      Constructors:
        * CompositeTriggerType(java.lang.String, java.util.List, java.util.List, java.util.List)
        * CompositeTriggerType(java.lang.String, java.util.List, java.lang.String, java.lang.String, java.util.Set, org.openhab.core.automation.Visibility, java.util.List, java.util.List)
    
    """
    @typing.overload
    def __init__(self, UID: java.lang.String, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter], label: java.lang.String, description: java.lang.String, tags: java.util.Set[java.lang.String], visibility: org.openhab.core.automation.Visibility, outputs: java.util.List[Output], children: java.util.List[org.openhab.core.automation.Trigger]): ...
    @typing.overload
    def __init__(self, UID: java.lang.String, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter], outputs: java.util.List[Output], children: java.util.List[org.openhab.core.automation.Trigger]): ...
    def getChildren(self) -> java.util.List[org.openhab.core.automation.Trigger]: ...
