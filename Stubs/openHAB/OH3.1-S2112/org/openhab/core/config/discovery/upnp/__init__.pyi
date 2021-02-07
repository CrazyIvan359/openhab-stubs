import java.lang
import java.util
import org.jupnp.model.meta
import org.openhab.core.config.discovery
import org.openhab.core.thing
import typing


class UpnpDiscoveryParticipant(java.lang.Object):
    """
    @NonNullByDefault public interface UpnpDiscoveryParticipant
    
        A :class:`~org.openhab.core.config.discovery.upnp.UpnpDiscoveryParticipant` that is registered as a service is picked up
        by the UpnpDiscoveryService and can thus contribute
        :class:`~org.openhab.core.config.discovery.upnp.https:.github.com.openhab.infrastructure.org.openhab.core.reactor.org.openhab.core.reactor.bundles.org.openhab.core.config.discovery.apidocs.org.openhab.core.config.discovery.DiscoveryResult?is`s
        from UPnP scans.
    
    
    """
    MIN_MAX_AGE_SECS: typing.ClassVar[int] = ...
    def createResult(self, device: org.jupnp.model.meta.RemoteDevice) -> org.openhab.core.config.discovery.DiscoveryResult: ...
    def getSupportedThingTypeUIDs(self) -> java.util.Set[org.openhab.core.thing.ThingTypeUID]: ...
    def getThingUID(self, device: org.jupnp.model.meta.RemoteDevice) -> org.openhab.core.thing.ThingUID: ...
