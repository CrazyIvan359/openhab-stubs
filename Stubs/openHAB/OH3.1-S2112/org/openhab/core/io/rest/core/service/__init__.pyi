import java.lang


class ConfigurableServiceDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.core.service.ConfigurableServiceDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConfigurableServiceDTO(java.lang.String, java.lang.String, java.lang.String, java.lang.String, boolean)
    
      Attributes:
        id (java.lang.String): field
        label (java.lang.String): field
        category (java.lang.String): field
        configDescriptionURI (java.lang.String): field
        multiple (boolean): field
    
    """
    id: java.lang.String = ...
    label: java.lang.String = ...
    category: java.lang.String = ...
    configDescriptionURI: java.lang.String = ...
    multiple: bool = ...
    def __init__(self, id: java.lang.String, label: java.lang.String, category: java.lang.String, configDescriptionURI: java.lang.String, multiple: bool): ...
