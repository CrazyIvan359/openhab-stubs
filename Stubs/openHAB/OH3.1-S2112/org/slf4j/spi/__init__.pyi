import java.lang
import java.util
import org.slf4j
import typing


class LocationAwareLogger(org.slf4j.Logger):
    """
    Java class 'org.slf4j.spi.LocationAwareLogger'
    
        Interfaces:
            org.slf4j.Logger
    
      Attributes:
        TRACE_INT (int): final static field
        DEBUG_INT (int): final static field
        INFO_INT (int): final static field
        WARN_INT (int): final static field
        ERROR_INT (int): final static field
    
    """
    TRACE_INT: typing.ClassVar[int] = ...
    DEBUG_INT: typing.ClassVar[int] = ...
    INFO_INT: typing.ClassVar[int] = ...
    WARN_INT: typing.ClassVar[int] = ...
    ERROR_INT: typing.ClassVar[int] = ...
    def log(self, marker: org.slf4j.Marker, string: java.lang.String, int: int, string2: java.lang.String, objectArray: typing.List[typing.Any], throwable: java.lang.Throwable) -> None: ...

class LoggerFactoryBinder(java.lang.Object):
    """
    Java class 'org.slf4j.spi.LoggerFactoryBinder'
    
    """
    def getLoggerFactory(self) -> org.slf4j.ILoggerFactory: ...
    def getLoggerFactoryClassStr(self) -> java.lang.String: ...

class MDCAdapter(java.lang.Object):
    """
    Java class 'org.slf4j.spi.MDCAdapter'
    
    """
    def clear(self) -> None: ...
    def get(self, string: java.lang.String) -> java.lang.String: ...
    def getCopyOfContextMap(self) -> java.util.Map[java.lang.String, java.lang.String]: ...
    def put(self, string: java.lang.String, string2: java.lang.String) -> None: ...
    def remove(self, string: java.lang.String) -> None: ...
    def setContextMap(self, map: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> None: ...

class MarkerFactoryBinder(java.lang.Object):
    """
    Java class 'org.slf4j.spi.MarkerFactoryBinder'
    
    """
    def getMarkerFactory(self) -> org.slf4j.IMarkerFactory: ...
    def getMarkerFactoryClassStr(self) -> java.lang.String: ...
