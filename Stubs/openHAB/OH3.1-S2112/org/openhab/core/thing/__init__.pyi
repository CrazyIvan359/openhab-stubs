import java.lang
import java.util
import org
import org.openhab.core.common
import org.openhab.core.common.registry
import org.openhab.core.config.core
import org.openhab.core.storage
import org.openhab.core.thing.binding
import org.openhab.core.thing.i18n
import org.openhab.core.thing.type
import org.openhab.core.util
import typing


class Channel(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.Channel'
    
        Extends:
            java.lang.Object
    
    """
    def getAcceptedItemType(self) -> java.lang.String: ...
    def getAutoUpdatePolicy(self) -> org.openhab.core.thing.type.AutoUpdatePolicy: ...
    def getChannelTypeUID(self) -> org.openhab.core.thing.type.ChannelTypeUID: ...
    def getConfiguration(self) -> org.openhab.core.config.core.Configuration: ...
    def getDefaultTags(self) -> java.util.Set[java.lang.String]: ...
    def getDescription(self) -> java.lang.String: ...
    def getKind(self) -> org.openhab.core.thing.type.ChannelKind: ...
    def getLabel(self) -> java.lang.String: ...
    def getProperties(self) -> java.util.Map[java.lang.String, java.lang.String]: ...
    def getUID(self) -> 'ChannelUID': ...

class CommonTriggerEvents(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.CommonTriggerEvents'
    
        Extends:
            java.lang.Object
    
      Attributes:
        PRESSED (java.lang.String): final static field
        RELEASED (java.lang.String): final static field
        SHORT_PRESSED (java.lang.String): final static field
        DOUBLE_PRESSED (java.lang.String): final static field
        LONG_PRESSED (java.lang.String): final static field
        DIR1_PRESSED (java.lang.String): final static field
        DIR1_RELEASED (java.lang.String): final static field
        DIR2_PRESSED (java.lang.String): final static field
        DIR2_RELEASED (java.lang.String): final static field
    
    """
    PRESSED: typing.ClassVar[java.lang.String] = ...
    RELEASED: typing.ClassVar[java.lang.String] = ...
    SHORT_PRESSED: typing.ClassVar[java.lang.String] = ...
    DOUBLE_PRESSED: typing.ClassVar[java.lang.String] = ...
    LONG_PRESSED: typing.ClassVar[java.lang.String] = ...
    DIR1_PRESSED: typing.ClassVar[java.lang.String] = ...
    DIR1_RELEASED: typing.ClassVar[java.lang.String] = ...
    DIR2_PRESSED: typing.ClassVar[java.lang.String] = ...
    DIR2_RELEASED: typing.ClassVar[java.lang.String] = ...

class DefaultSystemChannelTypeProvider(org.openhab.core.thing.type.ChannelTypeProvider):
    """
    Java class 'org.openhab.core.thing.DefaultSystemChannelTypeProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.type.ChannelTypeProvider
    
      Constructors:
        * DefaultSystemChannelTypeProvider(org.openhab.core.thing.i18n.ChannelTypeI18nLocalizationService, org.openhab.core.util.BundleResolver)
    
      Attributes:
        SYSTEM_CHANNEL_SIGNAL_STRENGTH (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_CHANNEL_LOW_BATTERY (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_CHANNEL_BATTERY_LEVEL (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_TRIGGER (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_RAWBUTTON (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_BUTTON (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_RAWROCKER (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_POWER (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_LOCATION (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_MOTION (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_BRIGHTNESS (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_COLOR (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_COLOR_TEMPERATURE (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_VOLUME (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_MUTE (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_MEDIA_CONTROL (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_MEDIA_TITLE (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_MEDIA_ARTIST (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_WIND_DIRECTION (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_WIND_SPEED (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_OUTDOOR_TEMPERATURE (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_ATMOSPHERIC_HUMIDITY (org.openhab.core.thing.type.ChannelType): final static field
        SYSTEM_BAROMETRIC_PRESSURE (org.openhab.core.thing.type.ChannelType): final static field
    
    """
    SYSTEM_CHANNEL_SIGNAL_STRENGTH: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_CHANNEL_LOW_BATTERY: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_CHANNEL_BATTERY_LEVEL: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_TRIGGER: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_RAWBUTTON: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_BUTTON: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_RAWROCKER: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_POWER: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_LOCATION: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_MOTION: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_BRIGHTNESS: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_COLOR: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_COLOR_TEMPERATURE: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_VOLUME: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_MUTE: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_MEDIA_CONTROL: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_MEDIA_TITLE: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_MEDIA_ARTIST: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_WIND_DIRECTION: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_WIND_SPEED: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_OUTDOOR_TEMPERATURE: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_ATMOSPHERIC_HUMIDITY: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    SYSTEM_BAROMETRIC_PRESSURE: typing.ClassVar[org.openhab.core.thing.type.ChannelType] = ...
    def __init__(self, channelTypeI18nLocalizationService: org.openhab.core.thing.i18n.ChannelTypeI18nLocalizationService, bundleResolver: org.openhab.core.util.BundleResolver): ...
    def getChannelType(self, channelTypeUID: org.openhab.core.thing.type.ChannelTypeUID, locale: java.util.Locale) -> org.openhab.core.thing.type.ChannelType: ...
    def getChannelTypes(self, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.thing.type.ChannelType]: ...

class Thing(org.openhab.core.common.registry.Identifiable[org.openhab.core.thing.ThingUID]):
    """
    Java class 'org.openhab.core.thing.Thing'
    
        Interfaces:
            org.openhab.core.common.registry.Identifiable
    
      Attributes:
        PROPERTY_VENDOR (java.lang.String): final static field
        PROPERTY_MODEL_ID (java.lang.String): final static field
        PROPERTY_SERIAL_NUMBER (java.lang.String): final static field
        PROPERTY_HARDWARE_VERSION (java.lang.String): final static field
        PROPERTY_FIRMWARE_VERSION (java.lang.String): final static field
        PROPERTY_MAC_ADDRESS (java.lang.String): final static field
    
    """
    PROPERTY_VENDOR: typing.ClassVar[java.lang.String] = ...
    PROPERTY_MODEL_ID: typing.ClassVar[java.lang.String] = ...
    PROPERTY_SERIAL_NUMBER: typing.ClassVar[java.lang.String] = ...
    PROPERTY_HARDWARE_VERSION: typing.ClassVar[java.lang.String] = ...
    PROPERTY_FIRMWARE_VERSION: typing.ClassVar[java.lang.String] = ...
    PROPERTY_MAC_ADDRESS: typing.ClassVar[java.lang.String] = ...
    def getBridgeUID(self) -> 'ThingUID': ...
    @typing.overload
    def getChannel(self, channelId: java.lang.String) -> Channel: ...
    @typing.overload
    def getChannel(self, channelUID: 'ChannelUID') -> Channel: ...
    def getChannels(self) -> java.util.List[Channel]: ...
    def getChannelsOfGroup(self, channelGroupId: java.lang.String) -> java.util.List[Channel]: ...
    def getConfiguration(self) -> org.openhab.core.config.core.Configuration: ...
    def getHandler(self) -> org.openhab.core.thing.binding.ThingHandler: ...
    def getLabel(self) -> java.lang.String: ...
    def getLocation(self) -> java.lang.String: ...
    def getProperties(self) -> java.util.Map[java.lang.String, java.lang.String]: ...
    def getStatus(self) -> 'ThingStatus': ...
    def getStatusInfo(self) -> 'ThingStatusInfo': ...
    def getThingTypeUID(self) -> 'ThingTypeUID': ...
    @typing.overload
    def getUID(self) -> 'ThingUID': ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    def isEnabled(self) -> bool: ...
    def setBridgeUID(self, bridgeUID: 'ThingUID') -> None: ...
    def setHandler(self, thingHandler: org.openhab.core.thing.binding.ThingHandler) -> None: ...
    def setLabel(self, label: java.lang.String) -> None: ...
    def setLocation(self, location: java.lang.String) -> None: ...
    def setProperties(self, properties: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> None: ...
    def setProperty(self, name: java.lang.String, value: java.lang.String) -> java.lang.String: ...
    def setStatusInfo(self, status: 'ThingStatusInfo') -> None: ...

class ThingManager(java.lang.Object):
    """
    @NonNullByDefault public interface ThingManager
    
        :class:`~org.openhab.core.thing.ThingManager` interface defines methods for managing a
        :class:`~org.openhab.core.thing.Thing`.
    
    
    """
    def isEnabled(self, thingUID: 'ThingUID') -> bool: ...
    def setEnabled(self, thingUID: 'ThingUID', isEnabled: bool) -> None: ...

class ThingProvider(org.openhab.core.common.registry.Provider[Thing]):
    """
    Java class 'org.openhab.core.thing.ThingProvider'
    
        Interfaces:
            org.openhab.core.common.registry.Provider
    
    """

class ThingRegistry(org.openhab.core.common.registry.Registry[Thing, org.openhab.core.thing.ThingUID]):
    """
    Java class 'org.openhab.core.thing.ThingRegistry'
    
        Interfaces:
            org.openhab.core.common.registry.Registry
    
    """
    def createThingOfType(self, thingTypeUID: 'ThingTypeUID', thingUID: 'ThingUID', bridgeUID: 'ThingUID', label: java.lang.String, configuration: org.openhab.core.config.core.Configuration) -> Thing: ...
    def forceRemove(self, thingUID: 'ThingUID') -> Thing: ...
    @typing.overload
    def get(self, uid: 'ThingUID') -> Thing: ...
    @typing.overload
    def get(self, object: typing.Any) -> org.openhab.core.common.registry.Identifiable: ...
    def getChannel(self, channelUID: 'ChannelUID') -> Channel: ...
    @typing.overload
    def remove(self, thingUID: 'ThingUID') -> Thing: ...
    @typing.overload
    def remove(self, object: typing.Any) -> org.openhab.core.common.registry.Identifiable: ...
    def updateConfiguration(self, thingUID: 'ThingUID', configurationParameters: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...

class ThingRegistryChangeListener(org.openhab.core.common.registry.RegistryChangeListener[Thing]):
    """
    Java class 'org.openhab.core.thing.ThingRegistryChangeListener'
    
        Interfaces:
            org.openhab.core.common.registry.RegistryChangeListener
    
    """

class ThingStatus(java.lang.Enum[org.openhab.core.thing.ThingStatus]):
    """
    Java class 'org.openhab.core.thing.ThingStatus'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        UNINITIALIZED (org.openhab.core.thing.ThingStatus): final static enum constant
        INITIALIZING (org.openhab.core.thing.ThingStatus): final static enum constant
        UNKNOWN (org.openhab.core.thing.ThingStatus): final static enum constant
        ONLINE (org.openhab.core.thing.ThingStatus): final static enum constant
        OFFLINE (org.openhab.core.thing.ThingStatus): final static enum constant
        REMOVING (org.openhab.core.thing.ThingStatus): final static enum constant
        REMOVED (org.openhab.core.thing.ThingStatus): final static enum constant
    
    """
    UNINITIALIZED: typing.ClassVar['ThingStatus'] = ...
    INITIALIZING: typing.ClassVar['ThingStatus'] = ...
    UNKNOWN: typing.ClassVar['ThingStatus'] = ...
    ONLINE: typing.ClassVar['ThingStatus'] = ...
    OFFLINE: typing.ClassVar['ThingStatus'] = ...
    REMOVING: typing.ClassVar['ThingStatus'] = ...
    REMOVED: typing.ClassVar['ThingStatus'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'ThingStatus': ...
    @classmethod
    def values(cls) -> typing.List['ThingStatus']: ...

class ThingStatusDetail(java.lang.Enum[org.openhab.core.thing.ThingStatusDetail]):
    """
    Java class 'org.openhab.core.thing.ThingStatusDetail'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        NONE (org.openhab.core.thing.ThingStatusDetail): final static enum constant
        HANDLER_MISSING_ERROR (org.openhab.core.thing.ThingStatusDetail): final static enum constant
        HANDLER_REGISTERING_ERROR (org.openhab.core.thing.ThingStatusDetail): final static enum constant
        HANDLER_INITIALIZING_ERROR (org.openhab.core.thing.ThingStatusDetail): final static enum constant
        HANDLER_CONFIGURATION_PENDING (org.openhab.core.thing.ThingStatusDetail): final static enum constant
        CONFIGURATION_PENDING (org.openhab.core.thing.ThingStatusDetail): final static enum constant
        COMMUNICATION_ERROR (org.openhab.core.thing.ThingStatusDetail): final static enum constant
        CONFIGURATION_ERROR (org.openhab.core.thing.ThingStatusDetail): final static enum constant
        BRIDGE_OFFLINE (org.openhab.core.thing.ThingStatusDetail): final static enum constant
        FIRMWARE_UPDATING (org.openhab.core.thing.ThingStatusDetail): final static enum constant
        DUTY_CYCLE (org.openhab.core.thing.ThingStatusDetail): final static enum constant
        BRIDGE_UNINITIALIZED (org.openhab.core.thing.ThingStatusDetail): final static enum constant
        GONE (org.openhab.core.thing.ThingStatusDetail): final static enum constant
        DISABLED (org.openhab.core.thing.ThingStatusDetail): final static enum constant
        UNINITIALIZED (org.openhab.core.thing.ThingStatusDetail$UninitializedStatus): final static field
        INITIALIZING (org.openhab.core.thing.ThingStatusDetail$NoneOnlyStatus): final static field
        UNKNOWN (org.openhab.core.thing.ThingStatusDetail$NoneOnlyStatus): final static field
        ONLINE (org.openhab.core.thing.ThingStatusDetail$OnlineStatus): final static field
        OFFLINE (org.openhab.core.thing.ThingStatusDetail$OfflineStatus): final static field
        REMOVING (org.openhab.core.thing.ThingStatusDetail$NoneOnlyStatus): final static field
        REMOVED (org.openhab.core.thing.ThingStatusDetail$NoneOnlyStatus): final static field
    
    """
    NONE: typing.ClassVar['ThingStatusDetail'] = ...
    HANDLER_MISSING_ERROR: typing.ClassVar['ThingStatusDetail'] = ...
    HANDLER_REGISTERING_ERROR: typing.ClassVar['ThingStatusDetail'] = ...
    HANDLER_INITIALIZING_ERROR: typing.ClassVar['ThingStatusDetail'] = ...
    HANDLER_CONFIGURATION_PENDING: typing.ClassVar['ThingStatusDetail'] = ...
    CONFIGURATION_PENDING: typing.ClassVar['ThingStatusDetail'] = ...
    COMMUNICATION_ERROR: typing.ClassVar['ThingStatusDetail'] = ...
    CONFIGURATION_ERROR: typing.ClassVar['ThingStatusDetail'] = ...
    BRIDGE_OFFLINE: typing.ClassVar['ThingStatusDetail'] = ...
    FIRMWARE_UPDATING: typing.ClassVar['ThingStatusDetail'] = ...
    DUTY_CYCLE: typing.ClassVar['ThingStatusDetail'] = ...
    BRIDGE_UNINITIALIZED: typing.ClassVar['ThingStatusDetail'] = ...
    GONE: typing.ClassVar['ThingStatusDetail'] = ...
    DISABLED: typing.ClassVar['ThingStatusDetail'] = ...
    UNINITIALIZED: typing.ClassVar['ThingStatusDetail.UninitializedStatus'] = ...
    INITIALIZING: typing.ClassVar['ThingStatusDetail.NoneOnlyStatus'] = ...
    UNKNOWN: typing.ClassVar['ThingStatusDetail.NoneOnlyStatus'] = ...
    ONLINE: typing.ClassVar['ThingStatusDetail.OnlineStatus'] = ...
    OFFLINE: typing.ClassVar['ThingStatusDetail.OfflineStatus'] = ...
    REMOVING: typing.ClassVar['ThingStatusDetail.NoneOnlyStatus'] = ...
    REMOVED: typing.ClassVar['ThingStatusDetail.NoneOnlyStatus'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'ThingStatusDetail': ...
    @classmethod
    def values(cls) -> typing.List['ThingStatusDetail']: ...
    class NoneOnlyStatus(java.lang.Object):
        """
        Java class 'org.openhab.core.thing.ThingStatusDetail$NoneOnlyStatus'
        
            Extends:
                java.lang.Object
        
          Attributes:
            NONE (org.openhab.core.thing.ThingStatusDetail): field
        
        """
        NONE: 'ThingStatusDetail' = ...
    class OfflineStatus(java.lang.Object):
        """
        Java class 'org.openhab.core.thing.ThingStatusDetail$OfflineStatus'
        
            Extends:
                java.lang.Object
        
          Attributes:
            NONE (org.openhab.core.thing.ThingStatusDetail): field
            COMMUNICATION_ERROR (org.openhab.core.thing.ThingStatusDetail): field
            CONFIGURATION_ERROR (org.openhab.core.thing.ThingStatusDetail): field
            BRIDGE_OFFLINE (org.openhab.core.thing.ThingStatusDetail): field
            FIRMWARE_UPDATING (org.openhab.core.thing.ThingStatusDetail): field
            DUTY_CYCLE (org.openhab.core.thing.ThingStatusDetail): field
            GONE (org.openhab.core.thing.ThingStatusDetail): field
        
        """
        NONE: 'ThingStatusDetail' = ...
        COMMUNICATION_ERROR: 'ThingStatusDetail' = ...
        CONFIGURATION_ERROR: 'ThingStatusDetail' = ...
        BRIDGE_OFFLINE: 'ThingStatusDetail' = ...
        FIRMWARE_UPDATING: 'ThingStatusDetail' = ...
        DUTY_CYCLE: 'ThingStatusDetail' = ...
        GONE: 'ThingStatusDetail' = ...
    class OnlineStatus(java.lang.Object):
        """
        Java class 'org.openhab.core.thing.ThingStatusDetail$OnlineStatus'
        
            Extends:
                java.lang.Object
        
          Attributes:
            NONE (org.openhab.core.thing.ThingStatusDetail): field
            CONFIGURATION_PENDING (org.openhab.core.thing.ThingStatusDetail): field
        
        """
        NONE: 'ThingStatusDetail' = ...
        CONFIGURATION_PENDING: 'ThingStatusDetail' = ...
    class UninitializedStatus(java.lang.Object):
        """
        Java class 'org.openhab.core.thing.ThingStatusDetail$UninitializedStatus'
        
            Extends:
                java.lang.Object
        
          Attributes:
            NONE (org.openhab.core.thing.ThingStatusDetail): field
            HANDLER_MISSING_ERROR (org.openhab.core.thing.ThingStatusDetail): field
            HANDLER_REGISTERING_ERROR (org.openhab.core.thing.ThingStatusDetail): field
            HANDLER_CONFIGURATION_PENDING (org.openhab.core.thing.ThingStatusDetail): field
            HANDLER_INITIALIZING_ERROR (org.openhab.core.thing.ThingStatusDetail): field
            BRIDGE_UNINITIALIZED (org.openhab.core.thing.ThingStatusDetail): field
        
        """
        NONE: 'ThingStatusDetail' = ...
        HANDLER_MISSING_ERROR: 'ThingStatusDetail' = ...
        HANDLER_REGISTERING_ERROR: 'ThingStatusDetail' = ...
        HANDLER_CONFIGURATION_PENDING: 'ThingStatusDetail' = ...
        HANDLER_INITIALIZING_ERROR: 'ThingStatusDetail' = ...
        BRIDGE_UNINITIALIZED: 'ThingStatusDetail' = ...

class ThingStatusInfo(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.ThingStatusInfo'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ThingStatusInfo(org.openhab.core.thing.ThingStatus, org.openhab.core.thing.ThingStatusDetail, java.lang.String)
    
    """
    def __init__(self, status: ThingStatus, statusDetail: ThingStatusDetail, description: java.lang.String): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getDescription(self) -> java.lang.String: ...
    def getStatus(self) -> ThingStatus: ...
    def getStatusDetail(self) -> ThingStatusDetail: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class ThingTypeMigrationService(java.lang.Object):
    """
    @NonNullByDefault public interface ThingTypeMigrationService
    
        The :class:`~org.openhab.core.thing.ThingTypeMigrationService` describes a service to change the thing type of a given
        :class:`~org.openhab.core.thing.Thing`.
    
    
    """
    def migrateThingType(self, thing: Thing, thingTypeUID: 'ThingTypeUID', configuration: org.openhab.core.config.core.Configuration) -> None: ...

class UID(org.openhab.core.common.AbstractUID):
    """
    Java class 'org.openhab.core.thing.UID'
    
        Extends:
            org.openhab.core.common.AbstractUID
    
      Constructors:
        * UID(java.lang.String[])
        * UID(java.lang.String)
        * UID()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, uid: java.lang.String): ...
    @typing.overload
    def __init__(self, segments: typing.List[java.lang.String]): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getAsString(self) -> java.lang.String: ...
    def getBindingId(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class Bridge(Thing):
    """
    Java class 'org.openhab.core.thing.Bridge'
    
        Interfaces:
            org.openhab.core.thing.Thing
    
    """
    @typing.overload
    def getHandler(self) -> org.openhab.core.thing.binding.BridgeHandler: ...
    @typing.overload
    def getHandler(self) -> org.openhab.core.thing.binding.ThingHandler: ...
    def getThing(self, thingUID: 'ThingUID') -> Thing: ...
    def getThings(self) -> java.util.List[Thing]: ...

class ChannelGroupUID(UID):
    """
    Java class 'org.openhab.core.thing.ChannelGroupUID'
    
        Extends:
            org.openhab.core.thing.UID
    
      Constructors:
        * ChannelGroupUID(org.openhab.core.thing.ThingUID, java.lang.String)
        * ChannelGroupUID(java.lang.String)
    
    """
    @typing.overload
    def __init__(self, channelGroupUid: java.lang.String): ...
    @typing.overload
    def __init__(self, thingUID: 'ThingUID', id: java.lang.String): ...
    def getId(self) -> java.lang.String: ...
    def getThingUID(self) -> 'ThingUID': ...

class ChannelUID(UID):
    """
    Java class 'org.openhab.core.thing.ChannelUID'
    
        Extends:
            org.openhab.core.thing.UID
    
      Constructors:
        * ChannelUID(org.openhab.core.thing.ThingUID, java.lang.String, java.lang.String)
        * ChannelUID(org.openhab.core.thing.ChannelGroupUID, java.lang.String)
        * ChannelUID(org.openhab.core.thing.ThingUID, java.lang.String)
        * ChannelUID(java.lang.String)
    
      Attributes:
        CHANNEL_SEGMENT_PATTERN (java.lang.String): final static field
        CHANNEL_GROUP_SEPARATOR (java.lang.String): final static field
    
    """
    CHANNEL_SEGMENT_PATTERN: typing.ClassVar[java.lang.String] = ...
    CHANNEL_GROUP_SEPARATOR: typing.ClassVar[java.lang.String] = ...
    @typing.overload
    def __init__(self, channelUid: java.lang.String): ...
    @typing.overload
    def __init__(self, channelGroupUID: ChannelGroupUID, id: java.lang.String): ...
    @typing.overload
    def __init__(self, thingUID: 'ThingUID', id: java.lang.String): ...
    @typing.overload
    def __init__(self, thingUID: 'ThingUID', groupId: java.lang.String, id: java.lang.String): ...
    def getGroupId(self) -> java.lang.String: ...
    def getId(self) -> java.lang.String: ...
    def getIdWithoutGroup(self) -> java.lang.String: ...
    def getThingUID(self) -> 'ThingUID': ...
    def isInGroup(self) -> bool: ...

class ManagedThingProvider(org.openhab.core.common.registry.DefaultAbstractManagedProvider[Thing, org.openhab.core.thing.ThingUID], ThingProvider):
    """
    Java class 'org.openhab.core.thing.ManagedThingProvider'
    
        Extends:
            org.openhab.core.common.registry.DefaultAbstractManagedProvider
    
        Interfaces:
            org.openhab.core.thing.ThingProvider
    
      Constructors:
        * ManagedThingProvider(org.openhab.core.storage.StorageService)
    
    """
    def __init__(self, storageService: org.openhab.core.storage.StorageService): ...

class ThingTypeUID(UID):
    """
    Java class 'org.openhab.core.thing.ThingTypeUID'
    
        Extends:
            org.openhab.core.thing.UID
    
      Constructors:
        * ThingTypeUID(java.lang.String, java.lang.String)
        * ThingTypeUID(java.lang.String)
    
    """
    @typing.overload
    def __init__(self, uid: java.lang.String): ...
    @typing.overload
    def __init__(self, bindingId: java.lang.String, thingTypeId: java.lang.String): ...
    def getId(self) -> java.lang.String: ...

class ThingUID(UID):
    """
    Java class 'org.openhab.core.thing.ThingUID'
    
        Extends:
            org.openhab.core.thing.UID
    
      Constructors:
        * ThingUID(java.lang.String, java.lang.String)
        * ThingUID(java.lang.String, org.openhab.core.thing.ThingUID, java.lang.String)
        * ThingUID(java.lang.String, java.lang.String, java.lang.String)
        * ThingUID(java.lang.String)
        * ThingUID(java.lang.String[])
        * ThingUID(org.openhab.core.thing.ThingTypeUID, java.lang.String)
        * ThingUID(org.openhab.core.thing.ThingTypeUID, org.openhab.core.thing.ThingUID, java.lang.String)
        * ThingUID(org.openhab.core.thing.ThingTypeUID, java.lang.String, java.lang.String[])
    
    """
    @typing.overload
    def __init__(self, thingUID: java.lang.String): ...
    @typing.overload
    def __init__(self, bindingId: java.lang.String, id: java.lang.String): ...
    @typing.overload
    def __init__(self, bindingId: java.lang.String, thingTypeId: java.lang.String, id: java.lang.String): ...
    @typing.overload
    def __init__(self, bindingId: java.lang.String, bridgeUID: 'ThingUID', id: java.lang.String): ...
    @typing.overload
    def __init__(self, segments: typing.List[java.lang.String]): ...
    @typing.overload
    def __init__(self, thingTypeUID: ThingTypeUID, id: java.lang.String): ...
    @typing.overload
    def __init__(self, thingTypeUID: ThingTypeUID, id: java.lang.String, bridgeIds: typing.List[java.lang.String]): ...
    @typing.overload
    def __init__(self, thingTypeUID: ThingTypeUID, bridgeUID: 'ThingUID', id: java.lang.String): ...
    def getBridgeIds(self) -> java.util.List[java.lang.String]: ...
    def getId(self) -> java.lang.String: ...
