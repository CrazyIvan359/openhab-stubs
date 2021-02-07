import java.lang
import javax.ws.rs.core
import org.openhab.core.io.rest
import typing


class UUIDResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.id.internal.UUIDResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * UUIDResource()
    
      Attributes:
        PATH_UUID (java.lang.String): final static field
    
    """
    PATH_UUID: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    def getInstanceUUID(self) -> javax.ws.rs.core.Response: ...
