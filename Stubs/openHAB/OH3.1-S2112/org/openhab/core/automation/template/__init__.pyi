import java.lang
import java.util
import org.openhab.core.automation
import org.openhab.core.common.registry
import org.openhab.core.config.core
import typing


class Template(org.openhab.core.common.registry.Identifiable[java.lang.String]):
    """
    @NonNullByDefault public interface Template extends org.openhab.core.common.registry.Identifiable<:class:`~org.openhab.core.automation.template.https:.docs.oracle.com.en.java.javase.11.docs.api.java.base.java.lang.String?is`>
    
        The templates define types of shared, ready to use definitions of automation objects, which can be instantiated and
        configured to produce automation instances. Each Template has a unique identifier (UID).
    
        The :class:`~org.openhab.core.automation.template.Template`s can be used by any creator of automation objects, but they
        can be modified only by its owner.
    
        Templates can have :code:`tags` - non-hierarchical keywords or terms for describing them.
    
    
    """
    def getDescription(self) -> java.lang.String: ...
    def getLabel(self) -> java.lang.String: ...
    def getTags(self) -> java.util.Set[java.lang.String]: ...
    @typing.overload
    def getUID(self) -> java.lang.String: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    def getVisibility(self) -> org.openhab.core.automation.Visibility: ...

_TemplateProvider__E = typing.TypeVar('_TemplateProvider__E', bound=Template)  # <E>
class TemplateProvider(org.openhab.core.common.registry.Provider[_TemplateProvider__E], typing.Generic[_TemplateProvider__E]):
    """
    @NonNullByDefault public interface TemplateProvider<E extends :class:`~org.openhab.core.automation.template.Template`> extends org.openhab.core.common.registry.Provider<E>
    
        This interface has to be implemented by all providers of :class:`~org.openhab.core.automation.template.Template`s. The
        :class:`~org.openhab.core.automation.template.TemplateRegistry` uses it to get access to available
        :class:`~org.openhab.core.automation.template.Template`s.
    
    
    """
    def getTemplate(self, UID: java.lang.String, locale: java.util.Locale) -> _TemplateProvider__E: ...
    def getTemplates(self, locale: java.util.Locale) -> java.util.Collection[_TemplateProvider__E]: ...

_TemplateRegistry__E = typing.TypeVar('_TemplateRegistry__E', bound=Template)  # <E>
class TemplateRegistry(org.openhab.core.common.registry.Registry[_TemplateRegistry__E, java.lang.String], typing.Generic[_TemplateRegistry__E]):
    """
    @NonNullByDefault public interface TemplateRegistry<E extends :class:`~org.openhab.core.automation.template.Template`> extends org.openhab.core.common.registry.Registry<E,​:class:`~org.openhab.core.automation.template.https:.docs.oracle.com.en.java.javase.11.docs.api.java.base.java.lang.String?is`>
    
        This interface provides functionality to get available :class:`~org.openhab.core.automation.template.Template`s. The
        :class:`~org.openhab.core.automation.template.Template` can be returned localized depending on locale parameter. When
        the parameter is not specified or there is no such localization resources the returned template is localized with
        default locale.
    
    
    """
    @typing.overload
    def get(self, uid: java.lang.String, locale: java.util.Locale) -> _TemplateRegistry__E: ...
    @typing.overload
    def get(self, key: typing.Any) -> _TemplateRegistry__E: ...
    @typing.overload
    def getAll(self, locale: java.util.Locale) -> java.util.Collection[_TemplateRegistry__E]: ...
    @typing.overload
    def getAll(self) -> java.util.Collection[_TemplateRegistry__E]: ...
    @typing.overload
    def getByTag(self, tag: java.lang.String) -> java.util.Collection[_TemplateRegistry__E]: ...
    @typing.overload
    def getByTag(self, tag: java.lang.String, locale: java.util.Locale) -> java.util.Collection[_TemplateRegistry__E]: ...
    @typing.overload
    def getByTags(self, tags: typing.List[java.lang.String]) -> java.util.Collection[_TemplateRegistry__E]: ...
    @typing.overload
    def getByTags(self, locale: java.util.Locale, tags: typing.List[java.lang.String]) -> java.util.Collection[_TemplateRegistry__E]: ...

class RuleTemplate(Template):
    """
    Java class 'org.openhab.core.automation.template.RuleTemplate'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.template.Template
    
      Constructors:
        * RuleTemplate(java.lang.String, java.lang.String, java.lang.String, java.util.Set, java.util.List, java.util.List, java.util.List, java.util.List, org.openhab.core.automation.Visibility)
    
    """
    def __init__(self, UID: java.lang.String, label: java.lang.String, description: java.lang.String, tags: java.util.Set[java.lang.String], triggers: java.util.List[org.openhab.core.automation.Trigger], conditions: java.util.List[org.openhab.core.automation.Condition], actions: java.util.List[org.openhab.core.automation.Action], configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter], visibility: org.openhab.core.automation.Visibility): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getActions(self) -> java.util.List[org.openhab.core.automation.Action]: ...
    def getConditions(self) -> java.util.List[org.openhab.core.automation.Condition]: ...
    def getConfigurationDescriptions(self) -> java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]: ...
    def getDescription(self) -> java.lang.String: ...
    def getLabel(self) -> java.lang.String: ...
    def getModule(self, moduleId: java.lang.String) -> org.openhab.core.automation.Module: ...
    _getModules__T = typing.TypeVar('_getModules__T', bound=org.openhab.core.automation.Module)  # <T>
    def getModules(self, moduleClazz: typing.Type[_getModules__T]) -> java.util.List[_getModules__T]: ...
    def getTags(self) -> java.util.Set[java.lang.String]: ...
    def getTriggers(self) -> java.util.List[org.openhab.core.automation.Trigger]: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    @typing.overload
    def getUID(self) -> java.lang.String: ...
    def getVisibility(self) -> org.openhab.core.automation.Visibility: ...
    def hashCode(self) -> int: ...

class RuleTemplateProvider(TemplateProvider[RuleTemplate]):
    """
    Java class 'org.openhab.core.automation.template.RuleTemplateProvider'
    
        Interfaces:
            org.openhab.core.automation.template.TemplateProvider
    
    """
