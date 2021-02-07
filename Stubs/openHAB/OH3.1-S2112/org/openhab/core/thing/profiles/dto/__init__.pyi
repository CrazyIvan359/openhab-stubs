import java.lang
import java.util
import org.openhab.core.thing.profiles
import typing


class ProfileTypeDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.profiles.dto.ProfileTypeDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ProfileTypeDTO()
        * ProfileTypeDTO(java.lang.String, java.lang.String, java.lang.String, java.util.Collection)
    
      Attributes:
        uid (java.lang.String): field
        label (java.lang.String): field
        kind (java.lang.String): field
        supportedItemTypes (java.util.Collection): field
    
    """
    uid: java.lang.String = ...
    label: java.lang.String = ...
    kind: java.lang.String = ...
    supportedItemTypes: java.util.Collection = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, uid: java.lang.String, label: java.lang.String, kind: java.lang.String, supportedItemTypes: typing.Union[java.util.Collection[java.lang.String], typing.Sequence[java.lang.String]]): ...

class ProfileTypeDTOMapper(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.profiles.dto.ProfileTypeDTOMapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ProfileTypeDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    def map(cls, profileType: org.openhab.core.thing.profiles.ProfileType) -> ProfileTypeDTO: ...
