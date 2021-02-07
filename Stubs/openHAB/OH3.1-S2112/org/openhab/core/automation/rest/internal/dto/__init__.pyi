import org.openhab.core.automation
import org.openhab.core.automation.dto
import typing


class EnrichedRuleDTO(org.openhab.core.automation.dto.RuleDTO):
    """
    Java class 'org.openhab.core.automation.rest.internal.dto.EnrichedRuleDTO'
    
        Extends:
            org.openhab.core.automation.dto.RuleDTO
    
      Constructors:
        * EnrichedRuleDTO()
    
      Attributes:
        status (org.openhab.core.automation.RuleStatusInfo): field
        editable (java.lang.Boolean): field
    
    """
    status: org.openhab.core.automation.RuleStatusInfo = ...
    editable: bool = ...
    def __init__(self): ...

class EnrichedRuleDTOMapper(org.openhab.core.automation.dto.RuleDTOMapper):
    """
    Java class 'org.openhab.core.automation.rest.internal.dto.EnrichedRuleDTOMapper'
    
        Extends:
            org.openhab.core.automation.dto.RuleDTOMapper
    
      Constructors:
        * EnrichedRuleDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, ruleDto: org.openhab.core.automation.dto.RuleDTO) -> org.openhab.core.automation.Rule: ...
    @classmethod
    @typing.overload
    def map(cls, rule: org.openhab.core.automation.Rule) -> org.openhab.core.automation.dto.RuleDTO: ...
    @classmethod
    @typing.overload
    def map(cls, rule: org.openhab.core.automation.Rule, ruleEngine: org.openhab.core.automation.RuleManager, managedRuleProvider: org.openhab.core.automation.ManagedRuleProvider) -> EnrichedRuleDTO: ...
