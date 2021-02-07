import java.lang
import java.util
import org.openhab.core.events
import org.openhab.core.io.console
import org.openhab.core.io.console.extensions
import org.openhab.core.items
import org.openhab.core.thing
import org.openhab.core.thing.firmware
import org.openhab.core.thing.i18n
import org.openhab.core.thing.link
import typing


class FirmwareUpdateConsoleCommandExtension(org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension):
    """
    Java class 'org.openhab.core.thing.internal.console.FirmwareUpdateConsoleCommandExtension'
    
        Extends:
            org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension
    
      Constructors:
        * FirmwareUpdateConsoleCommandExtension(org.openhab.core.thing.firmware.FirmwareUpdateService, org.openhab.core.thing.firmware.FirmwareRegistry, org.openhab.core.thing.ThingRegistry)
    
    """
    def __init__(self, firmwareUpdateService: org.openhab.core.thing.firmware.FirmwareUpdateService, firmwareRegistry: org.openhab.core.thing.firmware.FirmwareRegistry, thingRegistry: org.openhab.core.thing.ThingRegistry): ...
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...

class LinkConsoleCommandExtension(org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension):
    """
    Java class 'org.openhab.core.thing.internal.console.LinkConsoleCommandExtension'
    
        Extends:
            org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension
    
      Constructors:
        * LinkConsoleCommandExtension(org.openhab.core.thing.ThingRegistry, org.openhab.core.items.ItemRegistry, org.openhab.core.thing.link.ItemChannelLinkRegistry)
    
    """
    def __init__(self, thingRegistry: org.openhab.core.thing.ThingRegistry, itemRegistry: org.openhab.core.items.ItemRegistry, itemChannelLinkRegistry: org.openhab.core.thing.link.ItemChannelLinkRegistry): ...
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...

class ThingConsoleCommandExtension(org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension):
    """
    Java class 'org.openhab.core.thing.internal.console.ThingConsoleCommandExtension'
    
        Extends:
            org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension
    
      Constructors:
        * ThingConsoleCommandExtension(org.openhab.core.thing.ManagedThingProvider, org.openhab.core.thing.ThingRegistry, org.openhab.core.thing.i18n.ThingStatusInfoI18nLocalizationService, org.openhab.core.events.EventPublisher, org.openhab.core.thing.ThingManager)
    
    """
    def __init__(self, managedThingProvider: org.openhab.core.thing.ManagedThingProvider, thingRegistry: org.openhab.core.thing.ThingRegistry, thingStatusInfoI18nLocalizationService: org.openhab.core.thing.i18n.ThingStatusInfoI18nLocalizationService, eventPublisher: org.openhab.core.events.EventPublisher, thingManager: org.openhab.core.thing.ThingManager): ...
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...
