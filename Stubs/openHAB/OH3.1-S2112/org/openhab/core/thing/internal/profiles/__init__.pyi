import java.lang
import java.util
import java.util.function
import org.openhab.core.common
import org.openhab.core.events
import org.openhab.core.items
import org.openhab.core.thing
import org.openhab.core.thing.link
import org.openhab.core.thing.profiles
import org.openhab.core.thing.profiles.i18n
import org.openhab.core.thing.type
import org.openhab.core.types
import org.openhab.core.util
import typing


class ProfileCallbackImpl(org.openhab.core.thing.profiles.ProfileCallback):
    """
    Java class 'org.openhab.core.thing.internal.profiles.ProfileCallbackImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.ProfileCallback
    
      Constructors:
        * ProfileCallbackImpl(org.openhab.core.events.EventPublisher, org.openhab.core.common.SafeCaller, org.openhab.core.items.ItemStateConverter, org.openhab.core.thing.link.ItemChannelLink, java.util.function.Function, java.util.function.Function)
    
    """
    def __init__(self, eventPublisher: org.openhab.core.events.EventPublisher, safeCaller: org.openhab.core.common.SafeCaller, itemStateConverter: org.openhab.core.items.ItemStateConverter, link: org.openhab.core.thing.link.ItemChannelLink, thingProvider: typing.Union[java.util.function.Function[org.openhab.core.thing.ThingUID, org.openhab.core.thing.Thing], typing.Callable[[org.openhab.core.thing.ThingUID], org.openhab.core.thing.Thing]], itemProvider: typing.Union[java.util.function.Function[java.lang.String, org.openhab.core.items.Item], typing.Callable[[java.lang.String], org.openhab.core.items.Item]]): ...
    def handleCommand(self, command: org.openhab.core.types.Command) -> None: ...
    def sendCommand(self, command: org.openhab.core.types.Command) -> None: ...
    def sendUpdate(self, state: org.openhab.core.types.State) -> None: ...

class ProfileTypeRegistryImpl(org.openhab.core.thing.profiles.ProfileTypeRegistry):
    """
    Java class 'org.openhab.core.thing.internal.profiles.ProfileTypeRegistryImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.ProfileTypeRegistry
    
      Constructors:
        * ProfileTypeRegistryImpl()
    
    """
    def __init__(self): ...
    @typing.overload
    def getProfileTypes(self) -> java.util.List[org.openhab.core.thing.profiles.ProfileType]: ...
    @typing.overload
    def getProfileTypes(self, locale: java.util.Locale) -> java.util.List[org.openhab.core.thing.profiles.ProfileType]: ...

