import com.google.gson
import java.io
import java.lang
import java.lang.annotation
import java.lang.reflect
import javax.ws.rs.core
import javax.ws.rs.ext
import typing


_GsonMessageBodyReader__T = typing.TypeVar('_GsonMessageBodyReader__T')  # <T>
class GsonMessageBodyReader(javax.ws.rs.ext.MessageBodyReader[_GsonMessageBodyReader__T], typing.Generic[_GsonMessageBodyReader__T]):
    """
    Java class 'org.openhab.core.io.rest.core.internal.GsonMessageBodyReader'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            javax.ws.rs.ext.MessageBodyReader
    
      Constructors:
        * GsonMessageBodyReader(com.google.gson.Gson)
    
    """
    def __init__(self, gson: com.google.gson.Gson): ...
    def isReadable(self, type: typing.Type[typing.Any], genericType: java.lang.reflect.Type, annotations: typing.List[java.lang.annotation.Annotation], mediaType: javax.ws.rs.core.MediaType) -> bool: ...
    def readFrom(self, type: typing.Type[_GsonMessageBodyReader__T], genericType: java.lang.reflect.Type, annotations: typing.List[java.lang.annotation.Annotation], mediaType: javax.ws.rs.core.MediaType, httpHeaders: javax.ws.rs.core.MultivaluedMap[java.lang.String, java.lang.String], entityStream: java.io.InputStream) -> _GsonMessageBodyReader__T: ...

_GsonMessageBodyWriter__T = typing.TypeVar('_GsonMessageBodyWriter__T')  # <T>
class GsonMessageBodyWriter(javax.ws.rs.ext.MessageBodyWriter[_GsonMessageBodyWriter__T], typing.Generic[_GsonMessageBodyWriter__T]):
    """
    Java class 'org.openhab.core.io.rest.core.internal.GsonMessageBodyWriter'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            javax.ws.rs.ext.MessageBodyWriter
    
      Constructors:
        * GsonMessageBodyWriter(com.google.gson.Gson)
    
    """
    def __init__(self, gson: com.google.gson.Gson): ...
    def getSize(self, object: _GsonMessageBodyWriter__T, type: typing.Type[typing.Any], genericType: java.lang.reflect.Type, annotations: typing.List[java.lang.annotation.Annotation], mediaType: javax.ws.rs.core.MediaType) -> int: ...
    def isWriteable(self, type: typing.Type[typing.Any], genericType: java.lang.reflect.Type, annotations: typing.List[java.lang.annotation.Annotation], mediaType: javax.ws.rs.core.MediaType) -> bool: ...
    def writeTo(self, object: _GsonMessageBodyWriter__T, type: typing.Type[typing.Any], genericType: java.lang.reflect.Type, annotations: typing.List[java.lang.annotation.Annotation], mediaType: javax.ws.rs.core.MediaType, httpHeaders: javax.ws.rs.core.MultivaluedMap[java.lang.String, typing.Any], entityStream: java.io.OutputStream) -> None: ...

class JSONResponseExceptionMapper(javax.ws.rs.ext.ExceptionMapper[java.lang.Exception]):
    """
    Java class 'org.openhab.core.io.rest.core.internal.JSONResponseExceptionMapper'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            javax.ws.rs.ext.ExceptionMapper
    
      Constructors:
        * JSONResponseExceptionMapper()
    
    """
    def __init__(self): ...
    @typing.overload
    def toResponse(self, e: java.lang.Exception) -> javax.ws.rs.core.Response: ...
    @typing.overload
    def toResponse(self, throwable: java.lang.Throwable) -> javax.ws.rs.core.Response: ...

