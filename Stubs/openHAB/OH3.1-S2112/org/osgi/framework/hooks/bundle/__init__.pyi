import java.lang
import java.util
import org.osgi.framework
import typing


class CollisionHook(java.lang.Object):
    """
    Java class 'org.osgi.framework.hooks.bundle.CollisionHook'
    
      Attributes:
        INSTALLING (int): final static field
        UPDATING (int): final static field
    
    """
    INSTALLING: typing.ClassVar[int] = ...
    UPDATING: typing.ClassVar[int] = ...
    def filterCollisions(self, int: int, bundle: org.osgi.framework.Bundle, collection: typing.Union[java.util.Collection[org.osgi.framework.Bundle], typing.Sequence[org.osgi.framework.Bundle]]) -> None: ...

class EventHook(java.lang.Object):
    """
    Java class 'org.osgi.framework.hooks.bundle.EventHook'
    
    """
    def event(self, bundleEvent: org.osgi.framework.BundleEvent, collection: typing.Union[java.util.Collection[org.osgi.framework.BundleContext], typing.Sequence[org.osgi.framework.BundleContext]]) -> None: ...

class FindHook(java.lang.Object):
    """
    Java class 'org.osgi.framework.hooks.bundle.FindHook'
    
    """
    def find(self, bundleContext: org.osgi.framework.BundleContext, collection: typing.Union[java.util.Collection[org.osgi.framework.Bundle], typing.Sequence[org.osgi.framework.Bundle]]) -> None: ...
