import java.lang
import org.eclipse.xtext.scoping.impl
import org.openhab.core.model.persistence.persistence
import typing


class AbstractPersistenceScopeProvider(org.eclipse.xtext.scoping.impl.DelegatingScopeProvider):
    """
    Java class 'org.openhab.core.model.persistence.scoping.AbstractPersistenceScopeProvider'
    
        Extends:
            org.eclipse.xtext.scoping.impl.DelegatingScopeProvider
    
      Constructors:
        * AbstractPersistenceScopeProvider()
    
    """
    def __init__(self): ...

class GlobalStrategies(java.lang.Object):
    """
    Java class 'org.openhab.core.model.persistence.scoping.GlobalStrategies'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * GlobalStrategies()
    
      Attributes:
        UPDATE (org.openhab.core.model.persistence.persistence.Strategy): final static field
        CHANGE (org.openhab.core.model.persistence.persistence.Strategy): final static field
        RESTORE (org.openhab.core.model.persistence.persistence.Strategy): final static field
    
    """
    UPDATE: typing.ClassVar[org.openhab.core.model.persistence.persistence.Strategy] = ...
    CHANGE: typing.ClassVar[org.openhab.core.model.persistence.persistence.Strategy] = ...
    RESTORE: typing.ClassVar[org.openhab.core.model.persistence.persistence.Strategy] = ...
    def __init__(self): ...

class PersistenceGlobalScopeProvider(org.eclipse.xtext.scoping.impl.AbstractGlobalScopeProvider):
    """
    Java class 'org.openhab.core.model.persistence.scoping.PersistenceGlobalScopeProvider'
    
        Extends:
            org.eclipse.xtext.scoping.impl.AbstractGlobalScopeProvider
    
      Constructors:
        * PersistenceGlobalScopeProvider()
    
    """
    def __init__(self): ...

class PersistenceScopeProvider(org.eclipse.xtext.scoping.impl.AbstractDeclarativeScopeProvider):
    """
    Java class 'org.openhab.core.model.persistence.scoping.PersistenceScopeProvider'
    
        Extends:
            org.eclipse.xtext.scoping.impl.AbstractDeclarativeScopeProvider
    
      Constructors:
        * PersistenceScopeProvider()
    
    """
    def __init__(self): ...
