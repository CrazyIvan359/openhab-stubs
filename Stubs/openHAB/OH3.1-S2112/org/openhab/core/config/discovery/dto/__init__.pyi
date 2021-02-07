import java.lang
import java.util
import org.openhab.core.config.discovery
import typing


class DiscoveryResultDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.config.discovery.dto.DiscoveryResultDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * DiscoveryResultDTO()
        * DiscoveryResultDTO(java.lang.String, java.lang.String, java.lang.String, java.lang.String, org.openhab.core.config.discovery.DiscoveryResultFlag, java.util.Map, java.lang.String)
    
      Attributes:
        bridgeUID (java.lang.String): field
        flag (org.openhab.core.config.discovery.DiscoveryResultFlag): field
        label (java.lang.String): field
        properties (java.util.Map): field
        representationProperty (java.lang.String): field
        thingUID (java.lang.String): field
        thingTypeUID (java.lang.String): field
    
    """
    bridgeUID: java.lang.String = ...
    flag: org.openhab.core.config.discovery.DiscoveryResultFlag = ...
    label: java.lang.String = ...
    properties: java.util.Map = ...
    representationProperty: java.lang.String = ...
    thingUID: java.lang.String = ...
    thingTypeUID: java.lang.String = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, thingUID: java.lang.String, bridgeUID: java.lang.String, thingTypeUID: java.lang.String, label: java.lang.String, flag: org.openhab.core.config.discovery.DiscoveryResultFlag, properties: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]], representationProperty: java.lang.String): ...

class DiscoveryResultDTOMapper(java.lang.Object):
    """
    Java class 'org.openhab.core.config.discovery.dto.DiscoveryResultDTOMapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * DiscoveryResultDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, discoveryResultDTO: DiscoveryResultDTO) -> org.openhab.core.config.discovery.DiscoveryResult: ...
    @classmethod
    @typing.overload
    def map(cls, discoveryResult: org.openhab.core.config.discovery.DiscoveryResult) -> DiscoveryResultDTO: ...
