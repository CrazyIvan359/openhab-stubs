import java.lang
import java.util
import javax.sound.sampled
import org.openhab.core.audio
import org.openhab.core.library.types
import typing


class AudioPlayer(java.lang.Thread):
    """
    Java class 'org.openhab.core.audio.internal.javasound.AudioPlayer'
    
        Extends:
            java.lang.Thread
    
      Constructors:
        * AudioPlayer(org.openhab.core.audio.AudioStream)
    
    """
    def __init__(self, audioStream: org.openhab.core.audio.AudioStream): ...
    def run(self) -> None: ...

class JavaSoundAudioSink(org.openhab.core.audio.AudioSink):
    """
    Java class 'org.openhab.core.audio.internal.javasound.JavaSoundAudioSink'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.audio.AudioSink
    
      Constructors:
        * JavaSoundAudioSink()
    
    """
    def __init__(self): ...
    def getId(self) -> java.lang.String: ...
    def getLabel(self, locale: java.util.Locale) -> java.lang.String: ...
    def getSupportedFormats(self) -> java.util.Set[org.openhab.core.audio.AudioFormat]: ...
    def getSupportedStreams(self) -> java.util.Set[typing.Type[org.openhab.core.audio.AudioStream]]: ...
    def getVolume(self) -> org.openhab.core.library.types.PercentType: ...
    def process(self, audioStream: org.openhab.core.audio.AudioStream) -> None: ...
    def setVolume(self, volume: org.openhab.core.library.types.PercentType) -> None: ...

class JavaSoundAudioSource(org.openhab.core.audio.AudioSource):
    """
    Java class 'org.openhab.core.audio.internal.javasound.JavaSoundAudioSource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.audio.AudioSource
    
      Constructors:
        * JavaSoundAudioSource()
    
    """
    def __init__(self): ...
    def getId(self) -> java.lang.String: ...
    def getInputStream(self, expectedFormat: org.openhab.core.audio.AudioFormat) -> org.openhab.core.audio.AudioStream: ...
    def getLabel(self, locale: java.util.Locale) -> java.lang.String: ...
    def getSupportedFormats(self) -> java.util.Set[org.openhab.core.audio.AudioFormat]: ...
    def toString(self) -> java.lang.String: ...

class JavaSoundInputStream(org.openhab.core.audio.AudioStream):
    """
    Java class 'org.openhab.core.audio.internal.javasound.JavaSoundInputStream'
    
        Extends:
            org.openhab.core.audio.AudioStream
    
      Constructors:
        * JavaSoundInputStream(javax.sound.sampled.TargetDataLine, org.openhab.core.audio.AudioFormat)
    
    """
    def __init__(self, input: javax.sound.sampled.TargetDataLine, format: org.openhab.core.audio.AudioFormat): ...
    def close(self) -> None: ...
    def getFormat(self) -> org.openhab.core.audio.AudioFormat: ...
    @typing.overload
    def read(self) -> int: ...
    @typing.overload
    def read(self, b: typing.List[int]) -> int: ...
    @typing.overload
    def read(self, b: typing.List[int], off: int, len: int) -> int: ...
