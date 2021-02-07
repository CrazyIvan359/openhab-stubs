import java.lang
import java.net
import java.util
import org
import org.openhab.core.common.registry
import org.openhab.core.thing
import org.openhab.core.types
import typing


class AbstractDescriptionType(org.openhab.core.common.registry.Identifiable[org.openhab.core.thing.UID]):
    """
    Java class 'org.openhab.core.thing.type.AbstractDescriptionType'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.common.registry.Identifiable
    
      Constructors:
        * AbstractDescriptionType(org.openhab.core.thing.UID, java.lang.String, java.lang.String)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
    """
    def __init__(self, uid: org.openhab.core.thing.UID, label: java.lang.String, description: java.lang.String): ...
    def getDescription(self) -> java.lang.String: ...
    def getLabel(self) -> java.lang.String: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    @typing.overload
    def getUID(self) -> org.openhab.core.thing.UID: ...

class AutoUpdatePolicy(java.lang.Enum[org.openhab.core.thing.type.AutoUpdatePolicy]):
    """
    Java class 'org.openhab.core.thing.type.AutoUpdatePolicy'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        VETO (org.openhab.core.thing.type.AutoUpdatePolicy): final static enum constant
        DEFAULT (org.openhab.core.thing.type.AutoUpdatePolicy): final static enum constant
        RECOMMEND (org.openhab.core.thing.type.AutoUpdatePolicy): final static enum constant
    
    """
    VETO: typing.ClassVar['AutoUpdatePolicy'] = ...
    DEFAULT: typing.ClassVar['AutoUpdatePolicy'] = ...
    RECOMMEND: typing.ClassVar['AutoUpdatePolicy'] = ...
    @classmethod
    def parse(cls, input: java.lang.String) -> 'AutoUpdatePolicy': ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'AutoUpdatePolicy': ...
    @classmethod
    def values(cls) -> typing.List['AutoUpdatePolicy']: ...

