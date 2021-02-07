import java.lang
import java.net
import java.util
import javax.servlet.http
import org.openhab.core.io.http
import org.osgi.framework
import org.osgi.service.http


class CatchHandler(org.openhab.core.io.http.Handler):
    """
    Java class 'org.openhab.core.io.http.internal.CatchHandler'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.http.Handler
    
      Constructors:
        * CatchHandler(org.openhab.core.io.http.Handler)
    
    """
    def __init__(self, delegate: org.openhab.core.io.http.Handler): ...
    def getPriority(self) -> int: ...
    def handle(self, request: javax.servlet.http.HttpServletRequest, response: javax.servlet.http.HttpServletResponse, context: org.openhab.core.io.http.HandlerContext) -> None: ...
    def handleError(self, request: javax.servlet.http.HttpServletRequest, response: javax.servlet.http.HttpServletResponse, context: org.openhab.core.io.http.HandlerContext) -> None: ...

class DefaultHandlerContext(org.openhab.core.io.http.HandlerContext):
    """
    Java class 'org.openhab.core.io.http.internal.DefaultHandlerContext'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.http.HandlerContext
    
      Constructors:
        * DefaultHandlerContext(java.util.Deque)
    
    """
    def __init__(self, handlers: java.util.Deque[org.openhab.core.io.http.Handler]): ...
    def error(self, error: java.lang.Exception) -> None: ...
    def execute(self, request: javax.servlet.http.HttpServletRequest, response: javax.servlet.http.HttpServletResponse) -> None: ...
    def hasError(self) -> bool: ...

class HttpContextFactoryServiceImpl(org.openhab.core.io.http.HttpContextFactoryService):
    """
    Java class 'org.openhab.core.io.http.internal.HttpContextFactoryServiceImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.http.HttpContextFactoryService
    
      Constructors:
        * HttpContextFactoryServiceImpl()
    
    """
    def __init__(self): ...
    def createDefaultHttpContext(self, bundle: org.osgi.framework.Bundle) -> org.osgi.service.http.HttpContext: ...
    def setHttpContext(self, httpContext: org.openhab.core.io.http.WrappingHttpContext) -> None: ...
    def unsetHttpContext(self, httpContext: org.openhab.core.io.http.WrappingHttpContext) -> None: ...

class OpenHABHttpContext(org.openhab.core.io.http.WrappingHttpContext):
    """
    Java class 'org.openhab.core.io.http.internal.OpenHABHttpContext'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.http.WrappingHttpContext
    
      Constructors:
        * OpenHABHttpContext()
    
    """
    def __init__(self): ...
    def addHandler(self, handler: org.openhab.core.io.http.Handler) -> None: ...
    def getMimeType(self, name: java.lang.String) -> java.lang.String: ...
    def getResource(self, name: java.lang.String) -> java.net.URL: ...
    def handleSecurity(self, request: javax.servlet.http.HttpServletRequest, response: javax.servlet.http.HttpServletResponse) -> bool: ...
    def removeHandler(self, handler: org.openhab.core.io.http.Handler) -> None: ...
    def wrap(self, bundle: org.osgi.framework.Bundle) -> org.osgi.service.http.HttpContext: ...
