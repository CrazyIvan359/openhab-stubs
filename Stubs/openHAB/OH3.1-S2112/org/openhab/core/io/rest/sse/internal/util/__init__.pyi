import java.lang
import java.util
import javax.ws.rs.sse
import org.openhab.core.events
import org.openhab.core.io.rest.sse.internal.dto


class SseUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.sse.internal.util.SseUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SseUtil()
    
    """
    def __init__(self): ...
    @classmethod
    def buildDTO(cls, event: org.openhab.core.events.Event) -> org.openhab.core.io.rest.sse.internal.dto.EventDTO: ...
    @classmethod
    def buildEvent(cls, eventBuilder: javax.ws.rs.sse.OutboundSseEvent.Builder, event: org.openhab.core.io.rest.sse.internal.dto.EventDTO) -> javax.ws.rs.sse.OutboundSseEvent: ...
    @classmethod
    def convertToRegex(cls, topicFilter: java.lang.String) -> java.util.List[java.lang.String]: ...
    @classmethod
    def isValidTopicFilter(cls, topicFilter: java.lang.String) -> bool: ...
