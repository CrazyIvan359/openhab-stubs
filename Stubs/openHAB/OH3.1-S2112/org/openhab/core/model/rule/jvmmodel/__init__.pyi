import java.lang
import org.eclipse.emf.ecore
import org.eclipse.xtext.xbase.jvmmodel
import org.openhab.core.items
import org.openhab.core.model.core
import org.openhab.core.model.script.jvmmodel
import org.openhab.core.service
import org.openhab.core.thing
import typing


class RulesJvmModelInferrer(org.openhab.core.model.script.jvmmodel.ScriptJvmModelInferrer):
    """
    Java class 'org.openhab.core.model.rule.jvmmodel.RulesJvmModelInferrer'
    
        Extends:
            org.openhab.core.model.script.jvmmodel.ScriptJvmModelInferrer
    
      Constructors:
        * RulesJvmModelInferrer()
    
    """
    def __init__(self): ...
    def infer(self, ruleModel: org.eclipse.emf.ecore.EObject, acceptor: org.eclipse.xtext.xbase.jvmmodel.IJvmDeclaredTypeAcceptor, isPreIndexingPhase: bool) -> None: ...

class RulesRefresher(org.openhab.core.service.ReadyService.ReadyTracker):
    """
    Java class 'org.openhab.core.model.rule.jvmmodel.RulesRefresher'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.service.ReadyService.ReadyTracker
    
      Constructors:
        * RulesRefresher(org.openhab.core.model.core.ModelRepository, org.openhab.core.items.ItemRegistry, org.openhab.core.thing.ThingRegistry, org.openhab.core.service.ReadyService)
    
      Attributes:
        RULES_REFRESH_MARKER_TYPE (java.lang.String): final static field
        RULES_REFRESH (java.lang.String): final static field
    
    """
    RULES_REFRESH_MARKER_TYPE: typing.ClassVar[java.lang.String] = ...
    RULES_REFRESH: typing.ClassVar[java.lang.String] = ...
    def __init__(self, modelRepository: org.openhab.core.model.core.ModelRepository, itemRegistry: org.openhab.core.items.ItemRegistry, thingRegistry: org.openhab.core.thing.ThingRegistry, readyService: org.openhab.core.service.ReadyService): ...
    def onReadyMarkerAdded(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
    def onReadyMarkerRemoved(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
