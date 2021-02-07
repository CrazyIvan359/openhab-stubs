import java.lang
import java.security
import java.util
import org.osgi.framework.wiring
import typing


class WeavingException(java.lang.RuntimeException):
    """
    Java class 'org.osgi.framework.hooks.weaving.WeavingException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * WeavingException(java.lang.String, java.lang.Throwable)
        * WeavingException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self, string: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, throwable: java.lang.Throwable): ...

class WeavingHook(java.lang.Object):
    """
    Java class 'org.osgi.framework.hooks.weaving.WeavingHook'
    
    """
    def weave(self, wovenClass: 'WovenClass') -> None: ...

class WovenClass(java.lang.Object):
    """
    Java class 'org.osgi.framework.hooks.weaving.WovenClass'
    
      Attributes:
        TRANSFORMING (int): final static field
        TRANSFORMED (int): final static field
        DEFINED (int): final static field
        TRANSFORMING_FAILED (int): final static field
        DEFINE_FAILED (int): final static field
    
    """
    TRANSFORMING: typing.ClassVar[int] = ...
    TRANSFORMED: typing.ClassVar[int] = ...
    DEFINED: typing.ClassVar[int] = ...
    TRANSFORMING_FAILED: typing.ClassVar[int] = ...
    DEFINE_FAILED: typing.ClassVar[int] = ...
    def getBundleWiring(self) -> org.osgi.framework.wiring.BundleWiring: ...
    def getBytes(self) -> typing.List[int]: ...
    def getClassName(self) -> java.lang.String: ...
    def getDefinedClass(self) -> typing.Type[typing.Any]: ...
    def getDynamicImports(self) -> java.util.List[java.lang.String]: ...
    def getProtectionDomain(self) -> java.security.ProtectionDomain: ...
    def getState(self) -> int: ...
    def isWeavingComplete(self) -> bool: ...
    def setBytes(self, byteArray: typing.List[int]) -> None: ...

class WovenClassListener(java.lang.Object):
    """
    Java class 'org.osgi.framework.hooks.weaving.WovenClassListener'
    
    """
    def modified(self, wovenClass: WovenClass) -> None: ...
