import java.lang
import org.openhab.core.config.discovery
import org.openhab.core.config.discovery.dto
import org.openhab.core.events
import typing


class AbstractInboxEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.config.discovery.inbox.events.AbstractInboxEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
      Constructors:
        * AbstractInboxEvent(java.lang.String, java.lang.String, org.openhab.core.config.discovery.dto.DiscoveryResultDTO)
    
    """
    def __init__(self, topic: java.lang.String, payload: java.lang.String, discoveryResult: org.openhab.core.config.discovery.dto.DiscoveryResultDTO): ...
    def getDiscoveryResult(self) -> org.openhab.core.config.discovery.dto.DiscoveryResultDTO: ...

class InboxEventFactory(org.openhab.core.events.AbstractEventFactory):
    """
    Java class 'org.openhab.core.config.discovery.inbox.events.InboxEventFactory'
    
        Extends:
            org.openhab.core.events.AbstractEventFactory
    
      Constructors:
        * InboxEventFactory()
    
    """
    def __init__(self): ...
    @classmethod
    def createAddedEvent(cls, discoveryResult: org.openhab.core.config.discovery.DiscoveryResult) -> 'InboxAddedEvent': ...
    @classmethod
    def createRemovedEvent(cls, discoveryResult: org.openhab.core.config.discovery.DiscoveryResult) -> 'InboxRemovedEvent': ...
    @classmethod
    def createUpdatedEvent(cls, discoveryResult: org.openhab.core.config.discovery.DiscoveryResult) -> 'InboxUpdatedEvent': ...

class InboxAddedEvent(AbstractInboxEvent):
    """
    Java class 'org.openhab.core.config.discovery.inbox.events.InboxAddedEvent'
    
        Extends:
            org.openhab.core.config.discovery.inbox.events.AbstractInboxEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class InboxRemovedEvent(AbstractInboxEvent):
    """
    Java class 'org.openhab.core.config.discovery.inbox.events.InboxRemovedEvent'
    
        Extends:
            org.openhab.core.config.discovery.inbox.events.AbstractInboxEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class InboxUpdatedEvent(AbstractInboxEvent):
    """
    Java class 'org.openhab.core.config.discovery.inbox.events.InboxUpdatedEvent'
    
        Extends:
            org.openhab.core.config.discovery.inbox.events.AbstractInboxEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
