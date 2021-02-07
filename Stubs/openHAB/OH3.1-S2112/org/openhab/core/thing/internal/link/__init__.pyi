import java.lang
import java.net
import java.util
import org.openhab.core.config.core
import org.openhab.core.items
import org.openhab.core.thing
import org.openhab.core.thing.link
import org.openhab.core.thing.profiles
import typing


class ItemChannelLinkConfigDescriptionProvider(org.openhab.core.config.core.ConfigDescriptionProvider):
    """
    Java class 'org.openhab.core.thing.internal.link.ItemChannelLinkConfigDescriptionProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.core.ConfigDescriptionProvider
    
      Constructors:
        * ItemChannelLinkConfigDescriptionProvider(org.openhab.core.thing.profiles.ProfileTypeRegistry, org.openhab.core.thing.link.ItemChannelLinkRegistry, org.openhab.core.items.ItemRegistry, org.openhab.core.thing.ThingRegistry)
    
      Attributes:
        PARAM_PROFILE (java.lang.String): final static field
    
    """
    PARAM_PROFILE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, profileTypeRegistry: org.openhab.core.thing.profiles.ProfileTypeRegistry, itemChannelLinkRegistry: org.openhab.core.thing.link.ItemChannelLinkRegistry, itemRegistry: org.openhab.core.items.ItemRegistry, thingRegistry: org.openhab.core.thing.ThingRegistry): ...
    def getConfigDescription(self, uri: java.net.URI, locale: java.util.Locale) -> org.openhab.core.config.core.ConfigDescription: ...
    def getConfigDescriptions(self, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.config.core.ConfigDescription]: ...
