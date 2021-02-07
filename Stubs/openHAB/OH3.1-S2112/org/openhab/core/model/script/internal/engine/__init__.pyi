import java.util
import org.openhab.core.model.script
import org.openhab.core.model.script.engine
import org.openhab.core.model.script.engine.action
import org.openhab.core.thing.binding


class ServiceTrackerActionServiceProvider(org.openhab.core.model.script.engine.IActionServiceProvider):
    """
    Java class 'org.openhab.core.model.script.internal.engine.ServiceTrackerActionServiceProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.script.engine.IActionServiceProvider
    
      Constructors:
        * ServiceTrackerActionServiceProvider(org.openhab.core.model.script.ScriptServiceUtil)
    
    """
    def __init__(self, scriptServiceUtil: org.openhab.core.model.script.ScriptServiceUtil): ...
    def get(self) -> java.util.List[org.openhab.core.model.script.engine.action.ActionService]: ...

class ServiceTrackerThingActionsProvider(org.openhab.core.model.script.engine.IThingActionsProvider):
    """
    Java class 'org.openhab.core.model.script.internal.engine.ServiceTrackerThingActionsProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.script.engine.IThingActionsProvider
    
      Constructors:
        * ServiceTrackerThingActionsProvider(org.openhab.core.model.script.ScriptServiceUtil)
    
    """
    def __init__(self, scriptServiceUtil: org.openhab.core.model.script.ScriptServiceUtil): ...
    def get(self) -> java.util.List[org.openhab.core.thing.binding.ThingActions]: ...
