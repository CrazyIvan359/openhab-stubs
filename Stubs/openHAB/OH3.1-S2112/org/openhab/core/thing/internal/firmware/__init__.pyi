import java.io
import java.lang
import java.net
import java.util
import java.util.concurrent
import org.openhab.core.common
import org.openhab.core.config.core.validation
import org.openhab.core.events
import org.openhab.core.i18n
import org.openhab.core.thing
import org.openhab.core.thing.binding.firmware
import org.openhab.core.thing.firmware
import org.openhab.core.util
import typing


class FirmwareImpl(org.openhab.core.thing.binding.firmware.Firmware):
    """
    Java class 'org.openhab.core.thing.internal.firmware.FirmwareImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.binding.firmware.Firmware
    
      Constructors:
        * FirmwareImpl(org.openhab.core.thing.ThingTypeUID, java.lang.String, java.lang.String, boolean, java.lang.String, java.lang.String, java.lang.String, org.openhab.core.thing.binding.firmware.FirmwareRestriction, java.lang.String, java.net.URL, java.io.InputStream, java.lang.String, java.util.Map)
    
      Attributes:
        PROPERTY_REQUIRES_FACTORY_RESET (java.lang.String): final static field
    
    """
    PROPERTY_REQUIRES_FACTORY_RESET: typing.ClassVar[java.lang.String] = ...
    def __init__(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID, vendor: java.lang.String, model: java.lang.String, modelRestricted: bool, description: java.lang.String, version: java.lang.String, prerequisiteVersion: java.lang.String, firmwareRestriction: org.openhab.core.thing.binding.firmware.FirmwareRestriction, changelog: java.lang.String, onlineChangelog: java.net.URL, inputStream: java.io.InputStream, md5Hash: java.lang.String, properties: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]): ...
    @typing.overload
    def compareTo(self, object: typing.Any) -> int: ...
    @typing.overload
    def compareTo(self, firmware: org.openhab.core.thing.binding.firmware.Firmware) -> int: ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getBytes(self) -> typing.List[int]: ...
    def getChangelog(self) -> java.lang.String: ...
    def getDescription(self) -> java.lang.String: ...
    def getFirmwareRestriction(self) -> org.openhab.core.thing.binding.firmware.FirmwareRestriction: ...
    def getInputStream(self) -> java.io.InputStream: ...
    def getMd5Hash(self) -> java.lang.String: ...
    def getModel(self) -> java.lang.String: ...
    def getOnlineChangelog(self) -> java.net.URL: ...
    def getPrerequisiteVersion(self) -> java.lang.String: ...
    def getProperties(self) -> java.util.Map[java.lang.String, java.lang.String]: ...
    def getThingTypeUID(self) -> org.openhab.core.thing.ThingTypeUID: ...
    def getVendor(self) -> java.lang.String: ...
    def getVersion(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def isModelRestricted(self) -> bool: ...
    def isSuccessorVersion(self, firmwareVersion: java.lang.String) -> bool: ...
    def isSuitableFor(self, thing: org.openhab.core.thing.Thing) -> bool: ...
    def toString(self) -> java.lang.String: ...

class FirmwareRegistryImpl(org.openhab.core.thing.firmware.FirmwareRegistry):
    """
    Java class 'org.openhab.core.thing.internal.firmware.FirmwareRegistryImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.firmware.FirmwareRegistry
    
      Constructors:
        * FirmwareRegistryImpl(org.openhab.core.i18n.LocaleProvider)
    
    """
    def __init__(self, localeProvider: org.openhab.core.i18n.LocaleProvider): ...
    @typing.overload
    def getFirmware(self, thing: org.openhab.core.thing.Thing, firmwareVersion: java.lang.String) -> org.openhab.core.thing.binding.firmware.Firmware: ...
    @typing.overload
    def getFirmware(self, thing: org.openhab.core.thing.Thing, firmwareVersion: java.lang.String, locale: java.util.Locale) -> org.openhab.core.thing.binding.firmware.Firmware: ...
    @typing.overload
    def getFirmwares(self, thing: org.openhab.core.thing.Thing) -> java.util.Collection[org.openhab.core.thing.binding.firmware.Firmware]: ...
    @typing.overload
    def getFirmwares(self, thing: org.openhab.core.thing.Thing, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.thing.binding.firmware.Firmware]: ...
    @typing.overload
    def getLatestFirmware(self, thing: org.openhab.core.thing.Thing) -> org.openhab.core.thing.binding.firmware.Firmware: ...
    @typing.overload
    def getLatestFirmware(self, thing: org.openhab.core.thing.Thing, locale: java.util.Locale) -> org.openhab.core.thing.binding.firmware.Firmware: ...

class FirmwareUpdateServiceImpl(org.openhab.core.thing.firmware.FirmwareUpdateService, org.openhab.core.events.EventSubscriber):
    """
    Java class 'org.openhab.core.thing.internal.firmware.FirmwareUpdateServiceImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.firmware.FirmwareUpdateService,
            org.openhab.core.events.EventSubscriber
    
      Constructors:
        * FirmwareUpdateServiceImpl(org.openhab.core.util.BundleResolver, org.openhab.core.config.core.validation.ConfigDescriptionValidator, org.openhab.core.events.EventPublisher, org.openhab.core.thing.firmware.FirmwareRegistry, org.openhab.core.i18n.TranslationProvider, org.openhab.core.i18n.LocaleProvider, org.openhab.core.common.SafeCaller)
    
    """
    def __init__(self, bundleResolver: org.openhab.core.util.BundleResolver, configDescriptionValidator: org.openhab.core.config.core.validation.ConfigDescriptionValidator, eventPublisher: org.openhab.core.events.EventPublisher, firmwareRegistry: org.openhab.core.thing.firmware.FirmwareRegistry, i18nProvider: org.openhab.core.i18n.TranslationProvider, localeProvider: org.openhab.core.i18n.LocaleProvider, safeCaller: org.openhab.core.common.SafeCaller): ...
    def cancelFirmwareUpdate(self, thingUID: org.openhab.core.thing.ThingUID) -> None: ...
    def getEventFilter(self) -> org.openhab.core.events.EventFilter: ...
    def getFirmwareStatusInfo(self, thingUID: org.openhab.core.thing.ThingUID) -> org.openhab.core.thing.firmware.FirmwareStatusInfo: ...
    def getFirmwareStatusInfoJobDelay(self) -> int: ...
    def getFirmwareStatusInfoJobPeriod(self) -> int: ...
    def getFirmwareStatusInfoJobTimeUnit(self) -> java.util.concurrent.TimeUnit: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def receive(self, event: org.openhab.core.events.Event) -> None: ...
    def updateFirmware(self, thingUID: org.openhab.core.thing.ThingUID, firmwareVersion: java.lang.String, locale: java.util.Locale) -> None: ...
