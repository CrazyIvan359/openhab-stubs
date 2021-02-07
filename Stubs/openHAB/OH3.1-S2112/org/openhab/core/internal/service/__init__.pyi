import java.lang
import java.util
import org.openhab.core.service
import org.openhab.core.types
import org.openhab.core.util
import org.osgi.framework
import typing


class BundleResolverImpl(org.openhab.core.util.BundleResolver):
    """
    Java class 'org.openhab.core.internal.service.BundleResolverImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.util.BundleResolver
    
      Constructors:
        * BundleResolverImpl()
    
    """
    def __init__(self): ...
    def resolveBundle(self, clazz: typing.Type[typing.Any]) -> org.osgi.framework.Bundle: ...

class CommandDescriptionServiceImpl(org.openhab.core.service.CommandDescriptionService):
    """
    Java class 'org.openhab.core.internal.service.CommandDescriptionServiceImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.service.CommandDescriptionService
    
      Constructors:
        * CommandDescriptionServiceImpl()
    
    """
    def __init__(self): ...
    def getCommandDescription(self, itemName: java.lang.String, locale: java.util.Locale) -> org.openhab.core.types.CommandDescription: ...

class ReadyServiceImpl(org.openhab.core.service.ReadyService):
    """
    Java class 'org.openhab.core.internal.service.ReadyServiceImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.service.ReadyService
    
      Constructors:
        * ReadyServiceImpl()
    
    """
    def __init__(self): ...
    def isReady(self, readyMarker: org.openhab.core.service.ReadyMarker) -> bool: ...
    def markReady(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
    @typing.overload
    def registerTracker(self, readyTracker: org.openhab.core.service.ReadyService.ReadyTracker) -> None: ...
    @typing.overload
    def registerTracker(self, readyTracker: org.openhab.core.service.ReadyService.ReadyTracker, filter: org.openhab.core.service.ReadyMarkerFilter) -> None: ...
    def unmarkReady(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
    def unregisterTracker(self, readyTracker: org.openhab.core.service.ReadyService.ReadyTracker) -> None: ...

class StateDescriptionServiceImpl(org.openhab.core.service.StateDescriptionService):
    """
    Java class 'org.openhab.core.internal.service.StateDescriptionServiceImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.service.StateDescriptionService
    
      Constructors:
        * StateDescriptionServiceImpl()
    
    """
    def __init__(self): ...
    def addStateDescriptionFragmentProvider(self, provider: org.openhab.core.types.StateDescriptionFragmentProvider) -> None: ...
    def getStateDescription(self, itemName: java.lang.String, locale: java.util.Locale) -> org.openhab.core.types.StateDescription: ...
    def removeStateDescriptionFragmentProvider(self, provider: org.openhab.core.types.StateDescriptionFragmentProvider) -> None: ...
