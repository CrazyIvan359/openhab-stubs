import java.lang
import java.util
import org.openhab.core.io.console.extensions
import typing


class Console(java.lang.Object):
    """
    public interface Console
    
        This interface must be implemented by consoles which want to use the
        :class:`~org.openhab.core.io.console.ConsoleInterpreter`. It allows basic output commands.
    
    
    """
    def printUsage(self, s: java.lang.String) -> None: ...
    def printf(self, format: java.lang.String, args: typing.List[typing.Any]) -> None: ...
    def println(self, s: java.lang.String) -> None: ...

class ConsoleInterpreter(java.lang.Object):
    """
    Java class 'org.openhab.core.io.console.ConsoleInterpreter'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConsoleInterpreter()
    
    """
    def __init__(self): ...
    @classmethod
    def execute(cls, console: Console, extension: org.openhab.core.io.console.extensions.ConsoleCommandExtension, args: typing.List[java.lang.String]) -> None: ...
    @classmethod
    def getHelp(cls, base: java.lang.String, separator: java.lang.String, extensions: typing.Union[java.util.Collection[org.openhab.core.io.console.extensions.ConsoleCommandExtension], typing.Sequence[org.openhab.core.io.console.extensions.ConsoleCommandExtension]]) -> java.lang.String: ...
    @classmethod
    def getUsage(cls, consoleCommandExtensions: typing.Union[java.util.Collection[org.openhab.core.io.console.extensions.ConsoleCommandExtension], typing.Sequence[org.openhab.core.io.console.extensions.ConsoleCommandExtension]]) -> java.lang.String: ...
    @classmethod
    def getUsages(cls, consoleCommandExtensions: typing.Union[java.util.Collection[org.openhab.core.io.console.extensions.ConsoleCommandExtension], typing.Sequence[org.openhab.core.io.console.extensions.ConsoleCommandExtension]]) -> java.util.List[java.lang.String]: ...
    @classmethod
    def printHelp(cls, console: Console, base: java.lang.String, separator: java.lang.String, extensions: typing.Union[java.util.Collection[org.openhab.core.io.console.extensions.ConsoleCommandExtension], typing.Sequence[org.openhab.core.io.console.extensions.ConsoleCommandExtension]]) -> None: ...
