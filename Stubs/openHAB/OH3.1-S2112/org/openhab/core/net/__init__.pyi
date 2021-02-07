import java.lang
import java.net
import java.util
import org.openhab.core.common
import org.osgi.framework
import typing


class CidrAddress(java.lang.Object):
    """
    Java class 'org.openhab.core.net.CidrAddress'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * CidrAddress(java.net.InetAddress, short)
    
    """
    def __init__(self, address: java.net.InetAddress, networkPrefixLength: int): ...
    def equals(self, o: typing.Any) -> bool: ...
    def getAddress(self) -> java.net.InetAddress: ...
    def getPrefix(self) -> int: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class HttpServiceUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.net.HttpServiceUtil'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def getHttpServicePort(cls, bc: org.osgi.framework.BundleContext) -> int: ...
    @classmethod
    def getHttpServicePortSecure(cls, bc: org.osgi.framework.BundleContext) -> int: ...

class NetworkAddressChangeListener(java.lang.Object):
    """
    @NonNullByDefault public interface NetworkAddressChangeListener
    
        This is an interface for listeners who wants to be notified for the change of network address. There are only network
        address adds, and removes; it makes no effort to correlate which existing network is changed. Listeners should register
        themselves at the :class:`~org.openhab.core.net.NetworkAddressService`.
    
        Also see:
            :class:`~org.openhab.core.net.NetUtil`
    
    
    """
    def onChanged(self, added: java.util.List[CidrAddress], removed: java.util.List[CidrAddress]) -> None: ...
    def onPrimaryAddressChanged(self, oldPrimaryAddress: java.lang.String, newPrimaryAddress: java.lang.String) -> None: ...

class NetworkAddressService(java.lang.Object):
    """
    @NonNullByDefault public interface NetworkAddressService
    
        Interface that provides access to configured network addresses
    
    
    """
    def addNetworkAddressChangeListener(self, listener: NetworkAddressChangeListener) -> None: ...
    def getConfiguredBroadcastAddress(self) -> java.lang.String: ...
    def getPrimaryIpv4HostAddress(self) -> java.lang.String: ...
    def isUseIPv6(self) -> bool: ...
    def isUseOnlyOneAddress(self) -> bool: ...
    def removeNetworkAddressChangeListener(self, listener: NetworkAddressChangeListener) -> None: ...

class NetUtil(NetworkAddressService):
    """
    Java class 'org.openhab.core.net.NetUtil'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.net.NetworkAddressService
    
      Constructors:
        * NetUtil(org.openhab.core.common.SafeCaller)
    
      Attributes:
        POLL_INTERVAL_SECONDS (int): final static field
    
    """
    POLL_INTERVAL_SECONDS: typing.ClassVar[int] = ...
    def __init__(self, safeCaller: org.openhab.core.common.SafeCaller): ...
    def addNetworkAddressChangeListener(self, listener: NetworkAddressChangeListener) -> None: ...
    @classmethod
    def getAllBroadcastAddresses(cls) -> java.util.List[java.lang.String]: ...
    @classmethod
    def getAllInterfaceAddresses(cls) -> java.util.Collection[CidrAddress]: ...
    def getConfiguredBroadcastAddress(self) -> java.lang.String: ...
    @classmethod
    def getIpv4NetAddress(cls, ipAddressString: java.lang.String, netMask: int) -> java.lang.String: ...
    @classmethod
    def getIpv4NetBroadcastAddress(cls, ipAddressString: java.lang.String, prefix: int) -> java.lang.String: ...
    def getPrimaryIpv4HostAddress(self) -> java.lang.String: ...
    def isUseIPv6(self) -> bool: ...
    def isUseOnlyOneAddress(self) -> bool: ...
    @classmethod
    def isValidIPConfig(cls, ipAddress: java.lang.String) -> bool: ...
    def modified(self, config: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    @classmethod
    def networkPrefixLengthToNetmask(cls, prefixLength: int) -> java.lang.String: ...
    def removeNetworkAddressChangeListener(self, listener: NetworkAddressChangeListener) -> None: ...
