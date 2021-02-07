import java.util
import org.openhab.core.config.discovery
import org.openhab.core.config.discovery.usbserial
import org.openhab.core.thing
import typing


class UsbSerialDiscoveryService(org.openhab.core.config.discovery.AbstractDiscoveryService, org.openhab.core.config.discovery.usbserial.UsbSerialDiscoveryListener):
    """
    Java class 'org.openhab.core.config.discovery.usbserial.internal.UsbSerialDiscoveryService'
    
        Extends:
            org.openhab.core.config.discovery.AbstractDiscoveryService
    
        Interfaces:
            org.openhab.core.config.discovery.usbserial.UsbSerialDiscovery
            Listener
    
      Constructors:
        * UsbSerialDiscoveryService()
    
    """
    def __init__(self): ...
    @typing.overload
    def getSupportedThingTypes(self) -> java.util.Collection: ...
    @typing.overload
    def getSupportedThingTypes(self) -> java.util.Set[org.openhab.core.thing.ThingTypeUID]: ...
    def usbSerialDeviceDiscovered(self, usbSerialDeviceInformation: org.openhab.core.config.discovery.usbserial.UsbSerialDeviceInformation) -> None: ...
    def usbSerialDeviceRemoved(self, usbSerialDeviceInformation: org.openhab.core.config.discovery.usbserial.UsbSerialDeviceInformation) -> None: ...
