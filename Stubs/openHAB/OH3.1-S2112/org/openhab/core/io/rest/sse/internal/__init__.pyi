import java.lang
import java.util
import java.util.function
import javax.ws.rs.sse
import org.openhab.core.events
import org.openhab.core.items
import org.osgi.framework


class SseItemStatesEventBuilder(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.sse.internal.SseItemStatesEventBuilder'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SseItemStatesEventBuilder(org.osgi.framework.BundleContext, org.openhab.core.items.ItemRegistry)
    
    """
    def __init__(self, bundleContext: org.osgi.framework.BundleContext, itemRegistry: org.openhab.core.items.ItemRegistry): ...
    def buildEvent(self, eventBuilder: javax.ws.rs.sse.OutboundSseEvent.Builder, itemNames: java.util.Set[java.lang.String]) -> javax.ws.rs.sse.OutboundSseEvent: ...

class SsePublisher(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.sse.internal.SsePublisher'
    
    """
    def broadcast(self, event: org.openhab.core.events.Event) -> None: ...

class SseSinkItemInfo(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.sse.internal.SseSinkItemInfo'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SseSinkItemInfo()
    
    """
    def __init__(self): ...
    def getConnectionId(self) -> java.lang.String: ...
    @classmethod
    def hasConnectionId(cls, connectionId: java.lang.String) -> java.util.function.Predicate['SseSinkItemInfo']: ...
    @classmethod
    def tracksItem(cls, itemName: java.lang.String) -> java.util.function.Predicate['SseSinkItemInfo']: ...
    def updateTrackedItems(self, itemNames: java.util.Set[java.lang.String]) -> None: ...

class SseSinkTopicInfo(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.sse.internal.SseSinkTopicInfo'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SseSinkTopicInfo(java.lang.String)
    
    """
    def __init__(self, topicFilter: java.lang.String): ...
    @classmethod
    def matchesTopic(cls, topic: java.lang.String) -> java.util.function.Predicate['SseSinkTopicInfo']: ...
