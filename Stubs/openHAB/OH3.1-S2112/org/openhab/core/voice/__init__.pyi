import java.lang
import java.util
import org.openhab.core.audio
import org.openhab.core.library.types
import org.openhab.core.voice.text
import typing


class KSEvent(java.lang.Object):
    """
    public interface KSEvent
    
        A tagging interface for keyword spotting events.
    
    
    """

class KSException(java.lang.Exception):
    """
    Java class 'org.openhab.core.voice.KSException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * KSException(java.lang.Throwable)
        * KSException(java.lang.String)
        * KSException(java.lang.String, java.lang.Throwable)
        * KSException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, message: java.lang.String): ...
    @typing.overload
    def __init__(self, message: java.lang.String, cause: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, cause: java.lang.Throwable): ...

class KSListener(java.lang.Object):
    """
    public interface KSListener
    
        The listener interface for receiving :class:`~org.openhab.core.voice.KSEvent` events. A class interested in processing
        :class:`~org.openhab.core.voice.KSEvent` events implements this interface, and its instances are passed to the
        :code:`KSService`'s :code:`spot()` method. Such instances are then targeted for various
        :class:`~org.openhab.core.voice.KSEvent` events corresponding to the keyword spotting process.
    
    
    """
    def ksEventReceived(self, ksEvent: KSEvent) -> None: ...

class KSService(java.lang.Object):
    """
    public interface KSService
    
        This is the interface that a keyword spotting service has to implement.
    
    
    """
    def getId(self) -> java.lang.String: ...
    def getLabel(self, locale: java.util.Locale) -> java.lang.String: ...
    def getSupportedFormats(self) -> java.util.Set[org.openhab.core.audio.AudioFormat]: ...
    def getSupportedLocales(self) -> java.util.Set[java.util.Locale]: ...
    def spot(self, ksListener: KSListener, audioStream: org.openhab.core.audio.AudioStream, locale: java.util.Locale, keyword: java.lang.String) -> 'KSServiceHandle': ...

class KSServiceHandle(java.lang.Object):
    """
    public interface KSServiceHandle
    
        An handle to a :class:`~org.openhab.core.voice.KSService`
    
    
    """
    def abort(self) -> None: ...

class STTEvent(java.lang.Object):
    """
    public interface STTEvent
    
        A tagging interface for speech-to-text events.
    
    
    """

class STTException(java.lang.Exception):
    """
    Java class 'org.openhab.core.voice.STTException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * STTException(java.lang.Throwable)
        * STTException(java.lang.String)
        * STTException(java.lang.String, java.lang.Throwable)
        * STTException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, message: java.lang.String): ...
    @typing.overload
    def __init__(self, message: java.lang.String, cause: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, cause: java.lang.Throwable): ...

class STTListener(java.lang.Object):
    """
    public interface STTListener
    
        The listener interface for receiving :class:`~org.openhab.core.voice.STTEvent` events. A class interested in processing
        :class:`~org.openhab.core.voice.STTEvent` events implements this interface, and its instances are passed to the
        :code:`STTService`'s :code:`recognize()` method. Such instances are then targeted for various
        :class:`~org.openhab.core.voice.STTEvent` events corresponding to the speech recognition process.
    
    
    """
    def sttEventReceived(self, sttEvent: STTEvent) -> None: ...

class STTService(java.lang.Object):
    """
    public interface STTService
    
        This is the interface that a speech-to-text service has to implement.
    
    
    """
    def getId(self) -> java.lang.String: ...
    def getLabel(self, locale: java.util.Locale) -> java.lang.String: ...
    def getSupportedFormats(self) -> java.util.Set[org.openhab.core.audio.AudioFormat]: ...
    def getSupportedLocales(self) -> java.util.Set[java.util.Locale]: ...
    def recognize(self, sttListener: STTListener, audioStream: org.openhab.core.audio.AudioStream, locale: java.util.Locale, grammars: java.util.Set[java.lang.String]) -> 'STTServiceHandle': ...

class STTServiceHandle(java.lang.Object):
    """
    public interface STTServiceHandle
    
        An handle to a :class:`~org.openhab.core.voice.STTService`
    
    
    """
    def abort(self) -> None: ...

