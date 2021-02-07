import com.google.inject
import org.eclipse.xtext.ide
import org.eclipse.xtext.ide.editor.contentassist
import org.eclipse.xtext.ide.editor.contentassist.antlr
import org.eclipse.xtext.ide.refactoring
import org.eclipse.xtext.ide.server.rename
import org.openhab.core.model
import typing


class AbstractItemsIdeModule(org.eclipse.xtext.ide.DefaultIdeModule):
    """
    Java class 'org.openhab.core.model.ide.AbstractItemsIdeModule'
    
        Extends:
            org.eclipse.xtext.ide.DefaultIdeModule
    
      Constructors:
        * AbstractItemsIdeModule()
    
    """
    def __init__(self): ...
    def bindIContentAssistParser(self) -> typing.Type[org.eclipse.xtext.ide.editor.contentassist.antlr.IContentAssistParser]: ...
    def bindIPrefixMatcher(self) -> typing.Type[org.eclipse.xtext.ide.editor.contentassist.IPrefixMatcher]: ...
    def bindIProposalConflictHelper(self) -> typing.Type[org.eclipse.xtext.ide.editor.contentassist.IProposalConflictHelper]: ...
    def bindIRenameService2(self) -> typing.Type[org.eclipse.xtext.ide.server.rename.IRenameService2]: ...
    def bindIRenameStrategy2(self) -> typing.Type[org.eclipse.xtext.ide.refactoring.IRenameStrategy2]: ...
    def configureContentAssistLexer(self, binder: com.google.inject.Binder) -> None: ...

class ItemsIdeSetup(org.openhab.core.model.ItemsStandaloneSetup):
    """
    Java class 'org.openhab.core.model.ide.ItemsIdeSetup'
    
        Extends:
            org.openhab.core.model.ItemsStandaloneSetup
    
      Constructors:
        * ItemsIdeSetup()
    
    """
    def __init__(self): ...
    def createInjector(self) -> com.google.inject.Injector: ...

class ItemsIdeModule(AbstractItemsIdeModule):
    """
    Java class 'org.openhab.core.model.ide.ItemsIdeModule'
    
        Extends:
            org.openhab.core.model.ide.AbstractItemsIdeModule
    
      Constructors:
        * ItemsIdeModule()
    
    """
    def __init__(self): ...
