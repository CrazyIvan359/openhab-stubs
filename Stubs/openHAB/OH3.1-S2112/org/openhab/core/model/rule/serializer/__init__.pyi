import org.eclipse.emf.ecore
import org.eclipse.xtext.serializer
import org.eclipse.xtext.serializer.sequencer
import org.openhab.core.model.script.serializer


class AbstractRulesSemanticSequencer(org.openhab.core.model.script.serializer.ScriptSemanticSequencer):
    """
    Java class 'org.openhab.core.model.rule.serializer.AbstractRulesSemanticSequencer'
    
        Extends:
            org.openhab.core.model.script.serializer.ScriptSemanticSequencer
    
      Constructors:
        * AbstractRulesSemanticSequencer()
    
    """
    def __init__(self): ...
    def sequence(self, context: org.eclipse.xtext.serializer.ISerializationContext, semanticObject: org.eclipse.emf.ecore.EObject) -> None: ...

class AbstractRulesSyntacticSequencer(org.eclipse.xtext.serializer.sequencer.AbstractSyntacticSequencer):
    """
    Java class 'org.openhab.core.model.rule.serializer.AbstractRulesSyntacticSequencer'
    
        Extends:
            org.eclipse.xtext.serializer.sequencer.AbstractSyntacticSequencer
    
      Constructors:
        * AbstractRulesSyntacticSequencer()
    
    """
    def __init__(self): ...

class RulesSemanticSequencer(AbstractRulesSemanticSequencer):
    """
    Java class 'org.openhab.core.model.rule.serializer.RulesSemanticSequencer'
    
        Extends:
            org.openhab.core.model.rule.serializer.AbstractRulesSemanticSequencer
    
      Constructors:
        * RulesSemanticSequencer()
    
    """
    def __init__(self): ...

class RulesSyntacticSequencer(AbstractRulesSyntacticSequencer):
    """
    Java class 'org.openhab.core.model.rule.serializer.RulesSyntacticSequencer'
    
        Extends:
            org.openhab.core.model.rule.serializer.AbstractRulesSyntacticSequencer
    
      Constructors:
        * RulesSyntacticSequencer()
    
    """
    def __init__(self): ...
