import java.lang
import org.openhab.core.model.core


class PersistenceRuntimeActivator(org.openhab.core.model.core.ModelParser):
    """
    Java class 'org.openhab.core.model.persistence.runtime.internal.PersistenceRuntimeActivator'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.core.ModelParser
    
      Constructors:
        * PersistenceRuntimeActivator()
    
    """
    def __init__(self): ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def getExtension(self) -> java.lang.String: ...
