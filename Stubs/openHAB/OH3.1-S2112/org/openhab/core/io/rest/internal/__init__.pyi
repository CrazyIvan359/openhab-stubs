import java.lang
import java.util.stream
import javax.ws.rs.core
import org.openhab.core.io.rest
import typing


class Constants(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.internal.Constants'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Constants()
    
      Attributes:
        CORS_PROPERTY (java.lang.String): final static field
    
    """
    CORS_PROPERTY: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...

class DTOMapperImpl(org.openhab.core.io.rest.DTOMapper):
    """
    Java class 'org.openhab.core.io.rest.internal.DTOMapperImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.DTOMapper
    
      Constructors:
        * DTOMapperImpl()
    
    """
    def __init__(self): ...
    _limitToFields__T = typing.TypeVar('_limitToFields__T')  # <T>
    def limitToFields(self, itemStream: java.util.stream.Stream[_limitToFields__T], fields: java.lang.String) -> java.util.stream.Stream[_limitToFields__T]: ...

class RESTApplicationImpl(javax.ws.rs.core.Application):
    """
    Java class 'org.openhab.core.io.rest.internal.RESTApplicationImpl'
    
        Extends:
            javax.ws.rs.core.Application
    
      Constructors:
        * RESTApplicationImpl()
    
    """
    def __init__(self): ...
