import java.io
import java.lang
import java.util
import javax.script
import org.eclipse.xtext.xbase
import org.eclipse.xtext.xbase.interpreter
import org.openhab.core.automation.module.script
import org.openhab.core.model.core
import org.openhab.core.model.script.engine
import org.openhab.core.model.script.runtime
import typing


class DSLScriptEngine(javax.script.ScriptEngine):
    """
    Java class 'org.openhab.core.model.script.runtime.internal.engine.DSLScriptEngine'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            javax.script.ScriptEngine
    
      Constructors:
        * DSLScriptEngine(org.openhab.core.model.script.engine.ScriptEngine, org.openhab.core.model.script.runtime.DSLScriptContextProvider)
    
      Attributes:
        MIMETYPE_OPENHAB_DSL_RULE (java.lang.String): final static field
    
    """
    MIMETYPE_OPENHAB_DSL_RULE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, scriptEngine: org.openhab.core.model.script.engine.ScriptEngine, contextProvider: org.openhab.core.model.script.runtime.DSLScriptContextProvider): ...
    def createBindings(self) -> javax.script.Bindings: ...
    @typing.overload
    def eval(self, reader: java.io.Reader) -> typing.Any: ...
    @typing.overload
    def eval(self, reader: java.io.Reader, n: javax.script.Bindings) -> typing.Any: ...
    @typing.overload
    def eval(self, reader: java.io.Reader, context: javax.script.ScriptContext) -> typing.Any: ...
    @typing.overload
    def eval(self, script: java.lang.String) -> typing.Any: ...
    @typing.overload
    def eval(self, script: java.lang.String, n: javax.script.Bindings) -> typing.Any: ...
    @typing.overload
    def eval(self, script: java.lang.String, context: javax.script.ScriptContext) -> typing.Any: ...
    def get(self, key: java.lang.String) -> typing.Any: ...
    def getBindings(self, scope: int) -> javax.script.Bindings: ...
    def getContext(self) -> javax.script.ScriptContext: ...
    def getFactory(self) -> javax.script.ScriptEngineFactory: ...
    def put(self, key: java.lang.String, value: typing.Any) -> None: ...
    def setBindings(self, bindings: javax.script.Bindings, scope: int) -> None: ...
    def setContext(self, context: javax.script.ScriptContext) -> None: ...

class DSLScriptEngineFactory(org.openhab.core.automation.module.script.ScriptEngineFactory):
    """
    Java class 'org.openhab.core.model.script.runtime.internal.engine.DSLScriptEngineFactory'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.module.script.ScriptEngineFactory
    
      Constructors:
        * DSLScriptEngineFactory(org.openhab.core.model.script.engine.ScriptEngine)
    
    """
    def __init__(self, scriptEngine: org.openhab.core.model.script.engine.ScriptEngine): ...
    def createScriptEngine(self, scriptType: java.lang.String) -> javax.script.ScriptEngine: ...
    def getScriptTypes(self) -> java.util.List[java.lang.String]: ...
    def scopeValues(self, scriptEngine: javax.script.ScriptEngine, scopeValues: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...

class ScriptEngineImpl(org.openhab.core.model.script.engine.ScriptEngine, org.openhab.core.model.core.ModelParser):
    """
    Java class 'org.openhab.core.model.script.runtime.internal.engine.ScriptEngineImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.script.engine.ScriptEngine,
            org.openhab.core.model.core.ModelParser
    
      Constructors:
        * ScriptEngineImpl()
    
    """
    def __init__(self): ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def executeScript(self, scriptAsString: java.lang.String) -> typing.Any: ...
    def getExtension(self) -> java.lang.String: ...
    def newScriptFromString(self, scriptAsString: java.lang.String) -> org.openhab.core.model.script.engine.Script: ...
    def newScriptFromXExpression(self, expression: org.eclipse.xtext.xbase.XExpression) -> org.openhab.core.model.script.engine.Script: ...

class ScriptImpl(org.openhab.core.model.script.engine.Script):
    """
    Java class 'org.openhab.core.model.script.runtime.internal.engine.ScriptImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.script.engine.Script
    
      Constructors:
        * ScriptImpl()
    
    """
    def __init__(self): ...
    @typing.overload
    def execute(self) -> typing.Any: ...
    @typing.overload
    def execute(self, evaluationContext: org.eclipse.xtext.xbase.interpreter.IEvaluationContext) -> typing.Any: ...
