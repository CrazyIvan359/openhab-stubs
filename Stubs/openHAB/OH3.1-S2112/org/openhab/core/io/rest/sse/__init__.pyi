import java.lang
import java.util
import javax.servlet.http
import javax.ws.rs.sse
import org.openhab.core.events
import org.openhab.core.io.rest
import org.openhab.core.io.rest.sse.internal
import org.openhab.core.items.events
import typing


class SseResource(org.openhab.core.io.rest.RESTResource, org.openhab.core.io.rest.sse.internal.SsePublisher):
    """
    Java class 'org.openhab.core.io.rest.sse.SseResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource,
            org.openhab.core.io.rest.sse.internal.SsePublisher
    
      Constructors:
        * SseResource(org.openhab.core.io.rest.sse.internal.SseItemStatesEventBuilder)
    
      Attributes:
        PATH_EVENTS (java.lang.String): final static field
    
    """
    PATH_EVENTS: typing.ClassVar[java.lang.String] = ...
    def __init__(self, itemStatesEventBuilder: org.openhab.core.io.rest.sse.internal.SseItemStatesEventBuilder): ...
    def broadcast(self, event: org.openhab.core.events.Event) -> None: ...
    def deactivate(self) -> None: ...
    def getStateEvents(self, sseEventSink: javax.ws.rs.sse.SseEventSink, response: javax.servlet.http.HttpServletResponse) -> None: ...
    def handleEventBroadcastItemState(self, stateChangeEvent: org.openhab.core.items.events.ItemStateChangedEvent) -> None: ...
    def listen(self, sseEventSink: javax.ws.rs.sse.SseEventSink, response: javax.servlet.http.HttpServletResponse, eventFilter: java.lang.String) -> None: ...
    def updateTrackedItems(self, connectionId: java.lang.String, itemNames: java.util.Set[java.lang.String]) -> typing.Any: ...
