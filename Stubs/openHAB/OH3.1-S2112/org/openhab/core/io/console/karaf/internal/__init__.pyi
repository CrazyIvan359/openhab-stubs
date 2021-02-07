import java.lang
import java.util
import org.apache.karaf.shell.api.action
import org.apache.karaf.shell.api.console
import org.openhab.core.io.console
import org.openhab.core.io.console.extensions
import typing


class CommandWrapper(org.apache.karaf.shell.api.console.Command, org.apache.karaf.shell.api.action.Action):
    """
    Java class 'org.openhab.core.io.console.karaf.internal.CommandWrapper'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.apache.karaf.shell.api.console.Command,
            org.apache.karaf.shell.api.action.Action
    
      Constructors:
        * CommandWrapper()
        * CommandWrapper(org.openhab.core.io.console.extensions.ConsoleCommandExtension)
    
      Attributes:
        SCOPE (java.lang.String): final static field
    
    """
    SCOPE: typing.ClassVar[java.lang.String] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, command: org.openhab.core.io.console.extensions.ConsoleCommandExtension): ...
    @typing.overload
    def execute(self) -> typing.Any: ...
    @typing.overload
    def execute(self, session: org.apache.karaf.shell.api.console.Session, argList: java.util.List[typing.Any]) -> typing.Any: ...
    def getCompleter(self, arg0: bool) -> org.apache.karaf.shell.api.console.Completer: ...
    def getDescription(self) -> java.lang.String: ...
    def getName(self) -> java.lang.String: ...
    def getParser(self) -> org.apache.karaf.shell.api.console.Parser: ...
    def getScope(self) -> java.lang.String: ...

class ConsoleSupportKaraf(java.lang.Object):
    """
    Java class 'org.openhab.core.io.console.karaf.internal.ConsoleSupportKaraf'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConsoleSupportKaraf()
    
    """
    def __init__(self): ...
    def addConsoleCommandExtension(self, consoleCommandExtension: org.openhab.core.io.console.extensions.ConsoleCommandExtension) -> None: ...
    def removeConsoleCommandExtension(self, consoleCommandExtension: org.openhab.core.io.console.extensions.ConsoleCommandExtension) -> None: ...
    def setSessionFactory(self, sessionFactory: org.apache.karaf.shell.api.console.SessionFactory) -> None: ...
    def unsetSessionFactory(self, sessionFactory: org.apache.karaf.shell.api.console.SessionFactory) -> None: ...

class OSGiConsole(org.openhab.core.io.console.Console):
    """
    Java class 'org.openhab.core.io.console.karaf.internal.OSGiConsole'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.console.Console
    
      Constructors:
        * OSGiConsole(java.lang.String)
    
    """
    def __init__(self, scope: java.lang.String): ...
    def printUsage(self, s: java.lang.String) -> None: ...
    def printf(self, format: java.lang.String, args: typing.List[typing.Any]) -> None: ...
    def println(self, s: java.lang.String) -> None: ...
