import java.lang
import typing


class BindingInfoDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.binding.dto.BindingInfoDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * BindingInfoDTO()
        * BindingInfoDTO(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String)
    
      Attributes:
        author (java.lang.String): field
        description (java.lang.String): field
        id (java.lang.String): field
        name (java.lang.String): field
        configDescriptionURI (java.lang.String): field
    
    """
    author: java.lang.String = ...
    description: java.lang.String = ...
    id: java.lang.String = ...
    name: java.lang.String = ...
    configDescriptionURI: java.lang.String = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, id: java.lang.String, name: java.lang.String, author: java.lang.String, description: java.lang.String, configDescriptionURI: java.lang.String): ...
