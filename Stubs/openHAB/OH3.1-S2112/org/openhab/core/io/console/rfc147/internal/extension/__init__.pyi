import java.lang
import java.util
import org.openhab.core.io.console
import org.openhab.core.io.console.extensions
import org.openhab.core.io.console.rfc147.internal
import typing


class HelpConsoleCommandExtension(org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension):
    """
    Java class 'org.openhab.core.io.console.rfc147.internal.extension.HelpConsoleCommandExtension'
    
        Extends:
            org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension
    
      Constructors:
        * HelpConsoleCommandExtension()
    
    """
    def __init__(self): ...
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...
    def help(self, args: typing.List[java.lang.String]) -> None: ...
    def setConsoleCommandsContainer(self, commandsContainer: org.openhab.core.io.console.rfc147.internal.ConsoleCommandsContainer) -> None: ...
