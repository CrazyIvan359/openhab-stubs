import com.hivemq.client.mqtt.mqtt3.message.publish
import com.hivemq.client.mqtt.mqtt5.message.publish
import java.lang
import java.util
import org.openhab.core.io.transport.mqtt
import typing


class MqttBrokerConnectionServiceInstance(java.lang.Object):
    """
    Java class 'org.openhab.core.io.transport.mqtt.internal.MqttBrokerConnectionServiceInstance'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MqttBrokerConnectionServiceInstance(org.openhab.core.io.transport.mqtt.MqttService)
    
    """
    def __init__(self, mqttService: org.openhab.core.io.transport.mqtt.MqttService): ...
    def activate(self, config: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def deactivate(self) -> None: ...
    def modified(self, configMap: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...

class MqttBrokerConnectionServiceInstanceMarker(java.lang.Object):
    """
    Java class 'org.openhab.core.io.transport.mqtt.internal.MqttBrokerConnectionServiceInstanceMarker'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MqttBrokerConnectionServiceInstanceMarker()
    
    """
    def __init__(self): ...

class MqttServiceImpl(org.openhab.core.io.transport.mqtt.MqttService):
    """
    Java class 'org.openhab.core.io.transport.mqtt.internal.MqttServiceImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.mqtt.MqttService
    
      Constructors:
        * MqttServiceImpl()
    
    """
    def __init__(self): ...
    def addBrokerConnection(self, brokerID: java.lang.String, connection: org.openhab.core.io.transport.mqtt.MqttBrokerConnection) -> bool: ...
    def addBrokersListener(self, observer: org.openhab.core.io.transport.mqtt.MqttServiceObserver) -> None: ...
    def getAllBrokerConnections(self) -> java.util.Map[java.lang.String, org.openhab.core.io.transport.mqtt.MqttBrokerConnection]: ...
    def getBrokerConnection(self, brokerName: java.lang.String) -> org.openhab.core.io.transport.mqtt.MqttBrokerConnection: ...
    def hasBrokerObservers(self) -> bool: ...
    def removeBrokerConnection(self, brokerID: java.lang.String) -> org.openhab.core.io.transport.mqtt.MqttBrokerConnection: ...
    def removeBrokersListener(self, observer: org.openhab.core.io.transport.mqtt.MqttServiceObserver) -> None: ...

class Subscription(java.lang.Object):
    """
    Java class 'org.openhab.core.io.transport.mqtt.internal.Subscription'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Subscription()
    
    """
    def __init__(self): ...
    def add(self, subscriber: org.openhab.core.io.transport.mqtt.MqttMessageSubscriber) -> None: ...
    def isEmpty(self) -> bool: ...
    @typing.overload
    def messageArrived(self, message: com.hivemq.client.mqtt.mqtt3.message.publish.Mqtt3Publish) -> None: ...
    @typing.overload
    def messageArrived(self, message: com.hivemq.client.mqtt.mqtt5.message.publish.Mqtt5Publish) -> None: ...
    @typing.overload
    def messageArrived(self, topic: java.lang.String, payload: typing.List[int], retain: bool) -> None: ...
    def remove(self, subscriber: org.openhab.core.io.transport.mqtt.MqttMessageSubscriber) -> None: ...
