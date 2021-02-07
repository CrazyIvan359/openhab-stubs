import java.lang
import java.util
import java.util.concurrent
import org
import org.openhab.core.common.registry
import org.openhab.core.config.core
import org.openhab.core.thing
import org.openhab.core.thing.type
import org.openhab.core.types
import typing


class Profile(java.lang.Object):
    """
    @NonNullByDefault public interface Profile
    
        Common ancestor of all profile types. Profiles define the communication flow between the framework and bindings, i.e.
        how (and if) certain events and commands are forwarded from the framework to the thing handler and vice versa.
    
        Profiles are allowed to maintain some transient state internally, i.e. the same instance of a profile will be used per
        link for all communication so that the temporal dimension can be taken in account.
    
    
    """
    def getProfileTypeUID(self) -> 'ProfileTypeUID': ...
    def onStateUpdateFromItem(self, state: org.openhab.core.types.State) -> None: ...

class ProfileAdvisor(java.lang.Object):
    """
    @NonNullByDefault public interface ProfileAdvisor
    
        Implementors can give advice which :class:`~org.openhab.core.thing.profiles.Profile`s can/should be used for a given
        link.
    
    
    """
    @typing.overload
    def getSuggestedProfileTypeUID(self, channel: org.openhab.core.thing.Channel, itemType: java.lang.String) -> 'ProfileTypeUID': ...
    @typing.overload
    def getSuggestedProfileTypeUID(self, channelType: org.openhab.core.thing.type.ChannelType, itemType: java.lang.String) -> 'ProfileTypeUID': ...

class ProfileCallback(java.lang.Object):
    """
    @NonNullByDefault public interface ProfileCallback
    
        Gives access to the framework features for continuing the communication flow.
    
    
    """
    def handleCommand(self, command: org.openhab.core.types.Command) -> None: ...
    def sendCommand(self, command: org.openhab.core.types.Command) -> None: ...
    def sendUpdate(self, state: org.openhab.core.types.State) -> None: ...

class ProfileContext(java.lang.Object):
    """
    @NonNullByDefault public interface ProfileContext
    
        The profile's context It gives access to related information like the profile's configuration or a scheduler.
    
    
    """
    def getConfiguration(self) -> org.openhab.core.config.core.Configuration: ...
    def getExecutorService(self) -> java.util.concurrent.ScheduledExecutorService: ...

class ProfileFactory(java.lang.Object):
    """
    @NonNullByDefault public interface ProfileFactory
    
        Implementors are capable of creating :class:`~org.openhab.core.thing.profiles.Profile` instances.
    
    
    """
    def createProfile(self, profileTypeUID: 'ProfileTypeUID', callback: ProfileCallback, profileContext: ProfileContext) -> Profile: ...
    def getSupportedProfileTypeUIDs(self) -> java.util.Collection['ProfileTypeUID']: ...

class ProfileType(org.openhab.core.common.registry.Identifiable[org.openhab.core.thing.profiles.ProfileTypeUID]):
    """
    Java class 'org.openhab.core.thing.profiles.ProfileType'
    
        Interfaces:
            org.openhab.core.common.registry.Identifiable
    
    """
    def getLabel(self) -> java.lang.String: ...
    def getSupportedItemTypes(self) -> java.util.Collection[java.lang.String]: ...

