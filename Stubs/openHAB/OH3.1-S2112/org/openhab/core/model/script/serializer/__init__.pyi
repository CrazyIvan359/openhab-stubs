import org.eclipse.emf.ecore
import org.eclipse.xtext.serializer
import org.eclipse.xtext.serializer.sequencer
import org.eclipse.xtext.xbase.serializer


class AbstractScriptSemanticSequencer(org.eclipse.xtext.xbase.serializer.XbaseSemanticSequencer):
    """
    Java class 'org.openhab.core.model.script.serializer.AbstractScriptSemanticSequencer'
    
        Extends:
            org.eclipse.xtext.xbase.serializer.XbaseSemanticSequencer
    
      Constructors:
        * AbstractScriptSemanticSequencer()
    
    """
    def __init__(self): ...
    def sequence(self, context: org.eclipse.xtext.serializer.ISerializationContext, semanticObject: org.eclipse.emf.ecore.EObject) -> None: ...

class AbstractScriptSyntacticSequencer(org.eclipse.xtext.serializer.sequencer.AbstractSyntacticSequencer):
    """
    Java class 'org.openhab.core.model.script.serializer.AbstractScriptSyntacticSequencer'
    
        Extends:
            org.eclipse.xtext.serializer.sequencer.AbstractSyntacticSequencer
    
      Constructors:
        * AbstractScriptSyntacticSequencer()
    
    """
    def __init__(self): ...

class ScriptSemanticSequencer(AbstractScriptSemanticSequencer):
    """
    Java class 'org.openhab.core.model.script.serializer.ScriptSemanticSequencer'
    
        Extends:
            org.openhab.core.model.script.serializer.AbstractScriptSemanticSequencer
    
      Constructors:
        * ScriptSemanticSequencer()
    
    """
    def __init__(self): ...

class ScriptSyntacticSequencer(AbstractScriptSyntacticSequencer):
    """
    Java class 'org.openhab.core.model.script.serializer.ScriptSyntacticSequencer'
    
        Extends:
            org.openhab.core.model.script.serializer.AbstractScriptSyntacticSequencer
    
      Constructors:
        * ScriptSyntacticSequencer()
    
    """
    def __init__(self): ...
