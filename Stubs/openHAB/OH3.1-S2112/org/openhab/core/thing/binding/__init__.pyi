import java.lang
import java.lang.annotation
import java.util
import org.openhab.core.config.core
import org.openhab.core.config.core.status
import org.openhab.core.thing
import org.openhab.core.thing.binding.builder
import org.openhab.core.thing.type
import org.openhab.core.types
import typing


class BaseDynamicCommandDescriptionProvider(org.openhab.core.thing.type.DynamicCommandDescriptionProvider):
    """
    Java class 'org.openhab.core.thing.binding.BaseDynamicCommandDescriptionProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.type.DynamicCommandDescriptionProvider
    
      Constructors:
        * BaseDynamicCommandDescriptionProvider()
    
    """
    def __init__(self): ...
    def deactivate(self) -> None: ...
    def getCommandDescription(self, channel: org.openhab.core.thing.Channel, originalCommandDescription: org.openhab.core.types.CommandDescription, locale: java.util.Locale) -> org.openhab.core.types.CommandDescription: ...
    def setCommandOptions(self, channelUID: org.openhab.core.thing.ChannelUID, options: java.util.List[org.openhab.core.types.CommandOption]) -> None: ...

class BaseDynamicStateDescriptionProvider(org.openhab.core.thing.type.DynamicStateDescriptionProvider):
    """
    Java class 'org.openhab.core.thing.binding.BaseDynamicStateDescriptionProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.type.DynamicStateDescriptionProvider
    
      Constructors:
        * BaseDynamicStateDescriptionProvider()
    
    """
    def __init__(self): ...
    def deactivate(self) -> None: ...
    def getStateDescription(self, channel: org.openhab.core.thing.Channel, original: org.openhab.core.types.StateDescription, locale: java.util.Locale) -> org.openhab.core.types.StateDescription: ...
    def setStateOptions(self, channelUID: org.openhab.core.thing.ChannelUID, options: java.util.List[org.openhab.core.types.StateOption]) -> None: ...
    def setStatePattern(self, channelUID: org.openhab.core.thing.ChannelUID, pattern: java.lang.String) -> None: ...

