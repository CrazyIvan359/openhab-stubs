import java.lang
import java.util
import org.openhab.core.thing
import org.openhab.core.thing.binding.firmware
import org.openhab.core.thing.firmware
import typing


class MagicFirmwareProvider(org.openhab.core.thing.firmware.FirmwareProvider):
    """
    Java class 'org.openhab.core.magic.binding.internal.firmware.MagicFirmwareProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.firmware.FirmwareProvider
    
      Constructors:
        * MagicFirmwareProvider()
    
    """
    def __init__(self): ...
    @typing.overload
    def getFirmware(self, thing: org.openhab.core.thing.Thing, version: java.lang.String) -> org.openhab.core.thing.binding.firmware.Firmware: ...
    @typing.overload
    def getFirmware(self, thing: org.openhab.core.thing.Thing, version: java.lang.String, locale: java.util.Locale) -> org.openhab.core.thing.binding.firmware.Firmware: ...
    @typing.overload
    def getFirmwares(self, thing: org.openhab.core.thing.Thing) -> java.util.Set[org.openhab.core.thing.binding.firmware.Firmware]: ...
    @typing.overload
    def getFirmwares(self, thing: org.openhab.core.thing.Thing, locale: java.util.Locale) -> java.util.Set[org.openhab.core.thing.binding.firmware.Firmware]: ...
