import java.lang
import java.net
import java.util
import java.util.concurrent
import org
import org.openhab.core.common
import org.openhab.core.common.registry
import org.openhab.core.config.core
import org.openhab.core.config.core.metadata
import org.openhab.core.config.core.validation
import org.openhab.core.events
import org.openhab.core.items
import org.openhab.core.items.events
import org.openhab.core.service
import org.openhab.core.storage
import org.openhab.core.thing
import org.openhab.core.thing.binding
import org.openhab.core.thing.i18n
import org.openhab.core.thing.internal.profiles
import org.openhab.core.thing.link
import org.openhab.core.thing.profiles
import org.openhab.core.thing.type
import org.openhab.core.types
import org.openhab.core.util
import typing


class AutoUpdateConfigDescriptionProvider(org.openhab.core.config.core.metadata.MetadataConfigDescriptionProvider):
    """
    Java class 'org.openhab.core.thing.internal.AutoUpdateConfigDescriptionProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.core.metadata.MetadataConfigDescriptio
            nProvider
    
      Constructors:
        * AutoUpdateConfigDescriptionProvider()
    
    """
    def __init__(self): ...
    def getDescription(self, locale: java.util.Locale) -> java.lang.String: ...
    def getNamespace(self) -> java.lang.String: ...
    def getParameterOptions(self, locale: java.util.Locale) -> java.util.List[org.openhab.core.config.core.ParameterOption]: ...
    def getParameters(self, value: java.lang.String, locale: java.util.Locale) -> java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]: ...

