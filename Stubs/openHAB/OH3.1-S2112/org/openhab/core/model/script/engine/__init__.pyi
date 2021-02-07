import java.lang
import java.util
import org.eclipse.emf.ecore
import org.eclipse.emf.ecore.resource
import org.eclipse.xtext.validation
import org.eclipse.xtext.xbase
import org.eclipse.xtext.xbase.interpreter
import org.openhab.core.model.script.engine.action
import org.openhab.core.thing.binding
import typing


class IActionServiceProvider(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.engine.IActionServiceProvider'
    
    """
    def get(self) -> java.util.List[org.openhab.core.model.script.engine.action.ActionService]: ...

class IThingActionsProvider(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.engine.IThingActionsProvider'
    
    """
    def get(self) -> java.util.List[org.openhab.core.thing.binding.ThingActions]: ...

class Script(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.engine.Script'
    
      Attributes:
        SCRIPT_FILEEXT (java.lang.String): final static field
    
    """
    SCRIPT_FILEEXT: typing.ClassVar[java.lang.String] = ...
    @typing.overload
    def execute(self) -> typing.Any: ...
    @typing.overload
    def execute(self, evaluationContext: org.eclipse.xtext.xbase.interpreter.IEvaluationContext) -> typing.Any: ...

class ScriptEngine(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.engine.ScriptEngine'
    
    """
    def executeScript(self, scriptAsString: java.lang.String) -> typing.Any: ...
    def newScriptFromString(self, scriptAsString: java.lang.String) -> Script: ...
    def newScriptFromXExpression(self, expression: org.eclipse.xtext.xbase.XExpression) -> Script: ...

class ScriptError(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.engine.ScriptError'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ScriptError(java.lang.String, int, int, int)
        * ScriptError(java.lang.String, org.eclipse.emf.ecore.EObject)
    
    """
    @typing.overload
    def __init__(self, message: java.lang.String, line: int, column: int, length: int): ...
    @typing.overload
    def __init__(self, message: java.lang.String, atEObject: org.eclipse.emf.ecore.EObject): ...
    def getColumnNumber(self) -> int: ...
    def getLength(self) -> int: ...
    def getLineNumber(self) -> int: ...
    def getMessage(self) -> java.lang.String: ...

class ScriptException(java.lang.Exception):
    """
    Java class 'org.openhab.core.model.script.engine.ScriptException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * ScriptException(java.lang.String, java.lang.String, int, int, int)
        * ScriptException(java.lang.Throwable, java.lang.String, java.lang.String, int, int, int)
        * ScriptException(java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, message: java.lang.String, scriptText: java.lang.String, line: int, column: int, length: int): ...
    @typing.overload
    def __init__(self, message: java.lang.String, cause: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, cause: java.lang.Throwable, message: java.lang.String, scriptText: java.lang.String, line: int, column: int, length: int): ...
    def getErrors(self) -> java.util.List[ScriptError]: ...
    def getMessage(self) -> java.lang.String: ...
    def setScriptText(self, scriptText: java.lang.String) -> None: ...

class ScriptExecutionException(ScriptException):
    """
    Java class 'org.openhab.core.model.script.engine.ScriptExecutionException'
    
        Extends:
            org.openhab.core.model.script.engine.ScriptException
    
      Constructors:
        * ScriptExecutionException(java.lang.String, java.lang.Throwable)
        * ScriptExecutionException(java.lang.String)
        * ScriptExecutionException(java.lang.String, java.lang.Throwable, int, int, int)
        * ScriptExecutionException(org.openhab.core.model.script.engine.ScriptError)
        * ScriptExecutionException(java.lang.String, int, int, int)
    
    """
    @typing.overload
    def __init__(self, message: java.lang.String): ...
    @typing.overload
    def __init__(self, message: java.lang.String, line: int, column: int, length: int): ...
    @typing.overload
    def __init__(self, message: java.lang.String, exception: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, message: java.lang.String, cause: java.lang.Throwable, line: int, column: int, length: int): ...
    @typing.overload
    def __init__(self, scriptError: ScriptError): ...

class ScriptParsingException(ScriptException):
    """
    Java class 'org.openhab.core.model.script.engine.ScriptParsingException'
    
        Extends:
            org.openhab.core.model.script.engine.ScriptException
    
      Constructors:
        * ScriptParsingException(java.lang.String, java.lang.String)
        * ScriptParsingException(java.lang.String, java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, message: java.lang.String, scriptAsString: java.lang.String): ...
    @typing.overload
    def __init__(self, message: java.lang.String, scriptAsString: java.lang.String, t: java.lang.Throwable): ...
    def addDiagnosticErrors(self, errors: java.util.List[org.eclipse.emf.ecore.resource.Resource.Diagnostic]) -> 'ScriptParsingException': ...
    def addValidationIssues(self, validationErrors: java.lang.Iterable[org.eclipse.xtext.validation.Issue]) -> 'ScriptParsingException': ...
