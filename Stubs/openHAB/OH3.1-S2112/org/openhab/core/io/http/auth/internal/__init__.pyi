import javax.servlet.http
import org.openhab.core.auth
import org.openhab.core.i18n
import org.openhab.core.io.http
import org.openhab.core.io.http.auth
import org.osgi.framework
import org.osgi.service.http


class AbstractAuthPageServlet(javax.servlet.http.HttpServlet):
    """
    Java class 'org.openhab.core.io.http.auth.internal.AbstractAuthPageServlet'
    
        Extends:
            javax.servlet.http.HttpServlet
    
      Constructors:
        * AbstractAuthPageServlet(org.osgi.framework.BundleContext, org.osgi.service.http.HttpService, org.openhab.core.auth.UserRegistry, org.openhab.core.auth.AuthenticationProvider, org.openhab.core.i18n.LocaleProvider)
    
    """
    def __init__(self, bundleContext: org.osgi.framework.BundleContext, httpService: org.osgi.service.http.HttpService, userRegistry: org.openhab.core.auth.UserRegistry, authProvider: org.openhab.core.auth.AuthenticationProvider, localeProvider: org.openhab.core.i18n.LocaleProvider): ...

class AuthenticationHandler(org.openhab.core.io.http.Handler):
    """
    Java class 'org.openhab.core.io.http.auth.internal.AuthenticationHandler'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.http.Handler
    
      Constructors:
        * AuthenticationHandler()
    
    """
    def __init__(self): ...
    def addCredentialsExtractor(self, extractor: org.openhab.core.io.http.auth.CredentialsExtractor[javax.servlet.http.HttpServletRequest]) -> None: ...
    def getPriority(self) -> int: ...
    def handle(self, request: javax.servlet.http.HttpServletRequest, response: javax.servlet.http.HttpServletResponse, context: org.openhab.core.io.http.HandlerContext) -> None: ...
    def handleError(self, request: javax.servlet.http.HttpServletRequest, response: javax.servlet.http.HttpServletResponse, context: org.openhab.core.io.http.HandlerContext) -> None: ...
    def removeCredentialsExtractor(self, extractor: org.openhab.core.io.http.auth.CredentialsExtractor[javax.servlet.http.HttpServletRequest]) -> None: ...
    def setAuthenticationManager(self, authenticationManager: org.openhab.core.auth.AuthenticationManager) -> None: ...
    def unsetAuthenticationManager(self, authenticationManager: org.openhab.core.auth.AuthenticationManager) -> None: ...

class RedirectHandler(org.openhab.core.io.http.Handler):
    """
    Java class 'org.openhab.core.io.http.auth.internal.RedirectHandler'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.http.Handler
    
      Constructors:
        * RedirectHandler()
    
    """
    def __init__(self): ...
    def getPriority(self) -> int: ...
    def handle(self, request: javax.servlet.http.HttpServletRequest, response: javax.servlet.http.HttpServletResponse, context: org.openhab.core.io.http.HandlerContext) -> None: ...
    def handleError(self, request: javax.servlet.http.HttpServletRequest, response: javax.servlet.http.HttpServletResponse, context: org.openhab.core.io.http.HandlerContext) -> None: ...

class AuthorizePageServlet(AbstractAuthPageServlet):
    """
    Java class 'org.openhab.core.io.http.auth.internal.AuthorizePageServlet'
    
        Extends:
            org.openhab.core.io.http.auth.internal.AbstractAuthPageServlet
    
      Constructors:
        * AuthorizePageServlet(org.osgi.framework.BundleContext, org.osgi.service.http.HttpService, org.openhab.core.auth.UserRegistry, org.openhab.core.auth.AuthenticationProvider, org.openhab.core.i18n.LocaleProvider)
    
    """
    def __init__(self, bundleContext: org.osgi.framework.BundleContext, httpService: org.osgi.service.http.HttpService, userRegistry: org.openhab.core.auth.UserRegistry, authProvider: org.openhab.core.auth.AuthenticationProvider, localeProvider: org.openhab.core.i18n.LocaleProvider): ...
    def deactivate(self) -> None: ...

class ChangePasswordPageServlet(AbstractAuthPageServlet):
    """
    Java class 'org.openhab.core.io.http.auth.internal.ChangePasswordPageServlet'
    
        Extends:
            org.openhab.core.io.http.auth.internal.AbstractAuthPageServlet
    
      Constructors:
        * ChangePasswordPageServlet(org.osgi.framework.BundleContext, org.osgi.service.http.HttpService, org.openhab.core.auth.UserRegistry, org.openhab.core.auth.AuthenticationProvider, org.openhab.core.i18n.LocaleProvider)
    
    """
    def __init__(self, bundleContext: org.osgi.framework.BundleContext, httpService: org.osgi.service.http.HttpService, userRegistry: org.openhab.core.auth.UserRegistry, authProvider: org.openhab.core.auth.AuthenticationProvider, localeProvider: org.openhab.core.i18n.LocaleProvider): ...
    def deactivate(self) -> None: ...

class CreateAPITokenPageServlet(AbstractAuthPageServlet):
    """
    Java class 'org.openhab.core.io.http.auth.internal.CreateAPITokenPageServlet'
    
        Extends:
            org.openhab.core.io.http.auth.internal.AbstractAuthPageServlet
    
      Constructors:
        * CreateAPITokenPageServlet(org.osgi.framework.BundleContext, org.osgi.service.http.HttpService, org.openhab.core.auth.UserRegistry, org.openhab.core.auth.AuthenticationProvider, org.openhab.core.i18n.LocaleProvider)
    
    """
    def __init__(self, bundleContext: org.osgi.framework.BundleContext, httpService: org.osgi.service.http.HttpService, userRegistry: org.openhab.core.auth.UserRegistry, authProvider: org.openhab.core.auth.AuthenticationProvider, localeProvider: org.openhab.core.i18n.LocaleProvider): ...
    def deactivate(self) -> None: ...
