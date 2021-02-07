import java.lang
import java.util
import org
import org.openhab.core.common.registry
import org.openhab.core.config.core
import org.openhab.core.items
import org.openhab.core.storage
import org.openhab.core.thing
import typing


class AbstractLink(org.openhab.core.common.registry.Identifiable[java.lang.String]):
    """
    Java class 'org.openhab.core.thing.link.AbstractLink'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.common.registry.Identifiable
    
      Constructors:
        * AbstractLink(java.lang.String)
    
    """
    def __init__(self, itemName: java.lang.String): ...
    def equals(self, obj: typing.Any) -> bool: ...
    @classmethod
    def getIDFor(cls, itemName: java.lang.String, uid: org.openhab.core.thing.UID) -> java.lang.String: ...
    def getItemName(self) -> java.lang.String: ...
    def getLinkedUID(self) -> org.openhab.core.thing.UID: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    @typing.overload
    def getUID(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

_AbstractLinkRegistry__L = typing.TypeVar('_AbstractLinkRegistry__L', bound=AbstractLink)  # <L>
_AbstractLinkRegistry__P = typing.TypeVar('_AbstractLinkRegistry__P', bound=org.openhab.core.common.registry.Provider)  # <P>
class AbstractLinkRegistry(org.openhab.core.common.registry.AbstractRegistry[_AbstractLinkRegistry__L, java.lang.String, _AbstractLinkRegistry__P], typing.Generic[_AbstractLinkRegistry__L, _AbstractLinkRegistry__P]):
    """
    Java class 'org.openhab.core.thing.link.AbstractLinkRegistry'
    
        Extends:
            org.openhab.core.common.registry.AbstractRegistry
    
    """
    def getLinkedItemNames(self, uid: org.openhab.core.thing.UID) -> java.util.Set[java.lang.String]: ...
    @typing.overload
    def getLinks(self, itemName: java.lang.String) -> java.util.Set[_AbstractLinkRegistry__L]: ...
    @typing.overload
    def getLinks(self, uid: org.openhab.core.thing.UID) -> java.util.Set[_AbstractLinkRegistry__L]: ...
    @typing.overload
    def isLinked(self, itemName: java.lang.String) -> bool: ...
    @typing.overload
    def isLinked(self, itemName: java.lang.String, uid: org.openhab.core.thing.UID) -> bool: ...
    @typing.overload
    def isLinked(self, uid: org.openhab.core.thing.UID) -> bool: ...

class ItemChannelLinkProvider(org.openhab.core.common.registry.Provider[org.openhab.core.thing.link.ItemChannelLink]):
    """
    Java class 'org.openhab.core.thing.link.ItemChannelLinkProvider'
    
        Interfaces:
            org.openhab.core.common.registry.Provider
    
    """

class ItemChannelLink(AbstractLink):
    """
    Java class 'org.openhab.core.thing.link.ItemChannelLink'
    
        Extends:
            org.openhab.core.thing.link.AbstractLink
    
      Constructors:
        * ItemChannelLink(java.lang.String, org.openhab.core.thing.ChannelUID, org.openhab.core.config.core.Configuration)
        * ItemChannelLink(java.lang.String, org.openhab.core.thing.ChannelUID)
    
    """
    @typing.overload
    def __init__(self, itemName: java.lang.String, channelUID: org.openhab.core.thing.ChannelUID): ...
    @typing.overload
    def __init__(self, itemName: java.lang.String, channelUID: org.openhab.core.thing.ChannelUID, configuration: org.openhab.core.config.core.Configuration): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getConfiguration(self) -> org.openhab.core.config.core.Configuration: ...
    @typing.overload
    def getLinkedUID(self) -> org.openhab.core.thing.ChannelUID: ...
    @typing.overload
    def getLinkedUID(self) -> org.openhab.core.thing.UID: ...
    def hashCode(self) -> int: ...

class ItemChannelLinkRegistry(AbstractLinkRegistry[ItemChannelLink, ItemChannelLinkProvider]):
    """
    Java class 'org.openhab.core.thing.link.ItemChannelLinkRegistry'
    
        Extends:
            org.openhab.core.thing.link.AbstractLinkRegistry
    
      Constructors:
        * ItemChannelLinkRegistry(org.openhab.core.thing.ThingRegistry, org.openhab.core.items.ItemRegistry)
    
    """
    def __init__(self, thingRegistry: org.openhab.core.thing.ThingRegistry, itemRegistry: org.openhab.core.items.ItemRegistry): ...
    def getBoundChannels(self, itemName: java.lang.String) -> java.util.Set[org.openhab.core.thing.ChannelUID]: ...
    def getBoundThings(self, itemName: java.lang.String) -> java.util.Set[org.openhab.core.thing.Thing]: ...
    def getLinkedItemNames(self, uid: org.openhab.core.thing.UID) -> java.util.Set[java.lang.String]: ...
    def getLinkedItems(self, uid: org.openhab.core.thing.UID) -> java.util.Set[org.openhab.core.items.Item]: ...
    def removeLinksForThing(self, thingUID: org.openhab.core.thing.ThingUID) -> None: ...

class ManagedItemChannelLinkProvider(org.openhab.core.common.registry.DefaultAbstractManagedProvider[ItemChannelLink, java.lang.String], ItemChannelLinkProvider):
    """
    Java class 'org.openhab.core.thing.link.ManagedItemChannelLinkProvider'
    
        Extends:
            org.openhab.core.common.registry.DefaultAbstractManagedProvider
    
        Interfaces:
            org.openhab.core.thing.link.ItemChannelLinkProvider
    
      Constructors:
        * ManagedItemChannelLinkProvider(org.openhab.core.storage.StorageService)
    
    """
    def __init__(self, storageService: org.openhab.core.storage.StorageService): ...
    def removeLinksForThing(self, thingUID: org.openhab.core.thing.ThingUID) -> None: ...
