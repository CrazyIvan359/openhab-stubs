import java.lang
import javax.ws.rs.core
import org.openhab.core.io.rest
import org.openhab.core.thing.link
import org.openhab.core.thing.link.dto
import typing


class ItemChannelLinkResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.core.internal.link.ItemChannelLinkResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * ItemChannelLinkResource(org.openhab.core.thing.link.ItemChannelLinkRegistry)
    
      Attributes:
        PATH_LINKS (java.lang.String): final static field
    
    """
    PATH_LINKS: typing.ClassVar[java.lang.String] = ...
    def __init__(self, itemChannelLinkRegistry: org.openhab.core.thing.link.ItemChannelLinkRegistry): ...
    def getAll(self, channelUID: java.lang.String, itemName: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getLink(self, itemName: java.lang.String, channelUid: java.lang.String) -> javax.ws.rs.core.Response: ...
    def link(self, itemName: java.lang.String, channelUid: java.lang.String, bean: org.openhab.core.thing.link.dto.ItemChannelLinkDTO) -> javax.ws.rs.core.Response: ...
    def unlink(self, itemName: java.lang.String, channelUid: java.lang.String) -> javax.ws.rs.core.Response: ...
