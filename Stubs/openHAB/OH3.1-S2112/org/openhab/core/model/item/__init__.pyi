import java.lang
import org.openhab.core.config.core
import typing


class BindingConfigParseException(java.lang.Exception):
    """
    Java class 'org.openhab.core.model.item.BindingConfigParseException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * BindingConfigParseException(java.lang.String)
        * BindingConfigParseException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, msg: java.lang.String): ...
    @typing.overload
    def __init__(self, msg: java.lang.String, e: java.lang.Exception): ...

class BindingConfigReader(java.lang.Object):
    """
    Java class 'org.openhab.core.model.item.BindingConfigReader'
    
    """
    def getBindingType(self) -> java.lang.String: ...
    def processBindingConfiguration(self, context: java.lang.String, itemType: java.lang.String, itemName: java.lang.String, bindingConfig: java.lang.String, configuration: org.openhab.core.config.core.Configuration) -> None: ...
    def startConfigurationUpdate(self, context: java.lang.String) -> None: ...
    def stopConfigurationUpdate(self, context: java.lang.String) -> None: ...
    def validateItemType(self, itemType: java.lang.String, bindingConfig: java.lang.String) -> None: ...
