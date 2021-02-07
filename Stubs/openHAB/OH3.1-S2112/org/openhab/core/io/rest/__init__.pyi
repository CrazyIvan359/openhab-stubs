import java.io
import java.lang
import java.util
import java.util.function
import java.util.stream
import javax.ws.rs.core
import javax.ws.rs.ext
import javax.ws.rs.sse
import typing


class DTOMapper(java.lang.Object):
    """
    public interface DTOMapper
    
        Utilities for mapping/transforming DTOs.
    
    
    """
    _limitToFields__T = typing.TypeVar('_limitToFields__T')  # <T>
    def limitToFields(self, itemStream: java.util.stream.Stream[_limitToFields__T], fields: java.lang.String) -> java.util.stream.Stream[_limitToFields__T]: ...

class JSONInputStream(java.lang.Object):
    """
    @NonNullByDefault public interface JSONInputStream
    
        Marker interface for an input stream that provides a JSON string.
    
    
    """

class JSONResponse(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.JSONResponse'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def createErrorResponse(cls, status: javax.ws.rs.core.Response.StatusType, errormessage: java.lang.String) -> javax.ws.rs.core.Response: ...
    @classmethod
    def createResponse(cls, status: javax.ws.rs.core.Response.StatusType, entity: typing.Any, errormessage: java.lang.String) -> javax.ws.rs.core.Response: ...
    class ExceptionMapper(javax.ws.rs.ext.ExceptionMapper[java.lang.Exception]):
        """
        Java class 'org.openhab.core.io.rest.JSONResponse$ExceptionMapper'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                javax.ws.rs.ext.ExceptionMapper
        
          Constructors:
            * ExceptionMapper()
        
        """
        def __init__(self): ...
        @typing.overload
        def toResponse(self, e: java.lang.Exception) -> javax.ws.rs.core.Response: ...
        @typing.overload
        def toResponse(self, throwable: java.lang.Throwable) -> javax.ws.rs.core.Response: ...

class LocaleService(java.lang.Object):
    """
    @NonNullByDefault public interface LocaleService
    
        Provides helper method for working with locales.
    
    
    """
    def getLocale(self, acceptLanguageHttpHeader: java.lang.String) -> java.util.Locale: ...

class RESTConstants(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.RESTConstants'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RESTConstants()
    
      Attributes:
        REST_URI (java.lang.String): final static field
        JAX_RS_NAME (java.lang.String): final static field
        API_VERSION (java.lang.String): final static field
    
    """
    REST_URI: typing.ClassVar[java.lang.String] = ...
    JAX_RS_NAME: typing.ClassVar[java.lang.String] = ...
    API_VERSION: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...

class RESTResource(java.lang.Object):
    """
    @NonNullByDefault public interface RESTResource
    
        This is a marker interface for REST resource implementations
    
    
    """

_SseBroadcaster__Listener__I = typing.TypeVar('_SseBroadcaster__Listener__I')  # <I>
_SseBroadcaster__I = typing.TypeVar('_SseBroadcaster__I')  # <I>
class SseBroadcaster(java.io.Closeable, typing.Generic[_SseBroadcaster__I]):
    """
    Java class 'org.openhab.core.io.rest.SseBroadcaster'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Closeable
    
      Constructors:
        * SseBroadcaster()
    
    """
    def __init__(self): ...
    def add(self, sink: javax.ws.rs.sse.SseEventSink, info: _SseBroadcaster__I) -> _SseBroadcaster__I: ...
    def addListener(self, listener: 'SseBroadcaster.Listener'[_SseBroadcaster__I]) -> None: ...
    def close(self) -> None: ...
    def closeAndRemoveIf(self, predicate: typing.Union[java.util.function.Predicate[_SseBroadcaster__I], typing.Callable[[], _SseBroadcaster__I]]) -> None: ...
    def getInfo(self, sink: javax.ws.rs.sse.SseEventSink) -> _SseBroadcaster__I: ...
    def getInfoIf(self, predicate: typing.Union[java.util.function.Predicate[_SseBroadcaster__I], typing.Callable[[], _SseBroadcaster__I]]) -> java.util.stream.Stream[_SseBroadcaster__I]: ...
    def remove(self, sink: javax.ws.rs.sse.SseEventSink) -> _SseBroadcaster__I: ...
    def removeListener(self, listener: 'SseBroadcaster.Listener'[_SseBroadcaster__I]) -> None: ...
    def send(self, event: javax.ws.rs.sse.OutboundSseEvent) -> None: ...
    def sendIf(self, event: javax.ws.rs.sse.OutboundSseEvent, predicate: typing.Union[java.util.function.Predicate[_SseBroadcaster__I], typing.Callable[[], _SseBroadcaster__I]]) -> None: ...
    class Listener(java.lang.Object, typing.Generic[_SseBroadcaster__Listener__I]):
        """
        Java class 'org.openhab.core.io.rest.SseBroadcaster$Listener'
        
        """
        def sseEventSinkRemoved(self, sink: javax.ws.rs.sse.SseEventSink, info: _SseBroadcaster__Listener__I) -> None: ...

class LocaleServiceImpl(LocaleService):
    """
    Java class 'org.openhab.core.io.rest.LocaleServiceImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.LocaleService
    
      Constructors:
        * LocaleServiceImpl()
    
    """
    def __init__(self): ...
    def getLocale(self, acceptLanguageHttpHeader: java.lang.String) -> java.util.Locale: ...

class Stream2JSONInputStream(java.io.InputStream, JSONInputStream):
    """
    Java class 'org.openhab.core.io.rest.Stream2JSONInputStream'
    
        Extends:
            java.io.InputStream
    
        Interfaces:
            org.openhab.core.io.rest.JSONInputStream
    
      Constructors:
        * Stream2JSONInputStream(java.util.stream.Stream)
    
    """
    def __init__(self, source: java.util.stream.Stream[typing.Any]): ...
    def close(self) -> None: ...
    @typing.overload
    def read(self, byteArray: typing.List[int]) -> int: ...
    @typing.overload
    def read(self, byteArray: typing.List[int], int: int, int2: int) -> int: ...
    @typing.overload
    def read(self) -> int: ...
