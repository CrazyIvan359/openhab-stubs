import org.osgi.framework
import typing


class BundleStartLevel(org.osgi.framework.BundleReference):
    """
    Java class 'org.osgi.framework.startlevel.BundleStartLevel'
    
        Interfaces:
            org.osgi.framework.BundleReference
    
    """
    def getStartLevel(self) -> int: ...
    def isActivationPolicyUsed(self) -> bool: ...
    def isPersistentlyStarted(self) -> bool: ...
    def setStartLevel(self, int: int) -> None: ...

class FrameworkStartLevel(org.osgi.framework.BundleReference):
    """
    Java class 'org.osgi.framework.startlevel.FrameworkStartLevel'
    
        Interfaces:
            org.osgi.framework.BundleReference
    
    """
    def getInitialBundleStartLevel(self) -> int: ...
    def getStartLevel(self) -> int: ...
    def setInitialBundleStartLevel(self, int: int) -> None: ...
    def setStartLevel(self, int: int, frameworkListenerArray: typing.List[org.osgi.framework.FrameworkListener]) -> None: ...
