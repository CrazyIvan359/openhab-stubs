import java.lang
import java.util
import org.openhab.core.auth
import org.openhab.core.events
import org.openhab.core.io.console
import org.openhab.core.io.console.extensions
import org.openhab.core.items
import typing


class ItemConsoleCommandExtension(org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension):
    """
    Java class 'org.openhab.core.io.console.internal.extension.ItemConsoleCommandExtension'
    
        Extends:
            org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension
    
      Constructors:
        * ItemConsoleCommandExtension(org.openhab.core.items.ItemRegistry, org.openhab.core.items.ManagedItemProvider)
    
    """
    def __init__(self, itemRegistry: org.openhab.core.items.ItemRegistry, managedItemProvider: org.openhab.core.items.ManagedItemProvider): ...
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...

class MetadataConsoleCommandExtension(org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension):
    """
    Java class 'org.openhab.core.io.console.internal.extension.MetadataConsoleCommandExtension'
    
        Extends:
            org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension
    
      Constructors:
        * MetadataConsoleCommandExtension(org.openhab.core.items.ItemRegistry, org.openhab.core.items.MetadataRegistry)
    
    """
    def __init__(self, itemRegistry: org.openhab.core.items.ItemRegistry, metadataRegistry: org.openhab.core.items.MetadataRegistry): ...
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...

class SendConsoleCommandExtension(org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension):
    """
    Java class 'org.openhab.core.io.console.internal.extension.SendConsoleCommandExtension'
    
        Extends:
            org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension
    
      Constructors:
        * SendConsoleCommandExtension(org.openhab.core.items.ItemRegistry, org.openhab.core.events.EventPublisher)
    
    """
    def __init__(self, itemRegistry: org.openhab.core.items.ItemRegistry, eventPublisher: org.openhab.core.events.EventPublisher): ...
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...

class StatusConsoleCommandExtension(org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension):
    """
    Java class 'org.openhab.core.io.console.internal.extension.StatusConsoleCommandExtension'
    
        Extends:
            org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension
    
      Constructors:
        * StatusConsoleCommandExtension(org.openhab.core.items.ItemRegistry)
    
    """
    def __init__(self, itemRegistry: org.openhab.core.items.ItemRegistry): ...
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...

class UpdateConsoleCommandExtension(org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension):
    """
    Java class 'org.openhab.core.io.console.internal.extension.UpdateConsoleCommandExtension'
    
        Extends:
            org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension
    
      Constructors:
        * UpdateConsoleCommandExtension(org.openhab.core.items.ItemRegistry, org.openhab.core.events.EventPublisher)
    
    """
    def __init__(self, itemRegistry: org.openhab.core.items.ItemRegistry, eventPublisher: org.openhab.core.events.EventPublisher): ...
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...

class UserConsoleCommandExtension(org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension):
    """
    Java class 'org.openhab.core.io.console.internal.extension.UserConsoleCommandExtension'
    
        Extends:
            org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension
    
      Constructors:
        * UserConsoleCommandExtension(org.openhab.core.auth.UserRegistry)
    
    """
    def __init__(self, userRegistry: org.openhab.core.auth.UserRegistry): ...
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...
