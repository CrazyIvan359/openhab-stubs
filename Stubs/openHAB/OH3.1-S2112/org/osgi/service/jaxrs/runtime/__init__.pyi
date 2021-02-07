import java.lang
import org.osgi.service.jaxrs.runtime.dto
import typing


class JaxrsEndpoint(java.lang.Object):
    """
    Java class 'org.osgi.service.jaxrs.runtime.JaxrsEndpoint'
    
      Attributes:
        JAX_RS_URI (java.lang.String): final static field
        JAX_RS_BUNDLE_SYMBOLICNAME (java.lang.String): final static field
        JAX_RS_BUNDLE_ID (java.lang.String): final static field
        JAX_RS_BUNDLE_VERSION (java.lang.String): final static field
        JAX_RS_SERVICE_ID (java.lang.String): final static field
    
    """
    JAX_RS_URI: typing.ClassVar[java.lang.String] = ...
    JAX_RS_BUNDLE_SYMBOLICNAME: typing.ClassVar[java.lang.String] = ...
    JAX_RS_BUNDLE_ID: typing.ClassVar[java.lang.String] = ...
    JAX_RS_BUNDLE_VERSION: typing.ClassVar[java.lang.String] = ...
    JAX_RS_SERVICE_ID: typing.ClassVar[java.lang.String] = ...

class JaxrsServiceRuntime(java.lang.Object):
    """
    Java class 'org.osgi.service.jaxrs.runtime.JaxrsServiceRuntime'
    
    """
    def getRuntimeDTO(self) -> org.osgi.service.jaxrs.runtime.dto.RuntimeDTO: ...

class JaxrsServiceRuntimeConstants(java.lang.Object):
    """
    Java class 'org.osgi.service.jaxrs.runtime.JaxrsServiceRuntimeConstants'
    
        Extends:
            java.lang.Object
    
      Attributes:
        JAX_RS_SERVICE_ENDPOINT (java.lang.String): final static field
    
    """
    JAX_RS_SERVICE_ENDPOINT: typing.ClassVar[java.lang.String] = ...
