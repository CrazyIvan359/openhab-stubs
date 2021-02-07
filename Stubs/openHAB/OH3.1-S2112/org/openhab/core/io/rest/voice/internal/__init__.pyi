import java.lang
import java.util
import javax.ws.rs.core
import org.openhab.core.io.rest
import org.openhab.core.voice
import org.openhab.core.voice.text
import typing


class HLIMapper(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.voice.internal.HLIMapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * HLIMapper()
    
    """
    def __init__(self): ...
    @classmethod
    def map(cls, hli: org.openhab.core.voice.text.HumanLanguageInterpreter, locale: java.util.Locale) -> 'HumanLanguageInterpreterDTO': ...

class HumanLanguageInterpreterDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.voice.internal.HumanLanguageInterpreterDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * HumanLanguageInterpreterDTO()
    
      Attributes:
        id (java.lang.String): field
        label (java.lang.String): field
        locales (java.util.Set): field
    
    """
    id: java.lang.String = ...
    label: java.lang.String = ...
    locales: java.util.Set = ...
    def __init__(self): ...

class VoiceDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.voice.internal.VoiceDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * VoiceDTO()
    
      Attributes:
        id (java.lang.String): field
        label (java.lang.String): field
        locale (java.lang.String): field
    
    """
    id: java.lang.String = ...
    label: java.lang.String = ...
    locale: java.lang.String = ...
    def __init__(self): ...

class VoiceMapper(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.voice.internal.VoiceMapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * VoiceMapper()
    
    """
    def __init__(self): ...
    @classmethod
    def map(cls, voice: org.openhab.core.voice.Voice) -> VoiceDTO: ...

class VoiceResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.voice.internal.VoiceResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * VoiceResource(org.openhab.core.io.rest.LocaleService, org.openhab.core.voice.VoiceManager)
    
      Attributes:
        PATH_VOICE (java.lang.String): final static field
    
    """
    PATH_VOICE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, localeService: org.openhab.core.io.rest.LocaleService, voiceManager: org.openhab.core.voice.VoiceManager): ...
    def getDefaultVoice(self) -> javax.ws.rs.core.Response: ...
    def getInterpreter(self, language: java.lang.String, id: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getInterpreters(self, language: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getVoices(self) -> javax.ws.rs.core.Response: ...
    @typing.overload
    def interpret(self, language: java.lang.String, text: java.lang.String) -> javax.ws.rs.core.Response: ...
    @typing.overload
    def interpret(self, language: java.lang.String, text: java.lang.String, id: java.lang.String) -> javax.ws.rs.core.Response: ...
    def say(self, text: java.lang.String, voiceId: java.lang.String, sinkId: java.lang.String) -> javax.ws.rs.core.Response: ...