class ThingActionsScope(java.lang.annotation.Annotation):
    """
    Java class 'org.openhab.core.thing.binding.ThingActionsScope'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def name(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ThingConfigStatusSource(org.openhab.core.config.core.status.ConfigStatusSource):
    """
    Java class 'org.openhab.core.thing.binding.ThingConfigStatusSource'
    
        Extends:
            org.openhab.core.config.core.status.ConfigStatusSource
    
      Constructors:
        * ThingConfigStatusSource(java.lang.String)
    
    """
    def __init__(self, thingUID: java.lang.String): ...
    def getTopic(self) -> java.lang.String: ...

class ThingFactory(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.binding.ThingFactory'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ThingFactory()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def createThing(cls, thingUID: org.openhab.core.thing.ThingUID, configuration: org.openhab.core.config.core.Configuration, properties: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]], bridgeUID: org.openhab.core.thing.ThingUID, thingTypeUID: org.openhab.core.thing.ThingTypeUID, thingHandlerFactories: java.util.List['ThingHandlerFactory']) -> org.openhab.core.thing.Thing: ...
    @classmethod
    @typing.overload
    def createThing(cls, thingType: org.openhab.core.thing.type.ThingType, thingUID: org.openhab.core.thing.ThingUID, configuration: org.openhab.core.config.core.Configuration) -> org.openhab.core.thing.Thing: ...
    @classmethod
    @typing.overload
    def createThing(cls, thingType: org.openhab.core.thing.type.ThingType, thingUID: org.openhab.core.thing.ThingUID, configuration: org.openhab.core.config.core.Configuration, bridgeUID: org.openhab.core.thing.ThingUID) -> org.openhab.core.thing.Thing: ...
    @classmethod
    @typing.overload
    def createThing(cls, thingType: org.openhab.core.thing.type.ThingType, thingUID: org.openhab.core.thing.ThingUID, configuration: org.openhab.core.config.core.Configuration, bridgeUID: org.openhab.core.thing.ThingUID, configDescriptionRegistry: org.openhab.core.config.core.ConfigDescriptionRegistry) -> org.openhab.core.thing.Thing: ...
    @classmethod
    def generateRandomThingUID(cls, thingTypeUID: org.openhab.core.thing.ThingTypeUID) -> org.openhab.core.thing.ThingUID: ...

class ThingHandler(java.lang.Object):
    """
    @NonNullByDefault public interface ThingHandler
    
        A :class:`~org.openhab.core.thing.binding.ThingHandler` handles the communication between the openHAB framework and an
        entity from the real world, e.g. a physical device, a web service, etc. represented by a
        :class:`~org.openhab.core.thing.Thing`.
    
        The communication is bidirectional. The framework informs a thing handler about commands, state and configuration
        updates, and so on, by the corresponding handler methods. The handler can notify the framework about changes like state
        and status updates, updates of the whole thing, by a :class:`~org.openhab.core.thing.binding.ThingHandlerCallback`.
    
    
    
    """
    def bridgeStatusChanged(self, bridgeStatusInfo: org.openhab.core.thing.ThingStatusInfo) -> None: ...
    def channelLinked(self, channelUID: org.openhab.core.thing.ChannelUID) -> None: ...
    def channelUnlinked(self, channelUID: org.openhab.core.thing.ChannelUID) -> None: ...
    def dispose(self) -> None: ...
    def getServices(self) -> java.util.Collection[typing.Type['ThingHandlerService']]: ...
    def getThing(self) -> org.openhab.core.thing.Thing: ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def handleConfigurationUpdate(self, configurationParameters: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def handleRemoval(self) -> None: ...
    def initialize(self) -> None: ...
    def setCallback(self, thingHandlerCallback: 'ThingHandlerCallback') -> None: ...
    def thingUpdated(self, thing: org.openhab.core.thing.Thing) -> None: ...

class ThingHandlerCallback(java.lang.Object):
    """
    @NonNullByDefault public interface ThingHandlerCallback
    
        :class:`~org.openhab.core.thing.binding.ThingHandlerCallback` is callback interface for
        :class:`~org.openhab.core.thing.binding.ThingHandler`s. The implementation of a
        :class:`~org.openhab.core.thing.binding.ThingHandler` must use the callback to inform the framework about changes like
        state updates, status updated or an update of the whole thing.
    
    
    """
    def channelTriggered(self, thing: org.openhab.core.thing.Thing, channelUID: org.openhab.core.thing.ChannelUID, event: java.lang.String) -> None: ...
    def configurationUpdated(self, thing: org.openhab.core.thing.Thing) -> None: ...
    def createChannelBuilder(self, channelUID: org.openhab.core.thing.ChannelUID, channelTypeUID: org.openhab.core.thing.type.ChannelTypeUID) -> org.openhab.core.thing.binding.builder.ChannelBuilder: ...
    def createChannelBuilders(self, channelGroupUID: org.openhab.core.thing.ChannelGroupUID, channelGroupTypeUID: org.openhab.core.thing.type.ChannelGroupTypeUID) -> java.util.List[org.openhab.core.thing.binding.builder.ChannelBuilder]: ...
    def editChannel(self, thing: org.openhab.core.thing.Thing, channelUID: org.openhab.core.thing.ChannelUID) -> org.openhab.core.thing.binding.builder.ChannelBuilder: ...
    def getBridge(self, bridgeUID: org.openhab.core.thing.ThingUID) -> org.openhab.core.thing.Bridge: ...
    def isChannelLinked(self, channelUID: org.openhab.core.thing.ChannelUID) -> bool: ...
    def migrateThingType(self, thing: org.openhab.core.thing.Thing, thingTypeUID: org.openhab.core.thing.ThingTypeUID, configuration: org.openhab.core.config.core.Configuration) -> None: ...
    def postCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def stateUpdated(self, channelUID: org.openhab.core.thing.ChannelUID, state: org.openhab.core.types.State) -> None: ...
    def statusUpdated(self, thing: org.openhab.core.thing.Thing, thingStatus: org.openhab.core.thing.ThingStatusInfo) -> None: ...
    def thingUpdated(self, thing: org.openhab.core.thing.Thing) -> None: ...
    def validateConfigurationParameters(self, thing: org.openhab.core.thing.Thing, configurationParameters: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...

class ThingHandlerFactory(java.lang.Object):
    """
    @NonNullByDefault public interface ThingHandlerFactory
    
        The :class:`~org.openhab.core.thing.binding.ThingHandlerFactory` is responsible for creating
        :class:`~org.openhab.core.thing.Thing`s and :class:`~org.openhab.core.thing.binding.ThingHandler`s. Therefore the
        factory must be registered as OSGi service.
    
    
    """
    def createThing(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID, configuration: org.openhab.core.config.core.Configuration, thingUID: org.openhab.core.thing.ThingUID, bridgeUID: org.openhab.core.thing.ThingUID) -> org.openhab.core.thing.Thing: ...
    def registerHandler(self, thing: org.openhab.core.thing.Thing) -> ThingHandler: ...
    def removeThing(self, thingUID: org.openhab.core.thing.ThingUID) -> None: ...
    def supportsThingType(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID) -> bool: ...
    def unregisterHandler(self, thing: org.openhab.core.thing.Thing) -> None: ...

class ThingHandlerService(java.lang.Object):
    """
    @NonNullByDefault public interface ThingHandlerService
    
        Interface for a service that provides access to a :class:`~org.openhab.core.thing.binding.ThingHandler`.
    
    
    """
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def getThingHandler(self) -> ThingHandler: ...
    def setThingHandler(self, handler: ThingHandler) -> None: ...

class ThingTypeProvider(java.lang.Object):
    """
    @NonNullByDefault public interface ThingTypeProvider
    
        The :class:`~org.openhab.core.thing.binding.ThingTypeProvider` is responsible for providing thing types.
    
    
    """
    def getThingType(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID, locale: java.util.Locale) -> org.openhab.core.thing.type.ThingType: ...
    def getThingTypes(self, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.thing.type.ThingType]: ...

class BaseThingHandler(ThingHandler):
    """
    Java class 'org.openhab.core.thing.binding.BaseThingHandler'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.binding.ThingHandler
    
      Constructors:
        * BaseThingHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def bridgeStatusChanged(self, bridgeStatusInfo: org.openhab.core.thing.ThingStatusInfo) -> None: ...
    def channelLinked(self, channelUID: org.openhab.core.thing.ChannelUID) -> None: ...
    def channelUnlinked(self, channelUID: org.openhab.core.thing.ChannelUID) -> None: ...
    def dispose(self) -> None: ...
    def getThing(self) -> org.openhab.core.thing.Thing: ...
    def handleConfigurationUpdate(self, configurationParameters: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def handleRemoval(self) -> None: ...
    def setCallback(self, thingHandlerCallback: ThingHandlerCallback) -> None: ...
    def thingUpdated(self, thing: org.openhab.core.thing.Thing) -> None: ...

class BaseThingHandlerFactory(ThingHandlerFactory):
    """
    Java class 'org.openhab.core.thing.binding.BaseThingHandlerFactory'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.binding.ThingHandlerFactory
    
      Constructors:
        * BaseThingHandlerFactory()
    
    """
    def __init__(self): ...
    def createThing(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID, configuration: org.openhab.core.config.core.Configuration, thingUID: org.openhab.core.thing.ThingUID, bridgeUID: org.openhab.core.thing.ThingUID) -> org.openhab.core.thing.Thing: ...
    def registerHandler(self, thing: org.openhab.core.thing.Thing) -> ThingHandler: ...
    def removeThing(self, thingUID: org.openhab.core.thing.ThingUID) -> None: ...
    def unregisterHandler(self, thing: org.openhab.core.thing.Thing) -> None: ...

class BridgeHandler(ThingHandler):
    """
    Java class 'org.openhab.core.thing.binding.BridgeHandler'
    
        Interfaces:
            org.openhab.core.thing.binding.ThingHandler
    
    """
    def childHandlerDisposed(self, childHandler: ThingHandler, childThing: org.openhab.core.thing.Thing) -> None: ...
    def childHandlerInitialized(self, childHandler: ThingHandler, childThing: org.openhab.core.thing.Thing) -> None: ...

class ThingActions(ThingHandlerService):
    """
    Java class 'org.openhab.core.thing.binding.ThingActions'
    
        Interfaces:
            org.openhab.core.thing.binding.ThingHandlerService
    
    """

class BaseBridgeHandler(BaseThingHandler, BridgeHandler):
    """
    Java class 'org.openhab.core.thing.binding.BaseBridgeHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
        Interfaces:
            org.openhab.core.thing.binding.BridgeHandler
    
      Constructors:
        * BaseBridgeHandler(org.openhab.core.thing.Bridge)
    
    """
    def __init__(self, bridge: org.openhab.core.thing.Bridge): ...
    def childHandlerDisposed(self, childHandler: ThingHandler, childThing: org.openhab.core.thing.Thing) -> None: ...
    def childHandlerInitialized(self, childHandler: ThingHandler, childThing: org.openhab.core.thing.Thing) -> None: ...
    @typing.overload
    def getThing(self) -> org.openhab.core.thing.Bridge: ...
    @typing.overload
    def getThing(self) -> org.openhab.core.thing.Thing: ...

class ConfigStatusThingHandler(BaseThingHandler, org.openhab.core.config.core.status.ConfigStatusProvider):
    """
    Java class 'org.openhab.core.thing.binding.ConfigStatusThingHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
        Interfaces:
            org.openhab.core.config.core.status.ConfigStatusProvider
    
      Constructors:
        * ConfigStatusThingHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def handleConfigurationUpdate(self, configurationParameters: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def setConfigStatusCallback(self, configStatusCallback: org.openhab.core.config.core.status.ConfigStatusCallback) -> None: ...
    def supportsEntity(self, entityId: java.lang.String) -> bool: ...

class ConfigStatusBridgeHandler(BaseBridgeHandler, org.openhab.core.config.core.status.ConfigStatusProvider):
    """
    Java class 'org.openhab.core.thing.binding.ConfigStatusBridgeHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseBridgeHandler
    
        Interfaces:
            org.openhab.core.config.core.status.ConfigStatusProvider
    
      Constructors:
        * ConfigStatusBridgeHandler(org.openhab.core.thing.Bridge)
    
    """
    def __init__(self, bridge: org.openhab.core.thing.Bridge): ...
    def handleConfigurationUpdate(self, configurationParameters: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def setConfigStatusCallback(self, configStatusCallback: org.openhab.core.config.core.status.ConfigStatusCallback) -> None: ...
    def supportsEntity(self, entityId: java.lang.String) -> bool: ...