_MediaTypeExtension__T = typing.TypeVar('_MediaTypeExtension__T')  # <T>
class MediaTypeExtension(javax.ws.rs.ext.MessageBodyReader[_MediaTypeExtension__T], javax.ws.rs.ext.MessageBodyWriter[_MediaTypeExtension__T], typing.Generic[_MediaTypeExtension__T]):
    """
    Java class 'org.openhab.core.io.rest.core.internal.MediaTypeExtension'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            javax.ws.rs.ext.MessageBodyReader,
            javax.ws.rs.ext.MessageBodyWriter
    
      Constructors:
        * MediaTypeExtension()
    
    """
    def __init__(self): ...
    def isReadable(self, type: typing.Type[typing.Any], genericType: java.lang.reflect.Type, annotations: typing.List[java.lang.annotation.Annotation], mediaType: javax.ws.rs.core.MediaType) -> bool: ...
    def isWriteable(self, type: typing.Type[typing.Any], genericType: java.lang.reflect.Type, annotations: typing.List[java.lang.annotation.Annotation], mediaType: javax.ws.rs.core.MediaType) -> bool: ...
    def readFrom(self, type: typing.Type[_MediaTypeExtension__T], genericType: java.lang.reflect.Type, annotations: typing.List[java.lang.annotation.Annotation], mediaType: javax.ws.rs.core.MediaType, httpHeaders: javax.ws.rs.core.MultivaluedMap[java.lang.String, java.lang.String], entityStream: java.io.InputStream) -> _MediaTypeExtension__T: ...
    def writeTo(self, object: _MediaTypeExtension__T, type: typing.Type[typing.Any], genericType: java.lang.reflect.Type, annotations: typing.List[java.lang.annotation.Annotation], mediaType: javax.ws.rs.core.MediaType, httpHeaders: javax.ws.rs.core.MultivaluedMap[java.lang.String, typing.Any], entityStream: java.io.OutputStream) -> None: ...

_PlainMessageBodyReader__T = typing.TypeVar('_PlainMessageBodyReader__T')  # <T>
class PlainMessageBodyReader(javax.ws.rs.ext.MessageBodyReader[_PlainMessageBodyReader__T], typing.Generic[_PlainMessageBodyReader__T]):
    """
    Java class 'org.openhab.core.io.rest.core.internal.PlainMessageBodyReader'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            javax.ws.rs.ext.MessageBodyReader
    
      Constructors:
        * PlainMessageBodyReader()
    
    """
    def __init__(self): ...
    def isReadable(self, type: typing.Type[typing.Any], genericType: java.lang.reflect.Type, annotations: typing.List[java.lang.annotation.Annotation], mediaType: javax.ws.rs.core.MediaType) -> bool: ...
    def readFrom(self, type: typing.Type[_PlainMessageBodyReader__T], genericType: java.lang.reflect.Type, annotations: typing.List[java.lang.annotation.Annotation], mediaType: javax.ws.rs.core.MediaType, httpHeaders: javax.ws.rs.core.MultivaluedMap[java.lang.String, java.lang.String], entityStream: java.io.InputStream) -> _PlainMessageBodyReader__T: ...

_PlainMessageBodyWriter__T = typing.TypeVar('_PlainMessageBodyWriter__T')  # <T>
class PlainMessageBodyWriter(javax.ws.rs.ext.MessageBodyWriter[_PlainMessageBodyWriter__T], typing.Generic[_PlainMessageBodyWriter__T]):
    """
    Java class 'org.openhab.core.io.rest.core.internal.PlainMessageBodyWriter'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            javax.ws.rs.ext.MessageBodyWriter
    
      Constructors:
        * PlainMessageBodyWriter()
    
    """
    def __init__(self): ...
    def getSize(self, object: _PlainMessageBodyWriter__T, type: typing.Type[typing.Any], genericType: java.lang.reflect.Type, annotations: typing.List[java.lang.annotation.Annotation], mediaType: javax.ws.rs.core.MediaType) -> int: ...
    def isWriteable(self, type: typing.Type[typing.Any], genericType: java.lang.reflect.Type, annotations: typing.List[java.lang.annotation.Annotation], mediaType: javax.ws.rs.core.MediaType) -> bool: ...
    def writeTo(self, object: _PlainMessageBodyWriter__T, type: typing.Type[typing.Any], genericType: java.lang.reflect.Type, annotations: typing.List[java.lang.annotation.Annotation], mediaType: javax.ws.rs.core.MediaType, httpHeaders: javax.ws.rs.core.MultivaluedMap[java.lang.String, typing.Any], entityStream: java.io.OutputStream) -> None: ...
