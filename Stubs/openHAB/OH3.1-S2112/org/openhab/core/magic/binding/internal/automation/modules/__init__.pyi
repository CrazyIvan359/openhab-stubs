import java.lang
import java.util
import org.openhab.core.automation
import org.openhab.core.thing.binding
import typing


class MagicMultiActionMarker(java.lang.Object):
    """
    Java class 'org.openhab.core.magic.binding.internal.automation.modules.MagicMultiActionMarker'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MagicMultiActionMarker()
    
    """
    def __init__(self): ...

class MagicMultiServiceMultiActions(org.openhab.core.automation.AnnotatedActions):
    """
    Java class 'org.openhab.core.magic.binding.internal.automation.modules.MagicMultiServiceMultiActions'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.AnnotatedActions
    
      Constructors:
        * MagicMultiServiceMultiActions()
    
    """
    def __init__(self): ...
    def booleanMethod(self, input1: java.lang.String, input2: java.lang.String) -> bool: ...
    def testMethod(self, input1: java.lang.String, input2: java.lang.String) -> java.util.Map[java.lang.String, typing.Any]: ...
    def voidMethod(self, input1: java.lang.String, input2: java.lang.String) -> None: ...

class MagicSingleActionService(org.openhab.core.automation.AnnotatedActions):
    """
    Java class 'org.openhab.core.magic.binding.internal.automation.modules.MagicSingleActionService'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.AnnotatedActions
    
      Constructors:
        * MagicSingleActionService()
    
    """
    def __init__(self): ...
    def singleServiceAction(self, input1: java.lang.String, input2: java.lang.String, input3: java.lang.String, input4: java.lang.String) -> java.util.Map[java.lang.String, typing.Any]: ...

class MagicThingActionsService(org.openhab.core.thing.binding.ThingActions):
    """
    Java class 'org.openhab.core.magic.binding.internal.automation.modules.MagicThingActionsService'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.thing.binding.ThingActions
    
      Constructors:
        * MagicThingActionsService()
    
    """
    def __init__(self): ...
    def getThingHandler(self) -> org.openhab.core.thing.binding.ThingHandler: ...
    def setThingHandler(self, handler: org.openhab.core.thing.binding.ThingHandler) -> None: ...
    def thingHandlerAction(self, input1: java.lang.String, input2: java.lang.String) -> java.util.Map[java.lang.String, typing.Any]: ...
