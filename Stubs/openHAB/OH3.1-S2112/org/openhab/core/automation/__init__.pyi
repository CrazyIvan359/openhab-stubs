import java.lang
import java.util
import java.util.function
import org
import org.openhab.core.automation.dto
import org.openhab.core.common.registry
import org.openhab.core.config.core
import org.openhab.core.storage
import typing


class AnnotatedActions(java.lang.Object):
    """
    public interface AnnotatedActions
    
        Marker interface for RuleActions Every method in the implementation should provide annotations which are used to create
        the ModuleTypes
    
    
    """

class Module(java.lang.Object):
    """
    @NonNullByDefault public interface Module
    
        This interface represents automation :code:`Modules` which are building components of the
        :class:`~org.openhab.core.automation.Rule`s.
    
        Each module is identified by id, which is unique in scope of the :class:`~org.openhab.core.automation.Rule`.
    
        Each module has a :class:`~org.openhab.core.automation.type.ModuleType` which provides meta data of the module. The meta
        data defines :class:`~org.openhab.core.automation.type.Input`s, :class:`~org.openhab.core.automation.type.Output`s and
        :class:`~org.openhab.core.automation.https:.github.com.openhab.infrastructure.org.openhab.core.reactor.org.openhab.core.reactor.bundles.org.openhab.core.config.core.apidocs.org.openhab.core.config.core.ConfigDescriptionParameter?is`s
        which are the building elements of the :class:`~org.openhab.core.automation.Module`.
    
    
        Setters of the module don't have immediate effect on the Rule. To apply the changes, the Module should be set on the
        :class:`~org.openhab.core.automation.Rule` and the Rule has to be updated in
        :class:`~org.openhab.core.automation.RuleRegistry` by invoking :code:`update` method.
    
    
    """
    def getConfiguration(self) -> org.openhab.core.config.core.Configuration: ...
    def getDescription(self) -> java.lang.String: ...
    def getId(self) -> java.lang.String: ...
    def getLabel(self) -> java.lang.String: ...
    def getTypeUID(self) -> java.lang.String: ...

class ModuleHandlerCallback(java.lang.Object):
    """
    @NonNullByDefault public interface ModuleHandlerCallback
    
        This class is responsible to provide a :code:`RegistryChangeListener` logic. A instance of it is added to
        :class:`~org.openhab.core.automation.RuleRegistry` service, to listen for changes when a single
        :class:`~org.openhab.core.automation.Rule` has been added, updated, enabled, disabled or removed and to involve Rule
        Engine to process these changes. Also to send a :code:`run` command for a single
        :class:`~org.openhab.core.automation.Rule` to the Rule Engine.
    
    
    """
    def getStatus(self, ruleUID: java.lang.String) -> 'RuleStatus': ...
    def getStatusInfo(self, ruleUID: java.lang.String) -> 'RuleStatusInfo': ...
    def isEnabled(self, ruleUID: java.lang.String) -> bool: ...
    @typing.overload
    def runNow(self, uid: java.lang.String) -> None: ...
    @typing.overload
    def runNow(self, uid: java.lang.String, considerConditions: bool, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def setEnabled(self, uid: java.lang.String, isEnabled: bool) -> None: ...

class Rule(org.openhab.core.common.registry.Identifiable[java.lang.String]):
    """
    @NonNullByDefault public interface Rule extends org.openhab.core.common.registry.Identifiable<:class:`~org.openhab.core.automation.https:.docs.oracle.com.en.java.javase.11.docs.api.java.base.java.lang.String?is`>
    
        An automation Rule is built from :class:`~org.openhab.core.automation.Module`s and consists of three parts:
    
          - **Triggers:** a list of :class:`~org.openhab.core.automation.Trigger` modules. Each
            :class:`~org.openhab.core.automation.Trigger` from this list can start the evaluation of the Rule. A Rule with an empty
            list of :class:`~org.openhab.core.automation.Trigger`s can only be triggered through the
            :code:`RuleRegistry#runNow(String, boolean, java.util.Map)` method, or directly executed with the
            :code:`RuleRegistry#runNow(String)` method.
          - **Conditions:** a list of :class:`~org.openhab.core.automation.Condition` modules. When a Rule is triggered, the
            evaluation of the Rule :class:`~org.openhab.core.automation.Condition`s will determine if the Rule will be executed. A
            Rule will be executed only when all it's :class:`~org.openhab.core.automation.Condition`s are satisfied. If the
            :class:`~org.openhab.core.automation.Condition`s list is empty, the Rule is considered satisfied.
          - **Actions:** a list of :class:`~org.openhab.core.automation.Action` modules. These modules determine the actions that
            will be performed when a Rule is executed.
    
        Additionally, Rules can have :code:`**tags**` - non-hierarchical keywords or terms for describing them. They can help
        the user to classify or label the Rules, and to filter and search them.
    
    
    """
    def getActions(self) -> java.util.List['Action']: ...
    def getConditions(self) -> java.util.List['Condition']: ...
    def getConfiguration(self) -> org.openhab.core.config.core.Configuration: ...
    def getConfigurationDescriptions(self) -> java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]: ...
    def getDescription(self) -> java.lang.String: ...
    def getModule(self, moduleId: java.lang.String) -> Module: ...
    def getModules(self) -> java.util.List[Module]: ...
    def getName(self) -> java.lang.String: ...
    def getTags(self) -> java.util.Set[java.lang.String]: ...
    def getTemplateUID(self) -> java.lang.String: ...
    def getTriggers(self) -> java.util.List['Trigger']: ...
    @typing.overload
    def getUID(self) -> java.lang.String: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    def getVisibility(self) -> 'Visibility': ...

