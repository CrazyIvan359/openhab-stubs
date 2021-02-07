import java.lang
import typing


class PersistenceStrategy(java.lang.Object):
    """
    Java class 'org.openhab.core.persistence.strategy.PersistenceStrategy'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PersistenceStrategy(java.lang.String)
    
    """
    def __init__(self, name: java.lang.String): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getName(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    class Globals(java.lang.Object):
        """
        Java class 'org.openhab.core.persistence.strategy.PersistenceStrategy$Globals'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * Globals()
        
          Attributes:
            UPDATE (org.openhab.core.persistence.strategy.PersistenceStrategy): final static field
            CHANGE (org.openhab.core.persistence.strategy.PersistenceStrategy): final static field
            RESTORE (org.openhab.core.persistence.strategy.PersistenceStrategy): final static field
        
        """
        UPDATE: typing.ClassVar['PersistenceStrategy'] = ...
        CHANGE: typing.ClassVar['PersistenceStrategy'] = ...
        RESTORE: typing.ClassVar['PersistenceStrategy'] = ...
        def __init__(self): ...

class PersistenceCronStrategy(PersistenceStrategy):
    """
    Java class 'org.openhab.core.persistence.strategy.PersistenceCronStrategy'
    
        Extends:
            org.openhab.core.persistence.strategy.PersistenceStrategy
    
      Constructors:
        * PersistenceCronStrategy(java.lang.String, java.lang.String)
    
    """
    def __init__(self, name: java.lang.String, cronExpression: java.lang.String): ...
    def getCronExpression(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
