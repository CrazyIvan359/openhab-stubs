import java.lang
import org.eclipse.xtext
import org.eclipse.xtext.ide.editor.contentassist.antlr
import org.openhab.core.model.services


class ItemsParser(org.eclipse.xtext.ide.editor.contentassist.antlr.AbstractContentAssistParser):
    """
    Java class 'org.openhab.core.model.ide.contentassist.antlr.ItemsParser'
    
        Extends:
            org.eclipse.xtext.ide.editor.contentassist.antlr.AbstractContentAssistParser
    
      Constructors:
        * ItemsParser()
    
    """
    def __init__(self): ...
    def getGrammarAccess(self) -> org.openhab.core.model.services.ItemsGrammarAccess: ...
    def getNameMappings(self) -> 'ItemsParser.NameMappings': ...
    def setGrammarAccess(self, grammarAccess: org.openhab.core.model.services.ItemsGrammarAccess) -> None: ...
    def setNameMappings(self, nameMappings: 'ItemsParser.NameMappings') -> None: ...
    class NameMappings(java.lang.Object):
        """
        Java class 'org.openhab.core.model.ide.contentassist.antlr.ItemsParser$NameMappings'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * NameMappings(org.openhab.core.model.services.ItemsGrammarAccess)
        
        """
        def __init__(self, grammarAccess: org.openhab.core.model.services.ItemsGrammarAccess): ...
        def getRuleName(self, element: org.eclipse.xtext.AbstractElement) -> java.lang.String: ...

class PartialItemsContentAssistParser(ItemsParser):
    """
    Java class 'org.openhab.core.model.ide.contentassist.antlr.PartialItemsContentAssistParser'
    
        Extends:
            org.openhab.core.model.ide.contentassist.antlr.ItemsParser
    
      Constructors:
        * PartialItemsContentAssistParser()
    
    """
    def __init__(self): ...
    def initializeFor(self, rule: org.eclipse.xtext.AbstractRule) -> None: ...
