import java.lang
import org.eclipse.xtext.xbase
import org.eclipse.xtext.xbase.interpreter
import typing


class DSLScriptContextProvider(java.lang.Object):
    """
    @NonNullByDefault public interface DSLScriptContextProvider
    
        Interface of a provider that can provide Xbase-relevant object structures for a purely string based script. This is
        required to support DSL rules, which can have a context (variables) per file that is shared among multiple rules.
    
    
    """
    CONTEXT_IDENTIFIER: typing.ClassVar[java.lang.String] = ...
    def getContext(self, contextName: java.lang.String) -> org.eclipse.xtext.xbase.interpreter.IEvaluationContext: ...
    def getParsedScript(self, contextName: java.lang.String, ruleIndex: java.lang.String) -> org.eclipse.xtext.xbase.XExpression: ...

class ScriptRuntime(java.lang.Object):
    """
    public interface ScriptRuntime
    
        This is a marker interface for Script Runtimes.
    
    
    """