class ChannelDefinition(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.type.ChannelDefinition'
    
        Extends:
            java.lang.Object
    
    """
    def getAutoUpdatePolicy(self) -> AutoUpdatePolicy: ...
    def getChannelTypeUID(self) -> 'ChannelTypeUID': ...
    def getDescription(self) -> java.lang.String: ...
    def getId(self) -> java.lang.String: ...
    def getLabel(self) -> java.lang.String: ...
    def getProperties(self) -> java.util.Map[java.lang.String, java.lang.String]: ...
    def toString(self) -> java.lang.String: ...

class ChannelDefinitionBuilder(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.type.ChannelDefinitionBuilder'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelDefinitionBuilder(org.openhab.core.thing.type.ChannelDefinition)
        * ChannelDefinitionBuilder(java.lang.String, org.openhab.core.thing.type.ChannelTypeUID)
    
    """
    @typing.overload
    def __init__(self, id: java.lang.String, channelTypeUID: 'ChannelTypeUID'): ...
    @typing.overload
    def __init__(self, channelDefinition: ChannelDefinition): ...
    def build(self) -> ChannelDefinition: ...
    def withAutoUpdatePolicy(self, autoUpdatePolicy: AutoUpdatePolicy) -> 'ChannelDefinitionBuilder': ...
    def withDescription(self, description: java.lang.String) -> 'ChannelDefinitionBuilder': ...
    def withLabel(self, label: java.lang.String) -> 'ChannelDefinitionBuilder': ...
    def withProperties(self, properties: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> 'ChannelDefinitionBuilder': ...

class ChannelGroupDefinition(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.type.ChannelGroupDefinition'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelGroupDefinition(java.lang.String, org.openhab.core.thing.type.ChannelGroupTypeUID, java.lang.String, java.lang.String)
        * ChannelGroupDefinition(java.lang.String, org.openhab.core.thing.type.ChannelGroupTypeUID)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
    """
    @typing.overload
    def __init__(self, id: java.lang.String, typeUID: 'ChannelGroupTypeUID'): ...
    @typing.overload
    def __init__(self, id: java.lang.String, typeUID: 'ChannelGroupTypeUID', label: java.lang.String, description: java.lang.String): ...
    def getDescription(self) -> java.lang.String: ...
    def getId(self) -> java.lang.String: ...
    def getLabel(self) -> java.lang.String: ...
    def getTypeUID(self) -> 'ChannelGroupTypeUID': ...
    def toString(self) -> java.lang.String: ...

class ChannelGroupTypeBuilder(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.type.ChannelGroupTypeBuilder'
    
        Extends:
            java.lang.Object
    
    """
    def build(self) -> 'ChannelGroupType': ...
    @classmethod
    def instance(cls, channelGroupTypeUID: 'ChannelGroupTypeUID', label: java.lang.String) -> 'ChannelGroupTypeBuilder': ...
    def withCategory(self, category: java.lang.String) -> 'ChannelGroupTypeBuilder': ...
    def withChannelDefinitions(self, channelDefinitions: java.util.List[ChannelDefinition]) -> 'ChannelGroupTypeBuilder': ...
    def withDescription(self, description: java.lang.String) -> 'ChannelGroupTypeBuilder': ...

class ChannelGroupTypeProvider(java.lang.Object):
    """
    @NonNullByDefault public interface ChannelGroupTypeProvider
    
        The :class:`~org.openhab.core.thing.type.ChannelGroupTypeProvider` is responsible for providing channel group types.
    
        Also see:
            :class:`~org.openhab.core.thing.type.ChannelGroupTypeRegistry`
    
    
    """
    def getChannelGroupType(self, channelGroupTypeUID: 'ChannelGroupTypeUID', locale: java.util.Locale) -> 'ChannelGroupType': ...
    def getChannelGroupTypes(self, locale: java.util.Locale) -> java.util.Collection['ChannelGroupType']: ...

class ChannelGroupTypeRegistry(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.type.ChannelGroupTypeRegistry'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelGroupTypeRegistry()
    
    """
    def __init__(self): ...
    @typing.overload
    def getChannelGroupType(self, channelGroupTypeUID: 'ChannelGroupTypeUID') -> 'ChannelGroupType': ...
    @typing.overload
    def getChannelGroupType(self, channelGroupTypeUID: 'ChannelGroupTypeUID', locale: java.util.Locale) -> 'ChannelGroupType': ...
    @typing.overload
    def getChannelGroupTypes(self) -> java.util.List['ChannelGroupType']: ...
    @typing.overload
    def getChannelGroupTypes(self, locale: java.util.Locale) -> java.util.List['ChannelGroupType']: ...

class ChannelGroupTypeUID(org.openhab.core.thing.UID):
    """
    Java class 'org.openhab.core.thing.type.ChannelGroupTypeUID'
    
        Extends:
            org.openhab.core.thing.UID
    
      Constructors:
        * ChannelGroupTypeUID(java.lang.String)
        * ChannelGroupTypeUID(java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, channelGroupUid: java.lang.String): ...
    @typing.overload
    def __init__(self, bindingId: java.lang.String, id: java.lang.String): ...
    def getId(self) -> java.lang.String: ...

class ChannelKind(java.lang.Enum[org.openhab.core.thing.type.ChannelKind]):
    """
    Java class 'org.openhab.core.thing.type.ChannelKind'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        STATE (org.openhab.core.thing.type.ChannelKind): final static enum constant
        TRIGGER (org.openhab.core.thing.type.ChannelKind): final static enum constant
    
    """
    STATE: typing.ClassVar['ChannelKind'] = ...
    TRIGGER: typing.ClassVar['ChannelKind'] = ...
    @classmethod
    def parse(cls, input: java.lang.String) -> 'ChannelKind': ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'ChannelKind': ...
    @classmethod
    def values(cls) -> typing.List['ChannelKind']: ...

_ChannelTypeBuilder__T = typing.TypeVar('_ChannelTypeBuilder__T', bound='ChannelTypeBuilder')  # <T>
class ChannelTypeBuilder(java.lang.Object, typing.Generic[_ChannelTypeBuilder__T]):
    """
    @NonNullByDefault public interface ChannelTypeBuilder<T extends ChannelTypeBuilder<T>&gt;
    
        Interface for :class:`~org.openhab.core.thing.type.ChannelTypeBuilder`.
    
    
    """
    def build(self) -> 'ChannelType': ...
    def isAdvanced(self, advanced: bool) -> _ChannelTypeBuilder__T: ...
    @classmethod
    def state(cls, channelTypeUID: 'ChannelTypeUID', label: java.lang.String, itemType: java.lang.String) -> 'StateChannelTypeBuilder': ...
    @classmethod
    def trigger(cls, channelTypeUID: 'ChannelTypeUID', label: java.lang.String) -> 'TriggerChannelTypeBuilder': ...
    def withCategory(self, category: java.lang.String) -> _ChannelTypeBuilder__T: ...
    def withConfigDescriptionURI(self, configDescriptionURI: java.net.URI) -> _ChannelTypeBuilder__T: ...
    def withDescription(self, description: java.lang.String) -> _ChannelTypeBuilder__T: ...
    def withTag(self, tag: java.lang.String) -> _ChannelTypeBuilder__T: ...
    def withTags(self, tags: typing.Union[java.util.Collection[java.lang.String], typing.Sequence[java.lang.String]]) -> _ChannelTypeBuilder__T: ...

class ChannelTypeProvider(java.lang.Object):
    """
    @NonNullByDefault public interface ChannelTypeProvider
    
        The :class:`~org.openhab.core.thing.type.ChannelTypeProvider` is responsible for providing channel types.
    
        Also see:
            :class:`~org.openhab.core.thing.type.ChannelTypeRegistry`
    
    
    """
    def getChannelType(self, channelTypeUID: 'ChannelTypeUID', locale: java.util.Locale) -> 'ChannelType': ...
    def getChannelTypes(self, locale: java.util.Locale) -> java.util.Collection['ChannelType']: ...

class ChannelTypeRegistry(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.type.ChannelTypeRegistry'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelTypeRegistry()
    
    """
    def __init__(self): ...
    @typing.overload
    def getChannelType(self, channelTypeUID: 'ChannelTypeUID') -> 'ChannelType': ...
    @typing.overload
    def getChannelType(self, channelTypeUID: 'ChannelTypeUID', locale: java.util.Locale) -> 'ChannelType': ...
    @typing.overload
    def getChannelTypes(self) -> java.util.List['ChannelType']: ...
    @typing.overload
    def getChannelTypes(self, locale: java.util.Locale) -> java.util.List['ChannelType']: ...

class ChannelTypeUID(org.openhab.core.thing.UID):
    """
    Java class 'org.openhab.core.thing.type.ChannelTypeUID'
    
        Extends:
            org.openhab.core.thing.UID
    
      Constructors:
        * ChannelTypeUID(java.lang.String, java.lang.String)
        * ChannelTypeUID(java.lang.String)
    
    """
    @typing.overload
    def __init__(self, channelUid: java.lang.String): ...
    @typing.overload
    def __init__(self, bindingId: java.lang.String, id: java.lang.String): ...
    def getId(self) -> java.lang.String: ...

class DynamicCommandDescriptionProvider(java.lang.Object):
    """
    @NonNullByDefault public interface DynamicCommandDescriptionProvider
    
        Implementations may provide :class:`~org.openhab.core.thing.Channel` specific :code:`CommandDescription`s. Therefore the
        provider must be registered as OSGi service.
    
    
    """
    def getCommandDescription(self, channel: org.openhab.core.thing.Channel, originalCommandDescription: org.openhab.core.types.CommandDescription, locale: java.util.Locale) -> org.openhab.core.types.CommandDescription: ...

class DynamicStateDescriptionProvider(java.lang.Object):
    """
    @NonNullByDefault public interface DynamicStateDescriptionProvider
    
        The :class:`~org.openhab.core.thing.type.DynamicStateDescriptionProvider` is responsible for providing
        :code:`StateDescription` for a :class:`~org.openhab.core.thing.Channel` dynamically in the runtime. Therefore the
        provider must be registered as OSGi service.
    
    
    """
    def getStateDescription(self, channel: org.openhab.core.thing.Channel, originalStateDescription: org.openhab.core.types.StateDescription, locale: java.util.Locale) -> org.openhab.core.types.StateDescription: ...

class ThingTypeBuilder(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.type.ThingTypeBuilder'
    
        Extends:
            java.lang.Object
    
    """
    def build(self) -> 'ThingType': ...
    def buildBridge(self) -> 'BridgeType': ...
    @classmethod
    @typing.overload
    def instance(cls, bindingId: java.lang.String, thingTypeId: java.lang.String, label: java.lang.String) -> 'ThingTypeBuilder': ...
    @classmethod
    @typing.overload
    def instance(cls, thingTypeUID: org.openhab.core.thing.ThingTypeUID, label: java.lang.String) -> 'ThingTypeBuilder': ...
    @classmethod
    @typing.overload
    def instance(cls, thingType: 'ThingType') -> 'ThingTypeBuilder': ...
    def isListed(self, listed: bool) -> 'ThingTypeBuilder': ...
    def withCategory(self, category: java.lang.String) -> 'ThingTypeBuilder': ...
    def withChannelDefinitions(self, channelDefinitions: java.util.List[ChannelDefinition]) -> 'ThingTypeBuilder': ...
    def withChannelGroupDefinitions(self, channelGroupDefinitions: java.util.List[ChannelGroupDefinition]) -> 'ThingTypeBuilder': ...
    def withConfigDescriptionURI(self, configDescriptionURI: java.net.URI) -> 'ThingTypeBuilder': ...
    def withDescription(self, description: java.lang.String) -> 'ThingTypeBuilder': ...
    def withExtensibleChannelTypeIds(self, extensibleChannelTypeIds: java.util.List[java.lang.String]) -> 'ThingTypeBuilder': ...
    def withLabel(self, label: java.lang.String) -> 'ThingTypeBuilder': ...
    def withProperties(self, properties: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> 'ThingTypeBuilder': ...
    def withRepresentationProperty(self, representationProperty: java.lang.String) -> 'ThingTypeBuilder': ...
    def withSupportedBridgeTypeUIDs(self, supportedBridgeTypeUIDs: java.util.List[java.lang.String]) -> 'ThingTypeBuilder': ...

class ThingTypeRegistry(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.type.ThingTypeRegistry'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ThingTypeRegistry(org.openhab.core.thing.type.ChannelTypeRegistry)
    
    """
    def __init__(self, channelTypeRegistry: ChannelTypeRegistry): ...
    @typing.overload
    def getChannelType(self, channel: org.openhab.core.thing.Channel) -> 'ChannelType': ...
    @typing.overload
    def getChannelType(self, channel: org.openhab.core.thing.Channel, locale: java.util.Locale) -> 'ChannelType': ...
    @typing.overload
    def getThingType(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID) -> 'ThingType': ...
    @typing.overload
    def getThingType(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID, locale: java.util.Locale) -> 'ThingType': ...
    @typing.overload
    def getThingTypes(self) -> java.util.List['ThingType']: ...
    @typing.overload
    def getThingTypes(self, bindingId: java.lang.String) -> java.util.List['ThingType']: ...
    @typing.overload
    def getThingTypes(self, bindingId: java.lang.String, locale: java.util.Locale) -> java.util.List['ThingType']: ...
    @typing.overload
    def getThingTypes(self, locale: java.util.Locale) -> java.util.List['ThingType']: ...

class ChannelGroupType(AbstractDescriptionType):
    """
    Java class 'org.openhab.core.thing.type.ChannelGroupType'
    
        Extends:
            org.openhab.core.thing.type.AbstractDescriptionType
    
    """
    def getCategory(self) -> java.lang.String: ...
    def getChannelDefinitions(self) -> java.util.List[ChannelDefinition]: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    @typing.overload
    def getUID(self) -> org.openhab.core.thing.UID: ...
    @typing.overload
    def getUID(self) -> ChannelGroupTypeUID: ...
    def toString(self) -> java.lang.String: ...

class ChannelType(AbstractDescriptionType):
    """
    Java class 'org.openhab.core.thing.type.ChannelType'
    
        Extends:
            org.openhab.core.thing.type.AbstractDescriptionType
    
    """
    def getAutoUpdatePolicy(self) -> AutoUpdatePolicy: ...
    def getCategory(self) -> java.lang.String: ...
    def getCommandDescription(self) -> org.openhab.core.types.CommandDescription: ...
    def getConfigDescriptionURI(self) -> java.net.URI: ...
    def getEvent(self) -> org.openhab.core.types.EventDescription: ...
    def getItemType(self) -> java.lang.String: ...
    def getKind(self) -> ChannelKind: ...
    def getState(self) -> org.openhab.core.types.StateDescription: ...
    def getTags(self) -> java.util.Set[java.lang.String]: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    @typing.overload
    def getUID(self) -> org.openhab.core.thing.UID: ...
    @typing.overload
    def getUID(self) -> ChannelTypeUID: ...
    def isAdvanced(self) -> bool: ...
    def toString(self) -> java.lang.String: ...

class StateChannelTypeBuilder(ChannelTypeBuilder[org.openhab.core.thing.type.StateChannelTypeBuilder]):
    """
    Java class 'org.openhab.core.thing.type.StateChannelTypeBuilder'
    
        Interfaces:
            org.openhab.core.thing.type.ChannelTypeBuilder
    
    """
    def withAutoUpdatePolicy(self, autoUpdatePolicy: AutoUpdatePolicy) -> 'StateChannelTypeBuilder': ...
    def withCommandDescription(self, commandDescription: org.openhab.core.types.CommandDescription) -> 'StateChannelTypeBuilder': ...
    def withStateDescriptionFragment(self, stateDescriptionFragment: org.openhab.core.types.StateDescriptionFragment) -> 'StateChannelTypeBuilder': ...

class ThingType(AbstractDescriptionType):
    """
    Java class 'org.openhab.core.thing.type.ThingType'
    
        Extends:
            org.openhab.core.thing.type.AbstractDescriptionType
    
    """
    def equals(self, obj: typing.Any) -> bool: ...
    def getBindingId(self) -> java.lang.String: ...
    def getCategory(self) -> java.lang.String: ...
    def getChannelDefinitions(self) -> java.util.List[ChannelDefinition]: ...
    def getChannelGroupDefinitions(self) -> java.util.List[ChannelGroupDefinition]: ...
    def getConfigDescriptionURI(self) -> java.net.URI: ...
    def getExtensibleChannelTypeIds(self) -> java.util.List[java.lang.String]: ...
    def getProperties(self) -> java.util.Map[java.lang.String, java.lang.String]: ...
    def getRepresentationProperty(self) -> java.lang.String: ...
    def getSupportedBridgeTypeUIDs(self) -> java.util.List[java.lang.String]: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    @typing.overload
    def getUID(self) -> org.openhab.core.thing.ThingTypeUID: ...
    @typing.overload
    def getUID(self) -> org.openhab.core.thing.UID: ...
    def hashCode(self) -> int: ...
    def isListed(self) -> bool: ...
    def toString(self) -> java.lang.String: ...

class TriggerChannelTypeBuilder(ChannelTypeBuilder[org.openhab.core.thing.type.TriggerChannelTypeBuilder]):
    """
    Java class 'org.openhab.core.thing.type.TriggerChannelTypeBuilder'
    
        Interfaces:
            org.openhab.core.thing.type.ChannelTypeBuilder
    
    """
    def withEventDescription(self, eventDescription: org.openhab.core.types.EventDescription) -> 'TriggerChannelTypeBuilder': ...

class BridgeType(ThingType):
    """
    Java class 'org.openhab.core.thing.type.BridgeType'
    
        Extends:
            org.openhab.core.thing.type.ThingType
    
    """
