import org.eclipse.emf.ecore
import org.eclipse.xtext.serializer
import org.eclipse.xtext.serializer.sequencer


class AbstractThingSemanticSequencer(org.eclipse.xtext.serializer.sequencer.AbstractDelegatingSemanticSequencer):
    """
    Java class 'org.openhab.core.model.thing.serializer.AbstractThingSemanticSequencer'
    
        Extends:
            org.eclipse.xtext.serializer.sequencer.AbstractDelegatingSemanticSequencer
    
      Constructors:
        * AbstractThingSemanticSequencer()
    
    """
    def __init__(self): ...
    def sequence(self, iSerializationContext: org.eclipse.xtext.serializer.ISerializationContext, eObject: org.eclipse.emf.ecore.EObject) -> None: ...

class AbstractThingSyntacticSequencer(org.eclipse.xtext.serializer.sequencer.AbstractSyntacticSequencer):
    """
    Java class 'org.openhab.core.model.thing.serializer.AbstractThingSyntacticSequencer'
    
        Extends:
            org.eclipse.xtext.serializer.sequencer.AbstractSyntacticSequencer
    
      Constructors:
        * AbstractThingSyntacticSequencer()
    
    """
    def __init__(self): ...

class ThingSemanticSequencer(AbstractThingSemanticSequencer):
    """
    Java class 'org.openhab.core.model.thing.serializer.ThingSemanticSequencer'
    
        Extends:
            org.openhab.core.model.thing.serializer.AbstractThingSemanticSequencer
    
      Constructors:
        * ThingSemanticSequencer()
    
    """
    def __init__(self): ...

class ThingSyntacticSequencer(AbstractThingSyntacticSequencer):
    """
    Java class 'org.openhab.core.model.thing.serializer.ThingSyntacticSequencer'
    
        Extends:
            org.openhab.core.model.thing.serializer.AbstractThingSyntacticSequencer
    
      Constructors:
        * ThingSyntacticSequencer()
    
    """
    def __init__(self): ...

class ThingSyntacticSequencerExtension(ThingSyntacticSequencer):
    """
    Java class 'org.openhab.core.model.thing.serializer.ThingSyntacticSequencerExtension'
    
        Extends:
            org.openhab.core.model.thing.serializer.ThingSyntacticSequencer
    
      Constructors:
        * ThingSyntacticSequencerExtension()
    
    """
    def __init__(self): ...
