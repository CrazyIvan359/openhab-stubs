import java.lang
import org.openhab.core.audio
import org.openhab.core.ephemeris
import org.openhab.core.model.script.engine.action
import org.openhab.core.thing
import org.openhab.core.thing.binding
import org.openhab.core.voice
import typing


class AudioActionService(org.openhab.core.model.script.engine.action.ActionService):
    """
    Java class 'org.openhab.core.model.script.internal.engine.action.AudioActionService'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.script.engine.action.ActionService
    
      Constructors:
        * AudioActionService()
    
      Attributes:
        audioManager (org.openhab.core.audio.AudioManager): static field
    
    """
    audioManager: typing.ClassVar[org.openhab.core.audio.AudioManager] = ...
    def __init__(self): ...
    def getActionClass(self) -> typing.Type[typing.Any]: ...

class EphemerisActionService(org.openhab.core.model.script.engine.action.ActionService):
    """
    Java class 'org.openhab.core.model.script.internal.engine.action.EphemerisActionService'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.script.engine.action.ActionService
    
      Constructors:
        * EphemerisActionService()
    
      Attributes:
        ephemerisManager (org.openhab.core.ephemeris.EphemerisManager): static field
    
    """
    ephemerisManager: typing.ClassVar[org.openhab.core.ephemeris.EphemerisManager] = ...
    def __init__(self): ...
    def getActionClass(self) -> typing.Type[typing.Any]: ...

class PersistenceActionService(org.openhab.core.model.script.engine.action.ActionService):
    """
    Java class 'org.openhab.core.model.script.internal.engine.action.PersistenceActionService'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.script.engine.action.ActionService
    
      Constructors:
        * PersistenceActionService()
    
    """
    def __init__(self): ...
    def getActionClass(self) -> typing.Type[typing.Any]: ...

class ThingActionService(org.openhab.core.model.script.engine.action.ActionService):
    """
    Java class 'org.openhab.core.model.script.internal.engine.action.ThingActionService'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.script.engine.action.ActionService
    
      Constructors:
        * ThingActionService(org.openhab.core.thing.ThingRegistry)
    
    """
    def __init__(self, thingRegistry: org.openhab.core.thing.ThingRegistry): ...
    def addThingActions(self, thingActions: org.openhab.core.thing.binding.ThingActions) -> None: ...
    def getActionClass(self) -> typing.Type[typing.Any]: ...
    @classmethod
    def getActions(cls, scope: java.lang.String, thingUid: java.lang.String) -> org.openhab.core.thing.binding.ThingActions: ...
    @classmethod
    def getThingStatusInfo(cls, thingUid: java.lang.String) -> org.openhab.core.thing.ThingStatusInfo: ...
    def removeThingActions(self, thingActions: org.openhab.core.thing.binding.ThingActions) -> None: ...

class TransformationActionService(org.openhab.core.model.script.engine.action.ActionService):
    """
    Java class 'org.openhab.core.model.script.internal.engine.action.TransformationActionService'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.script.engine.action.ActionService
    
      Constructors:
        * TransformationActionService()
    
    """
    def __init__(self): ...
    def getActionClass(self) -> typing.Type[typing.Any]: ...

class VoiceActionService(org.openhab.core.model.script.engine.action.ActionService):
    """
    Java class 'org.openhab.core.model.script.internal.engine.action.VoiceActionService'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.script.engine.action.ActionService
    
      Constructors:
        * VoiceActionService()
    
      Attributes:
        voiceManager (org.openhab.core.voice.VoiceManager): static field
    
    """
    voiceManager: typing.ClassVar[org.openhab.core.voice.VoiceManager] = ...
    def __init__(self): ...
    def getActionClass(self) -> typing.Type[typing.Any]: ...
