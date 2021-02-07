import java.lang
import org.osgi.service.http.runtime.dto
import typing


class HttpServiceRuntime(java.lang.Object):
    """
    Java class 'org.osgi.service.http.runtime.HttpServiceRuntime'
    
    """
    def calculateRequestInfoDTO(self, string: java.lang.String) -> org.osgi.service.http.runtime.dto.RequestInfoDTO: ...
    def getRuntimeDTO(self) -> org.osgi.service.http.runtime.dto.RuntimeDTO: ...

class HttpServiceRuntimeConstants(java.lang.Object):
    """
    Java class 'org.osgi.service.http.runtime.HttpServiceRuntimeConstants'
    
        Extends:
            java.lang.Object
    
      Attributes:
        HTTP_SERVICE_ENDPOINT (java.lang.String): final static field
        HTTP_SERVICE_ID (java.lang.String): final static field
    
    """
    HTTP_SERVICE_ENDPOINT: typing.ClassVar[java.lang.String] = ...
    HTTP_SERVICE_ID: typing.ClassVar[java.lang.String] = ...
