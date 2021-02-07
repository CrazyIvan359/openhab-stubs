import java.lang
import org.openhab.core.events
import typing


class StartlevelEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.events.system.StartlevelEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getStartlevel(self) -> int: ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class SystemEventFactory(org.openhab.core.events.AbstractEventFactory):
    """
    Java class 'org.openhab.core.events.system.SystemEventFactory'
    
        Extends:
            org.openhab.core.events.AbstractEventFactory
    
      Constructors:
        * SystemEventFactory()
    
    """
    def __init__(self): ...
    @typing.overload
    def createStartlevelEvent(self, topic: java.lang.String, payload: java.lang.String, source: java.lang.String) -> StartlevelEvent: ...
    @classmethod
    @typing.overload
    def createStartlevelEvent(cls, startlevel: int) -> StartlevelEvent: ...
    class SystemEventPayloadBean(java.lang.Object):
        """
        Java class 'org.openhab.core.events.system.SystemEventFactory$SystemEventPayloadBean'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * SystemEventPayloadBean(java.lang.Integer)
        
        """
        def __init__(self, startlevel: int): ...
        def getStartlevel(self) -> int: ...
