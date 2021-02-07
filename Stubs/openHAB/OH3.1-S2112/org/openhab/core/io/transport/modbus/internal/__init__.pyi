import java.io
import java.lang
import java.util.function
import net.wimpi.modbus
import net.wimpi.modbus.io
import net.wimpi.modbus.msg
import net.wimpi.modbus.net
import net.wimpi.modbus.procimg
import net.wimpi.modbus.util
import org.apache.commons.pool2
import org.apache.commons.pool2.impl
import org.openhab.core.io.transport.modbus
import org.openhab.core.io.transport.modbus.endpoint
import org.openhab.core.io.transport.modbus.exception
import typing


class AggregateStopWatch(java.lang.Object):
    """
    Java class 'org.openhab.core.io.transport.modbus.internal.AggregateStopWatch'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * AggregateStopWatch()
    
    """
    def __init__(self): ...
    def suspendAllRunning(self) -> None: ...
    def toString(self) -> java.lang.String: ...

class BasicPollTask(org.openhab.core.io.transport.modbus.PollTask):
    """
    Java class 'org.openhab.core.io.transport.modbus.internal.BasicPollTask'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.modbus.PollTask
    
      Constructors:
        * BasicPollTask(org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, org.openhab.core.io.transport.modbus.ModbusReadRequestBlueprint, org.openhab.core.io.transport.modbus.ModbusReadCallback, org.openhab.core.io.transport.modbus.ModbusFailureCallback)
    
    """
    def __init__(self, endpoint: org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, request: org.openhab.core.io.transport.modbus.ModbusReadRequestBlueprint, resultCallback: org.openhab.core.io.transport.modbus.ModbusReadCallback, failureCallback: typing.Union[org.openhab.core.io.transport.modbus.ModbusFailureCallback[org.openhab.core.io.transport.modbus.ModbusReadRequestBlueprint], typing.Callable[[], org.openhab.core.io.transport.modbus.ModbusReadRequestBlueprint]]): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getEndpoint(self) -> org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint: ...
    def getFailureCallback(self) -> org.openhab.core.io.transport.modbus.ModbusFailureCallback[org.openhab.core.io.transport.modbus.ModbusReadRequestBlueprint]: ...
    @typing.overload
    def getRequest(self) -> typing.Any: ...
    @typing.overload
    def getRequest(self) -> org.openhab.core.io.transport.modbus.ModbusReadRequestBlueprint: ...
    @typing.overload
    def getResultCallback(self) -> org.openhab.core.io.transport.modbus.ModbusReadCallback: ...
    @typing.overload
    def getResultCallback(self) -> org.openhab.core.io.transport.modbus.ModbusResultCallback: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class BasicWriteTask(org.openhab.core.io.transport.modbus.WriteTask):
    """
    Java class 'org.openhab.core.io.transport.modbus.internal.BasicWriteTask'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.modbus.WriteTask
    
      Constructors:
        * BasicWriteTask(org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, org.openhab.core.io.transport.modbus.ModbusWriteRequestBlueprint, org.openhab.core.io.transport.modbus.ModbusWriteCallback, org.openhab.core.io.transport.modbus.ModbusFailureCallback)
    
    """
    def __init__(self, endpoint: org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, request: org.openhab.core.io.transport.modbus.ModbusWriteRequestBlueprint, resultCallback: org.openhab.core.io.transport.modbus.ModbusWriteCallback, failureCallback: typing.Union[org.openhab.core.io.transport.modbus.ModbusFailureCallback[org.openhab.core.io.transport.modbus.ModbusWriteRequestBlueprint], typing.Callable[[], org.openhab.core.io.transport.modbus.ModbusWriteRequestBlueprint]]): ...
    def getEndpoint(self) -> org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint: ...
    def getFailureCallback(self) -> org.openhab.core.io.transport.modbus.ModbusFailureCallback[org.openhab.core.io.transport.modbus.ModbusWriteRequestBlueprint]: ...
    @typing.overload
    def getRequest(self) -> typing.Any: ...
    @typing.overload
    def getRequest(self) -> org.openhab.core.io.transport.modbus.ModbusWriteRequestBlueprint: ...
    @typing.overload
    def getResultCallback(self) -> org.openhab.core.io.transport.modbus.ModbusResultCallback: ...
    @typing.overload
    def getResultCallback(self) -> org.openhab.core.io.transport.modbus.ModbusWriteCallback: ...
    def toString(self) -> java.lang.String: ...

