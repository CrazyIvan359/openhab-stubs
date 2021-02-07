import org.eclipse.xtext.common.types
import org.eclipse.xtext.util
import org.eclipse.xtext.xbase
import org.eclipse.xtext.xbase.interpreter
import org.eclipse.xtext.xbase.interpreter.impl
import typing


class ScriptInterpreter(org.eclipse.xtext.xbase.interpreter.impl.XbaseInterpreter):
    """
    Java class 'org.openhab.core.model.script.interpreter.ScriptInterpreter'
    
        Extends:
            org.eclipse.xtext.xbase.interpreter.impl.XbaseInterpreter
    
      Constructors:
        * ScriptInterpreter()
    
    """
    def __init__(self): ...
    def _assignValueTo(self, jvmField: org.eclipse.xtext.common.types.JvmField, assignment: org.eclipse.xtext.xbase.XAbstractFeatureCall, value: typing.Any, context: org.eclipse.xtext.xbase.interpreter.IEvaluationContext, indicator: org.eclipse.xtext.util.CancelIndicator) -> typing.Any: ...
    def _doEvaluate(self, castedExpression: org.eclipse.xtext.xbase.XCastedExpression, context: org.eclipse.xtext.xbase.interpreter.IEvaluationContext, indicator: org.eclipse.xtext.util.CancelIndicator) -> typing.Any: ...
