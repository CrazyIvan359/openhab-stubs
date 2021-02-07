import java.lang
import java.util
import org.osgi.dto
import org.osgi.resource.dto


class BundleRevisionDTO(org.osgi.resource.dto.ResourceDTO):
    """
    Java class 'org.osgi.framework.wiring.dto.BundleRevisionDTO'
    
        Extends:
            org.osgi.resource.dto.ResourceDTO
    
      Constructors:
        * BundleRevisionDTO()
    
      Attributes:
        symbolicName (java.lang.String): field
        type (int): field
        version (java.lang.String): field
        bundle (long): field
    
    """
    symbolicName: java.lang.String = ...
    type: int = ...
    version: java.lang.String = ...
    bundle: int = ...
    def __init__(self): ...

class BundleWireDTO(org.osgi.resource.dto.WireDTO):
    """
    Java class 'org.osgi.framework.wiring.dto.BundleWireDTO'
    
        Extends:
            org.osgi.resource.dto.WireDTO
    
      Constructors:
        * BundleWireDTO()
    
      Attributes:
        providerWiring (int): field
        requirerWiring (int): field
    
    """
    providerWiring: int = ...
    requirerWiring: int = ...
    def __init__(self): ...

class BundleWiringDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.framework.wiring.dto.BundleWiringDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * BundleWiringDTO()
    
      Attributes:
        bundle (long): field
        root (int): field
        nodes (java.util.Set): field
        resources (java.util.Set): field
    
    """
    bundle: int = ...
    root: int = ...
    nodes: java.util.Set = ...
    resources: java.util.Set = ...
    def __init__(self): ...
    class NodeDTO(org.osgi.resource.dto.WiringDTO):
        """
        Java class 'org.osgi.framework.wiring.dto.BundleWiringDTO$NodeDTO'
        
            Extends:
                org.osgi.resource.dto.WiringDTO
        
          Constructors:
            * NodeDTO()
        
          Attributes:
            inUse (boolean): field
            current (boolean): field
        
        """
        inUse: bool = ...
        current: bool = ...
        def __init__(self): ...
