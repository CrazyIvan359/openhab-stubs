import java.lang
import org.eclipse.xtext
import org.eclipse.xtext.ide.editor.contentassist.antlr
import org.openhab.core.model.rule.services


class RulesParser(org.eclipse.xtext.ide.editor.contentassist.antlr.AbstractContentAssistParser):
    """
    Java class 'org.openhab.core.model.rule.ide.contentassist.antlr.RulesParser'
    
        Extends:
            org.eclipse.xtext.ide.editor.contentassist.antlr.AbstractContentAssistParser
    
      Constructors:
        * RulesParser()
    
    """
    def __init__(self): ...
    def getGrammarAccess(self) -> org.openhab.core.model.rule.services.RulesGrammarAccess: ...
    def getNameMappings(self) -> 'RulesParser.NameMappings': ...
    def setGrammarAccess(self, grammarAccess: org.openhab.core.model.rule.services.RulesGrammarAccess) -> None: ...
    def setNameMappings(self, nameMappings: 'RulesParser.NameMappings') -> None: ...
    class NameMappings(java.lang.Object):
        """
        Java class 'org.openhab.core.model.rule.ide.contentassist.antlr.RulesParser$NameMappings'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * NameMappings(org.openhab.core.model.rule.services.RulesGrammarAccess)
        
        """
        def __init__(self, grammarAccess: org.openhab.core.model.rule.services.RulesGrammarAccess): ...
        def getRuleName(self, element: org.eclipse.xtext.AbstractElement) -> java.lang.String: ...

class PartialRulesContentAssistParser(RulesParser):
    """
    Java class 'org.openhab.core.model.rule.ide.contentassist.antlr.PartialRulesContentAssistParser'
    
        Extends:
            org.openhab.core.model.rule.ide.contentassist.antlr.RulesParser
    
      Constructors:
        * PartialRulesContentAssistParser()
    
    """
    def __init__(self): ...
    def initializeFor(self, rule: org.eclipse.xtext.AbstractRule) -> None: ...
