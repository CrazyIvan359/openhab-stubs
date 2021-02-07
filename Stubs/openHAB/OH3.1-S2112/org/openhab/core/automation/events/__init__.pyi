import java.lang
import org.openhab.core.automation
import org.openhab.core.automation.dto
import org.openhab.core.events
import typing


class AbstractRuleRegistryEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.automation.events.AbstractRuleRegistryEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
      Constructors:
        * AbstractRuleRegistryEvent(java.lang.String, java.lang.String, java.lang.String, org.openhab.core.automation.dto.RuleDTO)
    
    """
    def __init__(self, topic: java.lang.String, payload: java.lang.String, source: java.lang.String, rule: org.openhab.core.automation.dto.RuleDTO): ...
    def getRule(self) -> org.openhab.core.automation.dto.RuleDTO: ...

class RuleStatusInfoEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.automation.events.RuleStatusInfoEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
      Constructors:
        * RuleStatusInfoEvent(java.lang.String, java.lang.String, java.lang.String, org.openhab.core.automation.RuleStatusInfo, java.lang.String)
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, topic: java.lang.String, payload: java.lang.String, source: java.lang.String, statusInfo: org.openhab.core.automation.RuleStatusInfo, ruleId: java.lang.String): ...
    def getRuleId(self) -> java.lang.String: ...
    def getStatusInfo(self) -> org.openhab.core.automation.RuleStatusInfo: ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class RuleAddedEvent(AbstractRuleRegistryEvent):
    """
    Java class 'org.openhab.core.automation.events.RuleAddedEvent'
    
        Extends:
            org.openhab.core.automation.events.AbstractRuleRegistryEvent
    
      Constructors:
        * RuleAddedEvent(java.lang.String, java.lang.String, java.lang.String, org.openhab.core.automation.dto.RuleDTO)
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, topic: java.lang.String, payload: java.lang.String, source: java.lang.String, rule: org.openhab.core.automation.dto.RuleDTO): ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class RuleRemovedEvent(AbstractRuleRegistryEvent):
    """
    Java class 'org.openhab.core.automation.events.RuleRemovedEvent'
    
        Extends:
            org.openhab.core.automation.events.AbstractRuleRegistryEvent
    
      Constructors:
        * RuleRemovedEvent(java.lang.String, java.lang.String, java.lang.String, org.openhab.core.automation.dto.RuleDTO)
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, topic: java.lang.String, payload: java.lang.String, source: java.lang.String, rule: org.openhab.core.automation.dto.RuleDTO): ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class RuleUpdatedEvent(AbstractRuleRegistryEvent):
    """
    Java class 'org.openhab.core.automation.events.RuleUpdatedEvent'
    
        Extends:
            org.openhab.core.automation.events.AbstractRuleRegistryEvent
    
      Constructors:
        * RuleUpdatedEvent(java.lang.String, java.lang.String, java.lang.String, org.openhab.core.automation.dto.RuleDTO, org.openhab.core.automation.dto.RuleDTO)
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, topic: java.lang.String, payload: java.lang.String, source: java.lang.String, rule: org.openhab.core.automation.dto.RuleDTO, oldRule: org.openhab.core.automation.dto.RuleDTO): ...
    def getOldRule(self) -> org.openhab.core.automation.dto.RuleDTO: ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
