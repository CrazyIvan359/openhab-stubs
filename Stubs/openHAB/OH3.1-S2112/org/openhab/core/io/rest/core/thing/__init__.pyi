import java.lang
import java.util
import org.openhab.core.thing
import org.openhab.core.thing.dto
import org.openhab.core.thing.firmware.dto
import typing


class EnrichedChannelDTO(org.openhab.core.thing.dto.ChannelDTO):
    """
    Java class 'org.openhab.core.io.rest.core.thing.EnrichedChannelDTO'
    
        Extends:
            org.openhab.core.thing.dto.ChannelDTO
    
      Constructors:
        * EnrichedChannelDTO(org.openhab.core.thing.dto.ChannelDTO, java.util.Set)
    
      Attributes:
        linkedItems (java.util.Set): final field
    
    """
    linkedItems: java.util.Set = ...
    def __init__(self, channelDTO: org.openhab.core.thing.dto.ChannelDTO, linkedItems: java.util.Set[java.lang.String]): ...

class EnrichedThingDTO(org.openhab.core.thing.dto.ThingDTO):
    """
    Java class 'org.openhab.core.io.rest.core.thing.EnrichedThingDTO'
    
        Extends:
            org.openhab.core.thing.dto.ThingDTO
    
      Attributes:
        statusInfo (org.openhab.core.thing.ThingStatusInfo): field
        firmwareStatus (org.openhab.core.thing.firmware.dto.FirmwareStatusDTO): final field
        editable (boolean): field
    
    """
    statusInfo: org.openhab.core.thing.ThingStatusInfo = ...
    firmwareStatus: org.openhab.core.thing.firmware.dto.FirmwareStatusDTO = ...
    editable: bool = ...

class EnrichedThingDTOMapper(org.openhab.core.thing.dto.ThingDTOMapper):
    """
    Java class 'org.openhab.core.io.rest.core.thing.EnrichedThingDTOMapper'
    
        Extends:
            org.openhab.core.thing.dto.ThingDTOMapper
    
      Constructors:
        * EnrichedThingDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, thing: org.openhab.core.thing.Thing, thingStatusInfo: org.openhab.core.thing.ThingStatusInfo, firmwareStatus: org.openhab.core.thing.firmware.dto.FirmwareStatusDTO, linkedItemsMap: typing.Union[java.util.Map[java.lang.String, java.util.Set[java.lang.String]], typing.Mapping[java.lang.String, java.util.Set[java.lang.String]]], editable: bool) -> EnrichedThingDTO: ...
    @classmethod
    @typing.overload
    def map(cls, thingDTO: org.openhab.core.thing.dto.ThingDTO, isBridge: bool) -> org.openhab.core.thing.Thing: ...
    @classmethod
    @typing.overload
    def map(cls, thing: org.openhab.core.thing.Thing) -> org.openhab.core.thing.dto.ThingDTO: ...
