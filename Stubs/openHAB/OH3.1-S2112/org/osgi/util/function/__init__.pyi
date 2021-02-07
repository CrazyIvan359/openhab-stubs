import java.lang
import typing


_Consumer__T = typing.TypeVar('_Consumer__T')  # <T>
class Consumer(java.lang.Object, typing.Generic[_Consumer__T]):
    """
    Java class 'org.osgi.util.function.Consumer'
    
    """
    def accept(self, t: _Consumer__T) -> None: ...

_Function__T = typing.TypeVar('_Function__T')  # <T>
_Function__R = typing.TypeVar('_Function__R')  # <R>
class Function(java.lang.Object, typing.Generic[_Function__T, _Function__R]):
    """
    Java class 'org.osgi.util.function.Function'
    
    """
    def apply(self, t: _Function__T) -> _Function__R: ...

_Predicate__T = typing.TypeVar('_Predicate__T')  # <T>
class Predicate(java.lang.Object, typing.Generic[_Predicate__T]):
    """
    Java class 'org.osgi.util.function.Predicate'
    
    """
    def test(self, t: _Predicate__T) -> bool: ...
