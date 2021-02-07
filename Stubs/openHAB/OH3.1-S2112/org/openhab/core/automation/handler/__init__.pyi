import java.lang
import java.util
import org.openhab.core.automation
import typing


class ModuleHandler(java.lang.Object):
    """
    @NonNullByDefault public interface ModuleHandler
    
        A common interface for all module Handler interfaces. The Handler interfaces are bridge between RuleManager and external
        modules used by the RuleManager.
    
        Also see:
            :class:`~org.openhab.core.automation.handler.ModuleHandlerFactory`
    
    
    """
    def dispose(self) -> None: ...
    def setCallback(self, callback: org.openhab.core.automation.ModuleHandlerCallback) -> None: ...

class ModuleHandlerFactory(java.lang.Object):
    """
    @NonNullByDefault public interface ModuleHandlerFactory
    
        This interface represents a factory for :class:`~org.openhab.core.automation.handler.ModuleHandler` instances. It is
        used for creating and disposing the :class:`~org.openhab.core.automation.handler.TriggerHandler`s,
        :class:`~org.openhab.core.automation.handler.ConditionHandler`s and
        :class:`~org.openhab.core.automation.handler.ActionHandler`s needed for the operation of the
        :class:`~org.openhab.core.automation.Module`s included in :class:`~org.openhab.core.automation.Rule`s.
    
        :class:`~org.openhab.core.automation.handler.ModuleHandlerFactory` implementations must be registered as services in the
        OSGi framework.
    
    
    """
    def getHandler(self, module: org.openhab.core.automation.Module, ruleUID: java.lang.String) -> ModuleHandler: ...
    def getTypes(self) -> java.util.Collection[java.lang.String]: ...
    def ungetHandler(self, module: org.openhab.core.automation.Module, ruleUID: java.lang.String, handler: ModuleHandler) -> None: ...

class TriggerHandlerCallback(org.openhab.core.automation.ModuleHandlerCallback):
    """
    Java class 'org.openhab.core.automation.handler.TriggerHandlerCallback'
    
        Interfaces:
            org.openhab.core.automation.ModuleHandlerCallback
    
    """
    def triggered(self, trigger: org.openhab.core.automation.Trigger, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...

class ActionHandler(ModuleHandler):
    """
    Java class 'org.openhab.core.automation.handler.ActionHandler'
    
        Interfaces:
            org.openhab.core.automation.handler.ModuleHandler
    
    """
    def execute(self, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> java.util.Map[java.lang.String, typing.Any]: ...

_BaseModuleHandler__T = typing.TypeVar('_BaseModuleHandler__T', bound=org.openhab.core.automation.Module)  # <T>
class BaseModuleHandler(ModuleHandler, typing.Generic[_BaseModuleHandler__T]):
    """
    Java class 'org.openhab.core.automation.handler.BaseModuleHandler'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.handler.ModuleHandler
    
      Constructors:
        * BaseModuleHandler(org.openhab.core.automation.Module)
    
    """
    def __init__(self, module: _BaseModuleHandler__T): ...
    def dispose(self) -> None: ...
    def setCallback(self, callback: org.openhab.core.automation.ModuleHandlerCallback) -> None: ...

class BaseModuleHandlerFactory(ModuleHandlerFactory):
    """
    Java class 'org.openhab.core.automation.handler.BaseModuleHandlerFactory'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.handler.ModuleHandlerFactory
    
      Constructors:
        * BaseModuleHandlerFactory()
    
    """
    def __init__(self): ...
    def getHandler(self, module: org.openhab.core.automation.Module, ruleUID: java.lang.String) -> ModuleHandler: ...
    def ungetHandler(self, module: org.openhab.core.automation.Module, ruleUID: java.lang.String, handler: ModuleHandler) -> None: ...

class ConditionHandler(ModuleHandler):
    """
    Java class 'org.openhab.core.automation.handler.ConditionHandler'
    
        Interfaces:
            org.openhab.core.automation.handler.ModuleHandler
    
    """
    def isSatisfied(self, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> bool: ...

class TriggerHandler(ModuleHandler):
    """
    Java class 'org.openhab.core.automation.handler.TriggerHandler'
    
        Interfaces:
            org.openhab.core.automation.handler.ModuleHandler
    
    """

class BaseActionModuleHandler(BaseModuleHandler[org.openhab.core.automation.Action], ActionHandler):
    """
    Java class 'org.openhab.core.automation.handler.BaseActionModuleHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseModuleHandler
    
        Interfaces:
            org.openhab.core.automation.handler.ActionHandler
    
      Constructors:
        * BaseActionModuleHandler(org.openhab.core.automation.Action)
    
    """
    def __init__(self, module: org.openhab.core.automation.Action): ...

class BaseConditionModuleHandler(BaseModuleHandler[org.openhab.core.automation.Condition], ConditionHandler):
    """
    Java class 'org.openhab.core.automation.handler.BaseConditionModuleHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseModuleHandler
    
        Interfaces:
            org.openhab.core.automation.handler.ConditionHandler
    
      Constructors:
        * BaseConditionModuleHandler(org.openhab.core.automation.Condition)
    
    """
    def __init__(self, module: org.openhab.core.automation.Condition): ...

class BaseTriggerModuleHandler(BaseModuleHandler[org.openhab.core.automation.Trigger], TriggerHandler):
    """
    Java class 'org.openhab.core.automation.handler.BaseTriggerModuleHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseModuleHandler
    
        Interfaces:
            org.openhab.core.automation.handler.TriggerHandler
    
      Constructors:
        * BaseTriggerModuleHandler(org.openhab.core.automation.Trigger)
    
    """
    def __init__(self, module: org.openhab.core.automation.Trigger): ...
