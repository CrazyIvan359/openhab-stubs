import java.lang
import java.net
import java.util
import org.openhab.core.audio
import org.openhab.core.config.core
import org.openhab.core.i18n
import org.openhab.core.io.console
import org.openhab.core.io.console.extensions
import org.openhab.core.io.http.servlet
import org.openhab.core.library.types
import org.osgi.service.http
import typing


class AudioConsoleCommandExtension(org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension):
    """
    Java class 'org.openhab.core.audio.internal.AudioConsoleCommandExtension'
    
        Extends:
            org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension
    
      Constructors:
        * AudioConsoleCommandExtension(org.openhab.core.audio.AudioManager, org.openhab.core.i18n.LocaleProvider)
    
    """
    def __init__(self, audioManager: org.openhab.core.audio.AudioManager, localeProvider: org.openhab.core.i18n.LocaleProvider): ...
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...

class AudioManagerImpl(org.openhab.core.audio.AudioManager, org.openhab.core.config.core.ConfigOptionProvider):
    """
    Java class 'org.openhab.core.audio.internal.AudioManagerImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.audio.AudioManager,
            org.openhab.core.config.core.ConfigOptionProvider
    
      Constructors:
        * AudioManagerImpl()
    
    """
    def __init__(self): ...
    def getAllSinks(self) -> java.util.Set[org.openhab.core.audio.AudioSink]: ...
    def getAllSources(self) -> java.util.Set[org.openhab.core.audio.AudioSource]: ...
    def getParameterOptions(self, uri: java.net.URI, param: java.lang.String, context: java.lang.String, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.config.core.ParameterOption]: ...
    @typing.overload
    def getSink(self) -> org.openhab.core.audio.AudioSink: ...
    @typing.overload
    def getSink(self, sinkId: java.lang.String) -> org.openhab.core.audio.AudioSink: ...
    def getSinkIds(self, pattern: java.lang.String) -> java.util.Set[java.lang.String]: ...
    def getSource(self) -> org.openhab.core.audio.AudioSource: ...
    def getSourceIds(self, pattern: java.lang.String) -> java.util.Set[java.lang.String]: ...
    def getVolume(self, sinkId: java.lang.String) -> org.openhab.core.library.types.PercentType: ...
    @typing.overload
    def play(self, audioStream: org.openhab.core.audio.AudioStream) -> None: ...
    @typing.overload
    def play(self, audioStream: org.openhab.core.audio.AudioStream, sinkId: java.lang.String) -> None: ...
    @typing.overload
    def play(self, audioStream: org.openhab.core.audio.AudioStream, sinkId: java.lang.String, volume: org.openhab.core.library.types.PercentType) -> None: ...
    @typing.overload
    def playFile(self, fileName: java.lang.String) -> None: ...
    @typing.overload
    def playFile(self, fileName: java.lang.String, sinkId: java.lang.String) -> None: ...
    @typing.overload
    def playFile(self, fileName: java.lang.String, sinkId: java.lang.String, volume: org.openhab.core.library.types.PercentType) -> None: ...
    @typing.overload
    def playFile(self, fileName: java.lang.String, volume: org.openhab.core.library.types.PercentType) -> None: ...
    def setVolume(self, volume: org.openhab.core.library.types.PercentType, sinkId: java.lang.String) -> None: ...
    @typing.overload
    def stream(self, url: java.lang.String) -> None: ...
    @typing.overload
    def stream(self, url: java.lang.String, sinkId: java.lang.String) -> None: ...

class AudioServlet(org.openhab.core.io.http.servlet.OpenHABServlet, org.openhab.core.audio.AudioHTTPServer):
    """
    Java class 'org.openhab.core.audio.internal.AudioServlet'
    
        Extends:
            org.openhab.core.io.http.servlet.OpenHABServlet
    
        Interfaces:
            org.openhab.core.audio.AudioHTTPServer
    
      Constructors:
        * AudioServlet(org.osgi.service.http.HttpService, org.osgi.service.http.HttpContext)
    
    """
    def __init__(self, httpService: org.osgi.service.http.HttpService, httpContext: org.osgi.service.http.HttpContext): ...
    @typing.overload
    def serve(self, stream: org.openhab.core.audio.AudioStream) -> java.lang.String: ...
    @typing.overload
    def serve(self, stream: org.openhab.core.audio.FixedLengthAudioStream, seconds: int) -> java.lang.String: ...
