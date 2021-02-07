import java.lang
import org.openhab.core.events
import org.openhab.core.thing.link
import org.openhab.core.thing.link.dto
import typing


class AbstractItemChannelLinkRegistryEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.thing.link.events.AbstractItemChannelLinkRegistryEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
      Constructors:
        * AbstractItemChannelLinkRegistryEvent(java.lang.String, java.lang.String, org.openhab.core.thing.link.dto.ItemChannelLinkDTO)
    
    """
    def __init__(self, topic: java.lang.String, payload: java.lang.String, link: org.openhab.core.thing.link.dto.ItemChannelLinkDTO): ...
    def getLink(self) -> org.openhab.core.thing.link.dto.ItemChannelLinkDTO: ...

class LinkEventFactory(org.openhab.core.events.AbstractEventFactory):
    """
    Java class 'org.openhab.core.thing.link.events.LinkEventFactory'
    
        Extends:
            org.openhab.core.events.AbstractEventFactory
    
      Constructors:
        * LinkEventFactory()
    
    """
    def __init__(self): ...
    @classmethod
    def createItemChannelLinkAddedEvent(cls, itemChannelLink: org.openhab.core.thing.link.ItemChannelLink) -> 'ItemChannelLinkAddedEvent': ...
    @classmethod
    def createItemChannelLinkRemovedEvent(cls, itemChannelLink: org.openhab.core.thing.link.ItemChannelLink) -> 'ItemChannelLinkRemovedEvent': ...

class ItemChannelLinkAddedEvent(AbstractItemChannelLinkRegistryEvent):
    """
    Java class 'org.openhab.core.thing.link.events.ItemChannelLinkAddedEvent'
    
        Extends:
            org.openhab.core.thing.link.events.AbstractItemChannelLinkRegistryEvent
    
      Constructors:
        * ItemChannelLinkAddedEvent(java.lang.String, java.lang.String, org.openhab.core.thing.link.dto.ItemChannelLinkDTO)
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, topic: java.lang.String, payload: java.lang.String, link: org.openhab.core.thing.link.dto.ItemChannelLinkDTO): ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ItemChannelLinkRemovedEvent(AbstractItemChannelLinkRegistryEvent):
    """
    Java class 'org.openhab.core.thing.link.events.ItemChannelLinkRemovedEvent'
    
        Extends:
            org.openhab.core.thing.link.events.AbstractItemChannelLinkRegistryEvent
    
      Constructors:
        * ItemChannelLinkRemovedEvent(java.lang.String, java.lang.String, org.openhab.core.thing.link.dto.ItemChannelLinkDTO)
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, topic: java.lang.String, payload: java.lang.String, link: org.openhab.core.thing.link.dto.ItemChannelLinkDTO): ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
