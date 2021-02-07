import java.lang
import org.osgi.framework
import typing


class BundleResolver(java.lang.Object):
    """
    public interface BundleResolver
    
        Resolve bundle specific information from the framework.
    
    
    """
    def resolveBundle(self, clazz: typing.Type[typing.Any]) -> org.osgi.framework.Bundle: ...

class HexUtils(java.lang.Object):
    """
    Java class 'org.openhab.core.util.HexUtils'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def byteToHex(cls, value: int) -> typing.List[int]: ...
    @classmethod
    @typing.overload
    def bytesToHex(cls, bytes: typing.List[int]) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def bytesToHex(cls, bytes: typing.List[int], delimiter: java.lang.CharSequence) -> java.lang.String: ...
    @classmethod
    def hexToByte(cls, high: int, low: int) -> int: ...
    @classmethod
    @typing.overload
    def hexToBytes(cls, hexString: java.lang.String) -> typing.List[int]: ...
    @classmethod
    @typing.overload
    def hexToBytes(cls, hexString: java.lang.String, delimiter: java.lang.String) -> typing.List[int]: ...

class UIDUtils(java.lang.Object):
    """
    Java class 'org.openhab.core.util.UIDUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * UIDUtils()
    
    """
    def __init__(self): ...
    @classmethod
    def decode(cls, value: java.lang.String) -> java.lang.String: ...
    @classmethod
    def encode(cls, value: java.lang.String) -> java.lang.String: ...
