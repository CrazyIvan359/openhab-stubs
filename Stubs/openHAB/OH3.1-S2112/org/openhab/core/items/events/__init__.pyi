import java.lang
import java.util
import org.openhab.core.events
import org.openhab.core.items
import org.openhab.core.items.dto
import org.openhab.core.types
import typing


class AbstractItemEventSubscriber(org.openhab.core.events.EventSubscriber):
    """
    Java class 'org.openhab.core.items.events.AbstractItemEventSubscriber'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.events.EventSubscriber
    
      Constructors:
        * AbstractItemEventSubscriber()
    
    """
    def __init__(self): ...
    def getEventFilter(self) -> org.openhab.core.events.EventFilter: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def receive(self, event: org.openhab.core.events.Event) -> None: ...

class AbstractItemRegistryEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.items.events.AbstractItemRegistryEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
    """
    def getItem(self) -> org.openhab.core.items.dto.ItemDTO: ...

class ItemEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.items.events.ItemEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
      Constructors:
        * ItemEvent(java.lang.String, java.lang.String, java.lang.String, java.lang.String)
    
    """
    def __init__(self, topic: java.lang.String, payload: java.lang.String, itemName: java.lang.String, source: java.lang.String): ...
    def getItemName(self) -> java.lang.String: ...

class ItemEventFactory(org.openhab.core.events.AbstractEventFactory):
    """
    Java class 'org.openhab.core.items.events.ItemEventFactory'
    
        Extends:
            org.openhab.core.events.AbstractEventFactory
    
      Constructors:
        * ItemEventFactory()
    
    """
    def __init__(self): ...
    @classmethod
    def createAddedEvent(cls, item: org.openhab.core.items.Item) -> 'ItemAddedEvent': ...
    @classmethod
    @typing.overload
    def createCommandEvent(cls, itemName: java.lang.String, command: org.openhab.core.types.Command) -> 'ItemCommandEvent': ...
    @classmethod
    @typing.overload
    def createCommandEvent(cls, itemName: java.lang.String, command: org.openhab.core.types.Command, source: java.lang.String) -> 'ItemCommandEvent': ...
    @classmethod
    def createGroupStateChangedEvent(cls, itemName: java.lang.String, memberName: java.lang.String, newState: org.openhab.core.types.State, oldState: org.openhab.core.types.State) -> 'GroupItemStateChangedEvent': ...
    @classmethod
    def createRemovedEvent(cls, item: org.openhab.core.items.Item) -> 'ItemRemovedEvent': ...
    @classmethod
    def createStateChangedEvent(cls, itemName: java.lang.String, newState: org.openhab.core.types.State, oldState: org.openhab.core.types.State) -> 'ItemStateChangedEvent': ...
    @classmethod
    @typing.overload
    def createStateEvent(cls, itemName: java.lang.String, state: org.openhab.core.types.State) -> ItemEvent: ...
    @classmethod
    @typing.overload
    def createStateEvent(cls, itemName: java.lang.String, state: org.openhab.core.types.State, source: java.lang.String) -> 'ItemStateEvent': ...
    @classmethod
    def createStatePredictedEvent(cls, itemName: java.lang.String, state: org.openhab.core.types.State, isConfirmation: bool) -> 'ItemStatePredictedEvent': ...
    @classmethod
    def createUpdateEvent(cls, item: org.openhab.core.items.Item, oldItem: org.openhab.core.items.Item) -> 'ItemUpdatedEvent': ...

class ItemAddedEvent(AbstractItemRegistryEvent):
    """
    Java class 'org.openhab.core.items.events.ItemAddedEvent'
    
        Extends:
            org.openhab.core.items.events.AbstractItemRegistryEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ItemCommandEvent(ItemEvent):
    """
    Java class 'org.openhab.core.items.events.ItemCommandEvent'
    
        Extends:
            org.openhab.core.items.events.ItemEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getItemCommand(self) -> org.openhab.core.types.Command: ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ItemRemovedEvent(AbstractItemRegistryEvent):
    """
    Java class 'org.openhab.core.items.events.ItemRemovedEvent'
    
        Extends:
            org.openhab.core.items.events.AbstractItemRegistryEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ItemStateChangedEvent(ItemEvent):
    """
    Java class 'org.openhab.core.items.events.ItemStateChangedEvent'
    
        Extends:
            org.openhab.core.items.events.ItemEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getItemState(self) -> org.openhab.core.types.State: ...
    def getOldItemState(self) -> org.openhab.core.types.State: ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ItemStateEvent(ItemEvent):
    """
    Java class 'org.openhab.core.items.events.ItemStateEvent'
    
        Extends:
            org.openhab.core.items.events.ItemEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getItemState(self) -> org.openhab.core.types.State: ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ItemStatePredictedEvent(ItemEvent):
    """
    Java class 'org.openhab.core.items.events.ItemStatePredictedEvent'
    
        Extends:
            org.openhab.core.items.events.ItemEvent
    
      Constructors:
        * ItemStatePredictedEvent(java.lang.String, java.lang.String, java.lang.String, org.openhab.core.types.State, boolean)
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, topic: java.lang.String, payload: java.lang.String, itemName: java.lang.String, predictedState: org.openhab.core.types.State, isConfirmation: bool): ...
    def getPredictedState(self) -> org.openhab.core.types.State: ...
    def getType(self) -> java.lang.String: ...
    def isConfirmation(self) -> bool: ...
    def toString(self) -> java.lang.String: ...

class ItemUpdatedEvent(AbstractItemRegistryEvent):
    """
    Java class 'org.openhab.core.items.events.ItemUpdatedEvent'
    
        Extends:
            org.openhab.core.items.events.AbstractItemRegistryEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getOldItem(self) -> org.openhab.core.items.dto.ItemDTO: ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class GroupItemStateChangedEvent(ItemStateChangedEvent):
    """
    Java class 'org.openhab.core.items.events.GroupItemStateChangedEvent'
    
        Extends:
            org.openhab.core.items.events.ItemStateChangedEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def getMemberName(self) -> java.lang.String: ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
