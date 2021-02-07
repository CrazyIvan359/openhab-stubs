import java.lang
import javax.ws.rs.core
import org.openhab.core.config.discovery
import org.openhab.core.config.discovery.inbox
import org.openhab.core.io.rest
import typing


class DiscoveryResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.core.internal.discovery.DiscoveryResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * DiscoveryResource(org.openhab.core.config.discovery.DiscoveryServiceRegistry)
    
      Attributes:
        PATH_DISCOVERY (java.lang.String): final static field
    
    """
    PATH_DISCOVERY: typing.ClassVar[java.lang.String] = ...
    def __init__(self, discoveryServiceRegistry: org.openhab.core.config.discovery.DiscoveryServiceRegistry): ...
    def getDiscoveryServices(self) -> javax.ws.rs.core.Response: ...
    def scan(self, bindingId: java.lang.String) -> javax.ws.rs.core.Response: ...

class InboxResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.core.internal.discovery.InboxResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * InboxResource(org.openhab.core.config.discovery.inbox.Inbox)
    
      Attributes:
        PATH_INBOX (java.lang.String): final static field
    
    """
    PATH_INBOX: typing.ClassVar[java.lang.String] = ...
    def __init__(self, inbox: org.openhab.core.config.discovery.inbox.Inbox): ...
    def approve(self, language: java.lang.String, thingUID: java.lang.String, label: java.lang.String, newThingId: java.lang.String) -> javax.ws.rs.core.Response: ...
    def delete(self, thingUID: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getAll(self) -> javax.ws.rs.core.Response: ...
    def ignore(self, thingUID: java.lang.String) -> javax.ws.rs.core.Response: ...
    def unignore(self, thingUID: java.lang.String) -> javax.ws.rs.core.Response: ...
