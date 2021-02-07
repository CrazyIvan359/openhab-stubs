import java.lang
import java.util
import org.openhab.core.automation
import org.openhab.core.automation.handler
import org.openhab.core.automation.module.script
import org.openhab.core.automation.module.script.rulesupport.shared
import org.openhab.core.automation.type
import org.openhab.core.common.registry
import typing


class AbstractScriptedModuleHandlerFactory(org.openhab.core.automation.handler.BaseModuleHandlerFactory):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.internal.AbstractScriptedModuleHandlerFactory'
    
        Extends:
            org.openhab.core.automation.handler.BaseModuleHandlerFactory
    
      Constructors:
        * AbstractScriptedModuleHandlerFactory()
    
    """
    def __init__(self): ...

class RuleSupportScriptExtension(org.openhab.core.automation.module.script.ScriptExtensionProvider):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.internal.RuleSupportScriptExtension'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.module.script.ScriptExtensionProvi
            der
    
      Constructors:
        * RuleSupportScriptExtension(org.openhab.core.automation.RuleRegistry, org.openhab.core.automation.module.script.rulesupport.shared.ScriptedRuleProvider, org.openhab.core.automation.module.script.rulesupport.internal.ScriptedCustomModuleHandlerFactory, org.openhab.core.automation.module.script.rulesupport.internal.ScriptedCustomModuleTypeProvider, org.openhab.core.automation.module.script.rulesupport.internal.ScriptedPrivateModuleHandlerFactory)
    
    """
    def __init__(self, ruleRegistry: org.openhab.core.automation.RuleRegistry, ruleProvider: org.openhab.core.automation.module.script.rulesupport.shared.ScriptedRuleProvider, scriptedCustomModuleHandlerFactory: 'ScriptedCustomModuleHandlerFactory', scriptedCustomModuleTypeProvider: 'ScriptedCustomModuleTypeProvider', scriptedPrivateModuleHandlerFactory: 'ScriptedPrivateModuleHandlerFactory'): ...
    def get(self, scriptIdentifier: java.lang.String, type: java.lang.String) -> typing.Any: ...
    def getDefaultPresets(self) -> java.util.Collection[java.lang.String]: ...
    def getPresets(self) -> java.util.Collection[java.lang.String]: ...
    def getTypes(self) -> java.util.Collection[java.lang.String]: ...
    def importPreset(self, scriptIdentifier: java.lang.String, preset: java.lang.String) -> java.util.Map[java.lang.String, typing.Any]: ...
    def unload(self, scriptIdentifier: java.lang.String) -> None: ...

class ScriptedCustomModuleTypeProvider(org.openhab.core.automation.type.ModuleTypeProvider):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.internal.ScriptedCustomModuleTypeProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.type.ModuleTypeProvider
    
      Constructors:
        * ScriptedCustomModuleTypeProvider()
    
    """
    def __init__(self): ...
    def addModuleType(self, moduleType: org.openhab.core.automation.type.ModuleType) -> None: ...
    def addProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[org.openhab.core.automation.type.ModuleType]) -> None: ...
    def getAll(self) -> java.util.Collection[org.openhab.core.automation.type.ModuleType]: ...
    _getModuleType__T = typing.TypeVar('_getModuleType__T', bound=org.openhab.core.automation.type.ModuleType)  # <T>
    def getModuleType(self, UID: java.lang.String, locale: java.util.Locale) -> _getModuleType__T: ...
    _getModuleTypes__T = typing.TypeVar('_getModuleTypes__T', bound=org.openhab.core.automation.type.ModuleType)  # <T>
    def getModuleTypes(self, locale: java.util.Locale) -> java.util.Collection[_getModuleTypes__T]: ...
    @typing.overload
    def removeModuleType(self, moduleTypeUID: java.lang.String) -> None: ...
    @typing.overload
    def removeModuleType(self, moduleType: org.openhab.core.automation.type.ModuleType) -> None: ...
    def removeProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[org.openhab.core.automation.type.ModuleType]) -> None: ...
    def updateModuleHandler(self, uid: java.lang.String) -> None: ...

class ScriptedCustomModuleHandlerFactory(AbstractScriptedModuleHandlerFactory):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.internal.ScriptedCustomModuleHandlerFactory'
    
        Extends:
            org.openhab.core.automation.module.script.rulesupport.internal.AbstractScriptedModuleHandlerFactory
    
      Constructors:
        * ScriptedCustomModuleHandlerFactory()
    
    """
    def __init__(self): ...
    def addModuleHandler(self, uid: java.lang.String, scriptedHandler: org.openhab.core.automation.module.script.rulesupport.shared.ScriptedHandler) -> None: ...
    def getTypes(self) -> java.util.Collection[java.lang.String]: ...
    def removeModuleHandler(self, uid: java.lang.String) -> None: ...

class ScriptedPrivateModuleHandlerFactory(AbstractScriptedModuleHandlerFactory):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.internal.ScriptedPrivateModuleHandlerFactory'
    
        Extends:
            org.openhab.core.automation.module.script.rulesupport.internal.AbstractScriptedModuleHandlerFactory
    
      Constructors:
        * ScriptedPrivateModuleHandlerFactory()
    
    """
    def __init__(self): ...
    @typing.overload
    def addHandler(self, privId: java.lang.String, scriptedHandler: org.openhab.core.automation.module.script.rulesupport.shared.ScriptedHandler) -> java.lang.String: ...
    @typing.overload
    def addHandler(self, scriptedHandler: org.openhab.core.automation.module.script.rulesupport.shared.ScriptedHandler) -> java.lang.String: ...
    def getTypes(self) -> java.util.Collection[java.lang.String]: ...
    def removeHandler(self, privId: java.lang.String) -> None: ...
