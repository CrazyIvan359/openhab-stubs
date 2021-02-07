import java.lang
import org.eclipse.osgi.framework.console
import org.openhab.core.io.console
import org.openhab.core.io.console.extensions
import typing


class ConsoleSupportEclipse(org.eclipse.osgi.framework.console.CommandProvider):
    """
    Java class 'org.openhab.core.io.console.eclipse.internal.ConsoleSupportEclipse'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.eclipse.osgi.framework.console.CommandProvider
    
      Constructors:
        * ConsoleSupportEclipse()
    
    """
    def __init__(self): ...
    def _openhab(self, interpreter: org.eclipse.osgi.framework.console.CommandInterpreter) -> typing.Any: ...
    def addConsoleCommandExtension(self, consoleCommandExtension: org.openhab.core.io.console.extensions.ConsoleCommandExtension) -> None: ...
    def getHelp(self) -> java.lang.String: ...
    def removeConsoleCommandExtension(self, consoleCommandExtension: org.openhab.core.io.console.extensions.ConsoleCommandExtension) -> None: ...

class OSGiConsole(org.openhab.core.io.console.Console):
    """
    Java class 'org.openhab.core.io.console.eclipse.internal.OSGiConsole'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.console.Console
    
      Constructors:
        * OSGiConsole(java.lang.String, org.eclipse.osgi.framework.console.CommandInterpreter)
    
    """
    def __init__(self, baseCommand: java.lang.String, interpreter: org.eclipse.osgi.framework.console.CommandInterpreter): ...
    def printUsage(self, s: java.lang.String) -> None: ...
    def println(self, s: java.lang.String) -> None: ...
