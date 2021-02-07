import java.lang
import java.util
import org.openhab.core.automation
import org.openhab.core.automation.handler
import org.openhab.core.automation.module.provider.i18n
import org.openhab.core.automation.type
import org.openhab.core.common.registry
import typing


class AnnotatedActionModuleTypeProvider(org.openhab.core.automation.handler.BaseModuleHandlerFactory, org.openhab.core.automation.type.ModuleTypeProvider):
    """
    Java class 'org.openhab.core.automation.internal.module.provider.AnnotatedActionModuleTypeProvider'
    
        Extends:
            org.openhab.core.automation.handler.BaseModuleHandlerFactory
    
        Interfaces:
            org.openhab.core.automation.type.ModuleTypeProvider
    
      Constructors:
        * AnnotatedActionModuleTypeProvider(org.openhab.core.automation.module.provider.i18n.ModuleTypeI18nService)
    
    """
    def __init__(self, moduleTypeI18nService: org.openhab.core.automation.module.provider.i18n.ModuleTypeI18nService): ...
    def addActionProvider(self, actionProvider: org.openhab.core.automation.AnnotatedActions, properties: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def addProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[org.openhab.core.automation.type.ModuleType]) -> None: ...
    def getAll(self) -> java.util.Collection[org.openhab.core.automation.type.ModuleType]: ...
    _getModuleType__T = typing.TypeVar('_getModuleType__T', bound=org.openhab.core.automation.type.ModuleType)  # <T>
    def getModuleType(self, UID: java.lang.String, locale: java.util.Locale) -> _getModuleType__T: ...
    _getModuleTypes__T = typing.TypeVar('_getModuleTypes__T', bound=org.openhab.core.automation.type.ModuleType)  # <T>
    def getModuleTypes(self, locale: java.util.Locale) -> java.util.Collection[_getModuleTypes__T]: ...
    def getTypes(self) -> java.util.Collection[java.lang.String]: ...
    def removeActionProvider(self, actionProvider: org.openhab.core.automation.AnnotatedActions, properties: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def removeProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[org.openhab.core.automation.type.ModuleType]) -> None: ...
