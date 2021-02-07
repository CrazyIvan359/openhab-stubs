import java.io
import java.lang
import java.util
import org.openhab.core.events
import org.osgi.service.event
import typing


class EventHandler(java.lang.AutoCloseable):
    """
    Java class 'org.openhab.core.internal.events.EventHandler'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.lang.AutoCloseable
    
      Constructors:
        * EventHandler(java.util.Map, java.util.Map)
    
    """
    def __init__(self, typedEventSubscribers: typing.Union[java.util.Map[java.lang.String, java.util.Set[org.openhab.core.events.EventSubscriber]], typing.Mapping[java.lang.String, java.util.Set[org.openhab.core.events.EventSubscriber]]], typedEventFactories: typing.Union[java.util.Map[java.lang.String, org.openhab.core.events.EventFactory], typing.Mapping[java.lang.String, org.openhab.core.events.EventFactory]]): ...
    def close(self) -> None: ...
    def handleEvent(self, osgiEvent: org.osgi.service.event.Event) -> None: ...

class OSGiEventManager(org.osgi.service.event.EventHandler):
    """
    Java class 'org.openhab.core.internal.events.OSGiEventManager'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.osgi.service.event.EventHandler
    
      Constructors:
        * OSGiEventManager()
    
    """
    def __init__(self): ...
    def handleEvent(self, osgiEvent: org.osgi.service.event.Event) -> None: ...

class OSGiEventPublisher(org.openhab.core.events.EventPublisher):
    """
    Java class 'org.openhab.core.internal.events.OSGiEventPublisher'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.events.EventPublisher
    
      Constructors:
        * OSGiEventPublisher()
    
    """
    def __init__(self): ...
    def post(self, event: org.openhab.core.events.Event) -> None: ...

class ThreadedEventHandler(java.io.Closeable):
    """
    Java class 'org.openhab.core.internal.events.ThreadedEventHandler'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Closeable
    
    """
    def close(self) -> None: ...