class TTSException(java.lang.Exception):
    """
    Java class 'org.openhab.core.voice.TTSException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * TTSException(java.lang.Throwable)
        * TTSException(java.lang.String)
        * TTSException(java.lang.String, java.lang.Throwable)
        * TTSException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, message: java.lang.String): ...
    @typing.overload
    def __init__(self, message: java.lang.String, cause: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, cause: java.lang.Throwable): ...

class TTSService(java.lang.Object):
    """
    public interface TTSService
    
        This is the interface that a text-to-speech service has to implement.
    
    
    """
    def getAvailableVoices(self) -> java.util.Set['Voice']: ...
    def getId(self) -> java.lang.String: ...
    def getLabel(self, locale: java.util.Locale) -> java.lang.String: ...
    def getSupportedFormats(self) -> java.util.Set[org.openhab.core.audio.AudioFormat]: ...
    def synthesize(self, text: java.lang.String, voice: 'Voice', requestedFormat: org.openhab.core.audio.AudioFormat) -> org.openhab.core.audio.AudioStream: ...

class Voice(java.lang.Object):
    """
    public interface Voice
    
        This is the interface that a text-to-speech voice has to implement.
    
    
    """
    def getLabel(self) -> java.lang.String: ...
    def getLocale(self) -> java.util.Locale: ...
    def getUID(self) -> java.lang.String: ...

class VoiceManager(java.lang.Object):
    """
    @NonNullByDefault public interface VoiceManager
    
        This service provides functionality around voice services and is the central service to be used directly by others.
    
    
    """
    def getAllVoices(self) -> java.util.Set[Voice]: ...
    def getDefaultVoice(self) -> Voice: ...
    @typing.overload
    def getHLI(self) -> org.openhab.core.voice.text.HumanLanguageInterpreter: ...
    @typing.overload
    def getHLI(self, id: java.lang.String) -> org.openhab.core.voice.text.HumanLanguageInterpreter: ...
    def getHLIs(self) -> java.util.Collection[org.openhab.core.voice.text.HumanLanguageInterpreter]: ...
    @typing.overload
    def getKS(self) -> KSService: ...
    @typing.overload
    def getKS(self, id: java.lang.String) -> KSService: ...
    def getKSs(self) -> java.util.Collection[KSService]: ...
    def getPreferredVoice(self, voices: java.util.Set[Voice]) -> Voice: ...
    @typing.overload
    def getSTT(self) -> STTService: ...
    @typing.overload
    def getSTT(self, id: java.lang.String) -> STTService: ...
    def getSTTs(self) -> java.util.Collection[STTService]: ...
    @typing.overload
    def getTTS(self) -> TTSService: ...
    @typing.overload
    def getTTS(self, id: java.lang.String) -> TTSService: ...
    def getTTSs(self) -> java.util.Collection[TTSService]: ...
    @typing.overload
    def interpret(self, text: java.lang.String) -> java.lang.String: ...
    @typing.overload
    def interpret(self, text: java.lang.String, hliId: java.lang.String) -> java.lang.String: ...
    @typing.overload
    def say(self, text: java.lang.String) -> None: ...
    @typing.overload
    def say(self, text: java.lang.String, voiceId: java.lang.String) -> None: ...
    @typing.overload
    def say(self, text: java.lang.String, voiceId: java.lang.String, sinkId: java.lang.String) -> None: ...
    @typing.overload
    def say(self, text: java.lang.String, voiceId: java.lang.String, sinkId: java.lang.String, volume: org.openhab.core.library.types.PercentType) -> None: ...
    @typing.overload
    def say(self, text: java.lang.String, voiceId: java.lang.String, volume: org.openhab.core.library.types.PercentType) -> None: ...
    @typing.overload
    def say(self, text: java.lang.String, volume: org.openhab.core.library.types.PercentType) -> None: ...
    @typing.overload
    def startDialog(self) -> None: ...
    @typing.overload
    def startDialog(self, ks: KSService, stt: STTService, tts: TTSService, hli: org.openhab.core.voice.text.HumanLanguageInterpreter, source: org.openhab.core.audio.AudioSource, sink: org.openhab.core.audio.AudioSink, locale: java.util.Locale, keyword: java.lang.String, listeningItem: java.lang.String) -> None: ...

class AudioStartEvent(STTEvent):
    """
    Java class 'org.openhab.core.voice.AudioStartEvent'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.voice.STTEvent
    
      Constructors:
        * AudioStartEvent()
    
    """
    def __init__(self): ...

class AudioStopEvent(STTEvent):
    """
    Java class 'org.openhab.core.voice.AudioStopEvent'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.voice.STTEvent
    
      Constructors:
        * AudioStopEvent()
    
    """
    def __init__(self): ...

class KSErrorEvent(KSEvent):
    """
    Java class 'org.openhab.core.voice.KSErrorEvent'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.voice.KSEvent
    
      Constructors:
        * KSErrorEvent(java.lang.String)
    
    """
    def __init__(self, message: java.lang.String): ...
    def getMessage(self) -> java.lang.String: ...

class KSpottedEvent(KSEvent):
    """
    Java class 'org.openhab.core.voice.KSpottedEvent'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.voice.KSEvent
    
      Constructors:
        * KSpottedEvent()
    
    """
    def __init__(self): ...

class RecognitionStartEvent(STTEvent):
    """
    Java class 'org.openhab.core.voice.RecognitionStartEvent'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.voice.STTEvent
    
      Constructors:
        * RecognitionStartEvent()
    
    """
    def __init__(self): ...

class RecognitionStopEvent(STTEvent):
    """
    Java class 'org.openhab.core.voice.RecognitionStopEvent'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.voice.STTEvent
    
      Constructors:
        * RecognitionStopEvent()
    
    """
    def __init__(self): ...

class SpeechRecognitionErrorEvent(STTEvent):
    """
    Java class 'org.openhab.core.voice.SpeechRecognitionErrorEvent'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.voice.STTEvent
    
      Constructors:
        * SpeechRecognitionErrorEvent(java.lang.String)
    
    """
    def __init__(self, message: java.lang.String): ...
    def getMessage(self) -> java.lang.String: ...

class SpeechRecognitionEvent(STTEvent):
    """
    Java class 'org.openhab.core.voice.SpeechRecognitionEvent'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.voice.STTEvent
    
      Constructors:
        * SpeechRecognitionEvent(java.lang.String, float)
    
    """
    def __init__(self, transcript: java.lang.String, confidence: float): ...
    def getConfidence(self) -> float: ...
    def getTranscript(self) -> java.lang.String: ...

class SpeechStartEvent(STTEvent):
    """
    Java class 'org.openhab.core.voice.SpeechStartEvent'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.voice.STTEvent
    
      Constructors:
        * SpeechStartEvent()
    
    """
    def __init__(self): ...

class SpeechStopEvent(STTEvent):
    """
    Java class 'org.openhab.core.voice.SpeechStopEvent'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.voice.STTEvent
    
      Constructors:
        * SpeechStopEvent()
    
    """
    def __init__(self): ...
