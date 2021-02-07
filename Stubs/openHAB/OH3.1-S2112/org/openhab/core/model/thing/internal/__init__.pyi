import java.lang
import java.util
import org.openhab.core.common.registry
import org.openhab.core.config.core
import org.openhab.core.model.core
import org.openhab.core.model.item
import org.openhab.core.service
import org.openhab.core.thing
import org.openhab.core.thing.binding
import org.openhab.core.thing.link
import typing


_AbstractProviderLazyNullness__E = typing.TypeVar('_AbstractProviderLazyNullness__E')  # <E>
class AbstractProviderLazyNullness(org.openhab.core.common.registry.AbstractProvider[_AbstractProviderLazyNullness__E], typing.Generic[_AbstractProviderLazyNullness__E]):
    """
    Java class 'org.openhab.core.model.thing.internal.AbstractProviderLazyNullness'
    
        Extends:
            org.openhab.core.common.registry.AbstractProvider
    
      Constructors:
        * AbstractProviderLazyNullness()
    
    """
    def __init__(self): ...

class GenericItemChannelLinkProvider(org.openhab.core.common.registry.AbstractProvider[org.openhab.core.thing.link.ItemChannelLink], org.openhab.core.model.item.BindingConfigReader, org.openhab.core.thing.link.ItemChannelLinkProvider):
    """
    Java class 'org.openhab.core.model.thing.internal.GenericItemChannelLinkProvider'
    
        Extends:
            org.openhab.core.common.registry.AbstractProvider
    
        Interfaces:
            org.openhab.core.model.item.BindingConfigReader,
            org.openhab.core.thing.link.ItemChannelLinkProvider
    
      Constructors:
        * GenericItemChannelLinkProvider()
    
    """
    def __init__(self): ...
    def getAll(self) -> java.util.Collection[org.openhab.core.thing.link.ItemChannelLink]: ...
    def getBindingType(self) -> java.lang.String: ...
    def processBindingConfiguration(self, string: java.lang.String, string2: java.lang.String, string3: java.lang.String, string4: java.lang.String, configuration: org.openhab.core.config.core.Configuration) -> None: ...
    def startConfigurationUpdate(self, string: java.lang.String) -> None: ...
    def stopConfigurationUpdate(self, string: java.lang.String) -> None: ...
    def validateItemType(self, string: java.lang.String, string2: java.lang.String) -> None: ...

class GenericThingProvider(AbstractProviderLazyNullness[org.openhab.core.thing.Thing], org.openhab.core.thing.ThingProvider, org.openhab.core.model.core.ModelRepositoryChangeListener, org.openhab.core.service.ReadyService.ReadyTracker):
    """
    Java class 'org.openhab.core.model.thing.internal.GenericThingProvider'
    
        Extends:
            org.openhab.core.model.thing.internal.AbstractProviderLazyNullness
    
        Interfaces:
            org.openhab.core.thing.ThingProvider,
            org.openhab.core.model.core.ModelRepositoryChangeListener,
            org.openhab.core.service.ReadyService.ReadyTracker
    
      Constructors:
        * GenericThingProvider()
    
    """
    def __init__(self): ...
    def activate(self) -> None: ...
    def getAll(self) -> java.util.Collection[org.openhab.core.thing.Thing]: ...
    def merge(self, object: typing.Any, object2: typing.Any) -> None: ...
    def modelChanged(self, string: java.lang.String, eventType: org.openhab.core.model.core.EventType) -> None: ...
    def onReadyMarkerAdded(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
    def onReadyMarkerRemoved(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
    def setReadyService(self, readyService: org.openhab.core.service.ReadyService) -> None: ...
    def thingHandlerFactoryAdded(self, thingHandlerFactory: org.openhab.core.thing.binding.ThingHandlerFactory) -> None: ...
    def unsetReadyService(self, readyService: org.openhab.core.service.ReadyService) -> None: ...
