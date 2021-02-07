import java.lang
import java.util
import org.openhab.core.config.discovery
import org.openhab.core.config.discovery.inbox
import org.openhab.core.io.console
import org.openhab.core.io.console.extensions
import org.osgi.service.cm
import typing


class DiscoveryConsoleCommandExtension(org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension):
    """
    Java class 'org.openhab.core.config.discovery.internal.console.DiscoveryConsoleCommandExtension'
    
        Extends:
            org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension
    
      Constructors:
        * DiscoveryConsoleCommandExtension(org.openhab.core.config.discovery.DiscoveryServiceRegistry, org.osgi.service.cm.ConfigurationAdmin)
    
    """
    def __init__(self, discoveryServiceRegistry: org.openhab.core.config.discovery.DiscoveryServiceRegistry, configurationAdmin: org.osgi.service.cm.ConfigurationAdmin): ...
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...

class InboxConsoleCommandExtension(org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension):
    """
    Java class 'org.openhab.core.config.discovery.internal.console.InboxConsoleCommandExtension'
    
        Extends:
            org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension
    
      Constructors:
        * InboxConsoleCommandExtension(org.openhab.core.config.discovery.inbox.Inbox)
    
    """
    def __init__(self, inbox: org.openhab.core.config.discovery.inbox.Inbox): ...
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...
