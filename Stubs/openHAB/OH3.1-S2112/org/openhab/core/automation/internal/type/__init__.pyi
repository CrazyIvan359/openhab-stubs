import java.lang
import java.util
import org.openhab.core.automation.type
import org.openhab.core.common.registry
import typing


class ModuleTypeRegistryImpl(org.openhab.core.common.registry.AbstractRegistry[org.openhab.core.automation.type.ModuleType, java.lang.String, org.openhab.core.automation.type.ModuleTypeProvider], org.openhab.core.automation.type.ModuleTypeRegistry):
    """
    Java class 'org.openhab.core.automation.internal.type.ModuleTypeRegistryImpl'
    
        Extends:
            org.openhab.core.common.registry.AbstractRegistry
    
        Interfaces:
            org.openhab.core.automation.type.ModuleTypeRegistry
    
      Constructors:
        * ModuleTypeRegistryImpl()
    
    """
    def __init__(self): ...
    @typing.overload
    def get(self, typeUID: java.lang.String) -> org.openhab.core.automation.type.ModuleType: ...
    _get_1__T = typing.TypeVar('_get_1__T', bound=org.openhab.core.automation.type.ModuleType)  # <T>
    @typing.overload
    def get(self, moduleTypeUID: java.lang.String, locale: java.util.Locale) -> _get_1__T: ...
    @typing.overload
    def get(self, object: typing.Any) -> org.openhab.core.common.registry.Identifiable: ...
    @typing.overload
    def getActions(self, tags: typing.List[java.lang.String]) -> java.util.Collection[org.openhab.core.automation.type.ActionType]: ...
    @typing.overload
    def getActions(self, locale: java.util.Locale, tags: typing.List[java.lang.String]) -> java.util.Collection[org.openhab.core.automation.type.ActionType]: ...
    _getByTag_0__T = typing.TypeVar('_getByTag_0__T', bound=org.openhab.core.automation.type.ModuleType)  # <T>
    @typing.overload
    def getByTag(self, moduleTypeTag: java.lang.String) -> java.util.Collection[_getByTag_0__T]: ...
    _getByTag_1__T = typing.TypeVar('_getByTag_1__T', bound=org.openhab.core.automation.type.ModuleType)  # <T>
    @typing.overload
    def getByTag(self, moduleTypeTag: java.lang.String, locale: java.util.Locale) -> java.util.Collection[_getByTag_1__T]: ...
    _getByTags_0__T = typing.TypeVar('_getByTags_0__T', bound=org.openhab.core.automation.type.ModuleType)  # <T>
    @typing.overload
    def getByTags(self, tags: typing.List[java.lang.String]) -> java.util.Collection[_getByTags_0__T]: ...
    _getByTags_1__T = typing.TypeVar('_getByTags_1__T', bound=org.openhab.core.automation.type.ModuleType)  # <T>
    @typing.overload
    def getByTags(self, locale: java.util.Locale, tags: typing.List[java.lang.String]) -> java.util.Collection[_getByTags_1__T]: ...
    @typing.overload
    def getConditions(self, tags: typing.List[java.lang.String]) -> java.util.Collection[org.openhab.core.automation.type.ConditionType]: ...
    @typing.overload
    def getConditions(self, locale: java.util.Locale, tags: typing.List[java.lang.String]) -> java.util.Collection[org.openhab.core.automation.type.ConditionType]: ...
    @typing.overload
    def getTriggers(self, tags: typing.List[java.lang.String]) -> java.util.Collection[org.openhab.core.automation.type.TriggerType]: ...
    @typing.overload
    def getTriggers(self, locale: java.util.Locale, tags: typing.List[java.lang.String]) -> java.util.Collection[org.openhab.core.automation.type.TriggerType]: ...