class AutoUpdateManager(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.internal.AutoUpdateManager'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * AutoUpdateManager(java.util.Map, org.openhab.core.thing.type.ChannelTypeRegistry, org.openhab.core.events.EventPublisher, org.openhab.core.thing.link.ItemChannelLinkRegistry, org.openhab.core.items.MetadataRegistry, org.openhab.core.thing.ThingRegistry)
    
    """
    def __init__(self, configuration: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]], channelTypeRegistry: org.openhab.core.thing.type.ChannelTypeRegistry, eventPublisher: org.openhab.core.events.EventPublisher, itemChannelLinkRegistry: org.openhab.core.thing.link.ItemChannelLinkRegistry, metadataRegistry: org.openhab.core.items.MetadataRegistry, thingRegistry: org.openhab.core.thing.ThingRegistry): ...
    def receiveCommand(self, commandEvent: org.openhab.core.items.events.ItemCommandEvent, item: org.openhab.core.items.Item) -> None: ...

class ChannelCommandDescriptionProvider(org.openhab.core.types.CommandDescriptionProvider):
    """
    Java class 'org.openhab.core.thing.internal.ChannelCommandDescriptionProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.types.CommandDescriptionProvider
    
      Constructors:
        * ChannelCommandDescriptionProvider(org.openhab.core.thing.link.ItemChannelLinkRegistry, org.openhab.core.thing.type.ThingTypeRegistry, org.openhab.core.thing.ThingRegistry)
    
    """
    def __init__(self, itemChannelLinkRegistry: org.openhab.core.thing.link.ItemChannelLinkRegistry, thingTypeRegistry: org.openhab.core.thing.type.ThingTypeRegistry, thingRegistry: org.openhab.core.thing.ThingRegistry): ...
    def getCommandDescription(self, itemName: java.lang.String, locale: java.util.Locale) -> org.openhab.core.types.CommandDescription: ...

class ChannelLinkNotifier(org.openhab.core.common.registry.RegistryChangeListener[org.openhab.core.thing.link.ItemChannelLink]):
    """
    Java class 'org.openhab.core.thing.internal.ChannelLinkNotifier'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.common.registry.RegistryChangeListener
    
      Constructors:
        * ChannelLinkNotifier(org.openhab.core.thing.link.ItemChannelLinkRegistry, org.openhab.core.thing.ThingRegistry)
    
    """
    def __init__(self, itemChannelLinkRegistry: org.openhab.core.thing.link.ItemChannelLinkRegistry, thingRegistry: org.openhab.core.thing.ThingRegistry): ...
    @typing.overload
    def added(self, object: typing.Any) -> None: ...
    @typing.overload
    def added(self, element: org.openhab.core.thing.link.ItemChannelLink) -> None: ...
    def deactivate(self) -> None: ...
    @typing.overload
    def removed(self, object: typing.Any) -> None: ...
    @typing.overload
    def removed(self, element: org.openhab.core.thing.link.ItemChannelLink) -> None: ...
    @typing.overload
    def updated(self, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def updated(self, oldElement: org.openhab.core.thing.link.ItemChannelLink, element: org.openhab.core.thing.link.ItemChannelLink) -> None: ...

class ChannelStateDescriptionProvider(org.openhab.core.types.StateDescriptionFragmentProvider):
    """
    Java class 'org.openhab.core.thing.internal.ChannelStateDescriptionProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.types.StateDescriptionFragmentProvider
    
      Constructors:
        * ChannelStateDescriptionProvider(org.openhab.core.thing.link.ItemChannelLinkRegistry, org.openhab.core.thing.type.ThingTypeRegistry, org.openhab.core.thing.ThingRegistry)
    
    """
    def __init__(self, itemChannelLinkRegistry: org.openhab.core.thing.link.ItemChannelLinkRegistry, thingTypeRegistry: org.openhab.core.thing.type.ThingTypeRegistry, thingRegistry: org.openhab.core.thing.ThingRegistry): ...
    def getRank(self) -> int: ...
    def getStateDescriptionFragment(self, itemName: java.lang.String, locale: java.util.Locale) -> org.openhab.core.types.StateDescriptionFragment: ...

class CommunicationManager(org.openhab.core.events.EventSubscriber, org.openhab.core.common.registry.RegistryChangeListener[org.openhab.core.thing.link.ItemChannelLink]):
    """
    Java class 'org.openhab.core.thing.internal.CommunicationManager'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.events.EventSubscriber,
            org.openhab.core.common.registry.RegistryChangeListener
    
      Constructors:
        * CommunicationManager(org.openhab.core.thing.internal.AutoUpdateManager, org.openhab.core.thing.type.ChannelTypeRegistry, org.openhab.core.thing.internal.profiles.SystemProfileFactory, org.openhab.core.thing.link.ItemChannelLinkRegistry, org.openhab.core.items.ItemRegistry, org.openhab.core.items.ItemStateConverter, org.openhab.core.events.EventPublisher, org.openhab.core.common.SafeCaller, org.openhab.core.thing.ThingRegistry)
    
      Attributes:
        THINGHANDLER_EVENT_TIMEOUT (long): final static field
    
    """
    THINGHANDLER_EVENT_TIMEOUT: typing.ClassVar[int] = ...
    def __init__(self, autoUpdateManager: AutoUpdateManager, channelTypeRegistry: org.openhab.core.thing.type.ChannelTypeRegistry, defaultProfileFactory: org.openhab.core.thing.internal.profiles.SystemProfileFactory, itemChannelLinkRegistry: org.openhab.core.thing.link.ItemChannelLinkRegistry, itemRegistry: org.openhab.core.items.ItemRegistry, itemStateConverter: org.openhab.core.items.ItemStateConverter, eventPublisher: org.openhab.core.events.EventPublisher, safeCaller: org.openhab.core.common.SafeCaller, thingRegistry: org.openhab.core.thing.ThingRegistry): ...
    @typing.overload
    def added(self, object: typing.Any) -> None: ...
    @typing.overload
    def added(self, element: org.openhab.core.thing.link.ItemChannelLink) -> None: ...
    def channelTriggered(self, thing: org.openhab.core.thing.Thing, channelUID: org.openhab.core.thing.ChannelUID, event: java.lang.String) -> None: ...
    def deactivate(self) -> None: ...
    def getEventFilter(self) -> org.openhab.core.events.EventFilter: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def postCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def receive(self, event: org.openhab.core.events.Event) -> None: ...
    @typing.overload
    def removed(self, object: typing.Any) -> None: ...
    @typing.overload
    def removed(self, element: org.openhab.core.thing.link.ItemChannelLink) -> None: ...
    def stateUpdated(self, channelUID: org.openhab.core.thing.ChannelUID, state: org.openhab.core.types.State) -> None: ...
    @typing.overload
    def updated(self, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def updated(self, oldElement: org.openhab.core.thing.link.ItemChannelLink, element: org.openhab.core.thing.link.ItemChannelLink) -> None: ...

class ProfileContextImpl(org.openhab.core.thing.profiles.ProfileContext):
    """
    Java class 'org.openhab.core.thing.internal.ProfileContextImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.ProfileContext
    
      Constructors:
        * ProfileContextImpl(org.openhab.core.config.core.Configuration)
    
    """
    def __init__(self, configuration: org.openhab.core.config.core.Configuration): ...
    def getConfiguration(self) -> org.openhab.core.config.core.Configuration: ...
    def getExecutorService(self) -> java.util.concurrent.ScheduledExecutorService: ...

class ThingConfigDescriptionAliasProvider(org.openhab.core.config.core.ConfigDescriptionAliasProvider):
    """
    Java class 'org.openhab.core.thing.internal.ThingConfigDescriptionAliasProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.core.ConfigDescriptionAliasProvider
    
      Constructors:
        * ThingConfigDescriptionAliasProvider(org.openhab.core.thing.ThingRegistry, org.openhab.core.thing.type.ThingTypeRegistry, org.openhab.core.thing.type.ChannelTypeRegistry)
    
    """
    def __init__(self, thingRegistry: org.openhab.core.thing.ThingRegistry, thingTypeRegistry: org.openhab.core.thing.type.ThingTypeRegistry, channelTypeRegistry: org.openhab.core.thing.type.ChannelTypeRegistry): ...
    def getAlias(self, uri: java.net.URI) -> java.net.URI: ...

class ThingFactoryHelper(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.internal.ThingFactoryHelper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ThingFactoryHelper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def applyDefaultConfiguration(cls, configuration: org.openhab.core.config.core.Configuration, channelType: org.openhab.core.thing.type.ChannelType, configDescriptionRegistry: org.openhab.core.config.core.ConfigDescriptionRegistry) -> None: ...
    @classmethod
    @typing.overload
    def applyDefaultConfiguration(cls, configuration: org.openhab.core.config.core.Configuration, thingType: org.openhab.core.thing.type.ThingType, configDescriptionRegistry: org.openhab.core.config.core.ConfigDescriptionRegistry) -> None: ...
    @classmethod
    def createChannels(cls, thingType: org.openhab.core.thing.type.ThingType, thingUID: org.openhab.core.thing.ThingUID, configDescriptionRegistry: org.openhab.core.config.core.ConfigDescriptionRegistry) -> java.util.List[org.openhab.core.thing.Channel]: ...

class ThingImpl(org.openhab.core.thing.Thing):
    """
    Java class 'org.openhab.core.thing.internal.ThingImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.Thing
    
      Constructors:
        * ThingImpl(org.openhab.core.thing.ThingTypeUID, org.openhab.core.thing.ThingUID)
        * ThingImpl(org.openhab.core.thing.ThingTypeUID, java.lang.String)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
    """
    @typing.overload
    def __init__(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID, thingId: java.lang.String): ...
    @typing.overload
    def __init__(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID, thingUID: org.openhab.core.thing.ThingUID): ...
    def addChannel(self, channel: org.openhab.core.thing.Channel) -> None: ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getBridgeUID(self) -> org.openhab.core.thing.ThingUID: ...
    @typing.overload
    def getChannel(self, channelId: java.lang.String) -> org.openhab.core.thing.Channel: ...
    @typing.overload
    def getChannel(self, channelUID: org.openhab.core.thing.ChannelUID) -> org.openhab.core.thing.Channel: ...
    def getChannels(self) -> java.util.List[org.openhab.core.thing.Channel]: ...
    def getChannelsOfGroup(self, channelGroupId: java.lang.String) -> java.util.List[org.openhab.core.thing.Channel]: ...
    def getConfiguration(self) -> org.openhab.core.config.core.Configuration: ...
    def getHandler(self) -> org.openhab.core.thing.binding.ThingHandler: ...
    def getLabel(self) -> java.lang.String: ...
    def getLocation(self) -> java.lang.String: ...
    def getProperties(self) -> java.util.Map[java.lang.String, java.lang.String]: ...
    def getStatus(self) -> org.openhab.core.thing.ThingStatus: ...
    def getStatusInfo(self) -> org.openhab.core.thing.ThingStatusInfo: ...
    def getThingTypeUID(self) -> org.openhab.core.thing.ThingTypeUID: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    @typing.overload
    def getUID(self) -> org.openhab.core.thing.ThingUID: ...
    def hashCode(self) -> int: ...
    def isEnabled(self) -> bool: ...
    def setBridgeUID(self, bridgeUID: org.openhab.core.thing.ThingUID) -> None: ...
    def setChannels(self, channels: java.util.List[org.openhab.core.thing.Channel]) -> None: ...
    def setConfiguration(self, configuration: org.openhab.core.config.core.Configuration) -> None: ...
    def setHandler(self, thingHandler: org.openhab.core.thing.binding.ThingHandler) -> None: ...
    def setId(self, id: org.openhab.core.thing.ThingUID) -> None: ...
    def setLabel(self, label: java.lang.String) -> None: ...
    def setLocation(self, location: java.lang.String) -> None: ...
    def setProperties(self, properties: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> None: ...
    def setProperty(self, name: java.lang.String, value: java.lang.String) -> java.lang.String: ...
    def setStatusInfo(self, status: org.openhab.core.thing.ThingStatusInfo) -> None: ...
    def setThingTypeUID(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID) -> None: ...

class ThingRegistryImpl(org.openhab.core.common.registry.AbstractRegistry[org.openhab.core.thing.Thing, org.openhab.core.thing.ThingUID, org.openhab.core.thing.ThingProvider], org.openhab.core.thing.ThingRegistry):
    """
    Java class 'org.openhab.core.thing.internal.ThingRegistryImpl'
    
        Extends:
            org.openhab.core.common.registry.AbstractRegistry
    
        Interfaces:
            org.openhab.core.thing.ThingRegistry
    
      Constructors:
        * ThingRegistryImpl()
    
    """
    def __init__(self): ...
    def addThingTracker(self, thingTracker: 'ThingTracker') -> None: ...
    def createThingOfType(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID, thingUID: org.openhab.core.thing.ThingUID, bridgeUID: org.openhab.core.thing.ThingUID, label: java.lang.String, configuration: org.openhab.core.config.core.Configuration) -> org.openhab.core.thing.Thing: ...
    def forceRemove(self, thingUID: org.openhab.core.thing.ThingUID) -> org.openhab.core.thing.Thing: ...
    @typing.overload
    def get(self, key: typing.Any) -> org.openhab.core.common.registry.Identifiable: ...
    @typing.overload
    def get(self, thingUID: org.openhab.core.thing.ThingUID) -> org.openhab.core.thing.Thing: ...
    def getChannel(self, channelUID: org.openhab.core.thing.ChannelUID) -> org.openhab.core.thing.Channel: ...
    @typing.overload
    def remove(self, object: typing.Any) -> org.openhab.core.common.registry.Identifiable: ...
    @typing.overload
    def remove(self, thingUID: org.openhab.core.thing.ThingUID) -> org.openhab.core.thing.Thing: ...
    def removeThingTracker(self, thingTracker: 'ThingTracker') -> None: ...
    def updateConfiguration(self, thingUID: org.openhab.core.thing.ThingUID, configurationParameters: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...

class ThingTracker(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.internal.ThingTracker'
    
    """
    def thingAdded(self, thing: org.openhab.core.thing.Thing, thingTrackerEvent: 'ThingTracker.ThingTrackerEvent') -> None: ...
    def thingRemoved(self, thing: org.openhab.core.thing.Thing, thingTrackerEvent: 'ThingTracker.ThingTrackerEvent') -> None: ...
    def thingRemoving(self, thing: org.openhab.core.thing.Thing, thingTrackerEvent: 'ThingTracker.ThingTrackerEvent') -> None: ...
    def thingUpdated(self, thing: org.openhab.core.thing.Thing, thingTrackerEvent: 'ThingTracker.ThingTrackerEvent') -> None: ...
    class ThingTrackerEvent(java.lang.Enum[org.openhab.core.thing.internal.ThingTracker.ThingTrackerEvent]):
        """
        Java class 'org.openhab.core.thing.internal.ThingTracker$ThingTrackerEvent'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            THING_ADDED (org.openhab.core.thing.internal.ThingTracker$ThingTrackerEvent): final static enum constant
            THING_REMOVING (org.openhab.core.thing.internal.ThingTracker$ThingTrackerEvent): final static enum constant
            THING_REMOVED (org.openhab.core.thing.internal.ThingTracker$ThingTrackerEvent): final static enum constant
            THING_UPDATED (org.openhab.core.thing.internal.ThingTracker$ThingTrackerEvent): final static enum constant
            TRACKER_ADDED (org.openhab.core.thing.internal.ThingTracker$ThingTrackerEvent): final static enum constant
            TRACKER_REMOVED (org.openhab.core.thing.internal.ThingTracker$ThingTrackerEvent): final static enum constant
        
        """
        THING_ADDED: typing.ClassVar['ThingTracker.ThingTrackerEvent'] = ...
        THING_REMOVING: typing.ClassVar['ThingTracker.ThingTrackerEvent'] = ...
        THING_REMOVED: typing.ClassVar['ThingTracker.ThingTrackerEvent'] = ...
        THING_UPDATED: typing.ClassVar['ThingTracker.ThingTrackerEvent'] = ...
        TRACKER_ADDED: typing.ClassVar['ThingTracker.ThingTrackerEvent'] = ...
        TRACKER_REMOVED: typing.ClassVar['ThingTracker.ThingTrackerEvent'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @typing.overload
        def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
        @classmethod
        @typing.overload
        def valueOf(cls, name: java.lang.String) -> 'ThingTracker.ThingTrackerEvent': ...
        @classmethod
        def values(cls) -> typing.List['ThingTracker.ThingTrackerEvent']: ...

class BridgeImpl(ThingImpl, org.openhab.core.thing.Bridge):
    """
    Java class 'org.openhab.core.thing.internal.BridgeImpl'
    
        Extends:
            org.openhab.core.thing.internal.ThingImpl
    
        Interfaces:
            org.openhab.core.thing.Bridge
    
      Constructors:
        * BridgeImpl(org.openhab.core.thing.ThingTypeUID, java.lang.String)
        * BridgeImpl(org.openhab.core.thing.ThingTypeUID, org.openhab.core.thing.ThingUID)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
    """
    @typing.overload
    def __init__(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID, bridgeId: java.lang.String): ...
    @typing.overload
    def __init__(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID, thingUID: org.openhab.core.thing.ThingUID): ...
    def addThing(self, thing: org.openhab.core.thing.Thing) -> None: ...
    @typing.overload
    def getHandler(self) -> org.openhab.core.thing.binding.BridgeHandler: ...
    @typing.overload
    def getHandler(self) -> org.openhab.core.thing.binding.ThingHandler: ...
    def getThing(self, thingUID: org.openhab.core.thing.ThingUID) -> org.openhab.core.thing.Thing: ...
    def getThings(self) -> java.util.List[org.openhab.core.thing.Thing]: ...
    def removeThing(self, thing: org.openhab.core.thing.Thing) -> None: ...

class ThingManagerImpl(org.openhab.core.thing.ThingManager, ThingTracker, org.openhab.core.thing.ThingTypeMigrationService, org.openhab.core.service.ReadyService.ReadyTracker):
    """
    Java class 'org.openhab.core.thing.internal.ThingManagerImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.ThingManager,
            org.openhab.core.thing.internal.ThingTracker,
            org.openhab.core.thing.ThingTypeMigrationService,
            org.openhab.core.service.ReadyService.ReadyTracker
    
      Constructors:
        * ThingManagerImpl(org.openhab.core.util.BundleResolver, org.openhab.core.thing.type.ChannelGroupTypeRegistry, org.openhab.core.thing.type.ChannelTypeRegistry, org.openhab.core.thing.internal.CommunicationManager, org.openhab.core.config.core.ConfigDescriptionRegistry, org.openhab.core.config.core.validation.ConfigDescriptionValidator, org.openhab.core.events.EventPublisher, org.openhab.core.thing.link.ItemChannelLinkRegistry, org.openhab.core.service.ReadyService, org.openhab.core.common.SafeCaller, org.openhab.core.storage.StorageService, org.openhab.core.thing.ThingRegistry, org.openhab.core.thing.i18n.ThingStatusInfoI18nLocalizationService, org.openhab.core.thing.type.ThingTypeRegistry)
    
    """
    def __init__(self, bundleResolver: org.openhab.core.util.BundleResolver, channelGroupTypeRegistry: org.openhab.core.thing.type.ChannelGroupTypeRegistry, channelTypeRegistry: org.openhab.core.thing.type.ChannelTypeRegistry, communicationManager: CommunicationManager, configDescriptionRegistry: org.openhab.core.config.core.ConfigDescriptionRegistry, configDescriptionValidator: org.openhab.core.config.core.validation.ConfigDescriptionValidator, eventPublisher: org.openhab.core.events.EventPublisher, itemChannelLinkRegistry: org.openhab.core.thing.link.ItemChannelLinkRegistry, readyService: org.openhab.core.service.ReadyService, safeCaller: org.openhab.core.common.SafeCaller, storageService: org.openhab.core.storage.StorageService, thingRegistry: org.openhab.core.thing.ThingRegistry, thingStatusInfoI18nLocalizationService: org.openhab.core.thing.i18n.ThingStatusInfoI18nLocalizationService, thingTypeRegistry: org.openhab.core.thing.type.ThingTypeRegistry): ...
    def isEnabled(self, thingUID: org.openhab.core.thing.ThingUID) -> bool: ...
    def migrateThingType(self, thing: org.openhab.core.thing.Thing, thingTypeUID: org.openhab.core.thing.ThingTypeUID, configuration: org.openhab.core.config.core.Configuration) -> None: ...
    def onReadyMarkerAdded(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
    def onReadyMarkerRemoved(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
    def setEnabled(self, thingUID: org.openhab.core.thing.ThingUID, enabled: bool) -> None: ...
    def thingAdded(self, thing: org.openhab.core.thing.Thing, thingTrackerEvent: ThingTracker.ThingTrackerEvent) -> None: ...
    def thingRemoved(self, thing: org.openhab.core.thing.Thing, thingTrackerEvent: ThingTracker.ThingTrackerEvent) -> None: ...
    def thingRemoving(self, thing: org.openhab.core.thing.Thing, thingTrackerEvent: ThingTracker.ThingTrackerEvent) -> None: ...
    def thingUpdated(self, thing: org.openhab.core.thing.Thing, thingTrackerEvent: ThingTracker.ThingTrackerEvent) -> None: ...
