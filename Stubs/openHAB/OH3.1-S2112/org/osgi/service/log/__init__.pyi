import java.lang
import java.util
import org.osgi.framework
import typing


class LogEntry(java.lang.Object):
    """
    Java class 'org.osgi.service.log.LogEntry'
    
    """
    def getBundle(self) -> org.osgi.framework.Bundle: ...
    def getException(self) -> java.lang.Throwable: ...
    def getLevel(self) -> int: ...
    def getMessage(self) -> java.lang.String: ...
    def getServiceReference(self) -> org.osgi.framework.ServiceReference: ...
    def getTime(self) -> int: ...

class LogListener(java.util.EventListener):
    """
    Java class 'org.osgi.service.log.LogListener'
    
        Interfaces:
            java.util.EventListener
    
    """
    def logged(self, logEntry: LogEntry) -> None: ...

class LogReaderService(java.lang.Object):
    """
    Java class 'org.osgi.service.log.LogReaderService'
    
    """
    def addLogListener(self, logListener: LogListener) -> None: ...
    def getLog(self) -> java.util.Enumeration: ...
    def removeLogListener(self, logListener: LogListener) -> None: ...

class LogService(java.lang.Object):
    """
    Java class 'org.osgi.service.log.LogService'
    
      Attributes:
        LOG_ERROR (int): final static field
        LOG_WARNING (int): final static field
        LOG_INFO (int): final static field
        LOG_DEBUG (int): final static field
    
    """
    LOG_ERROR: typing.ClassVar[int] = ...
    LOG_WARNING: typing.ClassVar[int] = ...
    LOG_INFO: typing.ClassVar[int] = ...
    LOG_DEBUG: typing.ClassVar[int] = ...
    @typing.overload
    def log(self, int: int, string: java.lang.String) -> None: ...
    @typing.overload
    def log(self, int: int, string: java.lang.String, throwable: java.lang.Throwable) -> None: ...
    @typing.overload
    def log(self, serviceReference: org.osgi.framework.ServiceReference, int: int, string: java.lang.String) -> None: ...
    @typing.overload
    def log(self, serviceReference: org.osgi.framework.ServiceReference, int: int, string: java.lang.String, throwable: java.lang.Throwable) -> None: ...
