import java.lang
import java.util
import org
import org.openhab.core.thing
import typing


class DiscoveryListener(java.lang.Object):
    """
    @NonNullByDefault public interface DiscoveryListener
    
        The :class:`~org.openhab.core.config.discovery.DiscoveryListener` interface for receiving discovery events.
    
        A class that is interested in processing discovery events fired synchronously by a
        :class:`~org.openhab.core.config.discovery.DiscoveryService` has to implement this interface.
    
        Also see:
            :class:`~org.openhab.core.config.discovery.DiscoveryService`
    
    
    """
    def removeOlderResults(self, source: 'DiscoveryService', timestamp: int, thingTypeUIDs: typing.Union[java.util.Collection[org.openhab.core.thing.ThingTypeUID], typing.Sequence[org.openhab.core.thing.ThingTypeUID]], bridgeUID: org.openhab.core.thing.ThingUID) -> java.util.Collection[org.openhab.core.thing.ThingUID]: ...
    def thingDiscovered(self, source: 'DiscoveryService', result: 'DiscoveryResult') -> None: ...
    def thingRemoved(self, source: 'DiscoveryService', thingUID: org.openhab.core.thing.ThingUID) -> None: ...

class DiscoveryResult(java.lang.Object):
    """
    @NonNullByDefault public interface DiscoveryResult
    
        The :class:`~org.openhab.core.config.discovery.DiscoveryResult` is a container for one result of a discovery process.
        The discovery process can lead to *0..N* :class:`~org.openhab.core.config.discovery.DiscoveryResult` objects which are
        fired as an event to registered :class:`~org.openhab.core.config.discovery.DiscoveryListener`s.
    
        Also see:
            :class:`~org.openhab.core.config.discovery.DiscoveryService`,
            :class:`~org.openhab.core.config.discovery.DiscoveryListener`
    
    
    """
    TTL_UNLIMITED: typing.ClassVar[int] = ...
    def getBindingId(self) -> java.lang.String: ...
    def getBridgeUID(self) -> org.openhab.core.thing.ThingUID: ...
    def getFlag(self) -> 'DiscoveryResultFlag': ...
    def getLabel(self) -> java.lang.String: ...
    def getProperties(self) -> java.util.Map[java.lang.String, typing.Any]: ...
    def getRepresentationProperty(self) -> java.lang.String: ...
    def getThingTypeUID(self) -> org.openhab.core.thing.ThingTypeUID: ...
    def getThingUID(self) -> org.openhab.core.thing.ThingUID: ...
    def getTimeToLive(self) -> int: ...
    def getTimestamp(self) -> int: ...

