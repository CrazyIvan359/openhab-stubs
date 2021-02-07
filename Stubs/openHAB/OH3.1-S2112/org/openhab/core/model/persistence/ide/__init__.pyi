import com.google.inject
import org.eclipse.xtext.ide
import org.eclipse.xtext.ide.editor.contentassist
import org.eclipse.xtext.ide.editor.contentassist.antlr
import org.eclipse.xtext.ide.refactoring
import org.eclipse.xtext.ide.server.rename
import org.openhab.core.model.persistence
import typing


class AbstractPersistenceIdeModule(org.eclipse.xtext.ide.DefaultIdeModule):
    """
    Java class 'org.openhab.core.model.persistence.ide.AbstractPersistenceIdeModule'
    
        Extends:
            org.eclipse.xtext.ide.DefaultIdeModule
    
      Constructors:
        * AbstractPersistenceIdeModule()
    
    """
    def __init__(self): ...
    def bindIContentAssistParser(self) -> typing.Type[org.eclipse.xtext.ide.editor.contentassist.antlr.IContentAssistParser]: ...
    def bindIPrefixMatcher(self) -> typing.Type[org.eclipse.xtext.ide.editor.contentassist.IPrefixMatcher]: ...
    def bindIProposalConflictHelper(self) -> typing.Type[org.eclipse.xtext.ide.editor.contentassist.IProposalConflictHelper]: ...
    def bindIRenameService2(self) -> typing.Type[org.eclipse.xtext.ide.server.rename.IRenameService2]: ...
    def bindIRenameStrategy2(self) -> typing.Type[org.eclipse.xtext.ide.refactoring.IRenameStrategy2]: ...
    def configureContentAssistLexer(self, binder: com.google.inject.Binder) -> None: ...

class PersistenceIdeSetup(org.openhab.core.model.persistence.PersistenceStandaloneSetup):
    """
    Java class 'org.openhab.core.model.persistence.ide.PersistenceIdeSetup'
    
        Extends:
            org.openhab.core.model.persistence.PersistenceStandaloneSetup
    
      Constructors:
        * PersistenceIdeSetup()
    
    """
    def __init__(self): ...
    def createInjector(self) -> com.google.inject.Injector: ...

class PersistenceIdeModule(AbstractPersistenceIdeModule):
    """
    Java class 'org.openhab.core.model.persistence.ide.PersistenceIdeModule'
    
        Extends:
            org.openhab.core.model.persistence.ide.AbstractPersistenceIdeModule
    
      Constructors:
        * PersistenceIdeModule()
    
    """
    def __init__(self): ...
