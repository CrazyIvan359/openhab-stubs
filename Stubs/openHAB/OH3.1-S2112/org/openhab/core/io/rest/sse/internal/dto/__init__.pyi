import java.lang
import org.osgi.dto


class EventDTO(org.osgi.dto.DTO):
    """
    Java class 'org.openhab.core.io.rest.sse.internal.dto.EventDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * EventDTO()
    
      Attributes:
        topic (java.lang.String): field
        payload (java.lang.String): field
        type (java.lang.String): field
    
    """
    topic: java.lang.String = ...
    payload: java.lang.String = ...
    type: java.lang.String = ...
    def __init__(self): ...

class StateDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.sse.internal.dto.StateDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * StateDTO()
    
      Attributes:
        state (java.lang.String): field
        displayState (java.lang.String): field
    
    """
    state: java.lang.String = ...
    displayState: java.lang.String = ...
    def __init__(self): ...
