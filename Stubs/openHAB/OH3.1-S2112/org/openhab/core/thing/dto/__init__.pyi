import java.lang
import java.util
import org.openhab.core.config.core
import org.openhab.core.config.core.dto
import org.openhab.core.thing
import org.openhab.core.thing.type
import org.openhab.core.types
import typing


class ChannelDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.dto.ChannelDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelDTO()
        * ChannelDTO(org.openhab.core.thing.ChannelUID, java.lang.String, java.lang.String, org.openhab.core.thing.type.ChannelKind, java.lang.String, java.lang.String, java.util.Map, org.openhab.core.config.core.Configuration, java.util.Set, org.openhab.core.thing.type.AutoUpdatePolicy)
    
      Attributes:
        uid (java.lang.String): field
        id (java.lang.String): field
        channelTypeUID (java.lang.String): field
        itemType (java.lang.String): field
        kind (java.lang.String): field
        label (java.lang.String): field
        description (java.lang.String): field
        defaultTags (java.util.Set): field
        properties (java.util.Map): field
        configuration (java.util.Map): field
        autoUpdatePolicy (java.lang.String): field
    
    """
    uid: java.lang.String = ...
    id: java.lang.String = ...
    channelTypeUID: java.lang.String = ...
    itemType: java.lang.String = ...
    kind: java.lang.String = ...
    label: java.lang.String = ...
    description: java.lang.String = ...
    defaultTags: java.util.Set = ...
    properties: java.util.Map = ...
    configuration: java.util.Map = ...
    autoUpdatePolicy: java.lang.String = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, uid: org.openhab.core.thing.ChannelUID, channelTypeUID: java.lang.String, itemType: java.lang.String, kind: org.openhab.core.thing.type.ChannelKind, label: java.lang.String, description: java.lang.String, properties: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]], configuration: org.openhab.core.config.core.Configuration, defaultTags: java.util.Set[java.lang.String], autoUpdatePolicy: org.openhab.core.thing.type.AutoUpdatePolicy): ...

class ChannelDTOMapper(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.dto.ChannelDTOMapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, channelDTO: ChannelDTO) -> org.openhab.core.thing.Channel: ...
    @classmethod
    @typing.overload
    def map(cls, channel: org.openhab.core.thing.Channel) -> ChannelDTO: ...

class ChannelDefinitionDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.dto.ChannelDefinitionDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelDefinitionDTO()
        * ChannelDefinitionDTO(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.util.Set, java.lang.String, org.openhab.core.types.StateDescription, boolean, java.util.Map)
    
      Attributes:
        description (java.lang.String): field
        id (java.lang.String): field
        label (java.lang.String): field
        tags (java.util.Set): field
        properties (java.util.Map): field
        category (java.lang.String): field
        stateDescription (org.openhab.core.types.StateDescription): field
        advanced (boolean): field
        typeUID (java.lang.String): field
    
    """
    description: java.lang.String = ...
    id: java.lang.String = ...
    label: java.lang.String = ...
    tags: java.util.Set = ...
    properties: java.util.Map = ...
    category: java.lang.String = ...
    stateDescription: org.openhab.core.types.StateDescription = ...
    advanced: bool = ...
    typeUID: java.lang.String = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, id: java.lang.String, typeUID: java.lang.String, label: java.lang.String, description: java.lang.String, tags: java.util.Set[java.lang.String], category: java.lang.String, stateDescription: org.openhab.core.types.StateDescription, advanced: bool, properties: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]): ...

class ChannelGroupDefinitionDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.dto.ChannelGroupDefinitionDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelGroupDefinitionDTO()
        * ChannelGroupDefinitionDTO(java.lang.String, java.lang.String, java.lang.String, java.util.List)
    
      Attributes:
        id (java.lang.String): field
        description (java.lang.String): field
        label (java.lang.String): field
        channels (java.util.List): field
    
    """
    id: java.lang.String = ...
    description: java.lang.String = ...
    label: java.lang.String = ...
    channels: java.util.List = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, id: java.lang.String, label: java.lang.String, description: java.lang.String, channels: java.util.List[ChannelDefinitionDTO]): ...

class ChannelTypeDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.dto.ChannelTypeDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelTypeDTO()
        * ChannelTypeDTO(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, org.openhab.core.thing.type.ChannelKind, java.util.List, java.util.List, org.openhab.core.types.StateDescription, java.util.Set, boolean, org.openhab.core.types.CommandDescription)
    
      Attributes:
        parameters (java.util.List): field
        parameterGroups (java.util.List): field
        description (java.lang.String): field
        label (java.lang.String): field
        category (java.lang.String): field
        itemType (java.lang.String): field
        kind (java.lang.String): field
        stateDescription (org.openhab.core.types.StateDescription): field
        tags (java.util.Set): field
        UID (java.lang.String): field
        advanced (boolean): field
        commandDescription (org.openhab.core.types.CommandDescription): field
    
    """
    parameters: java.util.List = ...
    parameterGroups: java.util.List = ...
    description: java.lang.String = ...
    label: java.lang.String = ...
    category: java.lang.String = ...
    itemType: java.lang.String = ...
    kind: java.lang.String = ...
    stateDescription: org.openhab.core.types.StateDescription = ...
    tags: java.util.Set = ...
    UID: java.lang.String = ...
    advanced: bool = ...
    commandDescription: org.openhab.core.types.CommandDescription = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, UID: java.lang.String, label: java.lang.String, description: java.lang.String, category: java.lang.String, itemType: java.lang.String, kind: org.openhab.core.thing.type.ChannelKind, parameters: java.util.List[org.openhab.core.config.core.dto.ConfigDescriptionParameterDTO], parameterGroups: java.util.List[org.openhab.core.config.core.dto.ConfigDescriptionParameterGroupDTO], stateDescription: org.openhab.core.types.StateDescription, tags: java.util.Set[java.lang.String], advanced: bool, commandDescription: org.openhab.core.types.CommandDescription): ...

class StrippedThingTypeDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.dto.StrippedThingTypeDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * StrippedThingTypeDTO()
        * StrippedThingTypeDTO(java.lang.String, java.lang.String, java.lang.String, java.lang.String, boolean, java.util.List, boolean)
    
      Attributes:
        UID (java.lang.String): field
        label (java.lang.String): field
        description (java.lang.String): field
        category (java.lang.String): field
        listed (boolean): field
        supportedBridgeTypeUIDs (java.util.List): field
        bridge (boolean): field
    
    """
    UID: java.lang.String = ...
    label: java.lang.String = ...
    description: java.lang.String = ...
    category: java.lang.String = ...
    listed: bool = ...
    supportedBridgeTypeUIDs: java.util.List = ...
    bridge: bool = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, UID: java.lang.String, label: java.lang.String, description: java.lang.String, category: java.lang.String, listed: bool, supportedBridgeTypeUIDs: java.util.List[java.lang.String], bridge: bool): ...

class StrippedThingTypeDTOMapper(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.dto.StrippedThingTypeDTOMapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * StrippedThingTypeDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    def map(cls, thingType: org.openhab.core.thing.type.ThingType, locale: java.util.Locale) -> StrippedThingTypeDTO: ...

class ThingDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.dto.ThingDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ThingDTO()
    
      Attributes:
        label (java.lang.String): field
        bridgeUID (java.lang.String): field
        configuration (java.util.Map): field
        properties (java.util.Map): field
        UID (java.lang.String): field
        thingTypeUID (java.lang.String): field
        channels (java.util.List): field
        location (java.lang.String): field
    
    """
    label: java.lang.String = ...
    bridgeUID: java.lang.String = ...
    configuration: java.util.Map = ...
    properties: java.util.Map = ...
    UID: java.lang.String = ...
    thingTypeUID: java.lang.String = ...
    channels: java.util.List = ...
    location: java.lang.String = ...
    def __init__(self): ...

class ThingDTOMapper(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.dto.ThingDTOMapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ThingDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, thingDTO: ThingDTO, isBridge: bool) -> org.openhab.core.thing.Thing: ...
    @classmethod
    @typing.overload
    def map(cls, thing: org.openhab.core.thing.Thing) -> ThingDTO: ...

class ThingTypeDTO(StrippedThingTypeDTO):
    """
    Java class 'org.openhab.core.thing.dto.ThingTypeDTO'
    
        Extends:
            org.openhab.core.thing.dto.StrippedThingTypeDTO
    
      Constructors:
        * ThingTypeDTO()
        * ThingTypeDTO(java.lang.String, java.lang.String, java.lang.String, java.lang.String, boolean, java.util.List, java.util.List, java.util.List, java.util.List, java.util.Map, boolean, java.util.List, java.util.List)
    
      Attributes:
        channels (java.util.List): field
        channelGroups (java.util.List): field
        configParameters (java.util.List): field
        parameterGroups (java.util.List): field
        properties (java.util.Map): field
        extensibleChannelTypeIds (java.util.List): field
    
    """
    channels: java.util.List = ...
    channelGroups: java.util.List = ...
    configParameters: java.util.List = ...
    parameterGroups: java.util.List = ...
    properties: java.util.Map = ...
    extensibleChannelTypeIds: java.util.List = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, UID: java.lang.String, label: java.lang.String, description: java.lang.String, category: java.lang.String, listed: bool, configParameters: java.util.List[org.openhab.core.config.core.dto.ConfigDescriptionParameterDTO], channels: java.util.List[ChannelDefinitionDTO], channelGroups: java.util.List[ChannelGroupDefinitionDTO], supportedBridgeTypeUIDs: java.util.List[java.lang.String], properties: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]], bridge: bool, parameterGroups: java.util.List[org.openhab.core.config.core.dto.ConfigDescriptionParameterGroupDTO], extensibleChannelTypeIds: java.util.List[java.lang.String]): ...
