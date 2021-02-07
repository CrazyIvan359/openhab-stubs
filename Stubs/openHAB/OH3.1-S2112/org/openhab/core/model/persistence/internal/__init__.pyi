import java.lang
import org.openhab.core.model.core


class PersistenceModelManager(org.openhab.core.model.core.ModelRepositoryChangeListener):
    """
    Java class 'org.openhab.core.model.persistence.internal.PersistenceModelManager'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.core.ModelRepositoryChangeListener
    
      Constructors:
        * PersistenceModelManager()
    
    """
    def __init__(self): ...
    def modelChanged(self, modelName: java.lang.String, type: org.openhab.core.model.core.EventType) -> None: ...
