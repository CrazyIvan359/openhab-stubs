import java.io
import org.eclipse.xtext.parser.antlr
import org.openhab.core.model.thing.services


class ThingAntlrTokenFileProvider(org.eclipse.xtext.parser.antlr.IAntlrTokenFileProvider):
    """
    Java class 'org.openhab.core.model.thing.parser.antlr.ThingAntlrTokenFileProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.eclipse.xtext.parser.antlr.IAntlrTokenFileProvider
    
      Constructors:
        * ThingAntlrTokenFileProvider()
    
    """
    def __init__(self): ...
    def getAntlrTokenFile(self) -> java.io.InputStream: ...

class ThingParser(org.eclipse.xtext.parser.antlr.AbstractAntlrParser):
    """
    Java class 'org.openhab.core.model.thing.parser.antlr.ThingParser'
    
        Extends:
            org.eclipse.xtext.parser.antlr.AbstractAntlrParser
    
      Constructors:
        * ThingParser()
    
    """
    def __init__(self): ...
    def getGrammarAccess(self) -> org.openhab.core.model.thing.services.ThingGrammarAccess: ...
    def setGrammarAccess(self, thingGrammarAccess: org.openhab.core.model.thing.services.ThingGrammarAccess) -> None: ...
