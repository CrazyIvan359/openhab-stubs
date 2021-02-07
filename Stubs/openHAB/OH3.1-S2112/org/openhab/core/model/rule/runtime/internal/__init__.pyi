import java.lang
import java.util
import org.eclipse.xtext.naming
import org.eclipse.xtext.xbase
import org.eclipse.xtext.xbase.interpreter
import org.eclipse.xtext.xbase.interpreter.impl
import org.openhab.core.automation
import org.openhab.core.common.registry
import org.openhab.core.model.core
import org.openhab.core.model.rule.rules
import org.openhab.core.model.script.engine
import org.openhab.core.model.script.runtime
import org.openhab.core.service
import org.osgi.framework
import typing


class DSLRuleProvider(org.openhab.core.automation.RuleProvider, org.openhab.core.model.core.ModelRepositoryChangeListener, org.openhab.core.model.script.runtime.DSLScriptContextProvider, org.openhab.core.service.ReadyService.ReadyTracker):
    """
    Java class 'org.openhab.core.model.rule.runtime.internal.DSLRuleProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.RuleProvider,
            org.openhab.core.model.core.ModelRepositoryChangeListener, org
            .openhab.core.model.script.runtime.DSLScriptContextProvider,
            org.openhab.core.service.ReadyService.ReadyTracker
    
      Constructors:
        * DSLRuleProvider(org.openhab.core.model.core.ModelRepository, org.openhab.core.service.ReadyService)
    
    """
    def __init__(self, modelRepository: org.openhab.core.model.core.ModelRepository, readyService: org.openhab.core.service.ReadyService): ...
    def addProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[org.openhab.core.automation.Rule]) -> None: ...
    def getAll(self) -> java.util.Collection[org.openhab.core.automation.Rule]: ...
    def getContext(self, contextName: java.lang.String) -> org.eclipse.xtext.xbase.interpreter.IEvaluationContext: ...
    def getParsedScript(self, modelName: java.lang.String, index: java.lang.String) -> org.eclipse.xtext.xbase.XExpression: ...
    def modelChanged(self, modelFileName: java.lang.String, type: org.openhab.core.model.core.EventType) -> None: ...
    def onReadyMarkerAdded(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
    def onReadyMarkerRemoved(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
    def removeProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[org.openhab.core.automation.Rule]) -> None: ...

class RuleContextHelper(java.lang.Object):
    """
    Java class 'org.openhab.core.model.rule.runtime.internal.RuleContextHelper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RuleContextHelper()
    
    """
    def __init__(self): ...
    @classmethod
    def getContext(cls, ruleModel: org.openhab.core.model.rule.rules.RuleModel) -> org.eclipse.xtext.xbase.interpreter.IEvaluationContext: ...
    @classmethod
    def getVariableDeclaration(cls, ruleModel: org.openhab.core.model.rule.rules.RuleModel) -> java.lang.String: ...

class RuleEvaluationContext(org.eclipse.xtext.xbase.interpreter.impl.DefaultEvaluationContext):
    """
    Java class 'org.openhab.core.model.rule.runtime.internal.RuleEvaluationContext'
    
        Extends:
            org.eclipse.xtext.xbase.interpreter.impl.DefaultEvaluationContext
    
      Constructors:
        * RuleEvaluationContext()
    
    """
    def __init__(self): ...
    def assignValue(self, qualifiedName: org.eclipse.xtext.naming.QualifiedName, value: typing.Any) -> None: ...
    def getValue(self, qualifiedName: org.eclipse.xtext.naming.QualifiedName) -> typing.Any: ...
    def setGlobalContext(self, context: org.eclipse.xtext.xbase.interpreter.IEvaluationContext) -> None: ...

class RuleRuntimeActivator(org.openhab.core.model.core.ModelParser):
    """
    Java class 'org.openhab.core.model.rule.runtime.internal.RuleRuntimeActivator'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.core.ModelParser
    
      Constructors:
        * RuleRuntimeActivator()
    
    """
    def __init__(self): ...
    def activate(self, bc: org.osgi.framework.BundleContext) -> None: ...
    def deactivate(self) -> None: ...
    def getExtension(self) -> java.lang.String: ...
    def setScriptEngine(self, scriptEngine: org.openhab.core.model.script.engine.ScriptEngine) -> None: ...
    def unsetScriptEngine(self, scriptEngine: org.openhab.core.model.script.engine.ScriptEngine) -> None: ...
