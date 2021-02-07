import java.lang
import java.util
import javax.ws.rs.core
import org.openhab.core.config.core
import org.openhab.core.config.core.status
import org.openhab.core.io.rest
import org.openhab.core.items
import org.openhab.core.thing
import org.openhab.core.thing.dto
import org.openhab.core.thing.firmware
import org.openhab.core.thing.i18n
import org.openhab.core.thing.link
import org.openhab.core.thing.type
import typing


class ThingResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.core.internal.thing.ThingResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * ThingResource(org.openhab.core.io.rest.DTOMapper, org.openhab.core.thing.type.ChannelTypeRegistry, org.openhab.core.config.core.status.ConfigStatusService, org.openhab.core.config.core.ConfigDescriptionRegistry, org.openhab.core.thing.firmware.FirmwareRegistry, org.openhab.core.thing.firmware.FirmwareUpdateService, org.openhab.core.thing.link.ItemChannelLinkRegistry, org.openhab.core.items.ItemFactory, org.openhab.core.items.ItemRegistry, org.openhab.core.io.rest.LocaleService, org.openhab.core.thing.link.ManagedItemChannelLinkProvider, org.openhab.core.items.ManagedItemProvider, org.openhab.core.thing.ManagedThingProvider, org.openhab.core.thing.ThingManager, org.openhab.core.thing.ThingRegistry, org.openhab.core.thing.i18n.ThingStatusInfoI18nLocalizationService, org.openhab.core.thing.type.ThingTypeRegistry)
    
      Attributes:
        PATH_THINGS (java.lang.String): final static field
    
    """
    PATH_THINGS: typing.ClassVar[java.lang.String] = ...
    def __init__(self, dtoMapper: org.openhab.core.io.rest.DTOMapper, channelTypeRegistry: org.openhab.core.thing.type.ChannelTypeRegistry, configStatusService: org.openhab.core.config.core.status.ConfigStatusService, configDescRegistry: org.openhab.core.config.core.ConfigDescriptionRegistry, firmwareRegistry: org.openhab.core.thing.firmware.FirmwareRegistry, firmwareUpdateService: org.openhab.core.thing.firmware.FirmwareUpdateService, itemChannelLinkRegistry: org.openhab.core.thing.link.ItemChannelLinkRegistry, itemFactory: org.openhab.core.items.ItemFactory, itemRegistry: org.openhab.core.items.ItemRegistry, localeService: org.openhab.core.io.rest.LocaleService, managedItemChannelLinkProvider: org.openhab.core.thing.link.ManagedItemChannelLinkProvider, managedItemProvider: org.openhab.core.items.ManagedItemProvider, managedThingProvider: org.openhab.core.thing.ManagedThingProvider, thingManager: org.openhab.core.thing.ThingManager, thingRegistry: org.openhab.core.thing.ThingRegistry, thingStatusInfoI18nLocalizationService: org.openhab.core.thing.i18n.ThingStatusInfoI18nLocalizationService, thingTypeRegistry: org.openhab.core.thing.type.ThingTypeRegistry): ...
    def create(self, language: java.lang.String, thingBean: org.openhab.core.thing.dto.ThingDTO) -> javax.ws.rs.core.Response: ...
    def getAll(self, language: java.lang.String, summary: bool) -> javax.ws.rs.core.Response: ...
    def getByUID(self, language: java.lang.String, thingUID: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getConfigStatus(self, language: java.lang.String, thingUID: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getFirmwareStatus(self, language: java.lang.String, thingUID: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getFirmwares(self, thingUID: java.lang.String, language: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getStatus(self, language: java.lang.String, thingUID: java.lang.String) -> javax.ws.rs.core.Response: ...
    def remove(self, language: java.lang.String, thingUID: java.lang.String, force: bool) -> javax.ws.rs.core.Response: ...
    def setEnabled(self, language: java.lang.String, thingUID: java.lang.String, enabled: java.lang.String) -> javax.ws.rs.core.Response: ...
    def update(self, language: java.lang.String, thingUID: java.lang.String, thingBean: org.openhab.core.thing.dto.ThingDTO) -> javax.ws.rs.core.Response: ...
    @typing.overload
    def updateConfiguration(self, language: java.lang.String, thingUID: java.lang.String, configurationParameters: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> javax.ws.rs.core.Response: ...
    @classmethod
    @typing.overload
    def updateConfiguration(cls, thing: org.openhab.core.thing.Thing, configuration: org.openhab.core.config.core.Configuration) -> None: ...
    def updateFirmware(self, language: java.lang.String, thingUID: java.lang.String, firmwareVersion: java.lang.String) -> javax.ws.rs.core.Response: ...

class ThingTypeResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.core.internal.thing.ThingTypeResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * ThingTypeResource(org.openhab.core.thing.type.ChannelTypeRegistry, org.openhab.core.thing.type.ChannelGroupTypeRegistry, org.openhab.core.config.core.ConfigDescriptionRegistry, org.openhab.core.io.rest.LocaleService, org.openhab.core.thing.type.ThingTypeRegistry)
    
      Attributes:
        PATH_THING_TYPES (java.lang.String): final static field
    
    """
    PATH_THING_TYPES: typing.ClassVar[java.lang.String] = ...
    def __init__(self, channelTypeRegistry: org.openhab.core.thing.type.ChannelTypeRegistry, channelGroupTypeRegistry: org.openhab.core.thing.type.ChannelGroupTypeRegistry, configDescriptionRegistry: org.openhab.core.config.core.ConfigDescriptionRegistry, localeService: org.openhab.core.io.rest.LocaleService, thingTypeRegistry: org.openhab.core.thing.type.ThingTypeRegistry): ...
    def getAll(self, language: java.lang.String, bindingId: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getByUID(self, thingTypeUID: java.lang.String, language: java.lang.String) -> javax.ws.rs.core.Response: ...
