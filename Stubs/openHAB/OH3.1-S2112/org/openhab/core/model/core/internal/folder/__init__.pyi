import java.lang
import org.openhab.core.model.core
import org.openhab.core.service
import org.osgi.service.component
import typing


class FolderObserver(org.openhab.core.service.AbstractWatchService):
    """
    Java class 'org.openhab.core.model.core.internal.folder.FolderObserver'
    
        Extends:
            org.openhab.core.service.AbstractWatchService
    
      Constructors:
        * FolderObserver(org.openhab.core.model.core.ModelRepository, org.openhab.core.service.ReadyService)
    
    """
    def __init__(self, modelRepo: org.openhab.core.model.core.ModelRepository, readyService: org.openhab.core.service.ReadyService): ...
    @typing.overload
    def activate(self, ctx: org.osgi.service.component.ComponentContext) -> None: ...
    @typing.overload
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def getExtension(self, filename: java.lang.String) -> java.lang.String: ...
