import java.lang
import java.util
import org.openhab.core.io.transport.mdns
import org.osgi.framework
import typing


class MDNSAnnouncer(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.mdns.internal.MDNSAnnouncer'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MDNSAnnouncer()
    
    """
    def __init__(self): ...
    def activate(self, bundleContext: org.osgi.framework.BundleContext, properties: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def deactivate(self) -> None: ...
    def setMDNSService(self, mdnsService: org.openhab.core.io.transport.mdns.MDNSService) -> None: ...
    def unsetMDNSService(self, mdnsService: org.openhab.core.io.transport.mdns.MDNSService) -> None: ...
