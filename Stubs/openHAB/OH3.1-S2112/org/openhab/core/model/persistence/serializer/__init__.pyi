import org.eclipse.emf.ecore
import org.eclipse.xtext.serializer
import org.eclipse.xtext.serializer.sequencer


class AbstractPersistenceSemanticSequencer(org.eclipse.xtext.serializer.sequencer.AbstractDelegatingSemanticSequencer):
    """
    Java class 'org.openhab.core.model.persistence.serializer.AbstractPersistenceSemanticSequencer'
    
        Extends:
            org.eclipse.xtext.serializer.sequencer.AbstractDelegatingSemanticSequencer
    
      Constructors:
        * AbstractPersistenceSemanticSequencer()
    
    """
    def __init__(self): ...
    def sequence(self, context: org.eclipse.xtext.serializer.ISerializationContext, semanticObject: org.eclipse.emf.ecore.EObject) -> None: ...

class AbstractPersistenceSyntacticSequencer(org.eclipse.xtext.serializer.sequencer.AbstractSyntacticSequencer):
    """
    Java class 'org.openhab.core.model.persistence.serializer.AbstractPersistenceSyntacticSequencer'
    
        Extends:
            org.eclipse.xtext.serializer.sequencer.AbstractSyntacticSequencer
    
      Constructors:
        * AbstractPersistenceSyntacticSequencer()
    
    """
    def __init__(self): ...

class PersistenceSemanticSequencer(AbstractPersistenceSemanticSequencer):
    """
    Java class 'org.openhab.core.model.persistence.serializer.PersistenceSemanticSequencer'
    
        Extends:
            org.openhab.core.model.persistence.serializer.AbstractPersistenceSemanticSequencer
    
      Constructors:
        * PersistenceSemanticSequencer()
    
    """
    def __init__(self): ...

class PersistenceSyntacticSequencer(AbstractPersistenceSyntacticSequencer):
    """
    Java class 'org.openhab.core.model.persistence.serializer.PersistenceSyntacticSequencer'
    
        Extends:
            org.openhab.core.model.persistence.serializer.AbstractPersistenceSyntacticSequencer
    
      Constructors:
        * PersistenceSyntacticSequencer()
    
    """
    def __init__(self): ...
