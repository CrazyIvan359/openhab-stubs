import java.lang
import java.net
import java.util
import javax.servlet.http
import org.osgi.framework
import typing


class ServletContextHelper(java.lang.Object):
    """
    Java class 'org.osgi.service.http.context.ServletContextHelper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ServletContextHelper()
        * ServletContextHelper(org.osgi.framework.Bundle)
    
      Attributes:
        REMOTE_USER (java.lang.String): final static field
        AUTHENTICATION_TYPE (java.lang.String): final static field
        AUTHORIZATION (java.lang.String): final static field
    
    """
    REMOTE_USER: typing.ClassVar[java.lang.String] = ...
    AUTHENTICATION_TYPE: typing.ClassVar[java.lang.String] = ...
    AUTHORIZATION: typing.ClassVar[java.lang.String] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, bundle: org.osgi.framework.Bundle): ...
    def getMimeType(self, string: java.lang.String) -> java.lang.String: ...
    def getRealPath(self, string: java.lang.String) -> java.lang.String: ...
    def getResource(self, string: java.lang.String) -> java.net.URL: ...
    def getResourcePaths(self, string: java.lang.String) -> java.util.Set[java.lang.String]: ...
    def handleSecurity(self, httpServletRequest: javax.servlet.http.HttpServletRequest, httpServletResponse: javax.servlet.http.HttpServletResponse) -> bool: ...
