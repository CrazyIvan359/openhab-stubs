import java.lang
import org.openhab.core.model.core


class ItemRuntimeActivator(org.openhab.core.model.core.ModelParser):
    """
    Java class 'org.openhab.core.model.item.runtime.internal.ItemRuntimeActivator'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.core.ModelParser
    
      Constructors:
        * ItemRuntimeActivator()
    
    """
    def __init__(self): ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def getExtension(self) -> java.lang.String: ...
