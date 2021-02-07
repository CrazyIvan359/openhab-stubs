import java.util.function
import net.wimpi.modbus.net
import org.apache.commons.pool2
import org.apache.commons.pool2.impl
import org.openhab.core.io.transport.modbus.endpoint
import typing


class ModbusSlaveConnectionEvictionPolicy(org.apache.commons.pool2.impl.EvictionPolicy[net.wimpi.modbus.net.ModbusSlaveConnection]):
    """
    Java class 'org.openhab.core.io.transport.modbus.internal.pooling.ModbusSlaveConnectionEvictionPolicy'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.apache.commons.pool2.impl.EvictionPolicy
    
      Constructors:
        * ModbusSlaveConnectionEvictionPolicy()
    
    """
    def __init__(self): ...
    def evict(self, config: org.apache.commons.pool2.impl.EvictionConfig, underTest: org.apache.commons.pool2.PooledObject[net.wimpi.modbus.net.ModbusSlaveConnection], idleCount: int) -> bool: ...

class ModbusSlaveConnectionFactory(org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpointVisitor[net.wimpi.modbus.net.ModbusSlaveConnection]):
    """
    Java class 'org.openhab.core.io.transport.modbus.internal.pooling.ModbusSlaveConnectionFactory'
    
        Interfaces:
            org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpo
            intVisitor
    
    """

class ModbusSlaveConnectionFactoryImpl(org.apache.commons.pool2.BaseKeyedPooledObjectFactory[org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, net.wimpi.modbus.net.ModbusSlaveConnection]):
    """
    Java class 'org.openhab.core.io.transport.modbus.internal.pooling.ModbusSlaveConnectionFactoryImpl'
    
        Extends:
            org.apache.commons.pool2.BaseKeyedPooledObjectFactory
    
      Constructors:
        * ModbusSlaveConnectionFactoryImpl()
    
    """
    def __init__(self): ...
    @typing.overload
    def activateObject(self, object: typing.Any, pooledObject: org.apache.commons.pool2.PooledObject) -> None: ...
    @typing.overload
    def activateObject(self, endpoint: org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, obj: org.apache.commons.pool2.PooledObject[net.wimpi.modbus.net.ModbusSlaveConnection]) -> None: ...
    @typing.overload
    def create(self, object: typing.Any) -> typing.Any: ...
    @typing.overload
    def create(self, endpoint: org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint) -> net.wimpi.modbus.net.ModbusSlaveConnection: ...
    @typing.overload
    def destroyObject(self, object: typing.Any, pooledObject: org.apache.commons.pool2.PooledObject) -> None: ...
    @typing.overload
    def destroyObject(self, endpoint: org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, obj: org.apache.commons.pool2.PooledObject[net.wimpi.modbus.net.ModbusSlaveConnection]) -> None: ...
    def disconnectOnReturn(self, endpoint: org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, disconnectBeforeConnectedMillis: int) -> None: ...
    def getEndpointPoolConfiguration(self, endpoint: org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint) -> org.openhab.core.io.transport.modbus.endpoint.EndpointPoolConfiguration: ...
    @typing.overload
    def passivateObject(self, object: typing.Any, pooledObject: org.apache.commons.pool2.PooledObject) -> None: ...
    @typing.overload
    def passivateObject(self, endpoint: org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, obj: org.apache.commons.pool2.PooledObject[net.wimpi.modbus.net.ModbusSlaveConnection]) -> None: ...
    def setDefaultPoolConfigurationFactory(self, defaultPoolConfigurationFactory: typing.Union[java.util.function.Function[org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, org.openhab.core.io.transport.modbus.endpoint.EndpointPoolConfiguration], typing.Callable[[org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint], org.openhab.core.io.transport.modbus.endpoint.EndpointPoolConfiguration]]) -> None: ...
    def setEndpointPoolConfiguration(self, endpoint: org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, config: org.openhab.core.io.transport.modbus.endpoint.EndpointPoolConfiguration) -> None: ...
    @typing.overload
    def validateObject(self, object: typing.Any, pooledObject: org.apache.commons.pool2.PooledObject) -> bool: ...
    @typing.overload
    def validateObject(self, key: org.openhab.core.io.transport.modbus.endpoint.ModbusSlaveEndpoint, p: org.apache.commons.pool2.PooledObject[net.wimpi.modbus.net.ModbusSlaveConnection]) -> bool: ...
    @classmethod
    def waitAtleast(cls, lastOperation: int, waitMillis: int) -> int: ...
    @typing.overload
    def wrap(self, object: typing.Any) -> org.apache.commons.pool2.PooledObject: ...
    @typing.overload
    def wrap(self, connection: net.wimpi.modbus.net.ModbusSlaveConnection) -> org.apache.commons.pool2.PooledObject[net.wimpi.modbus.net.ModbusSlaveConnection]: ...
