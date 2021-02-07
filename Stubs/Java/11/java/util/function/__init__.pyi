import java.lang
import java.util
import typing


_BiConsumer__T = typing.TypeVar('_BiConsumer__T')  # <T>
_BiConsumer__U = typing.TypeVar('_BiConsumer__U')  # <U>
class BiConsumer(java.lang.Object, typing.Generic[_BiConsumer__T, _BiConsumer__U]):
    """
    :class:`~java.lang.FunctionalInterface` public interface BiConsumer<T,​U>
    
        Represents an operation that accepts two input arguments and returns no result. This is the two-arity specialization of
        :class:`~java.util.function.Consumer`. Unlike most other functional interfaces, :code:`BiConsumer` is expected to
        operate via side-effects.
    
        This is a :class:`~java.util.function.package` whose functional method is :meth:`~java.util.function.BiConsumer.accept`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Consumer`
    
    
    """
    def accept(self, t: _BiConsumer__T, u: _BiConsumer__U) -> None: ...
    def andThen(self, biConsumer: typing.Union['BiConsumer'[_BiConsumer__T, _BiConsumer__U], typing.Callable[[_BiConsumer__T], _BiConsumer__U]]) -> 'BiConsumer'[_BiConsumer__T, _BiConsumer__U]: ...

_BiFunction__T = typing.TypeVar('_BiFunction__T')  # <T>
_BiFunction__U = typing.TypeVar('_BiFunction__U')  # <U>
_BiFunction__R = typing.TypeVar('_BiFunction__R')  # <R>
class BiFunction(java.lang.Object, typing.Generic[_BiFunction__T, _BiFunction__U, _BiFunction__R]):
    """
    :class:`~java.lang.FunctionalInterface` public interface BiFunction<T,​U,​R>
    
        Represents a function that accepts two arguments and produces a result. This is the two-arity specialization of
        :class:`~java.util.function.Function`.
    
        This is a :class:`~java.util.function.package` whose functional method is :meth:`~java.util.function.BiFunction.apply`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Function`
    
    
    """
    _andThen__V = typing.TypeVar('_andThen__V')  # <V>
    def andThen(self, function: typing.Union['Function'[_BiFunction__R, _andThen__V], typing.Callable[[_BiFunction__R], _andThen__V]]) -> 'BiFunction'[_BiFunction__T, _BiFunction__U, _andThen__V]: ...
    def apply(self, t: _BiFunction__T, u: _BiFunction__U) -> _BiFunction__R: ...

_BiPredicate__T = typing.TypeVar('_BiPredicate__T')  # <T>
_BiPredicate__U = typing.TypeVar('_BiPredicate__U')  # <U>
class BiPredicate(java.lang.Object, typing.Generic[_BiPredicate__T, _BiPredicate__U]):
    """
    :class:`~java.lang.FunctionalInterface` public interface BiPredicate<T,​U>
    
        Represents a predicate (boolean-valued function) of two arguments. This is the two-arity specialization of
        :class:`~java.util.function.Predicate`.
    
        This is a :class:`~java.util.function.package` whose functional method is :meth:`~java.util.function.BiPredicate.test`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Predicate`
    
    
    """
    def negate(self) -> 'BiPredicate'[_BiPredicate__T, _BiPredicate__U]: ...
    def test(self, t: _BiPredicate__T, u: _BiPredicate__U) -> bool: ...

