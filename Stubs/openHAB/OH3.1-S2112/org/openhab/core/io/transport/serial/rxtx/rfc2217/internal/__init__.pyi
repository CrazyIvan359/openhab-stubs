import gnu.io.rfc2217
import java.lang
import java.net
import java.util.stream
import org.openhab.core.io.transport.serial


class RFC2217PortProvider(org.openhab.core.io.transport.serial.SerialPortProvider):
    """
    Java class 'org.openhab.core.io.transport.serial.rxtx.rfc2217.internal.RFC2217PortProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.serial.SerialPortProvider
    
      Constructors:
        * RFC2217PortProvider()
    
    """
    def __init__(self): ...
    def getAcceptedProtocols(self) -> java.util.stream.Stream[org.openhab.core.io.transport.serial.ProtocolType]: ...
    def getPortIdentifier(self, portName: java.net.URI) -> org.openhab.core.io.transport.serial.SerialPortIdentifier: ...
    def getSerialPortIdentifiers(self) -> java.util.stream.Stream[org.openhab.core.io.transport.serial.SerialPortIdentifier]: ...

class SerialPortIdentifierImpl(org.openhab.core.io.transport.serial.SerialPortIdentifier):
    """
    Java class 'org.openhab.core.io.transport.serial.rxtx.rfc2217.internal.SerialPortIdentifierImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.serial.SerialPortIdentifier
    
      Constructors:
        * SerialPortIdentifierImpl(gnu.io.rfc2217.TelnetSerialPort, java.net.URI)
    
    """
    def __init__(self, id: gnu.io.rfc2217.TelnetSerialPort, uri: java.net.URI): ...
    def getCurrentOwner(self) -> java.lang.String: ...
    def getName(self) -> java.lang.String: ...
    def isCurrentlyOwned(self) -> bool: ...
    def open(self, owner: java.lang.String, timeout: int) -> org.openhab.core.io.transport.serial.SerialPort: ...
