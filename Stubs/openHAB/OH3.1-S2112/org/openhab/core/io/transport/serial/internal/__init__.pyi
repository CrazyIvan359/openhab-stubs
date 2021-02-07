import gnu.io
import java.io
import java.lang
import java.net
import java.util
import java.util.stream
import javax.comm
import org.openhab.core.io.transport.serial


class JavaCommPortProvider(org.openhab.core.io.transport.serial.SerialPortProvider):
    """
    Java class 'org.openhab.core.io.transport.serial.internal.JavaCommPortProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.serial.SerialPortProvider
    
      Constructors:
        * JavaCommPortProvider()
    
    """
    def __init__(self): ...
    def getAcceptedProtocols(self) -> java.util.stream.Stream[org.openhab.core.io.transport.serial.ProtocolType]: ...
    def getPortIdentifier(self, port: java.net.URI) -> org.openhab.core.io.transport.serial.SerialPortIdentifier: ...
    def getSerialPortIdentifiers(self) -> java.util.stream.Stream[org.openhab.core.io.transport.serial.SerialPortIdentifier]: ...

class RxTxPortProvider(org.openhab.core.io.transport.serial.SerialPortProvider):
    """
    Java class 'org.openhab.core.io.transport.serial.internal.RxTxPortProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.serial.SerialPortProvider
    
      Constructors:
        * RxTxPortProvider()
    
    """
    def __init__(self): ...
    def getAcceptedProtocols(self) -> java.util.stream.Stream[org.openhab.core.io.transport.serial.ProtocolType]: ...
    def getPortIdentifier(self, port: java.net.URI) -> org.openhab.core.io.transport.serial.SerialPortIdentifier: ...
    def getSerialPortIdentifiers(self) -> java.util.stream.Stream[org.openhab.core.io.transport.serial.SerialPortIdentifier]: ...

class SerialPortEventImpl(org.openhab.core.io.transport.serial.SerialPortEvent):
    """
    Java class 'org.openhab.core.io.transport.serial.internal.SerialPortEventImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.serial.SerialPortEvent
    
      Constructors:
        * SerialPortEventImpl(gnu.io.SerialPortEvent)
    
    """
    def __init__(self, event: gnu.io.SerialPortEvent): ...
    def getEventType(self) -> int: ...
    def getNewValue(self) -> bool: ...

class SerialPortIdentifierImpl(org.openhab.core.io.transport.serial.SerialPortIdentifier):
    """
    Java class 'org.openhab.core.io.transport.serial.internal.SerialPortIdentifierImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.serial.SerialPortIdentifier
    
      Constructors:
        * SerialPortIdentifierImpl(gnu.io.CommPortIdentifier)
    
    """
    def __init__(self, id: gnu.io.CommPortIdentifier): ...
    def getCurrentOwner(self) -> java.lang.String: ...
    def getName(self) -> java.lang.String: ...
    def isCurrentlyOwned(self) -> bool: ...
    def open(self, owner: java.lang.String, timeout: int) -> org.openhab.core.io.transport.serial.SerialPort: ...

class SerialPortImpl(org.openhab.core.io.transport.serial.SerialPort):
    """
    Java class 'org.openhab.core.io.transport.serial.internal.SerialPortImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.serial.SerialPort
    
      Constructors:
        * SerialPortImpl(javax.comm.SerialPort)
    
    """
    def __init__(self, sp: javax.comm.SerialPort): ...
    def addEventListener(self, listener: org.openhab.core.io.transport.serial.SerialPortEventListener) -> None: ...
    def close(self) -> None: ...
    def disableReceiveTimeout(self) -> None: ...
    def enableReceiveThreshold(self, i: int) -> None: ...
    def enableReceiveTimeout(self, timeout: int) -> None: ...
    def getInputStream(self) -> java.io.InputStream: ...
    def getName(self) -> java.lang.String: ...
    def getOutputStream(self) -> java.io.OutputStream: ...
    def notifyOnBreakInterrupt(self, enable: bool) -> None: ...
    def notifyOnDataAvailable(self, enable: bool) -> None: ...
    def notifyOnFramingError(self, enable: bool) -> None: ...
    def notifyOnOverrunError(self, enable: bool) -> None: ...
    def notifyOnParityError(self, enable: bool) -> None: ...
    def removeEventListener(self) -> None: ...
    def setFlowControlMode(self, flowcontrolRtsctsOut: int) -> None: ...
    def setRTS(self, enable: bool) -> None: ...
    def setSerialPortParams(self, baudrate: int, dataBits: int, stopBits: int, parity: int) -> None: ...

class SerialPortManagerImpl(org.openhab.core.io.transport.serial.SerialPortManager):
    """
    Java class 'org.openhab.core.io.transport.serial.internal.SerialPortManagerImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.serial.SerialPortManager
    
      Constructors:
        * SerialPortManagerImpl(org.openhab.core.io.transport.serial.internal.SerialPortRegistry)
    
    """
    def __init__(self, registry: 'SerialPortRegistry'): ...
    def getIdentifier(self, name: java.lang.String) -> org.openhab.core.io.transport.serial.SerialPortIdentifier: ...
    def getIdentifiers(self) -> java.util.stream.Stream[org.openhab.core.io.transport.serial.SerialPortIdentifier]: ...

class SerialPortRegistry(java.lang.Object):
    """
    Java class 'org.openhab.core.io.transport.serial.internal.SerialPortRegistry'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SerialPortRegistry()
    
    """
    def __init__(self): ...
    def getPortCreators(self) -> java.util.Collection[org.openhab.core.io.transport.serial.SerialPortProvider]: ...
    def getPortProvidersForPortName(self, portName: java.net.URI) -> java.util.Collection[org.openhab.core.io.transport.serial.SerialPortProvider]: ...

class SerialPortUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.io.transport.serial.internal.SerialPortUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SerialPortUtil()
    
    """
    def __init__(self): ...
    @classmethod
    def getPortIdentifier(cls, port: java.lang.String) -> gnu.io.CommPortIdentifier: ...
    @classmethod
    def getPortIdentifiersUsingProperty(cls) -> java.util.stream.Stream[gnu.io.CommPortIdentifier]: ...
    @classmethod
    def getPortIdentifiersUsingScan(cls) -> java.util.stream.Stream[gnu.io.CommPortIdentifier]: ...
