import java.lang
import org.eclipse.xtext
import org.eclipse.xtext.ide.editor.contentassist.antlr
import org.openhab.core.model.sitemap.services


class SitemapParser(org.eclipse.xtext.ide.editor.contentassist.antlr.AbstractContentAssistParser):
    """
    Java class 'org.openhab.core.model.sitemap.ide.contentassist.antlr.SitemapParser'
    
        Extends:
            org.eclipse.xtext.ide.editor.contentassist.antlr.AbstractContentAssistParser
    
      Constructors:
        * SitemapParser()
    
    """
    def __init__(self): ...
    def getGrammarAccess(self) -> org.openhab.core.model.sitemap.services.SitemapGrammarAccess: ...
    def getNameMappings(self) -> 'SitemapParser.NameMappings': ...
    def setGrammarAccess(self, grammarAccess: org.openhab.core.model.sitemap.services.SitemapGrammarAccess) -> None: ...
    def setNameMappings(self, nameMappings: 'SitemapParser.NameMappings') -> None: ...
    class NameMappings(java.lang.Object):
        """
        Java class 'org.openhab.core.model.sitemap.ide.contentassist.antlr.SitemapParser$NameMappings'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * NameMappings(org.openhab.core.model.sitemap.services.SitemapGrammarAccess)
        
        """
        def __init__(self, grammarAccess: org.openhab.core.model.sitemap.services.SitemapGrammarAccess): ...
        def getRuleName(self, element: org.eclipse.xtext.AbstractElement) -> java.lang.String: ...

class PartialSitemapContentAssistParser(SitemapParser):
    """
    Java class 'org.openhab.core.model.sitemap.ide.contentassist.antlr.PartialSitemapContentAssistParser'
    
        Extends:
            org.openhab.core.model.sitemap.ide.contentassist.antlr.SitemapParser
    
      Constructors:
        * PartialSitemapContentAssistParser()
    
    """
    def __init__(self): ...
    def initializeFor(self, rule: org.eclipse.xtext.AbstractRule) -> None: ...