_ProfileTypeBuilder__T = typing.TypeVar('_ProfileTypeBuilder__T', bound=ProfileType)  # <T>
class ProfileTypeBuilder(java.lang.Object, typing.Generic[_ProfileTypeBuilder__T]):
    """
    Java class 'org.openhab.core.thing.profiles.ProfileTypeBuilder'
    
        Extends:
            java.lang.Object
    
    """
    def build(self) -> _ProfileTypeBuilder__T: ...
    @classmethod
    def newState(cls, profileTypeUID: 'ProfileTypeUID', label: java.lang.String) -> 'ProfileTypeBuilder'['StateProfileType']: ...
    @classmethod
    def newTrigger(cls, profileTypeUID: 'ProfileTypeUID', label: java.lang.String) -> 'ProfileTypeBuilder'['TriggerProfileType']: ...
    @typing.overload
    def withSupportedChannelTypeUIDs(self, channelTypeUIDs: typing.Union[java.util.Collection[org.openhab.core.thing.type.ChannelTypeUID], typing.Sequence[org.openhab.core.thing.type.ChannelTypeUID]]) -> 'ProfileTypeBuilder'[_ProfileTypeBuilder__T]: ...
    @typing.overload
    def withSupportedChannelTypeUIDs(self, channelTypeUIDs: typing.List[org.openhab.core.thing.type.ChannelTypeUID]) -> 'ProfileTypeBuilder'[_ProfileTypeBuilder__T]: ...
    @typing.overload
    def withSupportedItemTypes(self, itemType: typing.List[java.lang.String]) -> 'ProfileTypeBuilder'[_ProfileTypeBuilder__T]: ...
    @typing.overload
    def withSupportedItemTypes(self, itemTypes: typing.Union[java.util.Collection[java.lang.String], typing.Sequence[java.lang.String]]) -> 'ProfileTypeBuilder'[_ProfileTypeBuilder__T]: ...
    @typing.overload
    def withSupportedItemTypesOfChannel(self, supportedItemTypesOfChannel: typing.List[java.lang.String]) -> 'ProfileTypeBuilder'[_ProfileTypeBuilder__T]: ...
    @typing.overload
    def withSupportedItemTypesOfChannel(self, supportedItemTypesOfChannel: typing.Union[java.util.Collection[java.lang.String], typing.Sequence[java.lang.String]]) -> 'ProfileTypeBuilder'[_ProfileTypeBuilder__T]: ...

class ProfileTypeProvider(java.lang.Object):
    """
    @NonNullByDefault public interface ProfileTypeProvider
    
        A :class:`~org.openhab.core.thing.profiles.ProfileTypeProvider` is responsible for providing
        :class:`~org.openhab.core.thing.profiles.ProfileType`s.
    
    
    """
    def getProfileTypes(self, locale: java.util.Locale) -> java.util.Collection[ProfileType]: ...

class ProfileTypeRegistry(java.lang.Object):
    """
    @NonNullByDefault public interface ProfileTypeRegistry
    
        The :class:`~org.openhab.core.thing.profiles.ProfileTypeRegistry` allows access to the
        :class:`~org.openhab.core.thing.profiles.ProfileType`s provided by all
        :class:`~org.openhab.core.thing.profiles.ProfileTypeProvider`s.
    
    
    """
    @typing.overload
    def getProfileTypes(self) -> java.util.List[ProfileType]: ...
    @typing.overload
    def getProfileTypes(self, locale: java.util.Locale) -> java.util.List[ProfileType]: ...

class ProfileTypeUID(org.openhab.core.thing.UID):
    """
    Java class 'org.openhab.core.thing.profiles.ProfileTypeUID'
    
        Extends:
            org.openhab.core.thing.UID
    
      Constructors:
        * ProfileTypeUID(java.lang.String)
        * ProfileTypeUID(java.lang.String, java.lang.String)
    
      Attributes:
        SYSTEM_SCOPE (java.lang.String): final static field
    
    """
    SYSTEM_SCOPE: typing.ClassVar[java.lang.String] = ...
    @typing.overload
    def __init__(self, profileType: java.lang.String): ...
    @typing.overload
    def __init__(self, scope: java.lang.String, id: java.lang.String): ...
    def getId(self) -> java.lang.String: ...
    def getScope(self) -> java.lang.String: ...

