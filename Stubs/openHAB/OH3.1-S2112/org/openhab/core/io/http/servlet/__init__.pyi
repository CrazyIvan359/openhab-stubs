import javax.servlet.http
import org.openhab.core.io.http
import org.osgi.service.http


class BaseOpenHABServlet(javax.servlet.http.HttpServlet):
    """
    Java class 'org.openhab.core.io.http.servlet.BaseOpenHABServlet'
    
        Extends:
            javax.servlet.http.HttpServlet
    
      Constructors:
        * BaseOpenHABServlet(org.osgi.service.http.HttpService)
    
    """
    def __init__(self, httpService: org.osgi.service.http.HttpService): ...

class OpenHABBundleServlet(BaseOpenHABServlet):
    """
    Java class 'org.openhab.core.io.http.servlet.OpenHABBundleServlet'
    
        Extends:
            org.openhab.core.io.http.servlet.BaseOpenHABServlet
    
      Constructors:
        * OpenHABBundleServlet(org.osgi.service.http.HttpService, org.openhab.core.io.http.HttpContextFactoryService)
    
    """
    def __init__(self, httpService: org.osgi.service.http.HttpService, httpContextFactoryService: org.openhab.core.io.http.HttpContextFactoryService): ...

class OpenHABServlet(BaseOpenHABServlet):
    """
    Java class 'org.openhab.core.io.http.servlet.OpenHABServlet'
    
        Extends:
            org.openhab.core.io.http.servlet.BaseOpenHABServlet
    
      Constructors:
        * OpenHABServlet(org.osgi.service.http.HttpService, org.osgi.service.http.HttpContext)
    
    """
    def __init__(self, httpService: org.osgi.service.http.HttpService, httpContext: org.osgi.service.http.HttpContext): ...