class RawButtonOnOffSwitchProfile(org.openhab.core.thing.profiles.TriggerProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.RawButtonOnOffSwitchProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.TriggerProfile
    
    """
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...
    def onTriggerFromHandler(self, event: java.lang.String) -> None: ...

class RawButtonTogglePlayerProfile(org.openhab.core.thing.profiles.TriggerProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.RawButtonTogglePlayerProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.TriggerProfile
    
      Constructors:
        * RawButtonTogglePlayerProfile(org.openhab.core.thing.profiles.ProfileCallback)
    
    """
    def __init__(self, callback: org.openhab.core.thing.profiles.ProfileCallback): ...
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...
    def onTriggerFromHandler(self, event: java.lang.String) -> None: ...

class RawButtonToggleRollershutterProfile(org.openhab.core.thing.profiles.TriggerProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.RawButtonToggleRollershutterProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.TriggerProfile
    
      Constructors:
        * RawButtonToggleRollershutterProfile(org.openhab.core.thing.profiles.ProfileCallback)
    
    """
    def __init__(self, callback: org.openhab.core.thing.profiles.ProfileCallback): ...
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...
    def onTriggerFromHandler(self, event: java.lang.String) -> None: ...

class RawButtonToggleSwitchProfile(org.openhab.core.thing.profiles.TriggerProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.RawButtonToggleSwitchProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.TriggerProfile
    
      Constructors:
        * RawButtonToggleSwitchProfile(org.openhab.core.thing.profiles.ProfileCallback)
    
    """
    def __init__(self, callback: org.openhab.core.thing.profiles.ProfileCallback): ...
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...
    def onTriggerFromHandler(self, event: java.lang.String) -> None: ...

class RawRockerDimmerProfile(org.openhab.core.thing.profiles.TriggerProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.RawRockerDimmerProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.TriggerProfile
    
    """
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...
    def onTriggerFromHandler(self, event: java.lang.String) -> None: ...

class RawRockerNextPreviousProfile(org.openhab.core.thing.profiles.TriggerProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.RawRockerNextPreviousProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.TriggerProfile
    
    """
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...
    def onTriggerFromHandler(self, event: java.lang.String) -> None: ...

class RawRockerOnOffProfile(org.openhab.core.thing.profiles.TriggerProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.RawRockerOnOffProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.TriggerProfile
    
    """
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...
    def onTriggerFromHandler(self, event: java.lang.String) -> None: ...

class RawRockerPlayPauseProfile(org.openhab.core.thing.profiles.TriggerProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.RawRockerPlayPauseProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.TriggerProfile
    
    """
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...
    def onTriggerFromHandler(self, event: java.lang.String) -> None: ...

class RawRockerRewindFastforwardProfile(org.openhab.core.thing.profiles.TriggerProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.RawRockerRewindFastforwardProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.TriggerProfile
    
    """
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...
    def onTriggerFromHandler(self, event: java.lang.String) -> None: ...

class RawRockerStopMoveProfile(org.openhab.core.thing.profiles.TriggerProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.RawRockerStopMoveProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.TriggerProfile
    
    """
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...
    def onTriggerFromHandler(self, event: java.lang.String) -> None: ...

class RawRockerUpDownProfile(org.openhab.core.thing.profiles.TriggerProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.RawRockerUpDownProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.TriggerProfile
    
    """
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...
    def onTriggerFromHandler(self, event: java.lang.String) -> None: ...

class StateProfileTypeImpl(org.openhab.core.thing.profiles.StateProfileType):
    """
    Java class 'org.openhab.core.thing.internal.profiles.StateProfileTypeImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.StateProfileType
    
      Constructors:
        * StateProfileTypeImpl(org.openhab.core.thing.profiles.ProfileTypeUID, java.lang.String, java.util.Collection, java.util.Collection)
    
    """
    def __init__(self, profileTypeUID: org.openhab.core.thing.profiles.ProfileTypeUID, label: java.lang.String, supportedItemTypes: typing.Union[java.util.Collection[java.lang.String], typing.Sequence[java.lang.String]], supportedItemTypesOfChannel: typing.Union[java.util.Collection[java.lang.String], typing.Sequence[java.lang.String]]): ...
    def getLabel(self) -> java.lang.String: ...
    def getSupportedItemTypes(self) -> java.util.Collection[java.lang.String]: ...
    def getSupportedItemTypesOfChannel(self) -> java.util.Collection[java.lang.String]: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    @typing.overload
    def getUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...

class SystemDefaultProfile(org.openhab.core.thing.profiles.StateProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.SystemDefaultProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.StateProfile
    
      Constructors:
        * SystemDefaultProfile(org.openhab.core.thing.profiles.ProfileCallback)
    
    """
    def __init__(self, callback: org.openhab.core.thing.profiles.ProfileCallback): ...
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onCommandFromHandler(self, command: org.openhab.core.types.Command) -> None: ...
    def onCommandFromItem(self, command: org.openhab.core.types.Command) -> None: ...
    def onStateUpdateFromHandler(self, state: org.openhab.core.types.State) -> None: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...

class SystemFollowProfile(org.openhab.core.thing.profiles.StateProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.SystemFollowProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.StateProfile
    
      Constructors:
        * SystemFollowProfile(org.openhab.core.thing.profiles.ProfileCallback)
    
    """
    def __init__(self, callback: org.openhab.core.thing.profiles.ProfileCallback): ...
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onCommandFromHandler(self, command: org.openhab.core.types.Command) -> None: ...
    def onCommandFromItem(self, command: org.openhab.core.types.Command) -> None: ...
    def onStateUpdateFromHandler(self, state: org.openhab.core.types.State) -> None: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...

class SystemHysteresisStateProfile(org.openhab.core.thing.profiles.StateProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.SystemHysteresisStateProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.StateProfile
    
      Constructors:
        * SystemHysteresisStateProfile(org.openhab.core.thing.profiles.ProfileCallback, org.openhab.core.thing.profiles.ProfileContext)
    
    """
    def __init__(self, callback: org.openhab.core.thing.profiles.ProfileCallback, context: org.openhab.core.thing.profiles.ProfileContext): ...
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onCommandFromHandler(self, command: org.openhab.core.types.Command) -> None: ...
    def onCommandFromItem(self, command: org.openhab.core.types.Command) -> None: ...
    def onStateUpdateFromHandler(self, state: org.openhab.core.types.State) -> None: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...

class SystemOffsetProfile(org.openhab.core.thing.profiles.StateProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.SystemOffsetProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.StateProfile
    
      Constructors:
        * SystemOffsetProfile(org.openhab.core.thing.profiles.ProfileCallback, org.openhab.core.thing.profiles.ProfileContext)
    
    """
    def __init__(self, callback: org.openhab.core.thing.profiles.ProfileCallback, context: org.openhab.core.thing.profiles.ProfileContext): ...
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onCommandFromHandler(self, command: org.openhab.core.types.Command) -> None: ...
    def onCommandFromItem(self, command: org.openhab.core.types.Command) -> None: ...
    def onStateUpdateFromHandler(self, state: org.openhab.core.types.State) -> None: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...

class SystemProfileFactory(org.openhab.core.thing.profiles.ProfileFactory, org.openhab.core.thing.profiles.ProfileAdvisor, org.openhab.core.thing.profiles.ProfileTypeProvider):
    """
    Java class 'org.openhab.core.thing.internal.profiles.SystemProfileFactory'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.ProfileFactory,
            org.openhab.core.thing.profiles.ProfileAdvisor,
            org.openhab.core.thing.profiles.ProfileTypeProvider
    
      Constructors:
        * SystemProfileFactory(org.openhab.core.thing.type.ChannelTypeRegistry, org.openhab.core.thing.profiles.i18n.ProfileTypeI18nLocalizationService, org.openhab.core.util.BundleResolver)
    
    """
    def __init__(self, channelTypeRegistry: org.openhab.core.thing.type.ChannelTypeRegistry, profileTypeI18nLocalizationService: org.openhab.core.thing.profiles.i18n.ProfileTypeI18nLocalizationService, bundleResolver: org.openhab.core.util.BundleResolver): ...
    def createProfile(self, profileTypeUID: org.openhab.core.thing.profiles.ProfileTypeUID, callback: org.openhab.core.thing.profiles.ProfileCallback, context: org.openhab.core.thing.profiles.ProfileContext) -> org.openhab.core.thing.profiles.Profile: ...
    def getProfileTypes(self, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.thing.profiles.ProfileType]: ...
    @typing.overload
    def getSuggestedProfileTypeUID(self, channel: org.openhab.core.thing.Channel, itemType: java.lang.String) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    @typing.overload
    def getSuggestedProfileTypeUID(self, channelType: org.openhab.core.thing.type.ChannelType, itemType: java.lang.String) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def getSupportedProfileTypeUIDs(self) -> java.util.Collection[org.openhab.core.thing.profiles.ProfileTypeUID]: ...

class TimestampChangeProfile(org.openhab.core.thing.profiles.StateProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.TimestampChangeProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.StateProfile
    
      Constructors:
        * TimestampChangeProfile(org.openhab.core.thing.profiles.ProfileCallback)
    
    """
    def __init__(self, callback: org.openhab.core.thing.profiles.ProfileCallback): ...
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onCommandFromHandler(self, command: org.openhab.core.types.Command) -> None: ...
    def onCommandFromItem(self, command: org.openhab.core.types.Command) -> None: ...
    def onStateUpdateFromHandler(self, state: org.openhab.core.types.State) -> None: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...

class TimestampUpdateProfile(org.openhab.core.thing.profiles.StateProfile):
    """
    Java class 'org.openhab.core.thing.internal.profiles.TimestampUpdateProfile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.StateProfile
    
      Constructors:
        * TimestampUpdateProfile(org.openhab.core.thing.profiles.ProfileCallback)
    
    """
    def __init__(self, callback: org.openhab.core.thing.profiles.ProfileCallback): ...
    def getProfileTypeUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
    def onCommandFromHandler(self, command: org.openhab.core.types.Command) -> None: ...
    def onCommandFromItem(self, command: org.openhab.core.types.Command) -> None: ...
    def onStateUpdateFromHandler(self, state: org.openhab.core.types.State) -> None: ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...

class TriggerProfileTypeImpl(org.openhab.core.thing.profiles.TriggerProfileType):
    """
    Java class 'org.openhab.core.thing.internal.profiles.TriggerProfileTypeImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.profiles.TriggerProfileType
    
      Constructors:
        * TriggerProfileTypeImpl(org.openhab.core.thing.profiles.ProfileTypeUID, java.lang.String, java.util.Collection, java.util.Collection)
    
    """
    def __init__(self, profileTypeUID: org.openhab.core.thing.profiles.ProfileTypeUID, label: java.lang.String, supportedItemTypes: typing.Union[java.util.Collection[java.lang.String], typing.Sequence[java.lang.String]], supportedChannelTypeUIDs: typing.Union[java.util.Collection[org.openhab.core.thing.type.ChannelTypeUID], typing.Sequence[org.openhab.core.thing.type.ChannelTypeUID]]): ...
    def getLabel(self) -> java.lang.String: ...
    def getSupportedChannelTypeUIDs(self) -> java.util.Collection[org.openhab.core.thing.type.ChannelTypeUID]: ...
    def getSupportedItemTypes(self) -> java.util.Collection[java.lang.String]: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    @typing.overload
    def getUID(self) -> org.openhab.core.thing.profiles.ProfileTypeUID: ...
