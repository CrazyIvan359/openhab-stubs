import java.lang
import java.util
import org.osgi.dto


class CapabilityDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.resource.dto.CapabilityDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * CapabilityDTO()
    
      Attributes:
        id (int): field
        namespace (java.lang.String): field
        directives (java.util.Map): field
        attributes (java.util.Map): field
        resource (int): field
    
    """
    id: int = ...
    namespace: java.lang.String = ...
    directives: java.util.Map = ...
    attributes: java.util.Map = ...
    resource: int = ...
    def __init__(self): ...

class CapabilityRefDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.resource.dto.CapabilityRefDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * CapabilityRefDTO()
    
      Attributes:
        capability (int): field
        resource (int): field
    
    """
    capability: int = ...
    resource: int = ...
    def __init__(self): ...

class RequirementDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.resource.dto.RequirementDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * RequirementDTO()
    
      Attributes:
        id (int): field
        namespace (java.lang.String): field
        directives (java.util.Map): field
        attributes (java.util.Map): field
        resource (int): field
    
    """
    id: int = ...
    namespace: java.lang.String = ...
    directives: java.util.Map = ...
    attributes: java.util.Map = ...
    resource: int = ...
    def __init__(self): ...

class RequirementRefDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.resource.dto.RequirementRefDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * RequirementRefDTO()
    
      Attributes:
        requirement (int): field
        resource (int): field
    
    """
    requirement: int = ...
    resource: int = ...
    def __init__(self): ...

class ResourceDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.resource.dto.ResourceDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * ResourceDTO()
    
      Attributes:
        id (int): field
        capabilities (java.util.List): field
        requirements (java.util.List): field
    
    """
    id: int = ...
    capabilities: java.util.List = ...
    requirements: java.util.List = ...
    def __init__(self): ...

class WireDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.resource.dto.WireDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * WireDTO()
    
      Attributes:
        capability (org.osgi.resource.dto.CapabilityRefDTO): field
        requirement (org.osgi.resource.dto.RequirementRefDTO): field
        provider (int): field
        requirer (int): field
    
    """
    capability: CapabilityRefDTO = ...
    requirement: RequirementRefDTO = ...
    provider: int = ...
    requirer: int = ...
    def __init__(self): ...

class WiringDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.resource.dto.WiringDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * WiringDTO()
    
      Attributes:
        id (int): field
        capabilities (java.util.List): field
        requirements (java.util.List): field
        providedWires (java.util.List): field
        requiredWires (java.util.List): field
        resource (int): field
    
    """
    id: int = ...
    capabilities: java.util.List = ...
    requirements: java.util.List = ...
    providedWires: java.util.List = ...
    requiredWires: java.util.List = ...
    resource: int = ...
    def __init__(self): ...