class BooleanSupplier(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface BooleanSupplier
    
        Represents a supplier of :code:`boolean`-valued results. This is the :code:`boolean`-producing primitive specialization
        of :class:`~java.util.function.Supplier`.
    
        There is no requirement that a new or distinct result be returned each time the supplier is invoked.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.BooleanSupplier.getAsBoolean`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Supplier`
    
    
    """
    def getAsBoolean(self) -> bool: ...

_Consumer__T = typing.TypeVar('_Consumer__T')  # <T>
class Consumer(java.lang.Object, typing.Generic[_Consumer__T]):
    """
    :class:`~java.lang.FunctionalInterface` public interface Consumer<T>
    
        Represents an operation that accepts a single input argument and returns no result. Unlike most other functional
        interfaces, :code:`Consumer` is expected to operate via side-effects.
    
        This is a :class:`~java.util.function.package` whose functional method is :meth:`~java.util.function.Consumer.accept`.
    
        Since:
            1.8
    
    
    """
    def accept(self, t: _Consumer__T) -> None: ...
    def andThen(self, consumer: typing.Union['Consumer'[_Consumer__T], typing.Callable[[], _Consumer__T]]) -> 'Consumer'[_Consumer__T]: ...

class DoubleBinaryOperator(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface DoubleBinaryOperator
    
        Represents an operation upon two :code:`double`-valued operands and producing a :code:`double`-valued result. This is
        the primitive type specialization of :class:`~java.util.function.BinaryOperator` for :code:`double`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.DoubleBinaryOperator.applyAsDouble`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.BinaryOperator`, :class:`~java.util.function.DoubleUnaryOperator`
    
    
    """
    def applyAsDouble(self, double: float, double2: float) -> float: ...

class DoubleConsumer(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface DoubleConsumer
    
        Represents an operation that accepts a single :code:`double`-valued argument and returns no result. This is the
        primitive type specialization of :class:`~java.util.function.Consumer` for :code:`double`. Unlike most other functional
        interfaces, :code:`DoubleConsumer` is expected to operate via side-effects.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.DoubleConsumer.accept`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Consumer`
    
    
    """
    def accept(self, double: float) -> None: ...
    def andThen(self, doubleConsumer: 'DoubleConsumer') -> 'DoubleConsumer': ...

_DoubleFunction__R = typing.TypeVar('_DoubleFunction__R')  # <R>
class DoubleFunction(java.lang.Object, typing.Generic[_DoubleFunction__R]):
    """
    :class:`~java.lang.FunctionalInterface` public interface DoubleFunction<R>
    
        Represents a function that accepts a double-valued argument and produces a result. This is the :code:`double`-consuming
        primitive specialization for :class:`~java.util.function.Function`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.DoubleFunction.apply`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Function`
    
    
    """
    def apply(self, double: float) -> _DoubleFunction__R: ...

class DoublePredicate(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface DoublePredicate
    
        Represents a predicate (boolean-valued function) of one :code:`double`-valued argument. This is the
        :code:`double`-consuming primitive type specialization of :class:`~java.util.function.Predicate`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.DoublePredicate.test`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Predicate`
    
    
    """
    def negate(self) -> 'DoublePredicate': ...
    def test(self, double: float) -> bool: ...

class DoubleSupplier(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface DoubleSupplier
    
        Represents a supplier of :code:`double`-valued results. This is the :code:`double`-producing primitive specialization of
        :class:`~java.util.function.Supplier`.
    
        There is no requirement that a distinct result be returned each time the supplier is invoked.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.DoubleSupplier.getAsDouble`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Supplier`
    
    
    """
    def getAsDouble(self) -> float: ...

class DoubleToIntFunction(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface DoubleToIntFunction
    
        Represents a function that accepts a double-valued argument and produces an int-valued result. This is the
        :code:`double`-to-:code:`int` primitive specialization for :class:`~java.util.function.Function`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.DoubleToIntFunction.applyAsInt`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Function`
    
    
    """
    def applyAsInt(self, double: float) -> int: ...

class DoubleToLongFunction(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface DoubleToLongFunction
    
        Represents a function that accepts a double-valued argument and produces a long-valued result. This is the
        :code:`double`-to-:code:`long` primitive specialization for :class:`~java.util.function.Function`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.DoubleToLongFunction.applyAsLong`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Function`
    
    
    """
    def applyAsLong(self, double: float) -> int: ...

class DoubleUnaryOperator(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface DoubleUnaryOperator
    
        Represents an operation on a single :code:`double`-valued operand that produces a :code:`double`-valued result. This is
        the primitive type specialization of :class:`~java.util.function.UnaryOperator` for :code:`double`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.DoubleUnaryOperator.applyAsDouble`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.UnaryOperator`
    
    
    """
    def andThen(self, doubleUnaryOperator: 'DoubleUnaryOperator') -> 'DoubleUnaryOperator': ...
    def applyAsDouble(self, double: float) -> float: ...
    def compose(self, doubleUnaryOperator: 'DoubleUnaryOperator') -> 'DoubleUnaryOperator': ...
    @classmethod
    def identity(cls) -> 'DoubleUnaryOperator': ...

_Function__T = typing.TypeVar('_Function__T')  # <T>
_Function__R = typing.TypeVar('_Function__R')  # <R>
class Function(java.lang.Object, typing.Generic[_Function__T, _Function__R]):
    """
    :class:`~java.lang.FunctionalInterface` public interface Function<T,​R>
    
        Represents a function that accepts one argument and produces a result.
    
        This is a :class:`~java.util.function.package` whose functional method is :meth:`~java.util.function.Function.apply`.
    
        Since:
            1.8
    
    
    """
    _andThen__V = typing.TypeVar('_andThen__V')  # <V>
    def andThen(self, function: typing.Union['Function'[_Function__R, _andThen__V], typing.Callable[[_Function__R], _andThen__V]]) -> 'Function'[_Function__T, _andThen__V]: ...
    def apply(self, t: _Function__T) -> _Function__R: ...
    _compose__V = typing.TypeVar('_compose__V')  # <V>
    def compose(self, function: typing.Union['Function'[_compose__V, _Function__T], typing.Callable[[_compose__V], _Function__T]]) -> 'Function'[_compose__V, _Function__R]: ...
    _identity__T = typing.TypeVar('_identity__T')  # <T>
    @classmethod
    def identity(cls) -> 'Function'[_identity__T, _identity__T]: ...

class IntBinaryOperator(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface IntBinaryOperator
    
        Represents an operation upon two :code:`int`-valued operands and producing an :code:`int`-valued result. This is the
        primitive type specialization of :class:`~java.util.function.BinaryOperator` for :code:`int`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.IntBinaryOperator.applyAsInt`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.BinaryOperator`, :class:`~java.util.function.IntUnaryOperator`
    
    
    """
    def applyAsInt(self, int: int, int2: int) -> int: ...

class IntConsumer(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface IntConsumer
    
        Represents an operation that accepts a single :code:`int`-valued argument and returns no result. This is the primitive
        type specialization of :class:`~java.util.function.Consumer` for :code:`int`. Unlike most other functional interfaces,
        :code:`IntConsumer` is expected to operate via side-effects.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.IntConsumer.accept`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Consumer`
    
    
    """
    def accept(self, int: int) -> None: ...
    def andThen(self, intConsumer: 'IntConsumer') -> 'IntConsumer': ...

_IntFunction__R = typing.TypeVar('_IntFunction__R')  # <R>
class IntFunction(java.lang.Object, typing.Generic[_IntFunction__R]):
    """
    :class:`~java.lang.FunctionalInterface` public interface IntFunction<R>
    
        Represents a function that accepts an int-valued argument and produces a result. This is the :code:`int`-consuming
        primitive specialization for :class:`~java.util.function.Function`.
    
        This is a :class:`~java.util.function.package` whose functional method is :meth:`~java.util.function.IntFunction.apply`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Function`
    
    
    """
    def apply(self, int: int) -> _IntFunction__R: ...

class IntPredicate(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface IntPredicate
    
        Represents a predicate (boolean-valued function) of one :code:`int`-valued argument. This is the :code:`int`-consuming
        primitive type specialization of :class:`~java.util.function.Predicate`.
    
        This is a :class:`~java.util.function.package` whose functional method is :meth:`~java.util.function.IntPredicate.test`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Predicate`
    
    
    """
    def negate(self) -> 'IntPredicate': ...
    def test(self, int: int) -> bool: ...

class IntSupplier(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface IntSupplier
    
        Represents a supplier of :code:`int`-valued results. This is the :code:`int`-producing primitive specialization of
        :class:`~java.util.function.Supplier`.
    
        There is no requirement that a distinct result be returned each time the supplier is invoked.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.IntSupplier.getAsInt`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Supplier`
    
    
    """
    def getAsInt(self) -> int: ...

class IntToDoubleFunction(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface IntToDoubleFunction
    
        Represents a function that accepts an int-valued argument and produces a double-valued result. This is the
        :code:`int`-to-:code:`double` primitive specialization for :class:`~java.util.function.Function`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.IntToDoubleFunction.applyAsDouble`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Function`
    
    
    """
    def applyAsDouble(self, int: int) -> float: ...

class IntToLongFunction(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface IntToLongFunction
    
        Represents a function that accepts an int-valued argument and produces a long-valued result. This is the
        :code:`int`-to-:code:`long` primitive specialization for :class:`~java.util.function.Function`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.IntToLongFunction.applyAsLong`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Function`
    
    
    """
    def applyAsLong(self, int: int) -> int: ...

class IntUnaryOperator(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface IntUnaryOperator
    
        Represents an operation on a single :code:`int`-valued operand that produces an :code:`int`-valued result. This is the
        primitive type specialization of :class:`~java.util.function.UnaryOperator` for :code:`int`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.IntUnaryOperator.applyAsInt`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.UnaryOperator`
    
    
    """
    def andThen(self, intUnaryOperator: 'IntUnaryOperator') -> 'IntUnaryOperator': ...
    def applyAsInt(self, int: int) -> int: ...
    def compose(self, intUnaryOperator: 'IntUnaryOperator') -> 'IntUnaryOperator': ...
    @classmethod
    def identity(cls) -> 'IntUnaryOperator': ...

class LongBinaryOperator(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface LongBinaryOperator
    
        Represents an operation upon two :code:`long`-valued operands and producing a :code:`long`-valued result. This is the
        primitive type specialization of :class:`~java.util.function.BinaryOperator` for :code:`long`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.LongBinaryOperator.applyAsLong`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.BinaryOperator`, :class:`~java.util.function.LongUnaryOperator`
    
    
    """
    def applyAsLong(self, long: int, long2: int) -> int: ...

class LongConsumer(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface LongConsumer
    
        Represents an operation that accepts a single :code:`long`-valued argument and returns no result. This is the primitive
        type specialization of :class:`~java.util.function.Consumer` for :code:`long`. Unlike most other functional interfaces,
        :code:`LongConsumer` is expected to operate via side-effects.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.LongConsumer.accept`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Consumer`
    
    
    """
    def accept(self, long: int) -> None: ...
    def andThen(self, longConsumer: 'LongConsumer') -> 'LongConsumer': ...

_LongFunction__R = typing.TypeVar('_LongFunction__R')  # <R>
class LongFunction(java.lang.Object, typing.Generic[_LongFunction__R]):
    """
    :class:`~java.lang.FunctionalInterface` public interface LongFunction<R>
    
        Represents a function that accepts a long-valued argument and produces a result. This is the :code:`long`-consuming
        primitive specialization for :class:`~java.util.function.Function`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.LongFunction.apply`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Function`
    
    
    """
    def apply(self, long: int) -> _LongFunction__R: ...

class LongPredicate(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface LongPredicate
    
        Represents a predicate (boolean-valued function) of one :code:`long`-valued argument. This is the :code:`long`-consuming
        primitive type specialization of :class:`~java.util.function.Predicate`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.LongPredicate.test`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Predicate`
    
    
    """
    def negate(self) -> 'LongPredicate': ...
    def test(self, long: int) -> bool: ...

class LongSupplier(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface LongSupplier
    
        Represents a supplier of :code:`long`-valued results. This is the :code:`long`-producing primitive specialization of
        :class:`~java.util.function.Supplier`.
    
        There is no requirement that a distinct result be returned each time the supplier is invoked.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.LongSupplier.getAsLong`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Supplier`
    
    
    """
    def getAsLong(self) -> int: ...

class LongToDoubleFunction(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface LongToDoubleFunction
    
        Represents a function that accepts a long-valued argument and produces a double-valued result. This is the
        :code:`long`-to-:code:`double` primitive specialization for :class:`~java.util.function.Function`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.LongToDoubleFunction.applyAsDouble`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Function`
    
    
    """
    def applyAsDouble(self, long: int) -> float: ...

class LongToIntFunction(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface LongToIntFunction
    
        Represents a function that accepts a long-valued argument and produces an int-valued result. This is the
        :code:`long`-to-:code:`int` primitive specialization for :class:`~java.util.function.Function`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.LongToIntFunction.applyAsInt`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Function`
    
    
    """
    def applyAsInt(self, long: int) -> int: ...

class LongUnaryOperator(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface LongUnaryOperator
    
        Represents an operation on a single :code:`long`-valued operand that produces a :code:`long`-valued result. This is the
        primitive type specialization of :class:`~java.util.function.UnaryOperator` for :code:`long`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.LongUnaryOperator.applyAsLong`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.UnaryOperator`
    
    
    """
    def andThen(self, longUnaryOperator: 'LongUnaryOperator') -> 'LongUnaryOperator': ...
    def applyAsLong(self, long: int) -> int: ...
    def compose(self, longUnaryOperator: 'LongUnaryOperator') -> 'LongUnaryOperator': ...
    @classmethod
    def identity(cls) -> 'LongUnaryOperator': ...

_ObjDoubleConsumer__T = typing.TypeVar('_ObjDoubleConsumer__T')  # <T>
class ObjDoubleConsumer(java.lang.Object, typing.Generic[_ObjDoubleConsumer__T]):
    """
    :class:`~java.lang.FunctionalInterface` public interface ObjDoubleConsumer<T>
    
        Represents an operation that accepts an object-valued and a :code:`double`-valued argument, and returns no result. This
        is the :code:`(reference, double)` specialization of :class:`~java.util.function.BiConsumer`. Unlike most other
        functional interfaces, :code:`ObjDoubleConsumer` is expected to operate via side-effects.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.ObjDoubleConsumer.accept`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.BiConsumer`
    
    
    """
    def accept(self, t: _ObjDoubleConsumer__T, double: float) -> None: ...

_ObjIntConsumer__T = typing.TypeVar('_ObjIntConsumer__T')  # <T>
class ObjIntConsumer(java.lang.Object, typing.Generic[_ObjIntConsumer__T]):
    """
    :class:`~java.lang.FunctionalInterface` public interface ObjIntConsumer<T>
    
        Represents an operation that accepts an object-valued and a :code:`int`-valued argument, and returns no result. This is
        the :code:`(reference, int)` specialization of :class:`~java.util.function.BiConsumer`. Unlike most other functional
        interfaces, :code:`ObjIntConsumer` is expected to operate via side-effects.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.ObjIntConsumer.accept`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.BiConsumer`
    
    
    """
    def accept(self, t: _ObjIntConsumer__T, int: int) -> None: ...

_ObjLongConsumer__T = typing.TypeVar('_ObjLongConsumer__T')  # <T>
class ObjLongConsumer(java.lang.Object, typing.Generic[_ObjLongConsumer__T]):
    """
    :class:`~java.lang.FunctionalInterface` public interface ObjLongConsumer<T>
    
        Represents an operation that accepts an object-valued and a :code:`long`-valued argument, and returns no result. This is
        the :code:`(reference, long)` specialization of :class:`~java.util.function.BiConsumer`. Unlike most other functional
        interfaces, :code:`ObjLongConsumer` is expected to operate via side-effects.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.ObjLongConsumer.accept`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.BiConsumer`
    
    
    """
    def accept(self, t: _ObjLongConsumer__T, long: int) -> None: ...

_Predicate__T = typing.TypeVar('_Predicate__T')  # <T>
class Predicate(java.lang.Object, typing.Generic[_Predicate__T]):
    """
    :class:`~java.lang.FunctionalInterface` public interface Predicate<T>
    
        Represents a predicate (boolean-valued function) of one argument.
    
        This is a :class:`~java.util.function.package` whose functional method is :meth:`~java.util.function.Predicate.test`.
    
        Since:
            1.8
    
    
    """
    _isEqual__T = typing.TypeVar('_isEqual__T')  # <T>
    @classmethod
    def isEqual(cls, object: typing.Any) -> 'Predicate'[_isEqual__T]: ...
    def negate(self) -> 'Predicate'[_Predicate__T]: ...
    def test(self, t: _Predicate__T) -> bool: ...

_Supplier__T = typing.TypeVar('_Supplier__T')  # <T>
class Supplier(java.lang.Object, typing.Generic[_Supplier__T]):
    """
    :class:`~java.lang.FunctionalInterface` public interface Supplier<T>
    
        Represents a supplier of results.
    
        There is no requirement that a new or distinct result be returned each time the supplier is invoked.
    
        This is a :class:`~java.util.function.package` whose functional method is :meth:`~java.util.function.Supplier.get`.
    
        Since:
            1.8
    
    
    """
    def get(self) -> _Supplier__T: ...

_ToDoubleBiFunction__T = typing.TypeVar('_ToDoubleBiFunction__T')  # <T>
_ToDoubleBiFunction__U = typing.TypeVar('_ToDoubleBiFunction__U')  # <U>
class ToDoubleBiFunction(java.lang.Object, typing.Generic[_ToDoubleBiFunction__T, _ToDoubleBiFunction__U]):
    """
    :class:`~java.lang.FunctionalInterface` public interface ToDoubleBiFunction<T,​U>
    
        Represents a function that accepts two arguments and produces a double-valued result. This is the
        :code:`double`-producing primitive specialization for :class:`~java.util.function.BiFunction`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.ToDoubleBiFunction.applyAsDouble`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.BiFunction`
    
    
    """
    def applyAsDouble(self, t: _ToDoubleBiFunction__T, u: _ToDoubleBiFunction__U) -> float: ...

_ToDoubleFunction__T = typing.TypeVar('_ToDoubleFunction__T')  # <T>
class ToDoubleFunction(java.lang.Object, typing.Generic[_ToDoubleFunction__T]):
    """
    :class:`~java.lang.FunctionalInterface` public interface ToDoubleFunction<T>
    
        Represents a function that produces a double-valued result. This is the :code:`double`-producing primitive
        specialization for :class:`~java.util.function.Function`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.ToDoubleFunction.applyAsDouble`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Function`
    
    
    """
    def applyAsDouble(self, t: _ToDoubleFunction__T) -> float: ...

_ToIntBiFunction__T = typing.TypeVar('_ToIntBiFunction__T')  # <T>
_ToIntBiFunction__U = typing.TypeVar('_ToIntBiFunction__U')  # <U>
class ToIntBiFunction(java.lang.Object, typing.Generic[_ToIntBiFunction__T, _ToIntBiFunction__U]):
    """
    :class:`~java.lang.FunctionalInterface` public interface ToIntBiFunction<T,​U>
    
        Represents a function that accepts two arguments and produces an int-valued result. This is the :code:`int`-producing
        primitive specialization for :class:`~java.util.function.BiFunction`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.ToIntBiFunction.applyAsInt`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.BiFunction`
    
    
    """
    def applyAsInt(self, t: _ToIntBiFunction__T, u: _ToIntBiFunction__U) -> int: ...

_ToIntFunction__T = typing.TypeVar('_ToIntFunction__T')  # <T>
class ToIntFunction(java.lang.Object, typing.Generic[_ToIntFunction__T]):
    """
    :class:`~java.lang.FunctionalInterface` public interface ToIntFunction<T>
    
        Represents a function that produces an int-valued result. This is the :code:`int`-producing primitive specialization for
        :class:`~java.util.function.Function`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.ToIntFunction.applyAsInt`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Function`
    
    
    """
    def applyAsInt(self, t: _ToIntFunction__T) -> int: ...

_ToLongBiFunction__T = typing.TypeVar('_ToLongBiFunction__T')  # <T>
_ToLongBiFunction__U = typing.TypeVar('_ToLongBiFunction__U')  # <U>
class ToLongBiFunction(java.lang.Object, typing.Generic[_ToLongBiFunction__T, _ToLongBiFunction__U]):
    """
    :class:`~java.lang.FunctionalInterface` public interface ToLongBiFunction<T,​U>
    
        Represents a function that accepts two arguments and produces a long-valued result. This is the :code:`long`-producing
        primitive specialization for :class:`~java.util.function.BiFunction`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.ToLongBiFunction.applyAsLong`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.BiFunction`
    
    
    """
    def applyAsLong(self, t: _ToLongBiFunction__T, u: _ToLongBiFunction__U) -> int: ...

_ToLongFunction__T = typing.TypeVar('_ToLongFunction__T')  # <T>
class ToLongFunction(java.lang.Object, typing.Generic[_ToLongFunction__T]):
    """
    :class:`~java.lang.FunctionalInterface` public interface ToLongFunction<T>
    
        Represents a function that produces a long-valued result. This is the :code:`long`-producing primitive specialization
        for :class:`~java.util.function.Function`.
    
        This is a :class:`~java.util.function.package` whose functional method is
        :meth:`~java.util.function.ToLongFunction.applyAsLong`.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.util.function.Function`
    
    
    """
    def applyAsLong(self, t: _ToLongFunction__T) -> int: ...

_BinaryOperator__T = typing.TypeVar('_BinaryOperator__T')  # <T>
class BinaryOperator(BiFunction[_BinaryOperator__T, _BinaryOperator__T, _BinaryOperator__T], typing.Generic[_BinaryOperator__T]):
    """
    Java class 'java.util.function.BinaryOperator'
    
        Interfaces:
            java.util.function.BiFunction
    
    """
    _maxBy__T = typing.TypeVar('_maxBy__T')  # <T>
    @classmethod
    def maxBy(cls, comparator: typing.Union[java.util.Comparator[_maxBy__T], typing.Callable[[], _maxBy__T]]) -> 'BinaryOperator'[_maxBy__T]: ...
    _minBy__T = typing.TypeVar('_minBy__T')  # <T>
    @classmethod
    def minBy(cls, comparator: typing.Union[java.util.Comparator[_minBy__T], typing.Callable[[], _minBy__T]]) -> 'BinaryOperator'[_minBy__T]: ...

_UnaryOperator__T = typing.TypeVar('_UnaryOperator__T')  # <T>
class UnaryOperator(Function[_UnaryOperator__T, _UnaryOperator__T], typing.Generic[_UnaryOperator__T]):
    """
    Java class 'java.util.function.UnaryOperator'
    
        Interfaces:
            java.util.function.Function
    
    """
    _identity__T = typing.TypeVar('_identity__T')  # <T>
    @classmethod
    def identity(cls) -> 'UnaryOperator'[_identity__T]: ...
