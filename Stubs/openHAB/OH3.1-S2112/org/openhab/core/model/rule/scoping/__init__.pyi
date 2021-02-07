import java.lang
import java.util
import org.eclipse.xtext.common.types.access.impl
import org.eclipse.xtext.common.types.util
import org.openhab.core.model.script.engine.action
import org.openhab.core.model.script.scoping
import org.openhab.core.thing.binding
import typing


class AbstractRulesScopeProvider(org.openhab.core.model.script.scoping.ScriptScopeProvider):
    """
    Java class 'org.openhab.core.model.rule.scoping.AbstractRulesScopeProvider'
    
        Extends:
            org.openhab.core.model.script.scoping.ScriptScopeProvider
    
      Constructors:
        * AbstractRulesScopeProvider()
    
    """
    def __init__(self): ...

class RulesClassCache(java.util.HashMap[java.lang.String, typing.Type[typing.Any]]):
    """
    Java class 'org.openhab.core.model.rule.scoping.RulesClassCache'
    
        Extends:
            java.util.HashMap
    
      Constructors:
        * RulesClassCache()
    
    """
    def __init__(self): ...
    def addActionService(self, actionService: org.openhab.core.model.script.engine.action.ActionService) -> None: ...
    def addThingActions(self, thingActions: org.openhab.core.thing.binding.ThingActions) -> None: ...
    def deactivate(self) -> None: ...
    @classmethod
    def getInstance(cls) -> 'RulesClassCache': ...
    def removeActionService(self, actionService: org.openhab.core.model.script.engine.action.ActionService) -> None: ...
    def removeThingActions(self, thingActions: org.openhab.core.thing.binding.ThingActions) -> None: ...

class RulesClassFinder(org.eclipse.xtext.common.types.access.impl.ClassFinder):
    """
    Java class 'org.openhab.core.model.rule.scoping.RulesClassFinder'
    
        Extends:
            org.eclipse.xtext.common.types.access.impl.ClassFinder
    
    """
    @typing.overload
    def forName(self, name: java.lang.String) -> typing.Type[typing.Any]: ...
    @typing.overload
    def forName(self, string: java.lang.String) -> typing.Any: ...

class RulesImplicitlyImportedTypes(org.openhab.core.model.script.scoping.ScriptImplicitlyImportedTypes):
    """
    Java class 'org.openhab.core.model.rule.scoping.RulesImplicitlyImportedTypes'
    
        Extends:
            org.openhab.core.model.script.scoping.ScriptImplicitlyImportedTypes
    
      Constructors:
        * RulesImplicitlyImportedTypes()
    
    """
    def __init__(self): ...

class RulesJavaReflectAccess(org.eclipse.xtext.common.types.util.JavaReflectAccess):
    """
    Java class 'org.openhab.core.model.rule.scoping.RulesJavaReflectAccess'
    
        Extends:
            org.eclipse.xtext.common.types.util.JavaReflectAccess
    
      Constructors:
        * RulesJavaReflectAccess()
    
    """
    def __init__(self): ...
    def getClassFinder(self) -> org.eclipse.xtext.common.types.access.impl.ClassFinder: ...
    def setClassLoader(self, classLoader: java.lang.ClassLoader) -> None: ...

class RulesScopeProvider(AbstractRulesScopeProvider):
    """
    Java class 'org.openhab.core.model.rule.scoping.RulesScopeProvider'
    
        Extends:
            org.openhab.core.model.rule.scoping.AbstractRulesScopeProvider
    
      Constructors:
        * RulesScopeProvider()
    
    """
    def __init__(self): ...
