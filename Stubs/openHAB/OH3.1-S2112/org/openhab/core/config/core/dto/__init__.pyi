import java.lang
import java.math
import java.util
import org.openhab.core.config.core
import typing


class ConfigDescriptionDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.dto.ConfigDescriptionDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConfigDescriptionDTO(java.lang.String, java.util.List, java.util.List)
    
      Attributes:
        uri (java.lang.String): field
        parameters (java.util.List): field
        parameterGroups (java.util.List): field
    
    """
    uri: java.lang.String = ...
    parameters: java.util.List = ...
    parameterGroups: java.util.List = ...
    def __init__(self, uri: java.lang.String, parameters: java.util.List['ConfigDescriptionParameterDTO'], parameterGroups: java.util.List['ConfigDescriptionParameterGroupDTO']): ...

class ConfigDescriptionDTOMapper(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.dto.ConfigDescriptionDTOMapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConfigDescriptionDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, parameters: java.util.List['ConfigDescriptionParameterDTO']) -> java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]: ...
    @classmethod
    @typing.overload
    def map(cls, configDescription: org.openhab.core.config.core.ConfigDescription) -> ConfigDescriptionDTO: ...
    @classmethod
    def mapParameterGroups(cls, parameterGroups: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameterGroup]) -> java.util.List['ConfigDescriptionParameterGroupDTO']: ...
    @classmethod
    def mapParameters(cls, parameters: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]) -> java.util.List['ConfigDescriptionParameterDTO']: ...

class ConfigDescriptionParameterDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.dto.ConfigDescriptionParameterDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConfigDescriptionParameterDTO()
        * ConfigDescriptionParameterDTO(java.lang.String, org.openhab.core.config.core.ConfigDescriptionParameter.Type, java.math.BigDecimal, java.math.BigDecimal, java.math.BigDecimal, java.lang.String, java.lang.Boolean, java.lang.Boolean, java.lang.Boolean, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.util.List, java.util.List, java.lang.String, java.lang.Boolean, java.lang.Boolean, java.lang.Integer, java.lang.String, java.lang.String, java.lang.Boolean)
    
      Attributes:
        context (java.lang.String): field
        defaultValue (java.lang.String): field
        description (java.lang.String): field
        label (java.lang.String): field
        name (java.lang.String): field
        required (boolean): field
        type (org.openhab.core.config.core.ConfigDescriptionParameter$Type): field
        min (java.math.BigDecimal): field
        max (java.math.BigDecimal): field
        stepsize (java.math.BigDecimal): field
        pattern (java.lang.String): field
        readOnly (java.lang.Boolean): field
        multiple (java.lang.Boolean): field
        multipleLimit (java.lang.Integer): field
        groupName (java.lang.String): field
        advanced (java.lang.Boolean): field
        verify (java.lang.Boolean): field
        limitToOptions (java.lang.Boolean): field
        unit (java.lang.String): field
        unitLabel (java.lang.String): field
        options (java.util.List): field
        filterCriteria (java.util.List): field
    
    """
    context: java.lang.String = ...
    defaultValue: java.lang.String = ...
    description: java.lang.String = ...
    label: java.lang.String = ...
    name: java.lang.String = ...
    required: bool = ...
    type: org.openhab.core.config.core.ConfigDescriptionParameter.Type = ...
    min: java.math.BigDecimal = ...
    max: java.math.BigDecimal = ...
    stepsize: java.math.BigDecimal = ...
    pattern: java.lang.String = ...
    readOnly: bool = ...
    multiple: bool = ...
    multipleLimit: int = ...
    groupName: java.lang.String = ...
    advanced: bool = ...
    verify: bool = ...
    limitToOptions: bool = ...
    unit: java.lang.String = ...
    unitLabel: java.lang.String = ...
    options: java.util.List = ...
    filterCriteria: java.util.List = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, name: java.lang.String, type: org.openhab.core.config.core.ConfigDescriptionParameter.Type, minimum: java.math.BigDecimal, maximum: java.math.BigDecimal, stepsize: java.math.BigDecimal, pattern: java.lang.String, required: bool, readOnly: bool, multiple: bool, context: java.lang.String, defaultValue: java.lang.String, label: java.lang.String, description: java.lang.String, options: java.util.List['ParameterOptionDTO'], filterCriteria: java.util.List['FilterCriteriaDTO'], groupName: java.lang.String, advanced: bool, limitToOptions: bool, multipleLimit: int, unit: java.lang.String, unitLabel: java.lang.String, verify: bool): ...

class ConfigDescriptionParameterGroupDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.dto.ConfigDescriptionParameterGroupDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConfigDescriptionParameterGroupDTO()
        * ConfigDescriptionParameterGroupDTO(java.lang.String, java.lang.String, java.lang.Boolean, java.lang.String, java.lang.String)
    
      Attributes:
        name (java.lang.String): field
        context (java.lang.String): field
        advanced (java.lang.Boolean): field
        label (java.lang.String): field
        description (java.lang.String): field
    
    """
    name: java.lang.String = ...
    context: java.lang.String = ...
    advanced: bool = ...
    label: java.lang.String = ...
    description: java.lang.String = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, name: java.lang.String, context: java.lang.String, advanced: bool, label: java.lang.String, description: java.lang.String): ...

class FilterCriteriaDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.dto.FilterCriteriaDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * FilterCriteriaDTO()
        * FilterCriteriaDTO(java.lang.String, java.lang.String)
    
      Attributes:
        value (java.lang.String): field
        name (java.lang.String): field
    
    """
    value: java.lang.String = ...
    name: java.lang.String = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, name: java.lang.String, value: java.lang.String): ...

class ParameterOptionDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.dto.ParameterOptionDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ParameterOptionDTO()
        * ParameterOptionDTO(java.lang.String, java.lang.String)
    
      Attributes:
        label (java.lang.String): field
        value (java.lang.String): field
    
    """
    label: java.lang.String = ...
    value: java.lang.String = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, value: java.lang.String, label: java.lang.String): ...
