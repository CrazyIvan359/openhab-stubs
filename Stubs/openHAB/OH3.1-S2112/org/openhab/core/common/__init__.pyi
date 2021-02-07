import java.lang
import java.util
import java.util.concurrent
import java.util.function
import typing


class AbstractUID(java.lang.Object):
    """
    Java class 'org.openhab.core.common.AbstractUID'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * AbstractUID(java.util.List)
        * AbstractUID(java.lang.String[])
        * AbstractUID(java.lang.String)
        * AbstractUID()
    
      Attributes:
        SEGMENT_PATTERN (java.lang.String): final static field
        SEPARATOR (java.lang.String): final static field
    
    """
    SEGMENT_PATTERN: typing.ClassVar[java.lang.String] = ...
    SEPARATOR: typing.ClassVar[java.lang.String] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, uid: java.lang.String): ...
    @typing.overload
    def __init__(self, segments: typing.List[java.lang.String]): ...
    @typing.overload
    def __init__(self, segments: java.util.List[java.lang.String]): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getAsString(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class NamedThreadFactory(java.util.concurrent.ThreadFactory):
    """
    Java class 'org.openhab.core.common.NamedThreadFactory'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.util.concurrent.ThreadFactory
    
      Constructors:
        * NamedThreadFactory(java.lang.String, boolean, int)
        * NamedThreadFactory(java.lang.String, boolean)
        * NamedThreadFactory(java.lang.String)
    
    """
    @typing.overload
    def __init__(self, id: java.lang.String): ...
    @typing.overload
    def __init__(self, id: java.lang.String, daemonize: bool): ...
    @typing.overload
    def __init__(self, id: java.lang.String, daemonize: bool, priority: int): ...
    def newThread(self, runnable: java.lang.Runnable) -> java.lang.Thread: ...

class QueueingThreadPoolExecutor(java.util.concurrent.ThreadPoolExecutor):
    """
    Java class 'org.openhab.core.common.QueueingThreadPoolExecutor'
    
        Extends:
            java.util.concurrent.ThreadPoolExecutor
    
    """
    @classmethod
    def createInstance(cls, name: java.lang.String, threadPoolSize: int) -> 'QueueingThreadPoolExecutor': ...
    def execute(self, command: java.lang.Runnable) -> None: ...
    def getQueue(self) -> java.util.concurrent.BlockingQueue[java.lang.Runnable]: ...
    def setRejectedExecutionHandler(self, handler: java.util.concurrent.RejectedExecutionHandler) -> None: ...

class SafeCaller(java.lang.Object):
    """
    @NonNullByDefault public interface SafeCaller
    
        OSGi service to obtain a :class:`~org.openhab.core.common.SafeCallerBuilder`. Safe-calls are used within the framework
        in order to protect it from hanging/blocking binding code and log meaningful messages to detect and identify such
        hanging code.
    
    
    """
    DEFAULT_TIMEOUT: typing.ClassVar[int] = ...
    _create__T = typing.TypeVar('_create__T')  # <T>
    def create(self, target: _create__T, interfaceType: typing.Type[_create__T]) -> 'SafeCallerBuilder'[_create__T]: ...

_SafeCallerBuilder__T = typing.TypeVar('_SafeCallerBuilder__T')  # <T>
class SafeCallerBuilder(java.lang.Object, typing.Generic[_SafeCallerBuilder__T]):
    """
    @NonNullByDefault public interface SafeCallerBuilder<T>
    
        Builder to create a safe-call wrapper for another object.
    
    
    """
    def build(self) -> _SafeCallerBuilder__T: ...
    def onException(self, exceptionHandler: typing.Union[java.util.function.Consumer[java.lang.Throwable], typing.Callable[[], java.lang.Throwable]]) -> 'SafeCallerBuilder'[_SafeCallerBuilder__T]: ...
    def onTimeout(self, timeoutHandler: java.lang.Runnable) -> 'SafeCallerBuilder'[_SafeCallerBuilder__T]: ...
    def withAsync(self) -> 'SafeCallerBuilder'[_SafeCallerBuilder__T]: ...
    def withIdentifier(self, identifier: typing.Any) -> 'SafeCallerBuilder'[_SafeCallerBuilder__T]: ...
    def withTimeout(self, timeout: int) -> 'SafeCallerBuilder'[_SafeCallerBuilder__T]: ...

class ThreadFactoryBuilder(java.lang.Object):
    """
    Java class 'org.openhab.core.common.ThreadFactoryBuilder'
    
        Extends:
            java.lang.Object
    
    """
    def build(self) -> java.util.concurrent.ThreadFactory: ...
    @classmethod
    def create(cls) -> 'ThreadFactoryBuilder': ...
    def withDaemonThreads(self, daemonThreads: bool) -> 'ThreadFactoryBuilder': ...
    def withName(self, name: java.lang.String) -> 'ThreadFactoryBuilder': ...
    def withNamePrefix(self, namePrefix: java.lang.String) -> 'ThreadFactoryBuilder': ...
    def withPriority(self, priority: int) -> 'ThreadFactoryBuilder': ...
    def withUncaughtExceptionHandler(self, uncaughtExceptionHandler: java.lang.Thread.UncaughtExceptionHandler) -> 'ThreadFactoryBuilder': ...
    def withWrappedThreadFactory(self, wrappedThreadFactory: java.util.concurrent.ThreadFactory) -> 'ThreadFactoryBuilder': ...

class ThreadPoolManager(java.lang.Object):
    """
    Java class 'org.openhab.core.common.ThreadPoolManager'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ThreadPoolManager()
    
      Attributes:
        CONFIGURATION_PID (java.lang.String): final static field
        THREAD_POOL_NAME_COMMON (java.lang.String): final static field
    
    """
    CONFIGURATION_PID: typing.ClassVar[java.lang.String] = ...
    THREAD_POOL_NAME_COMMON: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    @classmethod
    def getPool(cls, poolName: java.lang.String) -> java.util.concurrent.ExecutorService: ...
    @classmethod
    def getScheduledPool(cls, poolName: java.lang.String) -> java.util.concurrent.ScheduledExecutorService: ...
