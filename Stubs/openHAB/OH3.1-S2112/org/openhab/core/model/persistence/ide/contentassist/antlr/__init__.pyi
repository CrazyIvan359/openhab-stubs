import java.lang
import org.eclipse.xtext
import org.eclipse.xtext.ide.editor.contentassist.antlr
import org.openhab.core.model.persistence.services


class PersistenceParser(org.eclipse.xtext.ide.editor.contentassist.antlr.AbstractContentAssistParser):
    """
    Java class 'org.openhab.core.model.persistence.ide.contentassist.antlr.PersistenceParser'
    
        Extends:
            org.eclipse.xtext.ide.editor.contentassist.antlr.AbstractContentAssistParser
    
      Constructors:
        * PersistenceParser()
    
    """
    def __init__(self): ...
    def getGrammarAccess(self) -> org.openhab.core.model.persistence.services.PersistenceGrammarAccess: ...
    def getNameMappings(self) -> 'PersistenceParser.NameMappings': ...
    def setGrammarAccess(self, grammarAccess: org.openhab.core.model.persistence.services.PersistenceGrammarAccess) -> None: ...
    def setNameMappings(self, nameMappings: 'PersistenceParser.NameMappings') -> None: ...
    class NameMappings(java.lang.Object):
        """
        Java class 'org.openhab.core.model.persistence.ide.contentassist.antlr.PersistenceParser$NameMappings'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * NameMappings(org.openhab.core.model.persistence.services.PersistenceGrammarAccess)
        
        """
        def __init__(self, grammarAccess: org.openhab.core.model.persistence.services.PersistenceGrammarAccess): ...
        def getRuleName(self, element: org.eclipse.xtext.AbstractElement) -> java.lang.String: ...

class PartialPersistenceContentAssistParser(PersistenceParser):
    """
    Java class 'org.openhab.core.model.persistence.ide.contentassist.antlr.PartialPersistenceContentAssistParser'
    
        Extends:
            org.openhab.core.model.persistence.ide.contentassist.antlr.PersistenceParser
    
      Constructors:
        * PartialPersistenceContentAssistParser()
    
    """
    def __init__(self): ...
    def initializeFor(self, rule: org.eclipse.xtext.AbstractRule) -> None: ...