class ModbusConnectionPool(org.apache.commons.pool2.impl.GenericKeyedObjectPool[org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, net.wimpi.modbus.net.ModbusSlaveConnection]):
    """
    Java class 'org.openhab.core.io.transport.modbus.internal.ModbusConnectionPool'
    
        Extends:
            org.apache.commons.pool2.impl.GenericKeyedObjectPool
    
      Constructors:
        * ModbusConnectionPool(org.apache.commons.pool2.KeyedPooledObjectFactory)
    
    """
    def __init__(self, factory: org.apache.commons.pool2.KeyedPooledObjectFactory[org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, net.wimpi.modbus.net.ModbusSlaveConnection]): ...
    def setConfig(self, conf: org.apache.commons.pool2.impl.GenericKeyedObjectPoolConfig[net.wimpi.modbus.net.ModbusSlaveConnection]) -> None: ...

class ModbusLibraryWrapper(java.lang.Object):
    """
    Java class 'org.openhab.core.io.transport.modbus.internal.ModbusLibraryWrapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ModbusLibraryWrapper()
    
    """
    def __init__(self): ...
    @classmethod
    def convertBits(cls, bits: org.openhab.core.io.transport.modbus.BitArray) -> net.wimpi.modbus.util.BitVector: ...
    @classmethod
    def convertRegisters(cls, arr: org.openhab.core.io.transport.modbus.ModbusRegisterArray) -> typing.List[net.wimpi.modbus.procimg.Register]: ...
    @classmethod
    @typing.overload
    def createRequest(cls, message: org.openhab.core.io.transport.modbus.ModbusReadRequestBlueprint) -> net.wimpi.modbus.msg.ModbusRequest: ...
    @classmethod
    @typing.overload
    def createRequest(cls, message: org.openhab.core.io.transport.modbus.ModbusWriteRequestBlueprint) -> net.wimpi.modbus.msg.ModbusRequest: ...
    @classmethod
    def createTransactionForEndpoint(cls, endpoint: org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, connection: net.wimpi.modbus.net.ModbusSlaveConnection) -> net.wimpi.modbus.io.ModbusTransaction: ...
    @classmethod
    def getNumberOfItemsInResponse(cls, response: net.wimpi.modbus.msg.ModbusResponse, request: org.openhab.core.io.transport.modbus.ModbusReadRequestBlueprint) -> int: ...
    @classmethod
    def invokeCallbackWithResponse(cls, request: org.openhab.core.io.transport.modbus.ModbusReadRequestBlueprint, callback: org.openhab.core.io.transport.modbus.ModbusReadCallback, response: net.wimpi.modbus.msg.ModbusResponse) -> None: ...

class ModbusManagerImpl(org.openhab.core.io.transport.modbus.ModbusManager):
    """
    Java class 'org.openhab.core.io.transport.modbus.internal.ModbusManagerImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.modbus.ModbusManager
    
      Constructors:
        * ModbusManagerImpl()
    
      Attributes:
        DEFAULT_TCP_INTER_TRANSACTION_DELAY_MILLIS (long): final static field
        DEFAULT_SERIAL_INTER_TRANSACTION_DELAY_MILLIS (long): final static field
    
    """
    DEFAULT_TCP_INTER_TRANSACTION_DELAY_MILLIS: typing.ClassVar[int] = ...
    DEFAULT_SERIAL_INTER_TRANSACTION_DELAY_MILLIS: typing.ClassVar[int] = ...
    def __init__(self): ...
    def getEndpointPoolConfiguration(self, endpoint: org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint) -> org.openhab.core.io.transport.modbus.endpoint.EndpointPoolConfiguration: ...
    def newModbusCommunicationInterface(self, endpoint: org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, configuration: org.openhab.core.io.transport.modbus.endpoint.EndpointPoolConfiguration) -> org.openhab.core.io.transport.modbus.ModbusCommunicationInterface: ...

class ModbusPoolConfig(org.apache.commons.pool2.impl.GenericKeyedObjectPoolConfig[net.wimpi.modbus.net.ModbusSlaveConnection]):
    """
    Java class 'org.openhab.core.io.transport.modbus.internal.ModbusPoolConfig'
    
        Extends:
            org.apache.commons.pool2.impl.GenericKeyedObjectPoolConfig
    
      Constructors:
        * ModbusPoolConfig()
    
    """
    def __init__(self): ...
    def setEvictionPolicyClassName(self, evictionPolicyClassName: java.lang.String) -> None: ...

