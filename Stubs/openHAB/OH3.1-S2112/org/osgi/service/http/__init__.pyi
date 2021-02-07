import java.lang
import java.net
import java.util
import javax.servlet
import javax.servlet.http
import typing


class HttpContext(java.lang.Object):
    """
    Java class 'org.osgi.service.http.HttpContext'
    
      Attributes:
        REMOTE_USER (java.lang.String): final static field
        AUTHENTICATION_TYPE (java.lang.String): final static field
        AUTHORIZATION (java.lang.String): final static field
    
    """
    REMOTE_USER: typing.ClassVar[java.lang.String] = ...
    AUTHENTICATION_TYPE: typing.ClassVar[java.lang.String] = ...
    AUTHORIZATION: typing.ClassVar[java.lang.String] = ...
    def getMimeType(self, string: java.lang.String) -> java.lang.String: ...
    def getResource(self, string: java.lang.String) -> java.net.URL: ...
    def handleSecurity(self, httpServletRequest: javax.servlet.http.HttpServletRequest, httpServletResponse: javax.servlet.http.HttpServletResponse) -> bool: ...

class HttpService(java.lang.Object):
    """
    Java class 'org.osgi.service.http.HttpService'
    
    """
    def createDefaultHttpContext(self) -> HttpContext: ...
    def registerResources(self, string: java.lang.String, string2: java.lang.String, httpContext: HttpContext) -> None: ...
    def registerServlet(self, string: java.lang.String, servlet: javax.servlet.Servlet, dictionary: java.util.Dictionary, httpContext: HttpContext) -> None: ...
    def unregister(self, string: java.lang.String) -> None: ...

class NamespaceException(java.lang.Exception):
    """
    Java class 'org.osgi.service.http.NamespaceException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * NamespaceException(java.lang.String)
        * NamespaceException(java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, string: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, throwable: java.lang.Throwable): ...
    def getCause(self) -> java.lang.Throwable: ...
    def getException(self) -> java.lang.Throwable: ...
    def initCause(self, throwable: java.lang.Throwable) -> java.lang.Throwable: ...
