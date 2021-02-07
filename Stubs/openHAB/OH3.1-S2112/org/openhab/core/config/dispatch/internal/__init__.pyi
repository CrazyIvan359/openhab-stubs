import java.io
import java.lang
import java.util
import org.openhab.core.service
import org.osgi.framework
import org.osgi.service.cm
import typing


class ConfigDispatcher(java.lang.Object):
    """
    Java class 'org.openhab.core.config.dispatch.internal.ConfigDispatcher'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConfigDispatcher(org.osgi.service.cm.ConfigurationAdmin)
    
      Attributes:
        SERVICE_CONTEXT_MARKER (java.lang.String): final static field
        SERVICECFG_PROG_ARGUMENT (java.lang.String): final static field
        SERVICE_PID_NAMESPACE (java.lang.String): final static field
        SERVICE_CFG_FILE (java.lang.String): final static field
    
    """
    SERVICE_CONTEXT_MARKER: typing.ClassVar[java.lang.String] = ...
    SERVICECFG_PROG_ARGUMENT: typing.ClassVar[java.lang.String] = ...
    SERVICE_PID_NAMESPACE: typing.ClassVar[java.lang.String] = ...
    SERVICE_CFG_FILE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, configAdmin: org.osgi.service.cm.ConfigurationAdmin): ...
    def activate(self, bundleContext: org.osgi.framework.BundleContext) -> None: ...
    def fileRemoved(self, path: java.lang.String) -> None: ...
    def processConfigFile(self, dir: java.io.File) -> None: ...
    class ExclusivePIDMap(java.lang.Object):
        """
        Java class 'org.openhab.core.config.dispatch.internal.ConfigDispatcher$ExclusivePIDMap'
        
            Extends:
                java.lang.Object
        
        """
        def contains(self, pid: java.lang.String) -> bool: ...
        def getOrphanPIDs(self) -> java.util.List[java.lang.String]: ...
        def initializeProcessPIDMapping(self) -> None: ...
        def removeExclusivePID(self, pid: java.lang.String) -> None: ...
        def setCurrentExclusivePIDList(self) -> None: ...
        def setFileRemoved(self, absolutePath: java.lang.String) -> None: ...
        def setProcessedPID(self, pid: java.lang.String, pathToFile: java.lang.String) -> None: ...

class ConfigDispatcherFileWatcher(org.openhab.core.service.AbstractWatchService):
    """
    Java class 'org.openhab.core.config.dispatch.internal.ConfigDispatcherFileWatcher'
    
        Extends:
            org.openhab.core.service.AbstractWatchService
    
      Constructors:
        * ConfigDispatcherFileWatcher(org.openhab.core.config.dispatch.internal.ConfigDispatcher)
    
      Attributes:
        SERVICEDIR_PROG_ARGUMENT (java.lang.String): final static field
        SERVICES_FOLDER (java.lang.String): final static field
    
    """
    SERVICEDIR_PROG_ARGUMENT: typing.ClassVar[java.lang.String] = ...
    SERVICES_FOLDER: typing.ClassVar[java.lang.String] = ...
    def __init__(self, configDispatcher: ConfigDispatcher): ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
