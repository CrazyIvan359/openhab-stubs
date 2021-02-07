import java.lang
import javax.servlet.http
import org.eclipse.jetty.proxy
import typing


class AsyncProxyServlet(org.eclipse.jetty.proxy.AsyncProxyServlet):
    """
    Java class 'org.openhab.core.ui.internal.proxy.AsyncProxyServlet'
    
        Extends:
            org.eclipse.jetty.proxy.AsyncProxyServlet
    
    """
    def getServletInfo(self) -> java.lang.String: ...

class BlockingProxyServlet(javax.servlet.http.HttpServlet):
    """
    Java class 'org.openhab.core.ui.internal.proxy.BlockingProxyServlet'
    
        Extends:
            javax.servlet.http.HttpServlet
    
    """
    def getServletInfo(self) -> java.lang.String: ...

class ProxyServletService(javax.servlet.http.HttpServlet):
    """
    Java class 'org.openhab.core.ui.internal.proxy.ProxyServletService'
    
        Extends:
            javax.servlet.http.HttpServlet
    
      Constructors:
        * ProxyServletService()
    
      Attributes:
        PROXY_ALIAS (java.lang.String): final static field
        ATTR_URI (java.lang.String): final static field
        ATTR_SERVLET_EXCEPTION (java.lang.String): final static field
    
    """
    PROXY_ALIAS: typing.ClassVar[java.lang.String] = ...
    ATTR_URI: typing.ClassVar[java.lang.String] = ...
    ATTR_SERVLET_EXCEPTION: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
