import java.io
import org.eclipse.xtext.parser.antlr
import org.openhab.core.model.script.services


class ScriptAntlrTokenFileProvider(org.eclipse.xtext.parser.antlr.IAntlrTokenFileProvider):
    """
    Java class 'org.openhab.core.model.script.parser.antlr.ScriptAntlrTokenFileProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.eclipse.xtext.parser.antlr.IAntlrTokenFileProvider
    
      Constructors:
        * ScriptAntlrTokenFileProvider()
    
    """
    def __init__(self): ...
    def getAntlrTokenFile(self) -> java.io.InputStream: ...

class ScriptParser(org.eclipse.xtext.parser.antlr.AbstractAntlrParser):
    """
    Java class 'org.openhab.core.model.script.parser.antlr.ScriptParser'
    
        Extends:
            org.eclipse.xtext.parser.antlr.AbstractAntlrParser
    
      Constructors:
        * ScriptParser()
    
    """
    def __init__(self): ...
    def getGrammarAccess(self) -> org.openhab.core.model.script.services.ScriptGrammarAccess: ...
    def setGrammarAccess(self, grammarAccess: org.openhab.core.model.script.services.ScriptGrammarAccess) -> None: ...
