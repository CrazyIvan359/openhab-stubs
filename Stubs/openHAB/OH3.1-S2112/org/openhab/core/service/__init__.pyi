import java.lang
import java.nio.file
import java.util
import org.openhab.core.events
import org.openhab.core.types
import org.osgi.framework
import typing


class AbstractWatchService(java.lang.Object):
    """
    Java class 'org.openhab.core.service.AbstractWatchService'
    
        Extends:
            java.lang.Object
    
    """
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def getSourcePath(self) -> java.nio.file.Path: ...

class CommandDescriptionService(java.lang.Object):
    """
    @NonNullByDefault public interface CommandDescriptionService
    
        An implementation of this service provides locale specific :class:`~org.openhab.core.types.CommandDescription`s for the
        given item.
    
    
    """
    def getCommandDescription(self, itemName: java.lang.String, locale: java.util.Locale) -> org.openhab.core.types.CommandDescription: ...

class ReadyMarker(java.lang.Object):
    """
    Java class 'org.openhab.core.service.ReadyMarker'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ReadyMarker(java.lang.String, java.lang.String)
    
    """
    def __init__(self, type: java.lang.String, identifier: java.lang.String): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getIdentifier(self) -> java.lang.String: ...
    def getType(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class ReadyMarkerFilter(java.lang.Object):
    """
    Java class 'org.openhab.core.service.ReadyMarkerFilter'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ReadyMarkerFilter()
    
    """
    def __init__(self): ...
    def apply(self, readyMarker: ReadyMarker) -> bool: ...
    def withIdentifier(self, identifier: java.lang.String) -> 'ReadyMarkerFilter': ...
    def withType(self, type: java.lang.String) -> 'ReadyMarkerFilter': ...

class ReadyMarkerUtils(java.lang.Object):
    """
    Java class 'org.openhab.core.service.ReadyMarkerUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ReadyMarkerUtils()
    
    """
    def __init__(self): ...
    @classmethod
    def debugString(cls, bundle: org.osgi.framework.Bundle) -> java.lang.String: ...
    @classmethod
    def getIdentifier(cls, bundle: org.osgi.framework.Bundle) -> java.lang.String: ...

class ReadyService(java.lang.Object):
    """
    @NonNullByDefault public interface ReadyService
    
        Registry for :class:`~org.openhab.core.service.ReadyMarker`s. Services may use the
        :class:`~org.openhab.core.service.ReadyService` in order to denote they have completed loading/processing something.
    
        Interested parties may register as a tracker for :class:`~org.openhab.core.service.ReadyMarker`s. Optionally they can
        provide a :class:`~org.openhab.core.service.ReadyMarkerFilter` in order to restrict the
        :class:`~org.openhab.core.service.ReadyMarker`s they get notified for.
    
        Alternatively, :meth:`~org.openhab.core.service.ReadyService.isReady` can be used to check for any given
        :class:`~org.openhab.core.service.ReadyMarker`.
    
    
    """
    def isReady(self, readyMarker: ReadyMarker) -> bool: ...
    def markReady(self, readyMarker: ReadyMarker) -> None: ...
    @typing.overload
    def registerTracker(self, readyTracker: 'ReadyService.ReadyTracker') -> None: ...
    @typing.overload
    def registerTracker(self, readyTracker: 'ReadyService.ReadyTracker', filter: ReadyMarkerFilter) -> None: ...
    def unmarkReady(self, readyMarker: ReadyMarker) -> None: ...
    def unregisterTracker(self, readyTracker: 'ReadyService.ReadyTracker') -> None: ...
    class ReadyTracker(java.lang.Object):
        """
        Java class 'org.openhab.core.service.ReadyService$ReadyTracker'
        
        """
        def onReadyMarkerAdded(self, readyMarker: ReadyMarker) -> None: ...
        def onReadyMarkerRemoved(self, readyMarker: ReadyMarker) -> None: ...

class StartLevelService(java.lang.Object):
    """
    Java class 'org.openhab.core.service.StartLevelService'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * StartLevelService(org.osgi.framework.BundleContext, org.openhab.core.service.ReadyService, org.openhab.core.events.EventPublisher)
    
      Attributes:
        STARTLEVEL_MARKER_TYPE (java.lang.String): final static field
        STARTLEVEL_OSGI (int): final static field
        STARTLEVEL_MODEL (int): final static field
        STARTLEVEL_STATES (int): final static field
        STARTLEVEL_RULES (int): final static field
        STARTLEVEL_RULEENGINE (int): final static field
        STARTLEVEL_UI (int): final static field
        STARTLEVEL_THINGS (int): final static field
        STARTLEVEL_COMPLETE (int): final static field
    
    """
    STARTLEVEL_MARKER_TYPE: typing.ClassVar[java.lang.String] = ...
    STARTLEVEL_OSGI: typing.ClassVar[int] = ...
    STARTLEVEL_MODEL: typing.ClassVar[int] = ...
    STARTLEVEL_STATES: typing.ClassVar[int] = ...
    STARTLEVEL_RULES: typing.ClassVar[int] = ...
    STARTLEVEL_RULEENGINE: typing.ClassVar[int] = ...
    STARTLEVEL_UI: typing.ClassVar[int] = ...
    STARTLEVEL_THINGS: typing.ClassVar[int] = ...
    STARTLEVEL_COMPLETE: typing.ClassVar[int] = ...
    def __init__(self, bundleContext: org.osgi.framework.BundleContext, readyService: ReadyService, eventPublisher: org.openhab.core.events.EventPublisher): ...
    def getStartLevel(self) -> int: ...

class StateDescriptionService(java.lang.Object):
    """
    @NonNullByDefault public interface StateDescriptionService
    
        Implementations of this service provide strategies for merging info from different StateDescriptionProviders into one
        StateDescription.
    
    
    """
    def getStateDescription(self, itemName: java.lang.String, locale: java.util.Locale) -> org.openhab.core.types.StateDescription: ...

class WatchQueueReader(java.lang.Runnable):
    """
    Java class 'org.openhab.core.service.WatchQueueReader'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.lang.Runnable
    
    """
    @classmethod
    def getInstance(cls) -> 'WatchQueueReader': ...
    def run(self) -> None: ...
    def stopWatchService(self, service: AbstractWatchService) -> None: ...
