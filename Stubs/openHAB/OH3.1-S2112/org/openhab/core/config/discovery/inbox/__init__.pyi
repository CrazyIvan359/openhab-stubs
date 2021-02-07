import java.lang
import java.util
import java.util.function
import java.util.stream
import org.openhab.core.config.discovery
import org.openhab.core.thing


class Inbox(java.lang.Object):
    """
    @NonNullByDefault public interface Inbox
    
        The :class:`~org.openhab.core.config.discovery.inbox.Inbox` is a service interface providing a container for discovered
        :code:`Thing`s (e.g. found by a :class:`~org.openhab.core.config.discovery.DiscoveryService`) as
        :class:`~org.openhab.core.config.discovery.DiscoveryResult`s.
    
        A :class:`~org.openhab.core.config.discovery.DiscoveryResult` entry in this container is not a full configured
        :code:`Thing` and therefore no :code:`Thing` exists for it. A
        :class:`~org.openhab.core.config.discovery.DiscoveryResult` can be marked to be ignored, so that a specific
        :code:`Thing` is not considered to get part of the system.
    
        This container offers a listener registry for :class:`~org.openhab.core.config.discovery.inbox.InboxListener`s which are
        notified if a :class:`~org.openhab.core.config.discovery.DiscoveryResult` is added, updated or removed.
    
        Also see:
            :class:`~org.openhab.core.config.discovery.inbox.InboxListener`
    
    
    """
    def add(self, result: org.openhab.core.config.discovery.DiscoveryResult) -> bool: ...
    def addInboxListener(self, listener: 'InboxListener') -> None: ...
    def approve(self, thingUID: org.openhab.core.thing.ThingUID, label: java.lang.String, newThingId: java.lang.String) -> org.openhab.core.thing.Thing: ...
    def getAll(self) -> java.util.List[org.openhab.core.config.discovery.DiscoveryResult]: ...
    def remove(self, thingUID: org.openhab.core.thing.ThingUID) -> bool: ...
    def removeInboxListener(self, listener: 'InboxListener') -> None: ...
    def setFlag(self, thingUID: org.openhab.core.thing.ThingUID, flag: org.openhab.core.config.discovery.DiscoveryResultFlag) -> None: ...
    def stream(self) -> java.util.stream.Stream[org.openhab.core.config.discovery.DiscoveryResult]: ...

class InboxAutoApprovePredicate(java.util.function.Predicate[org.openhab.core.config.discovery.DiscoveryResult]):
    """
    Java class 'org.openhab.core.config.discovery.inbox.InboxAutoApprovePredicate'
    
        Interfaces:
            java.util.function.Predicate
    
    """

class InboxListener(java.lang.Object):
    """
    @NonNullByDefault public interface InboxListener
    
        The :class:`~org.openhab.core.config.discovery.inbox.InboxListener` interface for receiving
        :class:`~org.openhab.core.config.discovery.inbox.Inbox` events.
    
        A class that is interested in processing :class:`~org.openhab.core.config.discovery.inbox.Inbox` events fired
        synchronously by the :class:`~org.openhab.core.config.discovery.inbox.Inbox` service has to implement this interface.
    
        Also see:
            :class:`~org.openhab.core.config.discovery.inbox.Inbox`
    
    
    """
    def thingAdded(self, source: Inbox, result: org.openhab.core.config.discovery.DiscoveryResult) -> None: ...
    def thingRemoved(self, source: Inbox, result: org.openhab.core.config.discovery.DiscoveryResult) -> None: ...
    def thingUpdated(self, source: Inbox, result: org.openhab.core.config.discovery.DiscoveryResult) -> None: ...

class InboxPredicates(java.lang.Object):
    """
    Java class 'org.openhab.core.config.discovery.inbox.InboxPredicates'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * InboxPredicates()
    
    """
    def __init__(self): ...
    @classmethod
    def forBinding(cls, bindingId: java.lang.String) -> java.util.function.Predicate[org.openhab.core.config.discovery.DiscoveryResult]: ...
    @classmethod
    def forThingTypeUID(cls, uid: org.openhab.core.thing.ThingTypeUID) -> java.util.function.Predicate[org.openhab.core.config.discovery.DiscoveryResult]: ...
    @classmethod
    def forThingUID(cls, thingUID: org.openhab.core.thing.ThingUID) -> java.util.function.Predicate[org.openhab.core.config.discovery.DiscoveryResult]: ...
    @classmethod
    def withFlag(cls, flag: org.openhab.core.config.discovery.DiscoveryResultFlag) -> java.util.function.Predicate[org.openhab.core.config.discovery.DiscoveryResult]: ...
    @classmethod
    def withProperty(cls, propertyName: java.lang.String, propertyValue: java.lang.String) -> java.util.function.Predicate[org.openhab.core.config.discovery.DiscoveryResult]: ...
    @classmethod
    def withRepresentationProperty(cls, propertyName: java.lang.String) -> java.util.function.Predicate[org.openhab.core.config.discovery.DiscoveryResult]: ...
    @classmethod
    def withRepresentationPropertyValue(cls, propertyValue: java.lang.String) -> java.util.function.Predicate[org.openhab.core.config.discovery.DiscoveryResult]: ...
