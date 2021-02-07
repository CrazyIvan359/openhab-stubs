import org.osgi.dto


class BundleStartLevelDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.framework.startlevel.dto.BundleStartLevelDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * BundleStartLevelDTO()
    
      Attributes:
        bundle (long): field
        startLevel (int): field
        activationPolicyUsed (boolean): field
        persistentlyStarted (boolean): field
    
    """
    bundle: int = ...
    startLevel: int = ...
    activationPolicyUsed: bool = ...
    persistentlyStarted: bool = ...
    def __init__(self): ...

class FrameworkStartLevelDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.framework.startlevel.dto.FrameworkStartLevelDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * FrameworkStartLevelDTO()
    
      Attributes:
        startLevel (int): field
        initialBundleStartLevel (int): field
    
    """
    startLevel: int = ...
    initialBundleStartLevel: int = ...
    def __init__(self): ...
