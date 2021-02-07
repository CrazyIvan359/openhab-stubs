import org.eclipse.emf.ecore
import org.eclipse.xtext.serializer
import org.eclipse.xtext.serializer.sequencer


class AbstractItemsSemanticSequencer(org.eclipse.xtext.serializer.sequencer.AbstractDelegatingSemanticSequencer):
    """
    Java class 'org.openhab.core.model.serializer.AbstractItemsSemanticSequencer'
    
        Extends:
            org.eclipse.xtext.serializer.sequencer.AbstractDelegatingSemanticSequencer
    
      Constructors:
        * AbstractItemsSemanticSequencer()
    
    """
    def __init__(self): ...
    def sequence(self, context: org.eclipse.xtext.serializer.ISerializationContext, semanticObject: org.eclipse.emf.ecore.EObject) -> None: ...

class AbstractItemsSyntacticSequencer(org.eclipse.xtext.serializer.sequencer.AbstractSyntacticSequencer):
    """
    Java class 'org.openhab.core.model.serializer.AbstractItemsSyntacticSequencer'
    
        Extends:
            org.eclipse.xtext.serializer.sequencer.AbstractSyntacticSequencer
    
      Constructors:
        * AbstractItemsSyntacticSequencer()
    
    """
    def __init__(self): ...

class ItemsSemanticSequencer(AbstractItemsSemanticSequencer):
    """
    Java class 'org.openhab.core.model.serializer.ItemsSemanticSequencer'
    
        Extends:
            org.openhab.core.model.serializer.AbstractItemsSemanticSequencer
    
      Constructors:
        * ItemsSemanticSequencer()
    
    """
    def __init__(self): ...

class ItemsSyntacticSequencer(AbstractItemsSyntacticSequencer):
    """
    Java class 'org.openhab.core.model.serializer.ItemsSyntacticSequencer'
    
        Extends:
            org.openhab.core.model.serializer.AbstractItemsSyntacticSequencer
    
      Constructors:
        * ItemsSyntacticSequencer()
    
    """
    def __init__(self): ...
