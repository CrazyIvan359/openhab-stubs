import java.lang
import java.util
import org.openhab.core.config.discovery.usbserial
import typing


class DeltaUsbSerialScanner(java.lang.Object):
    """
    Java class 'org.openhab.core.config.discovery.usbserial.linuxsysfs.internal.DeltaUsbSerialScanner'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * DeltaUsbSerialScanner(org.openhab.core.config.discovery.usbserial.linuxsysfs.internal.UsbSerialScanner)
    
    """
    def __init__(self, usbSerialScanner: 'UsbSerialScanner'): ...
    def canPerformScans(self) -> bool: ...
    def scan(self) -> 'DeltaUsbSerialScanner.Delta'[org.openhab.core.config.discovery.usbserial.UsbSerialDeviceInformation]: ...
    class Delta: ...

class PollingUsbSerialScanner(org.openhab.core.config.discovery.usbserial.UsbSerialDiscovery):
    """
    Java class 'org.openhab.core.config.discovery.usbserial.linuxsysfs.internal.PollingUsbSerialScanner'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.discovery.usbserial.UsbSerialDiscovery
    
      Constructors:
        * PollingUsbSerialScanner(java.util.Map, org.openhab.core.config.discovery.usbserial.linuxsysfs.internal.UsbSerialScanner)
    
      Attributes:
        PAUSE_BETWEEN_SCANS_IN_SECONDS_ATTRIBUTE (java.lang.String): final static field
    
    """
    PAUSE_BETWEEN_SCANS_IN_SECONDS_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, config: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]], usbSerialScanner: 'UsbSerialScanner'): ...
    def doSingleScan(self) -> None: ...
    def registerDiscoveryListener(self, listener: org.openhab.core.config.discovery.usbserial.UsbSerialDiscoveryListener) -> None: ...
    def startBackgroundScanning(self) -> None: ...
    def stopBackgroundScanning(self) -> None: ...
    def unregisterDiscoveryListener(self, listener: org.openhab.core.config.discovery.usbserial.UsbSerialDiscoveryListener) -> None: ...

class UsbSerialScanner(java.lang.Object):
    """
    Java class 'org.openhab.core.config.discovery.usbserial.linuxsysfs.internal.UsbSerialScanner'
    
    """
    def canPerformScans(self) -> bool: ...
    def scan(self) -> java.util.Set[org.openhab.core.config.discovery.usbserial.UsbSerialDeviceInformation]: ...

class SysfsUsbSerialScanner(UsbSerialScanner):
    """
    Java class 'org.openhab.core.config.discovery.usbserial.linuxsysfs.internal.SysfsUsbSerialScanner'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.discovery.usbserial.linuxsysfs.interna
            l.UsbSerialScanner
    
      Constructors:
        * SysfsUsbSerialScanner()
    
      Attributes:
        SYSFS_TTY_DEVICES_DIRECTORY_ATTRIBUTE (java.lang.String): final static field
        DEV_DIRECTORY_ATTRIBUTE (java.lang.String): final static field
    
    """
    SYSFS_TTY_DEVICES_DIRECTORY_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    DEV_DIRECTORY_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    def canPerformScans(self) -> bool: ...
    def scan(self) -> java.util.Set[org.openhab.core.config.discovery.usbserial.UsbSerialDeviceInformation]: ...
