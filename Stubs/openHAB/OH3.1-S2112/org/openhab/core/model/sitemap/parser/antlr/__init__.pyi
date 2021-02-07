import java.io
import org.eclipse.xtext.parser.antlr
import org.openhab.core.model.sitemap.services


class SitemapAntlrTokenFileProvider(org.eclipse.xtext.parser.antlr.IAntlrTokenFileProvider):
    """
    Java class 'org.openhab.core.model.sitemap.parser.antlr.SitemapAntlrTokenFileProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.eclipse.xtext.parser.antlr.IAntlrTokenFileProvider
    
      Constructors:
        * SitemapAntlrTokenFileProvider()
    
    """
    def __init__(self): ...
    def getAntlrTokenFile(self) -> java.io.InputStream: ...

class SitemapParser(org.eclipse.xtext.parser.antlr.AbstractAntlrParser):
    """
    Java class 'org.openhab.core.model.sitemap.parser.antlr.SitemapParser'
    
        Extends:
            org.eclipse.xtext.parser.antlr.AbstractAntlrParser
    
      Constructors:
        * SitemapParser()
    
    """
    def __init__(self): ...
    def getGrammarAccess(self) -> org.openhab.core.model.sitemap.services.SitemapGrammarAccess: ...
    def setGrammarAccess(self, grammarAccess: org.openhab.core.model.sitemap.services.SitemapGrammarAccess) -> None: ...
