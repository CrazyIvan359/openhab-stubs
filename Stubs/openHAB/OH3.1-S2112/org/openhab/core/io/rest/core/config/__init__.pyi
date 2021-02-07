import java.lang
import java.math
import java.util
import org.openhab.core.config.core
import org.openhab.core.config.core.dto
import typing


class ConfigurationService(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.core.config.ConfigurationService'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConfigurationService()
    
    """
    def __init__(self): ...
    def delete(self, configId: java.lang.String) -> org.openhab.core.config.core.Configuration: ...
    def get(self, configId: java.lang.String) -> org.openhab.core.config.core.Configuration: ...
    def getProperty(self, servicePID: java.lang.String, key: java.lang.String) -> java.lang.String: ...
    @typing.overload
    def update(self, configId: java.lang.String, newConfiguration: org.openhab.core.config.core.Configuration) -> org.openhab.core.config.core.Configuration: ...
    @typing.overload
    def update(self, configId: java.lang.String, newConfiguration: org.openhab.core.config.core.Configuration, override: bool) -> org.openhab.core.config.core.Configuration: ...

class EnrichedConfigDescriptionDTOMapper(org.openhab.core.config.core.dto.ConfigDescriptionDTOMapper):
    """
    Java class 'org.openhab.core.io.rest.core.config.EnrichedConfigDescriptionDTOMapper'
    
        Extends:
            org.openhab.core.config.core.dto.ConfigDescriptionDTOMapper
    
      Constructors:
        * EnrichedConfigDescriptionDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, parameters: java.util.List[org.openhab.core.config.core.dto.ConfigDescriptionParameterDTO]) -> java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]: ...
    @classmethod
    @typing.overload
    def map(cls, configDescription: org.openhab.core.config.core.ConfigDescription) -> org.openhab.core.config.core.dto.ConfigDescriptionDTO: ...
    @classmethod
    def mapEnrichedParameters(cls, parameters: java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]) -> java.util.List[org.openhab.core.config.core.dto.ConfigDescriptionParameterDTO]: ...

class EnrichedConfigDescriptionParameterDTO(org.openhab.core.config.core.dto.ConfigDescriptionParameterDTO):
    """
    Java class 'org.openhab.core.io.rest.core.config.EnrichedConfigDescriptionParameterDTO'
    
        Extends:
            org.openhab.core.config.core.dto.ConfigDescriptionParameterDTO
    
      Constructors:
        * EnrichedConfigDescriptionParameterDTO(java.lang.String, org.openhab.core.config.core.ConfigDescriptionParameter.Type, java.math.BigDecimal, java.math.BigDecimal, java.math.BigDecimal, java.lang.String, java.lang.Boolean, java.lang.Boolean, java.lang.Boolean, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.util.List, java.util.List, java.lang.String, java.lang.Boolean, java.lang.Boolean, java.lang.Integer, java.lang.String, java.lang.String, java.lang.Boolean)
    
      Attributes:
        defaultValues (java.util.Collection): field
    
    """
    defaultValues: java.util.Collection = ...
    def __init__(self, name: java.lang.String, type: org.openhab.core.config.core.ConfigDescriptionParameter.Type, minimum: java.math.BigDecimal, maximum: java.math.BigDecimal, stepsize: java.math.BigDecimal, pattern: java.lang.String, required: bool, readOnly: bool, multiple: bool, context: java.lang.String, defaultValue: java.lang.String, label: java.lang.String, description: java.lang.String, options: java.util.List[org.openhab.core.config.core.dto.ParameterOptionDTO], filterCriteria: java.util.List[org.openhab.core.config.core.dto.FilterCriteriaDTO], groupName: java.lang.String, advanced: bool, limitToOptions: bool, multipleLimit: int, unit: java.lang.String, unitLabel: java.lang.String, verify: bool): ...