class ModbusResponseImpl(org.openhab.core.io.transport.modbus.ModbusResponse):
    """
    Java class 'org.openhab.core.io.transport.modbus.internal.ModbusResponseImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.modbus.ModbusResponse
    
      Constructors:
        * ModbusResponseImpl(net.wimpi.modbus.msg.ModbusMessage)
    
    """
    def __init__(self, response: net.wimpi.modbus.msg.ModbusMessage): ...
    def getFunctionCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class ModbusSlaveErrorResponseExceptionImpl(org.openhab.core.io.transport.modbus.exception.ModbusSlaveErrorResponseException):
    """
    Java class 'org.openhab.core.io.transport.modbus.internal.ModbusSlaveErrorResponseExceptionImpl'
    
        Extends:
            org.openhab.core.io.transport.modbus.exception.ModbusSlaveErrorResponseException
    
      Constructors:
        * ModbusSlaveErrorResponseExceptionImpl(net.wimpi.modbus.ModbusSlaveException)
    
    """
    def __init__(self, e: net.wimpi.modbus.ModbusSlaveException): ...
    def getExceptionCode(self) -> int: ...
    def getMessage(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ModbusSlaveIOExceptionImpl(org.openhab.core.io.transport.modbus.exception.ModbusSlaveIOException):
    """
    Java class 'org.openhab.core.io.transport.modbus.internal.ModbusSlaveIOExceptionImpl'
    
        Extends:
            org.openhab.core.io.transport.modbus.exception.ModbusSlaveIOException
    
      Constructors:
        * ModbusSlaveIOExceptionImpl(net.wimpi.modbus.ModbusIOException)
        * ModbusSlaveIOExceptionImpl(java.io.IOException)
    
    """
    @typing.overload
    def __init__(self, e: java.io.IOException): ...
    @typing.overload
    def __init__(self, e: net.wimpi.modbus.ModbusIOException): ...
    def getMessage(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

_SimpleStopWatch__SupplierWithPollTaskUnregisteredException__T = typing.TypeVar('_SimpleStopWatch__SupplierWithPollTaskUnregisteredException__T')  # <T>
class SimpleStopWatch(java.lang.Object):
    """
    Java class 'org.openhab.core.io.transport.modbus.internal.SimpleStopWatch'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SimpleStopWatch()
    
    """
    def __init__(self): ...
    def getTotalTimeMillis(self) -> int: ...
    def isRunning(self) -> bool: ...
    def resume(self) -> None: ...
    def suspend(self) -> None: ...
    _timeConsumer__T = typing.TypeVar('_timeConsumer__T')  # <T>
    def timeConsumer(self, consumer: typing.Union[java.util.function.Consumer[_timeConsumer__T], typing.Callable[[], _timeConsumer__T]], parameter: _timeConsumer__T) -> None: ...
    def timeRunnable(self, runnable: java.lang.Runnable) -> None: ...
    def timeRunnableWithModbusException(self, action: 'SimpleStopWatch.RunnableWithModbusException') -> None: ...
    _timeSupplier__R = typing.TypeVar('_timeSupplier__R')  # <R>
    def timeSupplier(self, supplier: typing.Union[java.util.function.Supplier[_timeSupplier__R], typing.Callable[[], _timeSupplier__R]]) -> _timeSupplier__R: ...
    _timeSupplierWithPollTaskUnregisteredException__R = typing.TypeVar('_timeSupplierWithPollTaskUnregisteredException__R')  # <R>
    def timeSupplierWithPollTaskUnregisteredException(self, supplier: typing.Union['SimpleStopWatch.SupplierWithPollTaskUnregisteredException'[_timeSupplierWithPollTaskUnregisteredException__R], typing.Callable[[], _timeSupplierWithPollTaskUnregisteredException__R]]) -> _timeSupplierWithPollTaskUnregisteredException__R: ...
    class RunnableWithModbusException(java.lang.Object):
        """
        Java class 'org.openhab.core.io.transport.modbus.internal.SimpleStopWatch$RunnableWithModbusException'
        
        """
        def run(self) -> None: ...
    class SupplierWithPollTaskUnregisteredException(java.lang.Object, typing.Generic[_SimpleStopWatch__SupplierWithPollTaskUnregisteredException__T]):
        """
        Java class 'org.openhab.core.io.transport.modbus.internal.SimpleStopWatch$SupplierWithPollTaskUnregisteredException'
        
        """
        def get(self) -> _SimpleStopWatch__SupplierWithPollTaskUnregisteredException__T: ...
