import javax.ws.rs.container


class CorsFilter(javax.ws.rs.container.ContainerResponseFilter):
    """
    Java class 'org.openhab.core.io.rest.internal.filter.CorsFilter'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            javax.ws.rs.container.ContainerResponseFilter
    
      Constructors:
        * CorsFilter()
    
    """
    def __init__(self): ...
    def filter(self, requestContext: javax.ws.rs.container.ContainerRequestContext, responseContext: javax.ws.rs.container.ContainerResponseContext) -> None: ...

class ProxyFilter(javax.ws.rs.container.ContainerRequestFilter):
    """
    Java class 'org.openhab.core.io.rest.internal.filter.ProxyFilter'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            javax.ws.rs.container.ContainerRequestFilter
    
      Constructors:
        * ProxyFilter()
    
    """
    def __init__(self): ...
    def filter(self, ctx: javax.ws.rs.container.ContainerRequestContext) -> None: ...
