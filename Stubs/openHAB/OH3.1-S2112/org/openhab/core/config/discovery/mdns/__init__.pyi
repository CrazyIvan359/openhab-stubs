import java.lang
import java.util
import javax.jmdns
import org.openhab.core.config.discovery
import org.openhab.core.thing


class MDNSDiscoveryParticipant(java.lang.Object):
    """
    @NonNullByDefault public interface MDNSDiscoveryParticipant
    
        A :class:`~org.openhab.core.config.discovery.mdns.MDNSDiscoveryParticipant` that is registered as a service is picked up
        by the :code:`MDNSDiscoveryService` and can thus contribute :code:`DiscoveryResult`s from mDNS scans.
    
    
    """
    def createResult(self, service: javax.jmdns.ServiceInfo) -> org.openhab.core.config.discovery.DiscoveryResult: ...
    def getServiceType(self) -> java.lang.String: ...
    def getSupportedThingTypeUIDs(self) -> java.util.Set[org.openhab.core.thing.ThingTypeUID]: ...
    def getThingUID(self, service: javax.jmdns.ServiceInfo) -> org.openhab.core.thing.ThingUID: ...
