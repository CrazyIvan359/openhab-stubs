import java.lang
import java.lang.reflect
import java.util
import java.util.concurrent
import java.util.function
import java.util.stream
import org
import org.openhab.core.common
import typing


class CombinedClassLoader(java.lang.ClassLoader):
    """
    Java class 'org.openhab.core.internal.common.CombinedClassLoader'
    
        Extends:
            java.lang.ClassLoader
    
    """
    @classmethod
    @typing.overload
    def fromClassLoaders(cls, parent: java.lang.ClassLoader, delegateClassLoaders: typing.List[java.lang.ClassLoader]) -> 'CombinedClassLoader': ...
    @classmethod
    @typing.overload
    def fromClassLoaders(cls, parent: java.lang.ClassLoader, delegateClassLoaders: java.util.stream.Stream[java.lang.ClassLoader]) -> 'CombinedClassLoader': ...
    @classmethod
    def fromClasses(cls, parent: java.lang.ClassLoader, delegateClasses: java.util.stream.Stream[typing.Type[typing.Any]]) -> 'CombinedClassLoader': ...

class SafeCallManager(java.lang.Object):
    """
    Java class 'org.openhab.core.internal.common.SafeCallManager'
    
    """
    def enqueue(self, invocation: 'Invocation') -> None: ...
    def getActiveInvocation(self) -> 'Invocation': ...
    def getScheduler(self) -> java.util.concurrent.ExecutorService: ...
    def recordCallEnd(self, invocation: 'Invocation') -> None: ...
    def recordCallStart(self, invocation: 'Invocation') -> None: ...

_SafeCallerBuilderImpl__T = typing.TypeVar('_SafeCallerBuilderImpl__T')  # <T>
class SafeCallerBuilderImpl(org.openhab.core.common.SafeCallerBuilder[_SafeCallerBuilderImpl__T], typing.Generic[_SafeCallerBuilderImpl__T]):
    """
    Java class 'org.openhab.core.internal.common.SafeCallerBuilderImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.common.SafeCallerBuilder
    
      Constructors:
        * SafeCallerBuilderImpl(java.lang.Object, java.lang.Class[], org.openhab.core.internal.common.SafeCallManager)
    
    """
    def __init__(self, target: _SafeCallerBuilderImpl__T, classes: typing.List[typing.Type[typing.Any]], manager: SafeCallManager): ...
    def build(self) -> _SafeCallerBuilderImpl__T: ...
    def onException(self, exceptionHandler: typing.Union[java.util.function.Consumer[java.lang.Throwable], typing.Callable[[], java.lang.Throwable]]) -> org.openhab.core.common.SafeCallerBuilder[_SafeCallerBuilderImpl__T]: ...
    def onTimeout(self, timeoutHandler: java.lang.Runnable) -> org.openhab.core.common.SafeCallerBuilder[_SafeCallerBuilderImpl__T]: ...
    def withAsync(self) -> org.openhab.core.common.SafeCallerBuilder[_SafeCallerBuilderImpl__T]: ...
    def withIdentifier(self, identifier: typing.Any) -> org.openhab.core.common.SafeCallerBuilder[_SafeCallerBuilderImpl__T]: ...
    def withTimeout(self, timeout: int) -> org.openhab.core.common.SafeCallerBuilder[_SafeCallerBuilderImpl__T]: ...

class SafeCallerImpl(org.openhab.core.common.SafeCaller):
    """
    Java class 'org.openhab.core.internal.common.SafeCallerImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.common.SafeCaller
    
      Constructors:
        * SafeCallerImpl(java.util.Map)
    
    """
    def __init__(self, properties: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]): ...
    _create__T = typing.TypeVar('_create__T')  # <T>
    def create(self, target: _create__T, interfaceType: typing.Type[_create__T]) -> org.openhab.core.common.SafeCallerBuilder[_create__T]: ...
    def deactivate(self) -> None: ...
    def modified(self, properties: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...

class WrappedScheduledExecutorService(java.util.concurrent.ScheduledThreadPoolExecutor):
    """
    Java class 'org.openhab.core.internal.common.WrappedScheduledExecutorService'
    
        Extends:
            java.util.concurrent.ScheduledThreadPoolExecutor
    
      Constructors:
        * WrappedScheduledExecutorService(int, java.util.concurrent.ThreadFactory)
    
    """
    def __init__(self, corePoolSize: int, threadFactory: java.util.concurrent.ThreadFactory): ...

class Invocation: ...

class SafeCallManagerImpl(SafeCallManager):
    """
    Java class 'org.openhab.core.internal.common.SafeCallManagerImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.internal.common.SafeCallManager
    
      Constructors:
        * SafeCallManagerImpl(java.util.concurrent.ScheduledExecutorService, java.util.concurrent.ExecutorService, boolean)
    
    """
    def __init__(self, watcher: java.util.concurrent.ScheduledExecutorService, scheduler: java.util.concurrent.ExecutorService, enforceSingleThreadPerIdentifier: bool): ...
    def dequeue(self, identifier: typing.Any) -> Invocation: ...
    def enqueue(self, invocation: Invocation) -> None: ...
    def getActiveInvocation(self) -> Invocation: ...
    def getScheduler(self) -> java.util.concurrent.ExecutorService: ...
    def recordCallEnd(self, invocation: Invocation) -> None: ...
    def recordCallStart(self, invocation: Invocation) -> None: ...
    def setEnforceSingleThreadPerIdentifier(self, enforceSingleThreadPerIdentifier: bool) -> None: ...

_InvocationHandlerSync__T = typing.TypeVar('_InvocationHandlerSync__T')  # <T>
class InvocationHandlerSync(org.openhab.core.internal.common.AbstractInvocationHandler[_InvocationHandlerSync__T], java.lang.reflect.InvocationHandler, typing.Generic[_InvocationHandlerSync__T]):
    """
    Java class 'org.openhab.core.internal.common.InvocationHandlerSync'
    
        Extends:
            org.openhab.core.internal.common.AbstractInvocationHandler
    
        Interfaces:
            java.lang.reflect.InvocationHandler
    
      Constructors:
        * InvocationHandlerSync(org.openhab.core.internal.common.SafeCallManager, java.lang.Object, java.lang.Object, long, java.util.function.Consumer, java.lang.Runnable)
    
    """
    def __init__(self, manager: SafeCallManager, target: _InvocationHandlerSync__T, identifier: typing.Any, timeout: int, exceptionHandler: typing.Union[java.util.function.Consumer[java.lang.Throwable], typing.Callable[[], java.lang.Throwable]], timeoutHandler: java.lang.Runnable): ...
    def invoke(self, proxy: typing.Any, method: java.lang.reflect.Method, args: typing.List[typing.Any]) -> typing.Any: ...

class AbstractInvocationHandler: ...
