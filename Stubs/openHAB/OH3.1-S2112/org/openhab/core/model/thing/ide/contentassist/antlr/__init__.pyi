import java.lang
import org.eclipse.xtext
import org.eclipse.xtext.ide.editor.contentassist.antlr
import org.openhab.core.model.thing.services


class ThingParser(org.eclipse.xtext.ide.editor.contentassist.antlr.AbstractContentAssistParser):
    """
    Java class 'org.openhab.core.model.thing.ide.contentassist.antlr.ThingParser'
    
        Extends:
            org.eclipse.xtext.ide.editor.contentassist.antlr.AbstractContentAssistParser
    
      Constructors:
        * ThingParser()
    
    """
    def __init__(self): ...
    def getGrammarAccess(self) -> org.openhab.core.model.thing.services.ThingGrammarAccess: ...
    def getNameMappings(self) -> 'ThingParser.NameMappings': ...
    def setGrammarAccess(self, grammarAccess: org.openhab.core.model.thing.services.ThingGrammarAccess) -> None: ...
    def setNameMappings(self, nameMappings: 'ThingParser.NameMappings') -> None: ...
    class NameMappings(java.lang.Object):
        """
        Java class 'org.openhab.core.model.thing.ide.contentassist.antlr.ThingParser$NameMappings'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * NameMappings(org.openhab.core.model.thing.services.ThingGrammarAccess)
        
        """
        def __init__(self, grammarAccess: org.openhab.core.model.thing.services.ThingGrammarAccess): ...
        def getRuleName(self, element: org.eclipse.xtext.AbstractElement) -> java.lang.String: ...

class PartialThingContentAssistParser(ThingParser):
    """
    Java class 'org.openhab.core.model.thing.ide.contentassist.antlr.PartialThingContentAssistParser'
    
        Extends:
            org.openhab.core.model.thing.ide.contentassist.antlr.ThingParser
    
      Constructors:
        * PartialThingContentAssistParser()
    
    """
    def __init__(self): ...
    def initializeFor(self, rule: org.eclipse.xtext.AbstractRule) -> None: ...
