import com.google.inject
import org.eclipse.xtext.ide
import org.eclipse.xtext.ide.editor.contentassist
import org.eclipse.xtext.ide.editor.contentassist.antlr
import org.eclipse.xtext.ide.refactoring
import org.eclipse.xtext.ide.server.rename
import org.openhab.core.model.sitemap
import typing


class AbstractSitemapIdeModule(org.eclipse.xtext.ide.DefaultIdeModule):
    """
    Java class 'org.openhab.core.model.sitemap.ide.AbstractSitemapIdeModule'
    
        Extends:
            org.eclipse.xtext.ide.DefaultIdeModule
    
      Constructors:
        * AbstractSitemapIdeModule()
    
    """
    def __init__(self): ...
    def bindIContentAssistParser(self) -> typing.Type[org.eclipse.xtext.ide.editor.contentassist.antlr.IContentAssistParser]: ...
    def bindIPrefixMatcher(self) -> typing.Type[org.eclipse.xtext.ide.editor.contentassist.IPrefixMatcher]: ...
    def bindIProposalConflictHelper(self) -> typing.Type[org.eclipse.xtext.ide.editor.contentassist.IProposalConflictHelper]: ...
    def bindIRenameService2(self) -> typing.Type[org.eclipse.xtext.ide.server.rename.IRenameService2]: ...
    def bindIRenameStrategy2(self) -> typing.Type[org.eclipse.xtext.ide.refactoring.IRenameStrategy2]: ...
    def configureContentAssistLexer(self, binder: com.google.inject.Binder) -> None: ...

class SitemapIdeSetup(org.openhab.core.model.sitemap.SitemapStandaloneSetup):
    """
    Java class 'org.openhab.core.model.sitemap.ide.SitemapIdeSetup'
    
        Extends:
            org.openhab.core.model.sitemap.SitemapStandaloneSetup
    
      Constructors:
        * SitemapIdeSetup()
    
    """
    def __init__(self): ...
    def createInjector(self) -> com.google.inject.Injector: ...

class SitemapIdeModule(AbstractSitemapIdeModule):
    """
    Java class 'org.openhab.core.model.sitemap.ide.SitemapIdeModule'
    
        Extends:
            org.openhab.core.model.sitemap.ide.AbstractSitemapIdeModule
    
      Constructors:
        * SitemapIdeModule()
    
    """
    def __init__(self): ...