class DiscoveryResultBuilder(java.lang.Object):
    """
    Java class 'org.openhab.core.config.discovery.DiscoveryResultBuilder'
    
        Extends:
            java.lang.Object
    
    """
    def build(self) -> DiscoveryResult: ...
    @classmethod
    def create(cls, thingUID: org.openhab.core.thing.ThingUID) -> 'DiscoveryResultBuilder': ...
    def withBridge(self, bridgeUID: org.openhab.core.thing.ThingUID) -> 'DiscoveryResultBuilder': ...
    def withLabel(self, label: java.lang.String) -> 'DiscoveryResultBuilder': ...
    def withProperties(self, properties: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> 'DiscoveryResultBuilder': ...
    def withProperty(self, key: java.lang.String, value: typing.Any) -> 'DiscoveryResultBuilder': ...
    def withRepresentationProperty(self, representationProperty: java.lang.String) -> 'DiscoveryResultBuilder': ...
    def withTTL(self, ttl: int) -> 'DiscoveryResultBuilder': ...
    def withThingType(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID) -> 'DiscoveryResultBuilder': ...

class DiscoveryResultFlag(java.lang.Enum[org.openhab.core.config.discovery.DiscoveryResultFlag]):
    """
    Java class 'org.openhab.core.config.discovery.DiscoveryResultFlag'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        NEW (org.openhab.core.config.discovery.DiscoveryResultFlag): final static enum constant
        IGNORED (org.openhab.core.config.discovery.DiscoveryResultFlag): final static enum constant
    
    """
    NEW: typing.ClassVar['DiscoveryResultFlag'] = ...
    IGNORED: typing.ClassVar['DiscoveryResultFlag'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'DiscoveryResultFlag': ...
    @classmethod
    def values(cls) -> typing.List['DiscoveryResultFlag']: ...

class DiscoveryService(java.lang.Object):
    """
    @NonNullByDefault public interface DiscoveryService
    
        The :class:`~org.openhab.core.config.discovery.DiscoveryService` is a service interface which each binding can implement
        to provide an auto discovery process for one or more :code:`Thing` s.
    
        As an example, a typical discovery mechanism could scan the network for *UPnP* devices, if requested.
    
        A :class:`~org.openhab.core.config.discovery.DiscoveryService` must be able to finish its discovery process without any
        user interaction.
    
        **There are two different kind of executions:**
    
          - **Background discovery:** If this mode is enabled, the discovery process should run in the background as long as this
            mode is not disabled again. Background discovery can be enabled and disabled and is configured through the configuration
            admin. The implementation class that registers an OSGi service must define a PID and has to react on configuration
            changes for it. See also
            :meth:`~org.openhab.core.config.discovery.DiscoveryService.CONFIG_PROPERTY_BACKGROUND_DISCOVERY`.
          - **Active scan:** If an active scan is triggered, the the service should try to actively query for new devices and should
            report new results within the defined scan timeout. An active scan can be aborted.
    
    
        Also see:
            :class:`~org.openhab.core.config.discovery.DiscoveryListener`,
            :class:`~org.openhab.core.config.discovery.DiscoveryServiceRegistry`
    
    
    """
    CONFIG_PROPERTY_BACKGROUND_DISCOVERY: typing.ClassVar[java.lang.String] = ...
    def abortScan(self) -> None: ...
    def addDiscoveryListener(self, listener: DiscoveryListener) -> None: ...
    def getScanTimeout(self) -> int: ...
    def getSupportedThingTypes(self) -> java.util.Collection[org.openhab.core.thing.ThingTypeUID]: ...
    def isBackgroundDiscoveryEnabled(self) -> bool: ...
    def removeDiscoveryListener(self, listener: DiscoveryListener) -> None: ...
    def startScan(self, listener: 'ScanListener') -> None: ...

class DiscoveryServiceRegistry(java.lang.Object):
    """
    @NonNullByDefault public interface DiscoveryServiceRegistry
    
        The :class:`~org.openhab.core.config.discovery.DiscoveryServiceRegistry` is a service interface which provides the
        following features.
    
          - Monitoring of :class:`~org.openhab.core.config.discovery.DiscoveryService`s
          - Direct accessing monitored :class:`~org.openhab.core.config.discovery.DiscoveryService`s
          - Forwarding all events received from the monitored :class:`~org.openhab.core.config.discovery.DiscoveryService`s.
    
    
        Also see:
            :class:`~org.openhab.core.config.discovery.DiscoveryService`,
            :class:`~org.openhab.core.config.discovery.DiscoveryListener`
    
    
    """
    @typing.overload
    def abortScan(self, bindingId: java.lang.String) -> bool: ...
    @typing.overload
    def abortScan(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID) -> bool: ...
    def addDiscoveryListener(self, listener: DiscoveryListener) -> None: ...
    @typing.overload
    def getMaxScanTimeout(self, bindingId: java.lang.String) -> int: ...
    @typing.overload
    def getMaxScanTimeout(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID) -> int: ...
    def getSupportedBindings(self) -> java.util.List[java.lang.String]: ...
    def getSupportedThingTypes(self) -> java.util.List[org.openhab.core.thing.ThingTypeUID]: ...
    def removeDiscoveryListener(self, listener: DiscoveryListener) -> None: ...
    @typing.overload
    def startScan(self, bindingId: java.lang.String, listener: 'ScanListener') -> bool: ...
    @typing.overload
    def startScan(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID, listener: 'ScanListener') -> bool: ...
    @typing.overload
    def supportsDiscovery(self, bindingId: java.lang.String) -> bool: ...
    @typing.overload
    def supportsDiscovery(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID) -> bool: ...

class ScanListener(java.lang.Object):
    """
    @NonNullByDefault public interface ScanListener
    
        The :class:`~org.openhab.core.config.discovery.ScanListener` interface for receiving scan operation events.
    
        A class that is interested in errors and termination of an active scan has to implement this interface.
    
        Also see:
            :class:`~org.openhab.core.config.discovery.DiscoveryService`
    
    
    """
    def onErrorOccurred(self, exception: java.lang.Exception) -> None: ...
    def onFinished(self) -> None: ...

class AbstractDiscoveryService(DiscoveryService):
    """
    Java class 'org.openhab.core.config.discovery.AbstractDiscoveryService'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.discovery.DiscoveryService
    
      Constructors:
        * AbstractDiscoveryService(int)
        * AbstractDiscoveryService(java.util.Set, int)
        * AbstractDiscoveryService(java.util.Set, int, boolean)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
    """
    @typing.overload
    def __init__(self, timeout: int): ...
    @typing.overload
    def __init__(self, supportedThingTypes: java.util.Set[org.openhab.core.thing.ThingTypeUID], timeout: int): ...
    @typing.overload
    def __init__(self, supportedThingTypes: java.util.Set[org.openhab.core.thing.ThingTypeUID], timeout: int, backgroundDiscoveryEnabledByDefault: bool): ...
    def abortScan(self) -> None: ...
    def addDiscoveryListener(self, listener: DiscoveryListener) -> None: ...
    def getScanTimeout(self) -> int: ...
    @typing.overload
    def getSupportedThingTypes(self) -> java.util.Collection: ...
    @typing.overload
    def getSupportedThingTypes(self) -> java.util.Set[org.openhab.core.thing.ThingTypeUID]: ...
    def isBackgroundDiscoveryEnabled(self) -> bool: ...
    def removeDiscoveryListener(self, listener: DiscoveryListener) -> None: ...
    def startScan(self, listener: ScanListener) -> None: ...
