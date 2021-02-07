import java.lang
import org.openhab.core.io.transport.modbus.endpoint
import typing


class ModbusTransportException(java.lang.Exception):
    """
    Java class 'org.openhab.core.io.transport.modbus.exception.ModbusTransportException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * ModbusTransportException()
    
    """
    def __init__(self): ...

class ModbusConnectionException(ModbusTransportException):
    """
    Java class 'org.openhab.core.io.transport.modbus.exception.ModbusConnectionException'
    
        Extends:
            org.openhab.core.io.transport.modbus.exception.ModbusTransportException
    
      Constructors:
        * ModbusConnectionException(org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint)
    
    """
    def __init__(self, endpoint: org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint): ...
    def getEndpoint(self) -> org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint: ...
    def getMessage(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ModbusSlaveErrorResponseException(ModbusTransportException):
    """
    Java class 'org.openhab.core.io.transport.modbus.exception.ModbusSlaveErrorResponseException'
    
        Extends:
            org.openhab.core.io.transport.modbus.exception.ModbusTransportException
    
      Constructors:
        * ModbusSlaveErrorResponseException()
    
      Attributes:
        ILLEGAL_FUNCTION (int): final static field
        ILLEGAL_DATA_ACCESS (int): final static field
        ILLEGAL_DATA_VALUE (int): final static field
        SLAVE_DEVICE_FAILURE (int): final static field
        ACKNOWLEDGE (int): final static field
        SLAVE_DEVICE_BUSY (int): final static field
        NEGATIVE_ACKNOWLEDGE (int): final static field
        MEMORY_PARITY_ERROR (int): final static field
        GATEWAY_PATH_UNVAVAILABLE (int): final static field
        GATEWAY_TARGET_DEVICE_FAILED_TO_RESPOND (int): final static field
    
    """
    ILLEGAL_FUNCTION: typing.ClassVar[int] = ...
    ILLEGAL_DATA_ACCESS: typing.ClassVar[int] = ...
    ILLEGAL_DATA_VALUE: typing.ClassVar[int] = ...
    SLAVE_DEVICE_FAILURE: typing.ClassVar[int] = ...
    ACKNOWLEDGE: typing.ClassVar[int] = ...
    SLAVE_DEVICE_BUSY: typing.ClassVar[int] = ...
    NEGATIVE_ACKNOWLEDGE: typing.ClassVar[int] = ...
    MEMORY_PARITY_ERROR: typing.ClassVar[int] = ...
    GATEWAY_PATH_UNVAVAILABLE: typing.ClassVar[int] = ...
    GATEWAY_TARGET_DEVICE_FAILED_TO_RESPOND: typing.ClassVar[int] = ...
    def __init__(self): ...
    def getExceptionCode(self) -> int: ...

class ModbusSlaveIOException(ModbusTransportException):
    """
    Java class 'org.openhab.core.io.transport.modbus.exception.ModbusSlaveIOException'
    
        Extends:
            org.openhab.core.io.transport.modbus.exception.ModbusTransportException
    
      Constructors:
        * ModbusSlaveIOException()
    
    """
    def __init__(self): ...

class ModbusUnexpectedResponseFunctionCodeException(ModbusTransportException):
    """
    Java class 'org.openhab.core.io.transport.modbus.exception.ModbusUnexpectedResponseFunctionCodeException'
    
        Extends:
            org.openhab.core.io.transport.modbus.exception.ModbusTransportException
    
      Constructors:
        * ModbusUnexpectedResponseFunctionCodeException(int, int)
    
    """
    def __init__(self, requestFunctionCode: int, responseFunctionCode: int): ...
    def getMessage(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ModbusUnexpectedResponseSizeException(ModbusTransportException):
    """
    Java class 'org.openhab.core.io.transport.modbus.exception.ModbusUnexpectedResponseSizeException'
    
        Extends:
            org.openhab.core.io.transport.modbus.exception.ModbusTransportException
    
      Constructors:
        * ModbusUnexpectedResponseSizeException(int, int)
    
    """
    def __init__(self, requestSize: int, responseSize: int): ...
    def getMessage(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ModbusUnexpectedTransactionIdException(ModbusTransportException):
    """
    Java class 'org.openhab.core.io.transport.modbus.exception.ModbusUnexpectedTransactionIdException'
    
        Extends:
            org.openhab.core.io.transport.modbus.exception.ModbusTransportException
    
      Constructors:
        * ModbusUnexpectedTransactionIdException(int, int)
    
    """
    def __init__(self, requestId: int, responseId: int): ...
    def getMessage(self) -> java.lang.String: ...
    def getRequestId(self) -> int: ...
    def getResponseId(self) -> int: ...
    def toString(self) -> java.lang.String: ...
