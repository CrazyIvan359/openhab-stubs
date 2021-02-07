import java.lang
import java.util
import org.openhab.core.io.console
import org.openhab.core.io.console.extensions
import org.openhab.core.model.script.engine
import typing


class ScriptEngineConsoleCommandExtension(org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension):
    """
    Java class 'org.openhab.core.model.script.extension.ScriptEngineConsoleCommandExtension'
    
        Extends:
            org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension
    
      Constructors:
        * ScriptEngineConsoleCommandExtension()
    
    """
    def __init__(self): ...
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...
    def setScriptEngine(self, scriptEngine: org.openhab.core.model.script.engine.ScriptEngine) -> None: ...
    def unsetScriptEngine(self, scriptEngine: org.openhab.core.model.script.engine.ScriptEngine) -> None: ...
