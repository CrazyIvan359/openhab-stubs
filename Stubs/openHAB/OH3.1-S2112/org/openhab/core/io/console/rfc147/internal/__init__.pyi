import java.lang
import java.util
import org.openhab.core.io.console
import org.openhab.core.io.console.extensions
import org.osgi.service.component
import typing


class CommandWrapper(java.lang.Object):
    """
    Java class 'org.openhab.core.io.console.rfc147.internal.CommandWrapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * CommandWrapper(org.openhab.core.io.console.extensions.ConsoleCommandExtension)
    
    """
    def __init__(self, command: org.openhab.core.io.console.extensions.ConsoleCommandExtension): ...
    def _main(self, args: typing.List[java.lang.String]) -> None: ...

class ConsoleCommandsContainer(java.lang.Object):
    """
    Java class 'org.openhab.core.io.console.rfc147.internal.ConsoleCommandsContainer'
    
    """
    def getConsoleCommandExtensions(self) -> java.util.Collection[org.openhab.core.io.console.extensions.ConsoleCommandExtension]: ...

class OSGiConsole(org.openhab.core.io.console.Console):
    """
    Java class 'org.openhab.core.io.console.rfc147.internal.OSGiConsole'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.console.Console
    
      Constructors:
        * OSGiConsole(java.lang.String)
    
    """
    def __init__(self, base: java.lang.String): ...
    def getBase(self) -> java.lang.String: ...
    def printUsage(self, s: java.lang.String) -> None: ...
    def printf(self, format: java.lang.String, args: typing.List[typing.Any]) -> None: ...
    def println(self, s: java.lang.String) -> None: ...

class ConsoleSupportRfc147(ConsoleCommandsContainer):
    """
    Java class 'org.openhab.core.io.console.rfc147.internal.ConsoleSupportRfc147'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.console.rfc147.internal.ConsoleCommandsCon
            tainer
    
      Constructors:
        * ConsoleSupportRfc147()
    
      Attributes:
        CONSOLE (org.openhab.core.io.console.rfc147.internal.OSGiConsole): final static field
    
    """
    CONSOLE: typing.ClassVar[OSGiConsole] = ...
    def __init__(self): ...
    def activate(self, ctx: org.osgi.service.component.ComponentContext) -> None: ...
    def addConsoleCommandExtension(self, consoleCommandExtension: org.openhab.core.io.console.extensions.ConsoleCommandExtension) -> None: ...
    def deactivate(self) -> None: ...
    def getConsoleCommandExtensions(self) -> java.util.Collection[org.openhab.core.io.console.extensions.ConsoleCommandExtension]: ...
    def removeConsoleCommandExtension(self, consoleCommandExtension: org.openhab.core.io.console.extensions.ConsoleCommandExtension) -> None: ...
