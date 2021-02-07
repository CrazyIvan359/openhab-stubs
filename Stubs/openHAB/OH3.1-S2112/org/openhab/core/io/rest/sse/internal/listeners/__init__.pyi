import java.lang
import java.util
import org.openhab.core.events
import org.openhab.core.io.rest.sse.internal


class SseEventSubscriber(org.openhab.core.events.EventSubscriber):
    """
    Java class 'org.openhab.core.io.rest.sse.internal.listeners.SseEventSubscriber'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.events.EventSubscriber
    
      Constructors:
        * SseEventSubscriber(org.openhab.core.io.rest.sse.internal.SsePublisher)
    
    """
    def __init__(self, ssePublisher: org.openhab.core.io.rest.sse.internal.SsePublisher): ...
    def getEventFilter(self) -> org.openhab.core.events.EventFilter: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def receive(self, event: org.openhab.core.events.Event) -> None: ...
