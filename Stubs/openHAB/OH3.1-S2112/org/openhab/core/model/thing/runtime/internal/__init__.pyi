import java.lang
import org.openhab.core.model.core


class ThingRuntimeActivator(org.openhab.core.model.core.ModelParser):
    """
    Java class 'org.openhab.core.model.thing.runtime.internal.ThingRuntimeActivator'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.core.ModelParser
    
      Constructors:
        * ThingRuntimeActivator()
    
    """
    def __init__(self): ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def getExtension(self) -> java.lang.String: ...
