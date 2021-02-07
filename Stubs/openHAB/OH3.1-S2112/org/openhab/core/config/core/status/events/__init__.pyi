import java.lang
import org.openhab.core.config.core.status
import org.openhab.core.events


class ConfigStatusEventFactory(org.openhab.core.events.AbstractEventFactory):
    """
    Java class 'org.openhab.core.config.core.status.events.ConfigStatusEventFactory'
    
        Extends:
            org.openhab.core.events.AbstractEventFactory
    
      Constructors:
        * ConfigStatusEventFactory()
    
    """
    def __init__(self): ...

class ConfigStatusInfoEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.config.core.status.events.ConfigStatusInfoEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
      Constructors:
        * ConfigStatusInfoEvent(java.lang.String, org.openhab.core.config.core.status.ConfigStatusInfo)
    
    """
    def __init__(self, topic: java.lang.String, configStatusInfo: org.openhab.core.config.core.status.ConfigStatusInfo): ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
