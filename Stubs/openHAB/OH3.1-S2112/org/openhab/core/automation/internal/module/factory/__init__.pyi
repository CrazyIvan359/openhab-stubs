import java.lang
import java.util
import org.openhab.core.automation.handler
import org.openhab.core.ephemeris


class CoreModuleHandlerFactory(org.openhab.core.automation.handler.BaseModuleHandlerFactory):
    """
    Java class 'org.openhab.core.automation.internal.module.factory.CoreModuleHandlerFactory'
    
        Extends:
            org.openhab.core.automation.handler.BaseModuleHandlerFactory
    
        Interfaces:
            org.openhab.core.automation.handler.ModuleHandlerFactory
    
      Constructors:
        * CoreModuleHandlerFactory()
    
    """
    def __init__(self): ...
    def getTypes(self) -> java.util.Collection[java.lang.String]: ...

class EphemerisModuleHandlerFactory(org.openhab.core.automation.handler.BaseModuleHandlerFactory):
    """
    Java class 'org.openhab.core.automation.internal.module.factory.EphemerisModuleHandlerFactory'
    
        Extends:
            org.openhab.core.automation.handler.BaseModuleHandlerFactory
    
        Interfaces:
            org.openhab.core.automation.handler.ModuleHandlerFactory
    
      Constructors:
        * EphemerisModuleHandlerFactory(org.openhab.core.ephemeris.EphemerisManager)
    
    """
    def __init__(self, ephemerisManager: org.openhab.core.ephemeris.EphemerisManager): ...
    def getTypes(self) -> java.util.Collection[java.lang.String]: ...
