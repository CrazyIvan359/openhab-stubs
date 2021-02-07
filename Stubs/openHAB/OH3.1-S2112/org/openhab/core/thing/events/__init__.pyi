import java.lang
import org.openhab.core.events
import org.openhab.core.thing
import org.openhab.core.thing.dto
import typing


class AbstractThingRegistryEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.thing.events.AbstractThingRegistryEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
    """
    def getThing(self) -> org.openhab.core.thing.dto.ThingDTO: ...

class ChannelTriggeredEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.thing.events.ChannelTriggeredEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getChannel(self) -> org.openhab.core.thing.ChannelUID: ...
    def getEvent(self) -> java.lang.String: ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ThingEventFactory(org.openhab.core.events.AbstractEventFactory):
    """
    Java class 'org.openhab.core.thing.events.ThingEventFactory'
    
        Extends:
            org.openhab.core.events.AbstractEventFactory
    
      Constructors:
        * ThingEventFactory()
    
    """
    def __init__(self): ...
    @classmethod
    def createAddedEvent(cls, thing: org.openhab.core.thing.Thing) -> 'ThingAddedEvent': ...
    @classmethod
    def createRemovedEvent(cls, thing: org.openhab.core.thing.Thing) -> 'ThingRemovedEvent': ...
    @classmethod
    def createStatusInfoChangedEvent(cls, thingUID: org.openhab.core.thing.ThingUID, thingStatusInfo: org.openhab.core.thing.ThingStatusInfo, oldThingStatusInfo: org.openhab.core.thing.ThingStatusInfo) -> 'ThingStatusInfoChangedEvent': ...
    @classmethod
    def createStatusInfoEvent(cls, thingUID: org.openhab.core.thing.ThingUID, thingStatusInfo: org.openhab.core.thing.ThingStatusInfo) -> 'ThingStatusInfoEvent': ...
    @typing.overload
    def createTriggerEvent(self, topic: java.lang.String, payload: java.lang.String, source: java.lang.String) -> ChannelTriggeredEvent: ...
    @classmethod
    @typing.overload
    def createTriggerEvent(cls, event: java.lang.String, channel: org.openhab.core.thing.ChannelUID) -> ChannelTriggeredEvent: ...
    @classmethod
    def createUpdateEvent(cls, thing: org.openhab.core.thing.Thing, oldThing: org.openhab.core.thing.Thing) -> 'ThingUpdatedEvent': ...
    class TriggerEventPayloadBean(java.lang.Object):
        """
        Java class 'org.openhab.core.thing.events.ThingEventFactory$TriggerEventPayloadBean'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * TriggerEventPayloadBean(java.lang.String, java.lang.String)
        
        """
        def __init__(self, event: java.lang.String, channel: java.lang.String): ...
        def getChannel(self) -> java.lang.String: ...
        def getEvent(self) -> java.lang.String: ...

class ThingStatusInfoChangedEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.thing.events.ThingStatusInfoChangedEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getOldStatusInfo(self) -> org.openhab.core.thing.ThingStatusInfo: ...
    def getStatusInfo(self) -> org.openhab.core.thing.ThingStatusInfo: ...
    def getThingUID(self) -> org.openhab.core.thing.ThingUID: ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ThingStatusInfoEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.thing.events.ThingStatusInfoEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getStatusInfo(self) -> org.openhab.core.thing.ThingStatusInfo: ...
    def getThingUID(self) -> org.openhab.core.thing.ThingUID: ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ThingAddedEvent(AbstractThingRegistryEvent):
    """
    Java class 'org.openhab.core.thing.events.ThingAddedEvent'
    
        Extends:
            org.openhab.core.thing.events.AbstractThingRegistryEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ThingRemovedEvent(AbstractThingRegistryEvent):
    """
    Java class 'org.openhab.core.thing.events.ThingRemovedEvent'
    
        Extends:
            org.openhab.core.thing.events.AbstractThingRegistryEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ThingUpdatedEvent(AbstractThingRegistryEvent):
    """
    Java class 'org.openhab.core.thing.events.ThingUpdatedEvent'
    
        Extends:
            org.openhab.core.thing.events.AbstractThingRegistryEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getOldThing(self) -> org.openhab.core.thing.dto.ThingDTO: ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
