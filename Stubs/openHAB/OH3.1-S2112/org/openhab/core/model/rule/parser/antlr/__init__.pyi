import java.io
import org.eclipse.xtext.parser.antlr
import org.openhab.core.model.rule.services


class RulesAntlrTokenFileProvider(org.eclipse.xtext.parser.antlr.IAntlrTokenFileProvider):
    """
    Java class 'org.openhab.core.model.rule.parser.antlr.RulesAntlrTokenFileProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.eclipse.xtext.parser.antlr.IAntlrTokenFileProvider
    
      Constructors:
        * RulesAntlrTokenFileProvider()
    
    """
    def __init__(self): ...
    def getAntlrTokenFile(self) -> java.io.InputStream: ...

class RulesParser(org.eclipse.xtext.parser.antlr.AbstractAntlrParser):
    """
    Java class 'org.openhab.core.model.rule.parser.antlr.RulesParser'
    
        Extends:
            org.eclipse.xtext.parser.antlr.AbstractAntlrParser
    
      Constructors:
        * RulesParser()
    
    """
    def __init__(self): ...
    def getGrammarAccess(self) -> org.openhab.core.model.rule.services.RulesGrammarAccess: ...
    def setGrammarAccess(self, grammarAccess: org.openhab.core.model.rule.services.RulesGrammarAccess) -> None: ...
