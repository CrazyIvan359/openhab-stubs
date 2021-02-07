import java.lang
import java.net
import javax.ws.rs.core
import org.openhab.core.io.rest
import typing


class LogConstants(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.log.internal.LogConstants'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * LogConstants()
    
      Attributes:
        LOG_SEVERITY_IS_NOT_SUPPORTED (java.lang.String): final static field
        LOG_HANDLE_ERROR (java.lang.String): final static field
        FRONTEND_LOG_PATTERN (java.lang.String): final static field
        LOG_BUFFER_LIMIT (int): final static field
    
    """
    LOG_SEVERITY_IS_NOT_SUPPORTED: typing.ClassVar[java.lang.String] = ...
    LOG_HANDLE_ERROR: typing.ClassVar[java.lang.String] = ...
    FRONTEND_LOG_PATTERN: typing.ClassVar[java.lang.String] = ...
    LOG_BUFFER_LIMIT: typing.ClassVar[int] = ...
    def __init__(self): ...

class LogHandler(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.log.internal.LogHandler'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * LogHandler()
    
      Attributes:
        PATH_LOG (java.lang.String): final static field
    
    """
    PATH_LOG: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    def getLastLogs(self, limit: int) -> javax.ws.rs.core.Response: ...
    def getLogLevels(self) -> javax.ws.rs.core.Response: ...
    def log(self, logMessage: 'LogHandler.LogMessage') -> javax.ws.rs.core.Response: ...
    class LogMessage(java.lang.Object):
        """
        Java class 'org.openhab.core.io.rest.log.internal.LogHandler$LogMessage'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * LogMessage(org.openhab.core.io.rest.log.internal.LogHandler)
        
          Attributes:
            timestamp (long): field
            severity (java.lang.String): field
            url (java.net.URL): field
            message (java.lang.String): field
        
        """
        timestamp: int = ...
        severity: java.lang.String = ...
        url: java.net.URL = ...
        message: java.lang.String = ...
        def __init__(self): ...
