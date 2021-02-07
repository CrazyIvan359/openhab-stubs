import java.io
import org.eclipse.xtext.parser.antlr
import org.openhab.core.model.services


class ItemsAntlrTokenFileProvider(org.eclipse.xtext.parser.antlr.IAntlrTokenFileProvider):
    """
    Java class 'org.openhab.core.model.parser.antlr.ItemsAntlrTokenFileProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.eclipse.xtext.parser.antlr.IAntlrTokenFileProvider
    
      Constructors:
        * ItemsAntlrTokenFileProvider()
    
    """
    def __init__(self): ...
    def getAntlrTokenFile(self) -> java.io.InputStream: ...

class ItemsParser(org.eclipse.xtext.parser.antlr.AbstractAntlrParser):
    """
    Java class 'org.openhab.core.model.parser.antlr.ItemsParser'
    
        Extends:
            org.eclipse.xtext.parser.antlr.AbstractAntlrParser
    
      Constructors:
        * ItemsParser()
    
    """
    def __init__(self): ...
    def getGrammarAccess(self) -> org.openhab.core.model.services.ItemsGrammarAccess: ...
    def setGrammarAccess(self, grammarAccess: org.openhab.core.model.services.ItemsGrammarAccess) -> None: ...
