import java.io
import org.eclipse.xtext.parser.antlr
import org.openhab.core.model.persistence.services


class PersistenceAntlrTokenFileProvider(org.eclipse.xtext.parser.antlr.IAntlrTokenFileProvider):
    """
    Java class 'org.openhab.core.model.persistence.parser.antlr.PersistenceAntlrTokenFileProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.eclipse.xtext.parser.antlr.IAntlrTokenFileProvider
    
      Constructors:
        * PersistenceAntlrTokenFileProvider()
    
    """
    def __init__(self): ...
    def getAntlrTokenFile(self) -> java.io.InputStream: ...

class PersistenceParser(org.eclipse.xtext.parser.antlr.AbstractAntlrParser):
    """
    Java class 'org.openhab.core.model.persistence.parser.antlr.PersistenceParser'
    
        Extends:
            org.eclipse.xtext.parser.antlr.AbstractAntlrParser
    
      Constructors:
        * PersistenceParser()
    
    """
    def __init__(self): ...
    def getGrammarAccess(self) -> org.openhab.core.model.persistence.services.PersistenceGrammarAccess: ...
    def setGrammarAccess(self, grammarAccess: org.openhab.core.model.persistence.services.PersistenceGrammarAccess) -> None: ...
