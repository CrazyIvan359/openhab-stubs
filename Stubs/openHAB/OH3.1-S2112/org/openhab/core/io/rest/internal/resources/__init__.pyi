import java.lang
import javax.ws.rs.core
import org.openhab.core.i18n
import org.openhab.core.io.rest
import org.osgi.service.jaxrs.runtime
import typing


class RootResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.internal.resources.RootResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * RootResource(org.osgi.service.jaxrs.runtime.JaxrsServiceRuntime, org.openhab.core.i18n.LocaleProvider, org.openhab.core.i18n.UnitProvider)
    
      Attributes:
        RESOURCE_NAME (java.lang.String): final static field
    
    """
    RESOURCE_NAME: typing.ClassVar[java.lang.String] = ...
    def __init__(self, runtime: org.osgi.service.jaxrs.runtime.JaxrsServiceRuntime, localeProvider: org.openhab.core.i18n.LocaleProvider, unitProvider: org.openhab.core.i18n.UnitProvider): ...
    def getRoot(self, uriInfo: javax.ws.rs.core.UriInfo) -> javax.ws.rs.core.Response: ...

class SystemInfoResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.internal.resources.SystemInfoResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * SystemInfoResource()
    
      Attributes:
        PATH_SYSTEMINFO (java.lang.String): final static field
    
    """
    PATH_SYSTEMINFO: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    def getSystemInfo(self, uriInfo: javax.ws.rs.core.UriInfo) -> javax.ws.rs.core.Response: ...
