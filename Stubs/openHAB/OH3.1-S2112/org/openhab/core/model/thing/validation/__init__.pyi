import java.lang
import org.eclipse.xtext.validation
import org.openhab.core.model.thing.thing
import org.openhab.core.thing
import typing


class AbstractThingValidator(org.eclipse.xtext.validation.AbstractDeclarativeValidator):
    """
    Java class 'org.openhab.core.model.thing.validation.AbstractThingValidator'
    
        Extends:
            org.eclipse.xtext.validation.AbstractDeclarativeValidator
    
      Constructors:
        * AbstractThingValidator()
    
    """
    def __init__(self): ...

class ThingValidator(AbstractThingValidator):
    """
    Java class 'org.openhab.core.model.thing.validation.ThingValidator'
    
        Extends:
            org.openhab.core.model.thing.validation.AbstractThingValidator
    
      Constructors:
        * ThingValidator()
    
      Attributes:
        INVALID_NAME (java.lang.String): final static field
    
    """
    INVALID_NAME: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    def check_thing_has_valid_id(self, modelThing: org.openhab.core.model.thing.thing.ModelThing) -> org.openhab.core.thing.ThingUID: ...
