import java.lang
import javax.ws.rs.core
import org.openhab.core.io.rest
import org.openhab.core.thing.profiles
import org.openhab.core.thing.type
import typing


class ProfileTypeResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.core.internal.profile.ProfileTypeResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * ProfileTypeResource(org.openhab.core.thing.type.ChannelTypeRegistry, org.openhab.core.io.rest.LocaleService, org.openhab.core.thing.profiles.ProfileTypeRegistry)
    
      Attributes:
        PATH_PROFILE_TYPES (java.lang.String): final static field
    
    """
    PATH_PROFILE_TYPES: typing.ClassVar[java.lang.String] = ...
    def __init__(self, channelTypeRegistry: org.openhab.core.thing.type.ChannelTypeRegistry, localeService: org.openhab.core.io.rest.LocaleService, profileTypeRegistry: org.openhab.core.thing.profiles.ProfileTypeRegistry): ...
    def getAll(self, language: java.lang.String, channelTypeUID: java.lang.String, itemType: java.lang.String) -> javax.ws.rs.core.Response: ...
