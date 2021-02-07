import java.lang


class PersistenceConfig(java.lang.Object):
    """
    Java class 'org.openhab.core.persistence.config.PersistenceConfig'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PersistenceConfig()
    
    """
    def __init__(self): ...

class PersistenceAllConfig(PersistenceConfig):
    """
    Java class 'org.openhab.core.persistence.config.PersistenceAllConfig'
    
        Extends:
            org.openhab.core.persistence.config.PersistenceConfig
    
      Constructors:
        * PersistenceAllConfig()
    
    """
    def __init__(self): ...
    def toString(self) -> java.lang.String: ...

class PersistenceGroupConfig(PersistenceConfig):
    """
    Java class 'org.openhab.core.persistence.config.PersistenceGroupConfig'
    
        Extends:
            org.openhab.core.persistence.config.PersistenceConfig
    
      Constructors:
        * PersistenceGroupConfig(java.lang.String)
    
    """
    def __init__(self, group: java.lang.String): ...
    def getGroup(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class PersistenceItemConfig(PersistenceConfig):
    """
    Java class 'org.openhab.core.persistence.config.PersistenceItemConfig'
    
        Extends:
            org.openhab.core.persistence.config.PersistenceConfig
    
      Constructors:
        * PersistenceItemConfig(java.lang.String)
    
    """
    def __init__(self, item: java.lang.String): ...
    def getItem(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
