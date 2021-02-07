import java.lang
import java.util
import javax.ws.rs.core
import org.openhab.core.audio
import org.openhab.core.io.rest
import typing


class AudioMapper(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.audio.internal.AudioMapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * AudioMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, sink: org.openhab.core.audio.AudioSink, locale: java.util.Locale) -> 'AudioSinkDTO': ...
    @classmethod
    @typing.overload
    def map(cls, source: org.openhab.core.audio.AudioSource, locale: java.util.Locale) -> 'AudioSourceDTO': ...

class AudioResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.audio.internal.AudioResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * AudioResource(org.openhab.core.audio.AudioManager, org.openhab.core.io.rest.LocaleService)
    
      Attributes:
        PATH_AUDIO (java.lang.String): final static field
    
    """
    PATH_AUDIO: typing.ClassVar[java.lang.String] = ...
    def __init__(self, audioManager: org.openhab.core.audio.AudioManager, localeService: org.openhab.core.io.rest.LocaleService): ...
    def getDefaultSink(self, language: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getDefaultSource(self, language: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getSinks(self, language: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getSources(self, language: java.lang.String) -> javax.ws.rs.core.Response: ...

class AudioSinkDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.audio.internal.AudioSinkDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * AudioSinkDTO(java.lang.String, java.lang.String)
    
      Attributes:
        id (java.lang.String): field
        label (java.lang.String): field
    
    """
    id: java.lang.String = ...
    label: java.lang.String = ...
    def __init__(self, id: java.lang.String, label: java.lang.String): ...

class AudioSourceDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.audio.internal.AudioSourceDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * AudioSourceDTO(java.lang.String, java.lang.String)
    
      Attributes:
        id (java.lang.String): field
        label (java.lang.String): field
    
    """
    id: java.lang.String = ...
    label: java.lang.String = ...
    def __init__(self, id: java.lang.String, label: java.lang.String): ...
