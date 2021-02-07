import java.lang
import java.util
import javax.jmdns
import org.openhab.core.config.discovery
import org.openhab.core.io.transport.mdns
import org.openhab.core.thing
import typing


class MDNSDiscoveryService(org.openhab.core.config.discovery.AbstractDiscoveryService, javax.jmdns.ServiceListener):
    """
    Java class 'org.openhab.core.config.discovery.mdns.internal.MDNSDiscoveryService'
    
        Extends:
            org.openhab.core.config.discovery.AbstractDiscoveryService
    
        Interfaces:
            javax.jmdns.ServiceListener
    
      Constructors:
        * MDNSDiscoveryService(java.util.Map, org.openhab.core.io.transport.mdns.MDNSClient)
    
    """
    def __init__(self, configProperties: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]], mdnsClient: org.openhab.core.io.transport.mdns.MDNSClient): ...
    @typing.overload
    def getSupportedThingTypes(self) -> java.util.Collection: ...
    @typing.overload
    def getSupportedThingTypes(self) -> java.util.Set[org.openhab.core.thing.ThingTypeUID]: ...
    def serviceAdded(self, serviceEvent: javax.jmdns.ServiceEvent) -> None: ...
    def serviceRemoved(self, serviceEvent: javax.jmdns.ServiceEvent) -> None: ...
    def serviceResolved(self, serviceEvent: javax.jmdns.ServiceEvent) -> None: ...