class RuleManager(java.lang.Object):
    """
    @NonNullByDefault public interface RuleManager
    
        This class is responsible to provide a :code:`RegistryChangeListener` logic. A instance of it is added to
        :class:`~org.openhab.core.automation.RuleRegistry` service, to listen for changes when a single
        :class:`~org.openhab.core.automation.Rule` has been added, updated, enabled, disabled or removed and to involve Rule
        Engine to process these changes. Also to send a :code:`run` command for a single
        :class:`~org.openhab.core.automation.Rule` to the Rule Engine.
    
    
    """
    def getStatus(self, ruleUID: java.lang.String) -> 'RuleStatus': ...
    def getStatusInfo(self, ruleUID: java.lang.String) -> 'RuleStatusInfo': ...
    def isEnabled(self, ruleUID: java.lang.String) -> bool: ...
    @typing.overload
    def runNow(self, uid: java.lang.String) -> None: ...
    @typing.overload
    def runNow(self, uid: java.lang.String, considerConditions: bool, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def setEnabled(self, uid: java.lang.String, isEnabled: bool) -> None: ...

class RulePredicates(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.RulePredicates'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RulePredicates()
    
      Attributes:
        PREFIX_SEPARATOR (java.lang.String): final static field
    
    """
    PREFIX_SEPARATOR: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    @classmethod
    def getPrefix(cls, rule: Rule) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def hasAllTags(cls, tags: typing.List[java.lang.String]) -> java.util.function.Predicate[Rule]: ...
    @classmethod
    @typing.overload
    def hasAllTags(cls, tags: typing.Union[java.util.Collection[java.lang.String], typing.Sequence[java.lang.String]]) -> java.util.function.Predicate[Rule]: ...
    @classmethod
    def hasAnyOfPrefixes(cls, prefixes: typing.List[java.lang.String]) -> java.util.function.Predicate[Rule]: ...
    @classmethod
    @typing.overload
    def hasAnyOfTags(cls, tags: typing.List[java.lang.String]) -> java.util.function.Predicate[Rule]: ...
    @classmethod
    @typing.overload
    def hasAnyOfTags(cls, tags: typing.Union[java.util.Collection[java.lang.String], typing.Sequence[java.lang.String]]) -> java.util.function.Predicate[Rule]: ...
    @classmethod
    def hasNoTags(cls) -> java.util.function.Predicate[Rule]: ...
    @classmethod
    def hasPrefix(cls, prefix: java.lang.String) -> java.util.function.Predicate[Rule]: ...
    @classmethod
    def hasTags(cls) -> java.util.function.Predicate[Rule]: ...

class RuleProvider(org.openhab.core.common.registry.Provider[Rule]):
    """
    @NonNullByDefault public interface RuleProvider extends org.openhab.core.common.registry.Provider<:class:`~org.openhab.core.automation.Rule`>
    
        This class is responsible for providing :class:`~org.openhab.core.automation.Rule`s.
        :class:`~org.openhab.core.automation.RuleProvider`s are tracked by the
        :class:`~org.openhab.core.automation.RuleRegistry` service, which collect all rules from different providers of the same
        type.
    
    
    """

class RuleRegistry(org.openhab.core.common.registry.Registry[Rule, java.lang.String]):
    """
    @NonNullByDefault public interface RuleRegistry extends org.openhab.core.common.registry.Registry<:class:`~org.openhab.core.automation.Rule`,​:class:`~org.openhab.core.automation.https:.docs.oracle.com.en.java.javase.11.docs.api.java.base.java.lang.String?is`>
    
        The :class:`~org.openhab.core.automation.RuleRegistry` provides basic functionality for managing
        :class:`~org.openhab.core.automation.Rule`s. It can be used to
    
          - Add Rules with the :code:`Registry#add(Object)` method.
          - Get the existing rules with the :meth:`~org.openhab.core.automation.RuleRegistry.getByTag`,
            :meth:`~org.openhab.core.automation.RuleRegistry.getByTags` methods.
          - Update the existing rules with the :code:`Registry#update(Object)` method.
          - Remove Rules with the :code:`Registry.remove(Object)` method.
          - Manage the state (**enabled** or **disabled**) of the Rules:
    
              - A newly added Rule is always **enabled**.
              - To check a Rule's state, use the :code:`#isEnabled(String)` method.
              - To change a Rule's state, use the :code:`#setEnabled(String, boolean)` method.
    
    
    
        The :class:`~org.openhab.core.automation.RuleRegistry` manages the status of the Rules:
    
          - To check a Rule's status info, use the :code:`#getStatusInfo(String)` method.
          - The status of a Rule enabled with :code:`#setEnabled(String, boolean)`, is first set to
            :meth:`~org.openhab.core.automation.RuleStatus.UNINITIALIZED`.
          - After a Rule is enabled, a verification procedure is initiated. If the verification of the modules IDs, connections
            between modules and configuration values of the modules is successful, and the module handlers are correctly set, the
            status is set to :meth:`~org.openhab.core.automation.RuleStatus.IDLE`.
          - If some of the module handlers disappear, the Rule will become
            :meth:`~org.openhab.core.automation.RuleStatus.UNINITIALIZED` again.
          - If one of the Rule's Triggers is triggered, the Rule becomes :meth:`~org.openhab.core.automation.RuleStatus.RUNNING`.
            When the execution is complete, it will become :meth:`~org.openhab.core.automation.RuleStatus.IDLE` again.
          - If a Rule is disabled with :code:`#setEnabled(String, boolean)`, it's status is set to :code:`RuleStatus#DISABLED`.
    
    
    
    """
    @typing.overload
    def add(self, rule: Rule) -> Rule: ...
    @typing.overload
    def add(self, identifiable: org.openhab.core.common.registry.Identifiable) -> org.openhab.core.common.registry.Identifiable: ...
    def getByTag(self, tag: java.lang.String) -> java.util.Collection[Rule]: ...
    def getByTags(self, tags: typing.List[java.lang.String]) -> java.util.Collection[Rule]: ...

class RuleStatus(java.lang.Enum[org.openhab.core.automation.RuleStatus]):
    """
    Java class 'org.openhab.core.automation.RuleStatus'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        UNINITIALIZED (org.openhab.core.automation.RuleStatus): final static enum constant
        INITIALIZING (org.openhab.core.automation.RuleStatus): final static enum constant
        IDLE (org.openhab.core.automation.RuleStatus): final static enum constant
        RUNNING (org.openhab.core.automation.RuleStatus): final static enum constant
    
    """
    UNINITIALIZED: typing.ClassVar['RuleStatus'] = ...
    INITIALIZING: typing.ClassVar['RuleStatus'] = ...
    IDLE: typing.ClassVar['RuleStatus'] = ...
    RUNNING: typing.ClassVar['RuleStatus'] = ...
    def getValue(self) -> int: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'RuleStatus': ...
    @classmethod
    def values(cls) -> typing.List['RuleStatus']: ...

class RuleStatusDetail(java.lang.Enum[org.openhab.core.automation.RuleStatusDetail]):
    """
    Java class 'org.openhab.core.automation.RuleStatusDetail'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        NONE (org.openhab.core.automation.RuleStatusDetail): final static enum constant
        HANDLER_MISSING_ERROR (org.openhab.core.automation.RuleStatusDetail): final static enum constant
        HANDLER_INITIALIZING_ERROR (org.openhab.core.automation.RuleStatusDetail): final static enum constant
        CONFIGURATION_ERROR (org.openhab.core.automation.RuleStatusDetail): final static enum constant
        TEMPLATE_MISSING_ERROR (org.openhab.core.automation.RuleStatusDetail): final static enum constant
        INVALID_RULE (org.openhab.core.automation.RuleStatusDetail): final static enum constant
        DISABLED (org.openhab.core.automation.RuleStatusDetail): final static enum constant
    
    """
    NONE: typing.ClassVar['RuleStatusDetail'] = ...
    HANDLER_MISSING_ERROR: typing.ClassVar['RuleStatusDetail'] = ...
    HANDLER_INITIALIZING_ERROR: typing.ClassVar['RuleStatusDetail'] = ...
    CONFIGURATION_ERROR: typing.ClassVar['RuleStatusDetail'] = ...
    TEMPLATE_MISSING_ERROR: typing.ClassVar['RuleStatusDetail'] = ...
    INVALID_RULE: typing.ClassVar['RuleStatusDetail'] = ...
    DISABLED: typing.ClassVar['RuleStatusDetail'] = ...
    def getValue(self) -> int: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'RuleStatusDetail': ...
    @classmethod
    def values(cls) -> typing.List['RuleStatusDetail']: ...

class RuleStatusInfo(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.RuleStatusInfo'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RuleStatusInfo(org.openhab.core.automation.RuleStatus, org.openhab.core.automation.RuleStatusDetail, java.lang.String)
        * RuleStatusInfo(org.openhab.core.automation.RuleStatus, org.openhab.core.automation.RuleStatusDetail)
        * RuleStatusInfo(org.openhab.core.automation.RuleStatus)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
    """
    @typing.overload
    def __init__(self, status: RuleStatus): ...
    @typing.overload
    def __init__(self, status: RuleStatus, statusDetail: RuleStatusDetail): ...
    @typing.overload
    def __init__(self, status: RuleStatus, statusDetail: RuleStatusDetail, description: java.lang.String): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getDescription(self) -> java.lang.String: ...
    def getStatus(self) -> RuleStatus: ...
    def getStatusDetail(self) -> RuleStatusDetail: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class StatusInfoCallback(java.lang.Object):
    """
    public interface StatusInfoCallback
    
        This interface is used by :class:`~org.openhab.core.automation.RuleRegistry` implementation to be notified of changes
        related to statuses of rules.
    
    
    """
    def statusInfoChanged(self, ruleUID: java.lang.String, statusInfo: RuleStatusInfo) -> None: ...

class Visibility(java.lang.Enum[org.openhab.core.automation.Visibility]):
    """
    Java class 'org.openhab.core.automation.Visibility'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        VISIBLE (org.openhab.core.automation.Visibility): final static enum constant
        HIDDEN (org.openhab.core.automation.Visibility): final static enum constant
        EXPERT (org.openhab.core.automation.Visibility): final static enum constant
    
    """
    VISIBLE: typing.ClassVar['Visibility'] = ...
    HIDDEN: typing.ClassVar['Visibility'] = ...
    EXPERT: typing.ClassVar['Visibility'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'Visibility': ...
    @classmethod
    def values(cls) -> typing.List['Visibility']: ...

class Action(Module):
    """
    Java class 'org.openhab.core.automation.Action'
    
        Interfaces:
            org.openhab.core.automation.Module
    
    """
    def getInputs(self) -> java.util.Map[java.lang.String, java.lang.String]: ...

class Condition(Module):
    """
    Java class 'org.openhab.core.automation.Condition'
    
        Interfaces:
            org.openhab.core.automation.Module
    
    """
    def getInputs(self) -> java.util.Map[java.lang.String, java.lang.String]: ...

class ManagedRuleProvider(org.openhab.core.common.registry.AbstractManagedProvider[Rule, java.lang.String, org.openhab.core.automation.dto.RuleDTO], RuleProvider):
    """
    Java class 'org.openhab.core.automation.ManagedRuleProvider'
    
        Extends:
            org.openhab.core.common.registry.AbstractManagedProvider
    
        Interfaces:
            org.openhab.core.automation.RuleProvider
    
      Constructors:
        * ManagedRuleProvider(org.openhab.core.storage.StorageService)
    
    """
    def __init__(self, storageService: org.openhab.core.storage.StorageService): ...

class Trigger(Module):
    """
    Java class 'org.openhab.core.automation.Trigger'
    
        Interfaces:
            org.openhab.core.automation.Module
    
    """
