import java.lang
import javax.ws.rs.core
import org.openhab.core.io.rest
import org.osgi.framework
import typing


class OpenApiResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.swagger.impl.OpenApiResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * OpenApiResource(org.osgi.framework.BundleContext, javax.ws.rs.core.Application)
    
      Attributes:
        API_TITLE (java.lang.String): final static field
        CONTACT_NAME (java.lang.String): final static field
        CONTACT_URL (java.lang.String): final static field
        OAUTH_AUTHORIZE_ENDPOINT (java.lang.String): final static field
        OAUTH_TOKEN_ENDPOINT (java.lang.String): final static field
    
    """
    API_TITLE: typing.ClassVar[java.lang.String] = ...
    CONTACT_NAME: typing.ClassVar[java.lang.String] = ...
    CONTACT_URL: typing.ClassVar[java.lang.String] = ...
    OAUTH_AUTHORIZE_ENDPOINT: typing.ClassVar[java.lang.String] = ...
    OAUTH_TOKEN_ENDPOINT: typing.ClassVar[java.lang.String] = ...
    def __init__(self, bc: org.osgi.framework.BundleContext, application: javax.ws.rs.core.Application): ...
    def getOpenAPI(self) -> typing.Any: ...
