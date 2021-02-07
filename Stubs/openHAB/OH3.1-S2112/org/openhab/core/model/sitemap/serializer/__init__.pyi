import org.eclipse.emf.ecore
import org.eclipse.xtext.serializer
import org.eclipse.xtext.serializer.sequencer


class AbstractSitemapSemanticSequencer(org.eclipse.xtext.serializer.sequencer.AbstractDelegatingSemanticSequencer):
    """
    Java class 'org.openhab.core.model.sitemap.serializer.AbstractSitemapSemanticSequencer'
    
        Extends:
            org.eclipse.xtext.serializer.sequencer.AbstractDelegatingSemanticSequencer
    
      Constructors:
        * AbstractSitemapSemanticSequencer()
    
    """
    def __init__(self): ...
    def sequence(self, context: org.eclipse.xtext.serializer.ISerializationContext, semanticObject: org.eclipse.emf.ecore.EObject) -> None: ...

class AbstractSitemapSyntacticSequencer(org.eclipse.xtext.serializer.sequencer.AbstractSyntacticSequencer):
    """
    Java class 'org.openhab.core.model.sitemap.serializer.AbstractSitemapSyntacticSequencer'
    
        Extends:
            org.eclipse.xtext.serializer.sequencer.AbstractSyntacticSequencer
    
      Constructors:
        * AbstractSitemapSyntacticSequencer()
    
    """
    def __init__(self): ...

class SitemapSemanticSequencer(AbstractSitemapSemanticSequencer):
    """
    Java class 'org.openhab.core.model.sitemap.serializer.SitemapSemanticSequencer'
    
        Extends:
            org.openhab.core.model.sitemap.serializer.AbstractSitemapSemanticSequencer
    
      Constructors:
        * SitemapSemanticSequencer()
    
    """
    def __init__(self): ...

class SitemapSyntacticSequencer(AbstractSitemapSyntacticSequencer):
    """
    Java class 'org.openhab.core.model.sitemap.serializer.SitemapSyntacticSequencer'
    
        Extends:
            org.openhab.core.model.sitemap.serializer.AbstractSitemapSyntacticSequencer
    
      Constructors:
        * SitemapSyntacticSequencer()
    
    """
    def __init__(self): ...
