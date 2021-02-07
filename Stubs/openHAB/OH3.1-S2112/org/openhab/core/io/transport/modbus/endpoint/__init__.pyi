import java.lang
import net.wimpi.modbus.util
import typing


class EndpointPoolConfiguration(java.lang.Object):
    """
    Java class 'org.openhab.core.io.transport.modbus.endpoint.EndpointPoolConfiguration'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * EndpointPoolConfiguration()
    
    """
    def __init__(self): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getConnectMaxTries(self) -> int: ...
    def getConnectTimeoutMillis(self) -> int: ...
    def getInterConnectDelayMillis(self) -> int: ...
    def getInterTransactionDelayMillis(self) -> int: ...
    def getReconnectAfterMillis(self) -> int: ...
    def hashCode(self) -> int: ...
    def setConnectMaxTries(self, connectMaxTries: int) -> None: ...
    def setConnectTimeoutMillis(self, connectTimeoutMillis: int) -> None: ...
    def setInterConnectDelayMillis(self, interConnectDelayMillis: int) -> None: ...
    def setInterTransactionDelayMillis(self, interTransactionDelayMillis: int) -> None: ...
    def setReconnectAfterMillis(self, reconnectAfterMillis: int) -> None: ...
    def toString(self) -> java.lang.String: ...

class ModbusSlaveEndpoint(java.lang.Object):
    """
    @NonNullByDefault public interface ModbusSlaveEndpoint
    
        ModbusSlaveEndpoint contains minimal connection information to establish connection to the slave. End point equals and
        hashCode methods should be implemented such that they can be used to differentiate different physical slaves. Read and
        write transactions are processed one at a time if they are associated with the same endpoint (in the sense of equals and
        hashCode). Note that, endpoint class might not include all configuration that might be necessary to actually communicate
        with the slave, just the data that is required to establish the connection.
    
    
    """
    _accept__R = typing.TypeVar('_accept__R')  # <R>
    def accept(self, visitor: 'ModbusSlaveEndpointVisitor'[_accept__R]) -> _accept__R: ...

_ModbusSlaveEndpointVisitor__R = typing.TypeVar('_ModbusSlaveEndpointVisitor__R')  # <R>
class ModbusSlaveEndpointVisitor(java.lang.Object, typing.Generic[_ModbusSlaveEndpointVisitor__R]):
    """
    @NonNullByDefault public interface ModbusSlaveEndpointVisitor<R>
    
        Visitor for ModbusSlaveEndpoint
    
    
    """
    @typing.overload
    def visit(self, endpoint: 'ModbusSerialSlaveEndpoint') -> _ModbusSlaveEndpointVisitor__R: ...
    @typing.overload
    def visit(self, endpoint: 'ModbusTCPSlaveEndpoint') -> _ModbusSlaveEndpointVisitor__R: ...
    @typing.overload
    def visit(self, endpoint: 'ModbusUDPSlaveEndpoint') -> _ModbusSlaveEndpointVisitor__R: ...

class ModbusIPSlaveEndpoint(ModbusSlaveEndpoint):
    """
    Java class 'org.openhab.core.io.transport.modbus.endpoint.ModbusIPSlaveEndpoint'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpo
            int
    
      Constructors:
        * ModbusIPSlaveEndpoint(java.lang.String, int)
    
    """
    def __init__(self, address: java.lang.String, port: int): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getAddress(self) -> java.lang.String: ...
    def getPort(self) -> int: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class ModbusSerialSlaveEndpoint(ModbusSlaveEndpoint):
    """
    Java class 'org.openhab.core.io.transport.modbus.endpoint.ModbusSerialSlaveEndpoint'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpo
            int
    
      Constructors:
        * ModbusSerialSlaveEndpoint(java.lang.String, int, java.lang.String, java.lang.String, int, java.lang.String, java.lang.String, java.lang.String, boolean, int)
        * ModbusSerialSlaveEndpoint(java.lang.String, int, int, int, int, int, int, java.lang.String, boolean, int)
    
    """
    @typing.overload
    def __init__(self, portName: java.lang.String, baudRate: int, flowControlIn: int, flowControlOut: int, databits: int, stopbits: int, parity: int, encoding: java.lang.String, echo: bool, receiveTimeoutMillis: int): ...
    @typing.overload
    def __init__(self, portName: java.lang.String, baudRate: int, flowControlIn: java.lang.String, flowControlOut: java.lang.String, databits: int, stopbits: java.lang.String, parity: java.lang.String, encoding: java.lang.String, echo: bool, receiveTimeoutMillis: int): ...
    _accept__R = typing.TypeVar('_accept__R')  # <R>
    def accept(self, factory: ModbusSlaveEndpointVisitor[_accept__R]) -> _accept__R: ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getPortName(self) -> java.lang.String: ...
    def getSerialParameters(self) -> net.wimpi.modbus.util.SerialParameters: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class ModbusTCPSlaveEndpoint(ModbusIPSlaveEndpoint):
    """
    Java class 'org.openhab.core.io.transport.modbus.endpoint.ModbusTCPSlaveEndpoint'
    
        Extends:
            org.openhab.core.io.transport.modbus.endpoint.ModbusIPSlaveEndpoint
    
      Constructors:
        * ModbusTCPSlaveEndpoint(java.lang.String, int, boolean)
    
    """
    def __init__(self, address: java.lang.String, port: int, rtuEncoded: bool): ...
    _accept__R = typing.TypeVar('_accept__R')  # <R>
    def accept(self, factory: ModbusSlaveEndpointVisitor[_accept__R]) -> _accept__R: ...
    def getRtuEncoded(self) -> bool: ...

class ModbusUDPSlaveEndpoint(ModbusIPSlaveEndpoint):
    """
    Java class 'org.openhab.core.io.transport.modbus.endpoint.ModbusUDPSlaveEndpoint'
    
        Extends:
            org.openhab.core.io.transport.modbus.endpoint.ModbusIPSlaveEndpoint
    
      Constructors:
        * ModbusUDPSlaveEndpoint(java.lang.String, int)
    
    """
    def __init__(self, address: java.lang.String, port: int): ...
    _accept__R = typing.TypeVar('_accept__R')  # <R>
    def accept(self, factory: ModbusSlaveEndpointVisitor[_accept__R]) -> _accept__R: ...
