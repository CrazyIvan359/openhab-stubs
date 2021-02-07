import com.google.inject
import org.eclipse.xtext.ide
import org.eclipse.xtext.ide.editor.contentassist
import org.eclipse.xtext.ide.editor.contentassist.antlr
import org.eclipse.xtext.ide.refactoring
import org.eclipse.xtext.ide.server.rename
import org.openhab.core.model.thing
import typing


class AbstractThingIdeModule(org.eclipse.xtext.ide.DefaultIdeModule):
    """
    Java class 'org.openhab.core.model.thing.ide.AbstractThingIdeModule'
    
        Extends:
            org.eclipse.xtext.ide.DefaultIdeModule
    
      Constructors:
        * AbstractThingIdeModule()
    
    """
    def __init__(self): ...
    def bindIContentAssistParser(self) -> typing.Type[org.eclipse.xtext.ide.editor.contentassist.antlr.IContentAssistParser]: ...
    def bindIPrefixMatcher(self) -> typing.Type[org.eclipse.xtext.ide.editor.contentassist.IPrefixMatcher]: ...
    def bindIProposalConflictHelper(self) -> typing.Type[org.eclipse.xtext.ide.editor.contentassist.IProposalConflictHelper]: ...
    def bindIRenameService2(self) -> typing.Type[org.eclipse.xtext.ide.server.rename.IRenameService2]: ...
    def bindIRenameStrategy2(self) -> typing.Type[org.eclipse.xtext.ide.refactoring.IRenameStrategy2]: ...
    def configureContentAssistLexer(self, binder: com.google.inject.Binder) -> None: ...

class ThingIdeSetup(org.openhab.core.model.thing.ThingStandaloneSetup):
    """
    Java class 'org.openhab.core.model.thing.ide.ThingIdeSetup'
    
        Extends:
            org.openhab.core.model.thing.ThingStandaloneSetup
    
      Constructors:
        * ThingIdeSetup()
    
    """
    def __init__(self): ...
    def createInjector(self) -> com.google.inject.Injector: ...

class ThingIdeModule(AbstractThingIdeModule):
    """
    Java class 'org.openhab.core.model.thing.ide.ThingIdeModule'
    
        Extends:
            org.openhab.core.model.thing.ide.AbstractThingIdeModule
    
      Constructors:
        * ThingIdeModule()
    
    """
    def __init__(self): ...
