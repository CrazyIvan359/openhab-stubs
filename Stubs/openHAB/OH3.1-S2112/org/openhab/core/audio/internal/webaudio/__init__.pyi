import java.lang
import java.util
import org.openhab.core.audio
import org.openhab.core.events
import org.openhab.core.library.types
import typing


class PlayURLEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.audio.internal.webaudio.PlayURLEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
      Constructors:
        * PlayURLEvent(java.lang.String, java.lang.String, java.lang.String)
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, topic: java.lang.String, payload: java.lang.String, url: java.lang.String): ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class WebAudioAudioSink(org.openhab.core.audio.AudioSink):
    """
    Java class 'org.openhab.core.audio.internal.webaudio.WebAudioAudioSink'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.audio.AudioSink
    
      Constructors:
        * WebAudioAudioSink(org.openhab.core.audio.AudioHTTPServer, org.openhab.core.events.EventPublisher)
    
    """
    def __init__(self, audioHTTPServer: org.openhab.core.audio.AudioHTTPServer, eventPublisher: org.openhab.core.events.EventPublisher): ...
    def getId(self) -> java.lang.String: ...
    def getLabel(self, locale: java.util.Locale) -> java.lang.String: ...
    def getSupportedFormats(self) -> java.util.Set[org.openhab.core.audio.AudioFormat]: ...
    def getSupportedStreams(self) -> java.util.Set[typing.Type[org.openhab.core.audio.AudioStream]]: ...
    def getVolume(self) -> org.openhab.core.library.types.PercentType: ...
    def process(self, audioStream: org.openhab.core.audio.AudioStream) -> None: ...
    def setVolume(self, volume: org.openhab.core.library.types.PercentType) -> None: ...

class WebAudioEventFactory(org.openhab.core.events.AbstractEventFactory):
    """
    Java class 'org.openhab.core.audio.internal.webaudio.WebAudioEventFactory'
    
        Extends:
            org.openhab.core.events.AbstractEventFactory
    
      Constructors:
        * WebAudioEventFactory()
    
    """
    def __init__(self): ...
    @classmethod
    def createPlayURLEvent(cls, url: java.lang.String) -> PlayURLEvent: ...
