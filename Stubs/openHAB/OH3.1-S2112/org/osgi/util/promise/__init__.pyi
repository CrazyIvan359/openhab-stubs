import java.lang
import java.util
import java.util.concurrent
import org.osgi.util.function
import typing


_Deferred__T = typing.TypeVar('_Deferred__T')  # <T>
class Deferred(java.lang.Object, typing.Generic[_Deferred__T]):
    """
    Java class 'org.osgi.util.promise.Deferred'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Deferred()
    
    """
    def __init__(self): ...
    def fail(self, throwable: java.lang.Throwable) -> None: ...
    def getPromise(self) -> 'Promise'[_Deferred__T]: ...
    def resolve(self, t: _Deferred__T) -> None: ...
    def resolveWith(self, promise: 'Promise'[_Deferred__T]) -> 'Promise'[None]: ...

class FailedPromisesException(java.lang.RuntimeException):
    """
    Java class 'org.osgi.util.promise.FailedPromisesException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * FailedPromisesException(java.util.Collection, java.lang.Throwable)
    
    """
    def __init__(self, collection: typing.Union[java.util.Collection['Promise'[typing.Any]], typing.Sequence['Promise'[typing.Any]]], throwable: java.lang.Throwable): ...
    def getFailedPromises(self) -> java.util.Collection['Promise'[typing.Any]]: ...

class Failure(java.lang.Object):
    """
    Java class 'org.osgi.util.promise.Failure'
    
    """
    def fail(self, promise: 'Promise'[typing.Any]) -> None: ...

_Promise__T = typing.TypeVar('_Promise__T')  # <T>
class Promise(java.lang.Object, typing.Generic[_Promise__T]):
    """
    Java class 'org.osgi.util.promise.Promise'
    
    """
    def fallbackTo(self, promise: 'Promise'[_Promise__T]) -> 'Promise'[_Promise__T]: ...
    def filter(self, predicate: org.osgi.util.function.Predicate[_Promise__T]) -> 'Promise'[_Promise__T]: ...
    _flatMap__R = typing.TypeVar('_flatMap__R')  # <R>
    def flatMap(self, function: org.osgi.util.function.Function[_Promise__T, 'Promise'[_flatMap__R]]) -> 'Promise'[_flatMap__R]: ...
    def getFailure(self) -> java.lang.Throwable: ...
    def getValue(self) -> _Promise__T: ...
    def isDone(self) -> bool: ...
    _map__R = typing.TypeVar('_map__R')  # <R>
    def map(self, function: org.osgi.util.function.Function[_Promise__T, _map__R]) -> 'Promise'[_map__R]: ...
    def onResolve(self, runnable: java.lang.Runnable) -> 'Promise'[_Promise__T]: ...
    def recover(self, function: org.osgi.util.function.Function['Promise'[typing.Any], _Promise__T]) -> 'Promise'[_Promise__T]: ...
    def recoverWith(self, function: org.osgi.util.function.Function['Promise'[typing.Any], 'Promise'[_Promise__T]]) -> 'Promise'[_Promise__T]: ...
    _then_0__R = typing.TypeVar('_then_0__R')  # <R>
    @typing.overload
    def then(self, success: 'Success'[_Promise__T, _then_0__R]) -> 'Promise'[_then_0__R]: ...
    _then_1__R = typing.TypeVar('_then_1__R')  # <R>
    @typing.overload
    def then(self, success: 'Success'[_Promise__T, _then_1__R], failure: Failure) -> 'Promise'[_then_1__R]: ...

class PromiseFactory(java.lang.Object):
    """
    Java class 'org.osgi.util.promise.PromiseFactory'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PromiseFactory(java.util.concurrent.Executor)
        * PromiseFactory(java.util.concurrent.Executor, java.util.concurrent.ScheduledExecutorService)
    
    """
    @typing.overload
    def __init__(self, executor: java.util.concurrent.Executor): ...
    @typing.overload
    def __init__(self, executor: java.util.concurrent.Executor, scheduledExecutorService: java.util.concurrent.ScheduledExecutorService): ...
    _all__T = typing.TypeVar('_all__T')  # <T>
    _all__S = typing.TypeVar('_all__S')  # <S>
    def all(self, collection: typing.Union[java.util.Collection[Promise[_all__S]], typing.Sequence[Promise[_all__S]]]) -> Promise[java.util.List[_all__T]]: ...
    _deferred__T = typing.TypeVar('_deferred__T')  # <T>
    def deferred(self) -> Deferred[_deferred__T]: ...
    def executor(self) -> java.util.concurrent.Executor: ...
    _failed__T = typing.TypeVar('_failed__T')  # <T>
    def failed(self, throwable: java.lang.Throwable) -> Promise[_failed__T]: ...
    @classmethod
    def inlineExecutor(cls) -> java.util.concurrent.Executor: ...
    _resolved__T = typing.TypeVar('_resolved__T')  # <T>
    def resolved(self, t: _resolved__T) -> Promise[_resolved__T]: ...
    def scheduledExecutor(self) -> java.util.concurrent.ScheduledExecutorService: ...
    _submit__T = typing.TypeVar('_submit__T')  # <T>
    def submit(self, callable: typing.Union[java.util.concurrent.Callable[_submit__T], typing.Callable[[], _submit__T]]) -> Promise[_submit__T]: ...

class Promises(java.lang.Object):
    """
    Java class 'org.osgi.util.promise.Promises'
    
        Extends:
            java.lang.Object
    
    """
    _all_0__T = typing.TypeVar('_all_0__T')  # <T>
    _all_0__S = typing.TypeVar('_all_0__S')  # <S>
    @classmethod
    @typing.overload
    def all(cls, collection: typing.Union[java.util.Collection[Promise[_all_0__S]], typing.Sequence[Promise[_all_0__S]]]) -> Promise[java.util.List[_all_0__T]]: ...
    _all_1__T = typing.TypeVar('_all_1__T')  # <T>
    @classmethod
    @typing.overload
    def all(cls, promiseArray: typing.List[Promise[_all_1__T]]) -> Promise[java.util.List[_all_1__T]]: ...
    _failed__T = typing.TypeVar('_failed__T')  # <T>
    @classmethod
    def failed(cls, throwable: java.lang.Throwable) -> Promise[_failed__T]: ...
    _resolved__T = typing.TypeVar('_resolved__T')  # <T>
    @classmethod
    def resolved(cls, t: _resolved__T) -> Promise[_resolved__T]: ...

_Success__T = typing.TypeVar('_Success__T')  # <T>
_Success__R = typing.TypeVar('_Success__R')  # <R>
class Success(java.lang.Object, typing.Generic[_Success__T, _Success__R]):
    """
    Java class 'org.osgi.util.promise.Success'
    
    """
    def call(self, promise: Promise[_Success__T]) -> Promise[_Success__R]: ...

class TimeoutException(java.lang.Exception):
    """
    Java class 'org.osgi.util.promise.TimeoutException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * TimeoutException()
    
    """
    def __init__(self): ...
