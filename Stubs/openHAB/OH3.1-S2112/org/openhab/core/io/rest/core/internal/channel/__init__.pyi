import java.lang
import javax.ws.rs.core
import org.openhab.core.config.core
import org.openhab.core.io.rest
import org.openhab.core.thing.profiles
import org.openhab.core.thing.type
import typing


class ChannelTypeResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.core.internal.channel.ChannelTypeResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * ChannelTypeResource(org.openhab.core.thing.type.ChannelTypeRegistry, org.openhab.core.config.core.ConfigDescriptionRegistry, org.openhab.core.io.rest.LocaleService, org.openhab.core.thing.profiles.ProfileTypeRegistry)
    
      Attributes:
        PATH_CHANNEL_TYPES (java.lang.String): final static field
    
    """
    PATH_CHANNEL_TYPES: typing.ClassVar[java.lang.String] = ...
    def __init__(self, channelTypeRegistry: org.openhab.core.thing.type.ChannelTypeRegistry, configDescriptionRegistry: org.openhab.core.config.core.ConfigDescriptionRegistry, localeService: org.openhab.core.io.rest.LocaleService, profileTypeRegistry: org.openhab.core.thing.profiles.ProfileTypeRegistry): ...
    def getAll(self, language: java.lang.String, prefixes: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getByUID(self, channelTypeUID: java.lang.String, language: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getLinkableItemTypes(self, channelTypeUID: java.lang.String) -> javax.ws.rs.core.Response: ...
