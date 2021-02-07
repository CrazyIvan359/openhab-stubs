import java.lang
import org.eclipse.xtext
import org.eclipse.xtext.ide.editor.contentassist.antlr
import org.openhab.core.model.script.services


class ScriptParser(org.eclipse.xtext.ide.editor.contentassist.antlr.AbstractContentAssistParser):
    """
    Java class 'org.openhab.core.model.script.ide.contentassist.antlr.ScriptParser'
    
        Extends:
            org.eclipse.xtext.ide.editor.contentassist.antlr.AbstractContentAssistParser
    
      Constructors:
        * ScriptParser()
    
    """
    def __init__(self): ...
    def getGrammarAccess(self) -> org.openhab.core.model.script.services.ScriptGrammarAccess: ...
    def getNameMappings(self) -> 'ScriptParser.NameMappings': ...
    def setGrammarAccess(self, grammarAccess: org.openhab.core.model.script.services.ScriptGrammarAccess) -> None: ...
    def setNameMappings(self, nameMappings: 'ScriptParser.NameMappings') -> None: ...
    class NameMappings(java.lang.Object):
        """
        Java class 'org.openhab.core.model.script.ide.contentassist.antlr.ScriptParser$NameMappings'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * NameMappings(org.openhab.core.model.script.services.ScriptGrammarAccess)
        
        """
        def __init__(self, grammarAccess: org.openhab.core.model.script.services.ScriptGrammarAccess): ...
        def getRuleName(self, element: org.eclipse.xtext.AbstractElement) -> java.lang.String: ...

class PartialScriptContentAssistParser(ScriptParser):
    """
    Java class 'org.openhab.core.model.script.ide.contentassist.antlr.PartialScriptContentAssistParser'
    
        Extends:
            org.openhab.core.model.script.ide.contentassist.antlr.ScriptParser
    
      Constructors:
        * PartialScriptContentAssistParser()
    
    """
    def __init__(self): ...
    def initializeFor(self, rule: org.eclipse.xtext.AbstractRule) -> None: ...
