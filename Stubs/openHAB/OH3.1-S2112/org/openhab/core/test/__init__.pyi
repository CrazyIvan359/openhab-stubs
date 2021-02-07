import java.lang
import java.util
import java.util.concurrent
import org.eclipse.jetty.servlet
import org.osgi.framework
import typing


_AsyncResultWrapper__T = typing.TypeVar('_AsyncResultWrapper__T')  # <T>
class AsyncResultWrapper(java.lang.Object, typing.Generic[_AsyncResultWrapper__T]):
    """
    Java class 'org.openhab.core.test.AsyncResultWrapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * AsyncResultWrapper()
    
    """
    def __init__(self): ...
    def getWrappedObject(self) -> _AsyncResultWrapper__T: ...
    def isSet(self) -> bool: ...
    def reset(self) -> None: ...
    def set(self, wrappedObject: _AsyncResultWrapper__T) -> None: ...

class BundleCloseable(java.lang.AutoCloseable):
    """
    Java class 'org.openhab.core.test.BundleCloseable'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.lang.AutoCloseable
    
      Constructors:
        * BundleCloseable(org.osgi.framework.Bundle)
    
    """
    def __init__(self, bundle: org.osgi.framework.Bundle): ...
    def bundle(self) -> org.osgi.framework.Bundle: ...
    def close(self) -> None: ...

class SyntheticBundleInstaller(java.lang.Object):
    """
    Java class 'org.openhab.core.test.SyntheticBundleInstaller'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SyntheticBundleInstaller()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def install(cls, bundleContext: org.osgi.framework.BundleContext, testBundleName: java.lang.String) -> org.osgi.framework.Bundle: ...
    @classmethod
    @typing.overload
    def install(cls, bundleContext: org.osgi.framework.BundleContext, testBundleName: java.lang.String, extensionsToInclude: typing.List[java.lang.String]) -> org.osgi.framework.Bundle: ...
    @classmethod
    @typing.overload
    def install(cls, bundleContext: org.osgi.framework.BundleContext, testBundleName: java.lang.String, extensionsToInclude: java.util.Set[java.lang.String]) -> org.osgi.framework.Bundle: ...
    @classmethod
    @typing.overload
    def installFragment(cls, bundleContext: org.osgi.framework.BundleContext, testBundleName: java.lang.String) -> org.osgi.framework.Bundle: ...
    @classmethod
    @typing.overload
    def installFragment(cls, bundleContext: org.osgi.framework.BundleContext, testBundleName: java.lang.String, extensionsToInclude: java.util.Set[java.lang.String]) -> org.osgi.framework.Bundle: ...
    @classmethod
    @typing.overload
    def uninstall(cls, bundle: org.osgi.framework.Bundle) -> None: ...
    @classmethod
    @typing.overload
    def uninstall(cls, bundleContext: org.osgi.framework.BundleContext, testBundleName: java.lang.String) -> None: ...
    @classmethod
    @typing.overload
    def update(cls, bundleContext: org.osgi.framework.BundleContext, bundleToUpdateName: java.lang.String, updateDirName: java.lang.String) -> org.osgi.framework.Bundle: ...
    @classmethod
    @typing.overload
    def update(cls, bundleContext: org.osgi.framework.BundleContext, bundleToUpdateName: java.lang.String, updateDirName: java.lang.String, extensionsToInclude: typing.List[java.lang.String]) -> org.osgi.framework.Bundle: ...
    @classmethod
    @typing.overload
    def update(cls, bundleContext: org.osgi.framework.BundleContext, bundleToUpdateName: java.lang.String, updateDirName: java.lang.String, extensionsToInclude: java.util.Set[java.lang.String]) -> org.osgi.framework.Bundle: ...
    @classmethod
    def waitUntilLoadingFinished(cls, context: org.osgi.framework.BundleContext, bundle: org.osgi.framework.Bundle) -> None: ...

class TestPortUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.test.TestPortUtil'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def findFreePort(cls) -> int: ...

class TestServer(java.lang.Object):
    """
    Java class 'org.openhab.core.test.TestServer'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * TestServer(java.lang.String, int, int, org.eclipse.jetty.servlet.ServletHolder)
    
    """
    def __init__(self, host: java.lang.String, port: int, timeout: int, servletHolder: org.eclipse.jetty.servlet.ServletHolder): ...
    def startServer(self) -> java.util.concurrent.CompletableFuture[bool]: ...
    def stopServer(self) -> None: ...
