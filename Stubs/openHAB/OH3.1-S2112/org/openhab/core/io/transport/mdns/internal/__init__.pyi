import java.lang
import java.time
import java.util
import javax.jmdns
import org.openhab.core.io.transport.mdns
import org.openhab.core.net
import org.osgi.framework
import typing


class MDNSActivator(org.osgi.framework.BundleActivator):
    """
    Java class 'org.openhab.core.io.transport.mdns.internal.MDNSActivator'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.osgi.framework.BundleActivator
    
      Constructors:
        * MDNSActivator()
    
    """
    def __init__(self): ...
    def start(self, context: org.osgi.framework.BundleContext) -> None: ...
    def stop(self, context: org.osgi.framework.BundleContext) -> None: ...

class MDNSClientImpl(org.openhab.core.io.transport.mdns.MDNSClient, org.openhab.core.net.NetworkAddressChangeListener):
    """
    Java class 'org.openhab.core.io.transport.mdns.internal.MDNSClientImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.mdns.MDNSClient,
            org.openhab.core.net.NetworkAddressChangeListener
    
      Constructors:
        * MDNSClientImpl(org.openhab.core.net.NetworkAddressService)
    
    """
    def __init__(self, networkAddressService: org.openhab.core.net.NetworkAddressService): ...
    def addServiceListener(self, type: java.lang.String, listener: javax.jmdns.ServiceListener) -> None: ...
    def close(self) -> None: ...
    def deactivate(self) -> None: ...
    def getClientInstances(self) -> java.util.Set[javax.jmdns.JmDNS]: ...
    @typing.overload
    def list(self, type: java.lang.String) -> typing.List[javax.jmdns.ServiceInfo]: ...
    @typing.overload
    def list(self, type: java.lang.String, timeout: java.time.Duration) -> typing.List[javax.jmdns.ServiceInfo]: ...
    def onChanged(self, added: java.util.List[org.openhab.core.net.CidrAddress], removed: java.util.List[org.openhab.core.net.CidrAddress]) -> None: ...
    def registerService(self, description: org.openhab.core.io.transport.mdns.ServiceDescription) -> None: ...
    def removeServiceListener(self, type: java.lang.String, listener: javax.jmdns.ServiceListener) -> None: ...
    def unregisterAllServices(self) -> None: ...
    def unregisterService(self, description: org.openhab.core.io.transport.mdns.ServiceDescription) -> None: ...

class MDNSServiceImpl(org.openhab.core.io.transport.mdns.MDNSService):
    """
    Java class 'org.openhab.core.io.transport.mdns.internal.MDNSServiceImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.transport.mdns.MDNSService
    
      Constructors:
        * MDNSServiceImpl()
    
    """
    def __init__(self): ...
    def deactivate(self) -> None: ...
    def registerService(self, description: org.openhab.core.io.transport.mdns.ServiceDescription) -> None: ...
    def unregisterService(self, description: org.openhab.core.io.transport.mdns.ServiceDescription) -> None: ...
