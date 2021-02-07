import java.lang
import typing


class MathUtils(java.lang.Object):
    """
    Java class 'org.openhab.core.model.core.internal.util.MathUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MathUtils()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def gcd(cls, m: int, n: int) -> int: ...
    @classmethod
    @typing.overload
    def gcd(cls, numbers: typing.List[int]) -> int: ...
    @classmethod
    @typing.overload
    def lcm(cls, m: int, n: int) -> int: ...
    @classmethod
    @typing.overload
    def lcm(cls, numbers: typing.List[int]) -> int: ...
