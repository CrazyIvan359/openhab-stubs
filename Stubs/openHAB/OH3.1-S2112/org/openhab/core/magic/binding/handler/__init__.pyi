import java.lang
import java.util
import org.openhab.core.magic.binding.internal
import org.openhab.core.thing
import org.openhab.core.thing.binding
import org.openhab.core.thing.binding.firmware
import org.openhab.core.types
import typing


class MagicActionModuleThingHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicActionModuleThingHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicActionModuleThingHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def communicateActionToDevice(self, doSomething: java.lang.String) -> None: ...
    def getServices(self) -> java.util.Collection[typing.Type[org.openhab.core.thing.binding.ThingHandlerService]]: ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicBridgeHandler(org.openhab.core.thing.binding.BaseBridgeHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicBridgeHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseBridgeHandler
    
      Constructors:
        * MagicBridgeHandler(org.openhab.core.thing.Bridge)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Bridge): ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicBridgedThingHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicBridgedThingHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicBridgedThingHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicChattyThingHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicChattyThingHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicChattyThingHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def channelLinked(self, channelUID: org.openhab.core.thing.ChannelUID) -> None: ...
    def channelUnlinked(self, channelUID: org.openhab.core.thing.ChannelUID) -> None: ...
    def dispose(self) -> None: ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicColorLightHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicColorLightHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicColorLightHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicConfigurableThingHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicConfigurableThingHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicConfigurableThingHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def handleConfigurationUpdate(self, configurationParameters: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def initialize(self) -> None: ...

class MagicContactHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicContactHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicContactHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicDelayedOnlineHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicDelayedOnlineHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicDelayedOnlineHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicDimmableLightHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicDimmableLightHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicDimmableLightHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicDynamicStateDescriptionThingHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicDynamicStateDescriptionThingHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicDynamicStateDescriptionThingHandler(org.openhab.core.thing.Thing, org.openhab.core.magic.binding.internal.MagicDynamicStateDescriptionProvider)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing, stateDescriptionProvider: org.openhab.core.magic.binding.internal.MagicDynamicStateDescriptionProvider): ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicExtensibleThingHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicExtensibleThingHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicExtensibleThingHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicFirmwareUpdateThingHandler(org.openhab.core.thing.binding.BaseThingHandler, org.openhab.core.thing.binding.firmware.FirmwareUpdateHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicFirmwareUpdateThingHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
        Interfaces:
            org.openhab.core.thing.binding.firmware.FirmwareUpdateHandler
    
      Constructors:
        * MagicFirmwareUpdateThingHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def cancel(self) -> None: ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...
    def isUpdateExecutable(self) -> bool: ...
    def updateFirmware(self, firmware: org.openhab.core.thing.binding.firmware.Firmware, progressCallback: org.openhab.core.thing.binding.firmware.ProgressCallback) -> None: ...

class MagicImageHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicImageHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicImageHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicLocationThingHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicLocationThingHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicLocationThingHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicOnOffLightHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicOnOffLightHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicOnOffLightHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicOnlineOfflineHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicOnlineOfflineHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicOnlineOfflineHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def dispose(self) -> None: ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicPlayerHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicPlayerHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicPlayerHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicRolllershutterHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicRolllershutterHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicRolllershutterHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...

class MagicThermostatThingHandler(org.openhab.core.thing.binding.BaseThingHandler):
    """
    Java class 'org.openhab.core.magic.binding.handler.MagicThermostatThingHandler'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandler
    
      Constructors:
        * MagicThermostatThingHandler(org.openhab.core.thing.Thing)
    
    """
    def __init__(self, thing: org.openhab.core.thing.Thing): ...
    def handleCommand(self, channelUID: org.openhab.core.thing.ChannelUID, command: org.openhab.core.types.Command) -> None: ...
    def initialize(self) -> None: ...
