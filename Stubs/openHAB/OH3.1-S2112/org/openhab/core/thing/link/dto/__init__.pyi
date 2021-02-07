import java.lang
import java.util
import typing


class AbstractLinkDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.link.dto.AbstractLinkDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * AbstractLinkDTO(java.lang.String)
    
      Attributes:
        itemName (java.lang.String): field
    
    """
    itemName: java.lang.String = ...
    def __init__(self, itemName: java.lang.String): ...

class ItemChannelLinkDTO(AbstractLinkDTO):
    """
    Java class 'org.openhab.core.thing.link.dto.ItemChannelLinkDTO'
    
        Extends:
            org.openhab.core.thing.link.dto.AbstractLinkDTO
    
      Constructors:
        * ItemChannelLinkDTO(java.lang.String, java.lang.String, java.util.Map)
    
      Attributes:
        channelUID (java.lang.String): field
        configuration (java.util.Map): field
    
    """
    channelUID: java.lang.String = ...
    configuration: java.util.Map = ...
    def __init__(self, itemName: java.lang.String, channelUID: java.lang.String, configuration: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]): ...
