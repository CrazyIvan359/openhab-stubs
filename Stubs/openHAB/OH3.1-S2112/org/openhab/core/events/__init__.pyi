import java.lang
import java.util
import typing


class Event(java.lang.Object):
    """
    @NonNullByDefault public interface Event
    
        :class:`~org.openhab.core.events.Event` objects are delivered by the :class:`~org.openhab.core.events.EventPublisher`
        through the openHAB event bus. The callback interface :class:`~org.openhab.core.events.EventSubscriber` can be
        implemented in order to receive such events.
    
    
    """
    def getPayload(self) -> java.lang.String: ...
    def getSource(self) -> java.lang.String: ...
    def getTopic(self) -> java.lang.String: ...
    def getType(self) -> java.lang.String: ...

class EventFactory(java.lang.Object):
    """
    @NonNullByDefault public interface EventFactory
    
        An :class:`~org.openhab.core.events.EventFactory` is responsible for creating :class:`~org.openhab.core.events.Event`
        instances of specific event types. Event Factories are used to create new Events
        (:meth:`~org.openhab.core.events.EventFactory.createEvent`) based on the event type, the topic, the payload and the
        source if an event type is supported (:meth:`~org.openhab.core.events.EventFactory.getSupportedEventTypes`).
    
    
    """
    def createEvent(self, eventType: java.lang.String, topic: java.lang.String, payload: java.lang.String, source: java.lang.String) -> Event: ...
    def getSupportedEventTypes(self) -> java.util.Set[java.lang.String]: ...

class EventFilter(java.lang.Object):
    """
    @NonNullByDefault public interface EventFilter
    
        An :class:`~org.openhab.core.events.EventFilter` can be provided by an :class:`~org.openhab.core.events.EventSubscriber`
        in order to receive specific :class:`~org.openhab.core.events.Event`s by an
        :class:`~org.openhab.core.events.EventPublisher` if the filter applies.
    
    
    """
    def apply(self, event: Event) -> bool: ...

class EventPublisher(java.lang.Object):
    """
    public interface EventPublisher
    
        The :class:`~org.openhab.core.events.EventPublisher` posts :class:`~org.openhab.core.events.Event`s through the openHAB
        event bus in an asynchronous way. Posted events can be received by implementing the
        :class:`~org.openhab.core.events.EventSubscriber` callback interface.
    
    
    """
    def post(self, event: Event) -> None: ...

class EventSubscriber(java.lang.Object):
    """
    @NonNullByDefault public interface EventSubscriber
    
        The :class:`~org.openhab.core.events.EventSubscriber` defines the callback interface for receiving events from the
        openHAB event bus.
    
    
    """
    ALL_EVENT_TYPES: typing.ClassVar[java.lang.String] = ...
    def getEventFilter(self) -> EventFilter: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def receive(self, event: Event) -> None: ...

class AbstractEvent(Event):
    """
    Java class 'org.openhab.core.events.AbstractEvent'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.events.Event
    
      Constructors:
        * AbstractEvent(java.lang.String, java.lang.String, java.lang.String)
    
    """
    def __init__(self, topic: java.lang.String, payload: java.lang.String, source: java.lang.String): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getPayload(self) -> java.lang.String: ...
    def getSource(self) -> java.lang.String: ...
    def getTopic(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...

class AbstractEventFactory(EventFactory):
    """
    Java class 'org.openhab.core.events.AbstractEventFactory'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.events.EventFactory
    
      Constructors:
        * AbstractEventFactory(java.util.Set)
    
    """
    def __init__(self, supportedEventTypes: java.util.Set[java.lang.String]): ...
    def createEvent(self, eventType: java.lang.String, topic: java.lang.String, payload: java.lang.String, source: java.lang.String) -> Event: ...
    def getSupportedEventTypes(self) -> java.util.Set[java.lang.String]: ...

_AbstractTypedEventSubscriber__T = typing.TypeVar('_AbstractTypedEventSubscriber__T', bound=Event)  # <T>
class AbstractTypedEventSubscriber(EventSubscriber, typing.Generic[_AbstractTypedEventSubscriber__T]):
    """
    Java class 'org.openhab.core.events.AbstractTypedEventSubscriber'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.events.EventSubscriber
    
    """
    def getEventFilter(self) -> EventFilter: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def receive(self, event: Event) -> None: ...

class TopicEventFilter(EventFilter):
    """
    Java class 'org.openhab.core.events.TopicEventFilter'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.events.EventFilter
    
      Constructors:
        * TopicEventFilter(java.lang.String)
    
    """
    def __init__(self, topicRegex: java.lang.String): ...
    def apply(self, event: Event) -> bool: ...
