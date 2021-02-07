import org.openhab.core.automation.module.script
import org.openhab.core.service


class ScriptFileWatcher(org.openhab.core.service.AbstractWatchService, org.openhab.core.service.ReadyService.ReadyTracker):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.internal.loader.ScriptFileWatcher'
    
        Extends:
            org.openhab.core.service.AbstractWatchService
    
        Interfaces:
            org.openhab.core.service.ReadyService.ReadyTracker
    
      Constructors:
        * ScriptFileWatcher(org.openhab.core.automation.module.script.ScriptEngineManager, org.openhab.core.service.ReadyService)
    
    """
    def __init__(self, manager: org.openhab.core.automation.module.script.ScriptEngineManager, readyService: org.openhab.core.service.ReadyService): ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def onReadyMarkerAdded(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
    def onReadyMarkerRemoved(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
