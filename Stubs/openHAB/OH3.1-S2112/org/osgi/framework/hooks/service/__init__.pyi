import java.lang
import java.util
import org.osgi.framework
import typing


class EventHook(java.lang.Object):
    """
    Java class 'org.osgi.framework.hooks.service.EventHook'
    
    """
    def event(self, serviceEvent: org.osgi.framework.ServiceEvent, collection: typing.Union[java.util.Collection[org.osgi.framework.BundleContext], typing.Sequence[org.osgi.framework.BundleContext]]) -> None: ...

class EventListenerHook(java.lang.Object):
    """
    Java class 'org.osgi.framework.hooks.service.EventListenerHook'
    
    """
    def event(self, serviceEvent: org.osgi.framework.ServiceEvent, map: typing.Union[java.util.Map[org.osgi.framework.BundleContext, typing.Union[java.util.Collection['ListenerHook.ListenerInfo'], typing.Sequence['ListenerHook.ListenerInfo']]], typing.Mapping[org.osgi.framework.BundleContext, typing.Union[java.util.Collection['ListenerHook.ListenerInfo'], typing.Sequence['ListenerHook.ListenerInfo']]]]) -> None: ...

class FindHook(java.lang.Object):
    """
    Java class 'org.osgi.framework.hooks.service.FindHook'
    
    """
    def find(self, bundleContext: org.osgi.framework.BundleContext, string: java.lang.String, string2: java.lang.String, boolean: bool, collection: typing.Union[java.util.Collection[org.osgi.framework.ServiceReference[typing.Any]], typing.Sequence[org.osgi.framework.ServiceReference[typing.Any]]]) -> None: ...

class ListenerHook(java.lang.Object):
    """
    Java class 'org.osgi.framework.hooks.service.ListenerHook'
    
    """
    def added(self, collection: typing.Union[java.util.Collection['ListenerHook.ListenerInfo'], typing.Sequence['ListenerHook.ListenerInfo']]) -> None: ...
    def removed(self, collection: typing.Union[java.util.Collection['ListenerHook.ListenerInfo'], typing.Sequence['ListenerHook.ListenerInfo']]) -> None: ...
    class ListenerInfo(java.lang.Object):
        """
        Java class 'org.osgi.framework.hooks.service.ListenerHook$ListenerInfo'
        
        """
        def equals(self, object: typing.Any) -> bool: ...
        def getBundleContext(self) -> org.osgi.framework.BundleContext: ...
        def getFilter(self) -> java.lang.String: ...
        def hashCode(self) -> int: ...
        def isRemoved(self) -> bool: ...