class SystemProfiles(java.lang.Object):
    """
    @NonNullByDefault public interface SystemProfiles
    
        System profile constants.
    
    
    """
    DEFAULT: typing.ClassVar[ProfileTypeUID] = ...
    FOLLOW: typing.ClassVar[ProfileTypeUID] = ...
    OFFSET: typing.ClassVar[ProfileTypeUID] = ...
    HYSTERESIS: typing.ClassVar[ProfileTypeUID] = ...
    RAWBUTTON_ON_OFF_SWITCH: typing.ClassVar[ProfileTypeUID] = ...
    RAWBUTTON_TOGGLE_PLAYER: typing.ClassVar[ProfileTypeUID] = ...
    RAWBUTTON_TOGGLE_ROLLERSHUTTER: typing.ClassVar[ProfileTypeUID] = ...
    RAWBUTTON_TOGGLE_SWITCH: typing.ClassVar[ProfileTypeUID] = ...
    RAWROCKER_DIMMER: typing.ClassVar[ProfileTypeUID] = ...
    RAWROCKER_NEXT_PREVIOUS: typing.ClassVar[ProfileTypeUID] = ...
    RAWROCKER_ON_OFF: typing.ClassVar[ProfileTypeUID] = ...
    RAWROCKER_PLAY_PAUSE: typing.ClassVar[ProfileTypeUID] = ...
    RAWROCKER_REWIND_FASTFORWARD: typing.ClassVar[ProfileTypeUID] = ...
    RAWROCKER_STOP_MOVE: typing.ClassVar[ProfileTypeUID] = ...
    RAWROCKER_UP_DOWN: typing.ClassVar[ProfileTypeUID] = ...
    TIMESTAMP_CHANGE: typing.ClassVar[ProfileTypeUID] = ...
    TIMESTAMP_UPDATE: typing.ClassVar[ProfileTypeUID] = ...
    DEFAULT_TYPE: typing.ClassVar['StateProfileType'] = ...
    FOLLOW_TYPE: typing.ClassVar['StateProfileType'] = ...
    OFFSET_TYPE: typing.ClassVar['StateProfileType'] = ...
    HYSTERESIS_TYPE: typing.ClassVar[ProfileType] = ...
    RAWBUTTON_ON_OFF_SWITCH_TYPE: typing.ClassVar['TriggerProfileType'] = ...
    RAWBUTTON_TOGGLE_PLAYER_TYPE: typing.ClassVar['TriggerProfileType'] = ...
    RAWBUTTON_TOGGLE_ROLLERSHUTTER_TYPE: typing.ClassVar['TriggerProfileType'] = ...
    RAWBUTTON_TOGGLE_SWITCH_TYPE: typing.ClassVar['TriggerProfileType'] = ...
    RAWROCKER_ON_OFF_TYPE: typing.ClassVar['TriggerProfileType'] = ...
    RAWROCKER_DIMMER_TYPE: typing.ClassVar['TriggerProfileType'] = ...
    RAWROCKER_NEXT_PREVIOUS_TYPE: typing.ClassVar['TriggerProfileType'] = ...
    RAWROCKER_PLAY_PAUSE_TYPE: typing.ClassVar['TriggerProfileType'] = ...
    RAWROCKER_REWIND_FASTFORWARD_TYPE: typing.ClassVar['TriggerProfileType'] = ...
    RAWROCKER_STOP_MOVE_TYPE: typing.ClassVar['TriggerProfileType'] = ...
    RAWROCKER_UP_DOWN_TYPE: typing.ClassVar['TriggerProfileType'] = ...
    TIMESTAMP_CHANGE_TYPE: typing.ClassVar['StateProfileType'] = ...
    TIMESTAMP_UPDATE_TYPE: typing.ClassVar['StateProfileType'] = ...

class StateProfile(Profile):
    """
    Java class 'org.openhab.core.thing.profiles.StateProfile'
    
        Interfaces:
            org.openhab.core.thing.profiles.Profile
    
    """
    def onCommandFromHandler(self, command: org.openhab.core.types.Command) -> None: ...
    def onCommandFromItem(self, command: org.openhab.core.types.Command) -> None: ...
    def onStateUpdateFromHandler(self, state: org.openhab.core.types.State) -> None: ...

class StateProfileType(ProfileType):
    """
    Java class 'org.openhab.core.thing.profiles.StateProfileType'
    
        Interfaces:
            org.openhab.core.thing.profiles.ProfileType
    
    """
    def getSupportedItemTypesOfChannel(self) -> java.util.Collection[java.lang.String]: ...

class TriggerProfile(Profile):
    """
    Java class 'org.openhab.core.thing.profiles.TriggerProfile'
    
        Interfaces:
            org.openhab.core.thing.profiles.Profile
    
    """
    def onTriggerFromHandler(self, event: java.lang.String) -> None: ...

class TriggerProfileType(ProfileType):
    """
    Java class 'org.openhab.core.thing.profiles.TriggerProfileType'
    
        Interfaces:
            org.openhab.core.thing.profiles.ProfileType
    
    """
    def getSupportedChannelTypeUIDs(self) -> java.util.Collection[org.openhab.core.thing.type.ChannelTypeUID]: ...
