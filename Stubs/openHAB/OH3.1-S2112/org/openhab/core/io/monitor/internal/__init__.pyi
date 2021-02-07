import java.lang
import java.util
import org.openhab.core.events
import org.openhab.core.service


class EventLogger(org.openhab.core.events.EventSubscriber, org.openhab.core.service.ReadyService.ReadyTracker):
    """
    Java class 'org.openhab.core.io.monitor.internal.EventLogger'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.events.EventSubscriber,
            org.openhab.core.service.ReadyService.ReadyTracker
    
      Constructors:
        * EventLogger(org.openhab.core.service.ReadyService)
    
    """
    def __init__(self, readyService: org.openhab.core.service.ReadyService): ...
    def getEventFilter(self) -> org.openhab.core.events.EventFilter: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def onReadyMarkerAdded(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
    def onReadyMarkerRemoved(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
    def receive(self, event: org.openhab.core.events.Event) -> None: ...
