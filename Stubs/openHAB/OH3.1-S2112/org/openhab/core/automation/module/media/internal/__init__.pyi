import java.lang
import java.util
import org.openhab.core.audio
import org.openhab.core.automation
import org.openhab.core.automation.handler
import org.openhab.core.automation.module.script
import org.openhab.core.automation.type
import org.openhab.core.common.registry
import org.openhab.core.voice
import typing


class MediaActionTypeProvider(org.openhab.core.automation.type.ModuleTypeProvider):
    """
    Java class 'org.openhab.core.automation.module.media.internal.MediaActionTypeProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.type.ModuleTypeProvider
    
      Constructors:
        * MediaActionTypeProvider(org.openhab.core.audio.AudioManager)
    
    """
    def __init__(self, audioManager: org.openhab.core.audio.AudioManager): ...
    def addProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[org.openhab.core.automation.type.ModuleType]) -> None: ...
    def getAll(self) -> java.util.Collection[org.openhab.core.automation.type.ModuleType]: ...
    def getModuleType(self, UID: java.lang.String, locale: java.util.Locale) -> org.openhab.core.automation.type.ModuleType: ...
    def getModuleTypes(self, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.automation.type.ModuleType]: ...
    def removeProviderChangeListener(self, listener: org.openhab.core.common.registry.ProviderChangeListener[org.openhab.core.automation.type.ModuleType]) -> None: ...

class MediaModuleHandlerFactory(org.openhab.core.automation.handler.BaseModuleHandlerFactory):
    """
    Java class 'org.openhab.core.automation.module.media.internal.MediaModuleHandlerFactory'
    
        Extends:
            org.openhab.core.automation.handler.BaseModuleHandlerFactory
    
      Constructors:
        * MediaModuleHandlerFactory(org.openhab.core.audio.AudioManager, org.openhab.core.voice.VoiceManager)
    
    """
    def __init__(self, audioManager: org.openhab.core.audio.AudioManager, voiceManager: org.openhab.core.voice.VoiceManager): ...
    def getTypes(self) -> java.util.Collection[java.lang.String]: ...

class MediaScriptScopeProvider(org.openhab.core.automation.module.script.ScriptExtensionProvider):
    """
    Java class 'org.openhab.core.automation.module.media.internal.MediaScriptScopeProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.module.script.ScriptExtensionProvi
            der
    
      Constructors:
        * MediaScriptScopeProvider()
    
    """
    def __init__(self): ...
    def get(self, scriptIdentifier: java.lang.String, type: java.lang.String) -> typing.Any: ...
    def getDefaultPresets(self) -> java.util.Collection[java.lang.String]: ...
    def getPresets(self) -> java.util.Collection[java.lang.String]: ...
    def getTypes(self) -> java.util.Collection[java.lang.String]: ...
    def importPreset(self, scriptIdentifier: java.lang.String, preset: java.lang.String) -> java.util.Map[java.lang.String, typing.Any]: ...
    def unload(self, scriptIdentifier: java.lang.String) -> None: ...

class PlayActionHandler(org.openhab.core.automation.handler.BaseActionModuleHandler):
    """
    Java class 'org.openhab.core.automation.module.media.internal.PlayActionHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseActionModuleHandler
    
      Constructors:
        * PlayActionHandler(org.openhab.core.automation.Action, org.openhab.core.audio.AudioManager)
    
      Attributes:
        TYPE_ID (java.lang.String): final static field
        PARAM_SOUND (java.lang.String): final static field
        PARAM_SINK (java.lang.String): final static field
        PARAM_VOLUME (java.lang.String): final static field
    
    """
    TYPE_ID: typing.ClassVar[java.lang.String] = ...
    PARAM_SOUND: typing.ClassVar[java.lang.String] = ...
    PARAM_SINK: typing.ClassVar[java.lang.String] = ...
    PARAM_VOLUME: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Action, audioManager: org.openhab.core.audio.AudioManager): ...
    def execute(self, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> java.util.Map[java.lang.String, typing.Any]: ...

class SayActionHandler(org.openhab.core.automation.handler.BaseActionModuleHandler):
    """
    Java class 'org.openhab.core.automation.module.media.internal.SayActionHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseActionModuleHandler
    
      Constructors:
        * SayActionHandler(org.openhab.core.automation.Action, org.openhab.core.voice.VoiceManager)
    
      Attributes:
        TYPE_ID (java.lang.String): final static field
        PARAM_TEXT (java.lang.String): final static field
        PARAM_SINK (java.lang.String): final static field
        PARAM_VOLUME (java.lang.String): final static field
    
    """
    TYPE_ID: typing.ClassVar[java.lang.String] = ...
    PARAM_TEXT: typing.ClassVar[java.lang.String] = ...
    PARAM_SINK: typing.ClassVar[java.lang.String] = ...
    PARAM_VOLUME: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Action, voiceManager: org.openhab.core.voice.VoiceManager): ...
    def execute(self, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> java.util.Map[java.lang.String, typing.Any]: ...
