import java.lang
import java.util
import org.osgi.dto
import typing


class BundleDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.framework.dto.BundleDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * BundleDTO()
    
      Attributes:
        id (long): field
        lastModified (long): field
        state (int): field
        symbolicName (java.lang.String): field
        version (java.lang.String): field
    
    """
    id: int = ...
    lastModified: int = ...
    state: int = ...
    symbolicName: java.lang.String = ...
    version: java.lang.String = ...
    def __init__(self): ...

class FrameworkDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.framework.dto.FrameworkDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * FrameworkDTO()
    
      Attributes:
        bundles (java.util.List): field
        properties (java.util.Map): field
        services (java.util.List): field
    
    """
    bundles: java.util.List = ...
    properties: java.util.Map = ...
    services: java.util.List = ...
    def __init__(self): ...

class ServiceReferenceDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.framework.dto.ServiceReferenceDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * ServiceReferenceDTO()
    
      Attributes:
        id (long): field
        bundle (long): field
        properties (java.util.Map): field
        usingBundles ([J): field
    
    """
    id: int = ...
    bundle: int = ...
    properties: java.util.Map = ...
    usingBundles: typing.List[int] = ...
    def __init__(self): ...
