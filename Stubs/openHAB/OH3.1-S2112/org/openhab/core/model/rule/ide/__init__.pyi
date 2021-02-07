import com.google.inject
import org.eclipse.xtext.ide.editor.contentassist
import org.eclipse.xtext.ide.editor.contentassist.antlr
import org.eclipse.xtext.ide.refactoring
import org.eclipse.xtext.ide.server.rename
import org.eclipse.xtext.xbase.ide
import org.eclipse.xtext.xbase.typesystem.internal
import org.openhab.core.model.rule
import typing


class AbstractRulesIdeModule(org.eclipse.xtext.xbase.ide.DefaultXbaseIdeModule):
    """
    Java class 'org.openhab.core.model.rule.ide.AbstractRulesIdeModule'
    
        Extends:
            org.eclipse.xtext.xbase.ide.DefaultXbaseIdeModule
    
      Constructors:
        * AbstractRulesIdeModule()
    
    """
    def __init__(self): ...
    def bindIContentAssistParser(self) -> typing.Type[org.eclipse.xtext.ide.editor.contentassist.antlr.IContentAssistParser]: ...
    def bindIPrefixMatcher(self) -> typing.Type[org.eclipse.xtext.ide.editor.contentassist.IPrefixMatcher]: ...
    def bindIProposalConflictHelper(self) -> typing.Type[org.eclipse.xtext.ide.editor.contentassist.IProposalConflictHelper]: ...
    def bindIRenameService2(self) -> typing.Type[org.eclipse.xtext.ide.server.rename.IRenameService2]: ...
    def bindIRenameStrategy2(self) -> typing.Type[org.eclipse.xtext.ide.refactoring.IRenameStrategy2]: ...
    def configureContentAssistLexer(self, binder: com.google.inject.Binder) -> None: ...

class RulesIdeSetup(org.openhab.core.model.rule.RulesStandaloneSetup):
    """
    Java class 'org.openhab.core.model.rule.ide.RulesIdeSetup'
    
        Extends:
            org.openhab.core.model.rule.RulesStandaloneSetup
    
      Constructors:
        * RulesIdeSetup()
    
    """
    def __init__(self): ...
    def createInjector(self) -> com.google.inject.Injector: ...

class RulesIdeModule(AbstractRulesIdeModule):
    """
    Java class 'org.openhab.core.model.rule.ide.RulesIdeModule'
    
        Extends:
            org.openhab.core.model.rule.ide.AbstractRulesIdeModule
    
      Constructors:
        * RulesIdeModule()
    
    """
    def __init__(self): ...
    def bindIFeatureScopeTrackerProvider(self) -> typing.Type[org.eclipse.xtext.xbase.typesystem.internal.IFeatureScopeTracker.Provider]: ...
