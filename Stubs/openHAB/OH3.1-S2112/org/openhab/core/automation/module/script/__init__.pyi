import java.io
import java.lang
import java.util
import javax.script
import typing


class ScriptEngineContainer(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.module.script.ScriptEngineContainer'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ScriptEngineContainer(javax.script.ScriptEngine, org.openhab.core.automation.module.script.ScriptEngineFactory, java.lang.String)
    
    """
    def __init__(self, scriptEngine: javax.script.ScriptEngine, factory: 'ScriptEngineFactory', identifier: java.lang.String): ...
    def getFactory(self) -> 'ScriptEngineFactory': ...
    def getIdentifier(self) -> java.lang.String: ...
    def getScriptEngine(self) -> javax.script.ScriptEngine: ...

class ScriptEngineFactory(java.lang.Object):
    """
    @NonNullByDefault public interface ScriptEngineFactory
    
        This class is used by the ScriptEngineManager to load ScriptEngines. This is meant as a way to allow other OSGi bundles
        to provide custom script-languages with special needs, e.g. Nashorn, Jython, Groovy, etc.
    
    
    """
    ENGINE_MANAGER: typing.ClassVar[javax.script.ScriptEngineManager] = ...
    CONTEXT_KEY_ENGINE_IDENTIFIER: typing.ClassVar[java.lang.String] = ...
    CONTEXT_KEY_EXTENSION_ACCESSOR: typing.ClassVar[java.lang.String] = ...
    def createScriptEngine(self, scriptType: java.lang.String) -> javax.script.ScriptEngine: ...
    def getScriptTypes(self) -> java.util.List[java.lang.String]: ...
    def scopeValues(self, scriptEngine: javax.script.ScriptEngine, scopeValues: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...

class ScriptEngineManager(java.lang.Object):
    """
    @NonNullByDefault public interface ScriptEngineManager
    
        The ScriptEngineManager provides the ability to load and unload scripts.
    
    
    """
    def createScriptEngine(self, scriptType: java.lang.String, engineIdentifier: java.lang.String) -> ScriptEngineContainer: ...
    def isSupported(self, scriptType: java.lang.String) -> bool: ...
    def loadScript(self, engineIdentifier: java.lang.String, scriptData: java.io.InputStreamReader) -> None: ...
    def removeEngine(self, engineIdentifier: java.lang.String) -> None: ...

class ScriptExtensionAccessor(java.lang.Object):
    """
    @NonNullByDefault public interface ScriptExtensionAccessor
    
        Accessor allowing script engines to lookup presets.
    
    
    """
    def findDefaultPresets(self, scriptIdentifier: java.lang.String) -> java.util.Map[java.lang.String, typing.Any]: ...
    def findPreset(self, preset: java.lang.String, scriptIdentifier: java.lang.String) -> java.util.Map[java.lang.String, typing.Any]: ...

class ScriptExtensionProvider(java.lang.Object):
    """
    @NonNullByDefault public interface ScriptExtensionProvider
    
        A :class:`~org.openhab.core.automation.module.script.ScriptExtensionProvider` can provide variable and types on
        ScriptEngine instance basis.
    
    
    """
    def get(self, scriptIdentifier: java.lang.String, type: java.lang.String) -> typing.Any: ...
    def getDefaultPresets(self) -> java.util.Collection[java.lang.String]: ...
    def getPresets(self) -> java.util.Collection[java.lang.String]: ...
    def getTypes(self) -> java.util.Collection[java.lang.String]: ...
    def importPreset(self, scriptIdentifier: java.lang.String, preset: java.lang.String) -> java.util.Map[java.lang.String, typing.Any]: ...
    def unload(self, scriptIdentifier: java.lang.String) -> None: ...

class AbstractScriptEngineFactory(ScriptEngineFactory):
    """
    Java class 'org.openhab.core.automation.module.script.AbstractScriptEngineFactory'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.module.script.ScriptEngineFactory
    
      Constructors:
        * AbstractScriptEngineFactory()
    
    """
    def __init__(self): ...
    def createScriptEngine(self, scriptType: java.lang.String) -> javax.script.ScriptEngine: ...
    def getScriptTypes(self) -> java.util.List[java.lang.String]: ...
    def scopeValues(self, scriptEngine: javax.script.ScriptEngine, scopeValues: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
