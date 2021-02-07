import java.lang
import java.util
import org.openhab.core.thing
import org.openhab.core.thing.binding
import org.openhab.core.thing.dto
import typing


class ThingHandlerHelper(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.util.ThingHandlerHelper'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    @typing.overload
    def isHandlerInitialized(cls, thing: org.openhab.core.thing.Thing) -> bool: ...
    @classmethod
    @typing.overload
    def isHandlerInitialized(cls, thingStatus: org.openhab.core.thing.ThingStatus) -> bool: ...
    @classmethod
    @typing.overload
    def isHandlerInitialized(cls, handler: org.openhab.core.thing.binding.ThingHandler) -> bool: ...

class ThingHelper(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.util.ThingHelper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ThingHelper()
    
    """
    def __init__(self): ...
    @classmethod
    def addChannelsToThing(cls, thing: org.openhab.core.thing.Thing, channels: typing.Union[java.util.Collection[org.openhab.core.thing.Channel], typing.Sequence[org.openhab.core.thing.Channel]]) -> None: ...
    @classmethod
    @typing.overload
    def ensureUniqueChannels(cls, channels: typing.Union[java.util.Collection[org.openhab.core.thing.Channel], typing.Sequence[org.openhab.core.thing.Channel]]) -> None: ...
    @classmethod
    @typing.overload
    def ensureUniqueChannels(cls, channels: typing.Union[java.util.Collection[org.openhab.core.thing.Channel], typing.Sequence[org.openhab.core.thing.Channel]], channel: org.openhab.core.thing.Channel) -> None: ...
    @classmethod
    @typing.overload
    def ensureUniqueChannels(cls, channels: typing.List[org.openhab.core.thing.Channel]) -> None: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool: ...
    @classmethod
    @typing.overload
    def equals(cls, a: org.openhab.core.thing.Thing, b: org.openhab.core.thing.Thing) -> bool: ...
    @classmethod
    def merge(cls, thing: org.openhab.core.thing.Thing, updatedContents: org.openhab.core.thing.dto.ThingDTO) -> org.openhab.core.thing.Thing: ...
