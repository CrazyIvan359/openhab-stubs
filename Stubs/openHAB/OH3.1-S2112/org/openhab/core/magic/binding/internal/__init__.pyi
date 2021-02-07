import java.lang
import java.math
import java.net
import java.util
import org.openhab.core.config.core
import org.openhab.core.config.discovery
import org.openhab.core.magic.binding
import org.openhab.core.thing
import org.openhab.core.thing.binding
import typing


class MagicDiscoveryService(org.openhab.core.config.discovery.AbstractDiscoveryService):
    """
    Java class 'org.openhab.core.magic.binding.internal.MagicDiscoveryService'
    
        Extends:
            org.openhab.core.config.discovery.AbstractDiscoveryService
    
      Constructors:
        * MagicDiscoveryService()
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
    """
    def __init__(self): ...

class MagicDynamicStateDescriptionProvider(org.openhab.core.thing.binding.BaseDynamicStateDescriptionProvider):
    """
    Java class 'org.openhab.core.magic.binding.internal.MagicDynamicStateDescriptionProvider'
    
        Extends:
            org.openhab.core.thing.binding.BaseDynamicStateDescriptionProvider
    
      Constructors:
        * MagicDynamicStateDescriptionProvider()
    
    """
    def __init__(self): ...

class MagicHandlerFactory(org.openhab.core.thing.binding.BaseThingHandlerFactory):
    """
    Java class 'org.openhab.core.magic.binding.internal.MagicHandlerFactory'
    
        Extends:
            org.openhab.core.thing.binding.BaseThingHandlerFactory
    
      Constructors:
        * MagicHandlerFactory(org.openhab.core.magic.binding.internal.MagicDynamicStateDescriptionProvider)
    
    """
    def __init__(self, stateDescriptionProvider: MagicDynamicStateDescriptionProvider): ...
    def supportsThingType(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID) -> bool: ...

class MagicServiceConfig(java.lang.Object):
    """
    Java class 'org.openhab.core.magic.binding.internal.MagicServiceConfig'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MagicServiceConfig()
    
      Attributes:
        text (java.lang.String): field
        bool (boolean): field
        decimal (java.math.BigDecimal): field
        integer (java.lang.Integer): field
        text_advanced (java.lang.String): field
        boolean_advanced (boolean): field
        decimal_advanced (java.math.BigDecimal): field
        integer_advanced (java.lang.Integer): field
        requiredTextParameter (java.lang.String): field
        verifiedTextParameter (java.lang.String): field
        select_limited (java.lang.String): field
        select_variable (java.lang.String): field
        multiselect_text_limit (java.util.List): field
        multiselect_integer_limit (java.util.List): field
        select_decimal_limit (java.math.BigDecimal): field
    
    """
    text: java.lang.String = ...
    bool: bool = ...
    decimal: java.math.BigDecimal = ...
    integer: int = ...
    text_advanced: java.lang.String = ...
    boolean_advanced: bool = ...
    decimal_advanced: java.math.BigDecimal = ...
    integer_advanced: int = ...
    requiredTextParameter: java.lang.String = ...
    verifiedTextParameter: java.lang.String = ...
    select_limited: java.lang.String = ...
    select_variable: java.lang.String = ...
    multiselect_text_limit: java.util.List = ...
    multiselect_integer_limit: java.util.List = ...
    select_decimal_limit: java.math.BigDecimal = ...
    def __init__(self): ...
    def toString(self) -> java.lang.String: ...

class MagicServiceImpl(org.openhab.core.magic.binding.MagicService):
    """
    Java class 'org.openhab.core.magic.binding.internal.MagicServiceImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.magic.binding.MagicService
    
      Constructors:
        * MagicServiceImpl()
    
    """
    def __init__(self): ...
    def activate(self, properties: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def getParameterOptions(self, uri: java.net.URI, param: java.lang.String, context: java.lang.String, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.config.core.ParameterOption]: ...
    def modified(self, properties: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
