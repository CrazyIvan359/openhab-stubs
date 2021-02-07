import java.lang
import java.util
import org.openhab.core.io.console
import typing


class ConsoleCommandExtension(java.lang.Object):
    """
    @NonNullByDefault public interface ConsoleCommandExtension
    
        Client which provide a console command have to implement this interface
    
    
    """
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getCommand(self) -> java.lang.String: ...
    def getDescription(self) -> java.lang.String: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...

class AbstractConsoleCommandExtension(ConsoleCommandExtension):
    """
    Java class 'org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.console.extensions.ConsoleCommandExtension
    
      Constructors:
        * AbstractConsoleCommandExtension(java.lang.String, java.lang.String)
    
    """
    def __init__(self, cmd: java.lang.String, desc: java.lang.String): ...
    def getCommand(self) -> java.lang.String: ...
    def getDescription(self) -> java.lang.String: ...
