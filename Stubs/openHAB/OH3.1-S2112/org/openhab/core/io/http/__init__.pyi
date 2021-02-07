import java.lang
import javax.servlet.http
import org.osgi.framework
import org.osgi.service.http
import typing


class Handler(java.lang.Object):
    """
    public interface Handler
    
        Handler which is responsible for processing request and response. This type is introduced to provide a unified way for
        injecting various logic on verification of requests sent via HTTP. Handlers are called before servlet who will receive
        request, thus they can not mutate servlet response, but they can generate its own response depending on actual needs.
        Pay attention to error handling - as a proper executions might report exceptions, but fault path handled in
        :meth:`~org.openhab.core.io.http.Handler.handleError`
    
    
    """
    def getPriority(self) -> int: ...
    def handle(self, request: javax.servlet.http.HttpServletRequest, response: javax.servlet.http.HttpServletResponse, context: 'HandlerContext') -> None: ...
    def handleError(self, request: javax.servlet.http.HttpServletRequest, response: javax.servlet.http.HttpServletResponse, context: 'HandlerContext') -> None: ...

class HandlerContext(java.lang.Object):
    """
    public interface HandlerContext
    
        Handler context represents a present state of all handlers placed in execution chain. There are two basic operations
        located in this type - first allows to continue execution and let next handler be called. Second is intended to break
        the chain and force handlers to process error and generate error response. When Handler decide to not call context by
        delegating further handler to get called via :meth:`~org.openhab.core.io.http.HandlerContext.execute` nor
        :meth:`~org.openhab.core.io.http.HandlerContext.error` then chain is stopped. By this simple way handlers can decide to
        hold processing and generate own response.
    
    
    """
    ERROR_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    def error(self, error: java.lang.Exception) -> None: ...
    def execute(self, request: javax.servlet.http.HttpServletRequest, response: javax.servlet.http.HttpServletResponse) -> None: ...
    def hasError(self) -> bool: ...

class HandlerPriorities(java.lang.Object):
    """
    public interface HandlerPriorities
    
        Constants for making handlers in proper order.
    
    
    """
    AUTHENTICATION: typing.ClassVar[int] = ...

class HttpContextFactoryService(java.lang.Object):
    """
    public interface HttpContextFactoryService
    
        Create :code:`HttpContext` instances when registering servlets, resources or filters using the
        :code:`HttpService.registerServlet(java.lang.String, javax.servlet.Servlet, java.util.Dictionary<?, ?>,
        org.osgi.service.http.HttpContext)` and corresponding methods.
    
    
    """
    def createDefaultHttpContext(self, bundle: org.osgi.framework.Bundle) -> org.osgi.service.http.HttpContext: ...

class WrappingHttpContext(org.osgi.service.http.HttpContext):
    """
    public interface WrappingHttpContext extends org.osgi.service.http.HttpContext
    
        Extension of standard :code:`HttpContext` interface which allows creation of "sub contexts". These sub contexts are
        nothing else but custom resource locators which provide new files to host, but should not influence overall processing
        logic of :code:`HttpContext.handleSecurity(javax.servlet.http.HttpServletRequest,
        javax.servlet.http.HttpServletResponse)` and :code:`HttpContext.getMimeType(String)`.
    
    
    """
    def wrap(self, bundle: org.osgi.framework.Bundle) -> org.osgi.service.http.HttpContext: ...
