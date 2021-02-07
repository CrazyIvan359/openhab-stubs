import java.lang
import java.util
import org.openhab.core.automation
import org.openhab.core.automation.template
import org.openhab.core.automation.type
import typing


class ModuleDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.dto.ModuleDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ModuleDTO()
    
      Attributes:
        id (java.lang.String): field
        label (java.lang.String): field
        description (java.lang.String): field
        configuration (java.util.Map): field
        type (java.lang.String): field
    
    """
    id: java.lang.String = ...
    label: java.lang.String = ...
    description: java.lang.String = ...
    configuration: java.util.Map = ...
    type: java.lang.String = ...
    def __init__(self): ...

class ModuleDTOMapper(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.dto.ModuleDTOMapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ModuleDTOMapper()
    
    """
    def __init__(self): ...

class ModuleTypeDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.dto.ModuleTypeDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ModuleTypeDTO()
    
      Attributes:
        uid (java.lang.String): field
        visibility (org.openhab.core.automation.Visibility): field
        tags (java.util.Set): field
        label (java.lang.String): field
        description (java.lang.String): field
        configDescriptions (java.util.List): field
    
    """
    uid: java.lang.String = ...
    visibility: org.openhab.core.automation.Visibility = ...
    tags: java.util.Set = ...
    label: java.lang.String = ...
    description: java.lang.String = ...
    configDescriptions: java.util.List = ...
    def __init__(self): ...

class ModuleTypeDTOMapper(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.dto.ModuleTypeDTOMapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ModuleTypeDTOMapper()
    
    """
    def __init__(self): ...

class RuleDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.dto.RuleDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RuleDTO()
    
      Attributes:
        triggers (java.util.List): field
        conditions (java.util.List): field
        actions (java.util.List): field
        configuration (java.util.Map): field
        configDescriptions (java.util.List): field
        templateUID (java.lang.String): field
        uid (java.lang.String): field
        name (java.lang.String): field
        tags (java.util.Set): field
        visibility (org.openhab.core.automation.Visibility): field
        description (java.lang.String): field
    
    """
    triggers: java.util.List = ...
    conditions: java.util.List = ...
    actions: java.util.List = ...
    configuration: java.util.Map = ...
    configDescriptions: java.util.List = ...
    templateUID: java.lang.String = ...
    uid: java.lang.String = ...
    name: java.lang.String = ...
    tags: java.util.Set = ...
    visibility: org.openhab.core.automation.Visibility = ...
    description: java.lang.String = ...
    def __init__(self): ...

class RuleDTOMapper(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.dto.RuleDTOMapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RuleDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, ruleDto: RuleDTO) -> org.openhab.core.automation.Rule: ...
    @classmethod
    @typing.overload
    def map(cls, rule: org.openhab.core.automation.Rule) -> RuleDTO: ...

class RuleTemplateDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.dto.RuleTemplateDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RuleTemplateDTO()
    
      Attributes:
        label (java.lang.String): field
        uid (java.lang.String): field
        tags (java.util.Set): field
        description (java.lang.String): field
        visibility (org.openhab.core.automation.Visibility): field
        configDescriptions (java.util.List): field
        triggers (java.util.List): field
        conditions (java.util.List): field
        actions (java.util.List): field
    
    """
    label: java.lang.String = ...
    uid: java.lang.String = ...
    tags: java.util.Set = ...
    description: java.lang.String = ...
    visibility: org.openhab.core.automation.Visibility = ...
    configDescriptions: java.util.List = ...
    triggers: java.util.List = ...
    conditions: java.util.List = ...
    actions: java.util.List = ...
    def __init__(self): ...

class RuleTemplateDTOMapper(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.dto.RuleTemplateDTOMapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RuleTemplateDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, template: org.openhab.core.automation.template.RuleTemplate) -> RuleTemplateDTO: ...
    @classmethod
    @typing.overload
    def map(cls, ruleTemplateDto: RuleTemplateDTO) -> org.openhab.core.automation.template.RuleTemplate: ...

class ActionDTO(ModuleDTO):
    """
    Java class 'org.openhab.core.automation.dto.ActionDTO'
    
        Extends:
            org.openhab.core.automation.dto.ModuleDTO
    
      Constructors:
        * ActionDTO()
    
      Attributes:
        inputs (java.util.Map): field
    
    """
    inputs: java.util.Map = ...
    def __init__(self): ...

class ActionDTOMapper(ModuleDTOMapper):
    """
    Java class 'org.openhab.core.automation.dto.ActionDTOMapper'
    
        Extends:
            org.openhab.core.automation.dto.ModuleDTOMapper
    
      Constructors:
        * ActionDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, actions: typing.Union[java.util.Collection[org.openhab.core.automation.Action], typing.Sequence[org.openhab.core.automation.Action]]) -> java.util.List[ActionDTO]: ...
    @classmethod
    @typing.overload
    def map(cls, action: org.openhab.core.automation.Action) -> ActionDTO: ...
    @classmethod
    @typing.overload
    def mapDto(cls, dtos: typing.Union[java.util.Collection[ActionDTO], typing.Sequence[ActionDTO]]) -> java.util.List[org.openhab.core.automation.Action]: ...
    @classmethod
    @typing.overload
    def mapDto(cls, actionDto: ActionDTO) -> org.openhab.core.automation.Action: ...

class ActionTypeDTO(ModuleTypeDTO):
    """
    Java class 'org.openhab.core.automation.dto.ActionTypeDTO'
    
        Extends:
            org.openhab.core.automation.dto.ModuleTypeDTO
    
      Constructors:
        * ActionTypeDTO()
    
      Attributes:
        inputs (java.util.List): field
        outputs (java.util.List): field
    
    """
    inputs: java.util.List = ...
    outputs: java.util.List = ...
    def __init__(self): ...

class ActionTypeDTOMapper(ModuleTypeDTOMapper):
    """
    Java class 'org.openhab.core.automation.dto.ActionTypeDTOMapper'
    
        Extends:
            org.openhab.core.automation.dto.ModuleTypeDTOMapper
    
      Constructors:
        * ActionTypeDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, types: typing.Union[java.util.Collection[org.openhab.core.automation.type.ActionType], typing.Sequence[org.openhab.core.automation.type.ActionType]]) -> java.util.List[ActionTypeDTO]: ...
    @classmethod
    @typing.overload
    def map(cls, actionType: org.openhab.core.automation.type.ActionType) -> ActionTypeDTO: ...
    @classmethod
    @typing.overload
    def map(cls, actionType: org.openhab.core.automation.type.CompositeActionType) -> 'CompositeActionTypeDTO': ...
    @classmethod
    @typing.overload
    def map(cls, actionTypeDto: 'CompositeActionTypeDTO') -> org.openhab.core.automation.type.ActionType: ...

class ConditionDTO(ModuleDTO):
    """
    Java class 'org.openhab.core.automation.dto.ConditionDTO'
    
        Extends:
            org.openhab.core.automation.dto.ModuleDTO
    
      Constructors:
        * ConditionDTO()
    
      Attributes:
        inputs (java.util.Map): field
    
    """
    inputs: java.util.Map = ...
    def __init__(self): ...

class ConditionDTOMapper(ModuleDTOMapper):
    """
    Java class 'org.openhab.core.automation.dto.ConditionDTOMapper'
    
        Extends:
            org.openhab.core.automation.dto.ModuleDTOMapper
    
      Constructors:
        * ConditionDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, conditions: java.util.List[org.openhab.core.automation.Condition]) -> java.util.List[ConditionDTO]: ...
    @classmethod
    @typing.overload
    def map(cls, condition: org.openhab.core.automation.Condition) -> ConditionDTO: ...
    @classmethod
    @typing.overload
    def mapDto(cls, dtos: java.util.List[ConditionDTO]) -> java.util.List[org.openhab.core.automation.Condition]: ...
    @classmethod
    @typing.overload
    def mapDto(cls, conditionDto: ConditionDTO) -> org.openhab.core.automation.Condition: ...

class ConditionTypeDTO(ModuleTypeDTO):
    """
    Java class 'org.openhab.core.automation.dto.ConditionTypeDTO'
    
        Extends:
            org.openhab.core.automation.dto.ModuleTypeDTO
    
      Constructors:
        * ConditionTypeDTO()
    
      Attributes:
        inputs (java.util.List): field
    
    """
    inputs: java.util.List = ...
    def __init__(self): ...

class ConditionTypeDTOMapper(ModuleTypeDTOMapper):
    """
    Java class 'org.openhab.core.automation.dto.ConditionTypeDTOMapper'
    
        Extends:
            org.openhab.core.automation.dto.ModuleTypeDTOMapper
    
      Constructors:
        * ConditionTypeDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, types: typing.Union[java.util.Collection[org.openhab.core.automation.type.ConditionType], typing.Sequence[org.openhab.core.automation.type.ConditionType]]) -> java.util.List[ConditionTypeDTO]: ...
    @classmethod
    @typing.overload
    def map(cls, conditionType: org.openhab.core.automation.type.CompositeConditionType) -> 'CompositeConditionTypeDTO': ...
    @classmethod
    @typing.overload
    def map(cls, conditionType: org.openhab.core.automation.type.ConditionType) -> ConditionTypeDTO: ...
    @classmethod
    @typing.overload
    def map(cls, conditionTypeDto: 'CompositeConditionTypeDTO') -> org.openhab.core.automation.type.ConditionType: ...

class TriggerDTO(ModuleDTO):
    """
    Java class 'org.openhab.core.automation.dto.TriggerDTO'
    
        Extends:
            org.openhab.core.automation.dto.ModuleDTO
    
      Constructors:
        * TriggerDTO()
    
    """
    def __init__(self): ...

class TriggerDTOMapper(ModuleDTOMapper):
    """
    Java class 'org.openhab.core.automation.dto.TriggerDTOMapper'
    
        Extends:
            org.openhab.core.automation.dto.ModuleDTOMapper
    
      Constructors:
        * TriggerDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, triggers: typing.Union[java.util.Collection[org.openhab.core.automation.Trigger], typing.Sequence[org.openhab.core.automation.Trigger]]) -> java.util.List[TriggerDTO]: ...
    @classmethod
    @typing.overload
    def map(cls, trigger: org.openhab.core.automation.Trigger) -> TriggerDTO: ...
    @classmethod
    @typing.overload
    def mapDto(cls, dtos: typing.Union[java.util.Collection[TriggerDTO], typing.Sequence[TriggerDTO]]) -> java.util.List[org.openhab.core.automation.Trigger]: ...
    @classmethod
    @typing.overload
    def mapDto(cls, triggerDto: TriggerDTO) -> org.openhab.core.automation.Trigger: ...

class TriggerTypeDTO(ModuleTypeDTO):
    """
    Java class 'org.openhab.core.automation.dto.TriggerTypeDTO'
    
        Extends:
            org.openhab.core.automation.dto.ModuleTypeDTO
    
      Constructors:
        * TriggerTypeDTO()
    
      Attributes:
        outputs (java.util.List): field
    
    """
    outputs: java.util.List = ...
    def __init__(self): ...

class TriggerTypeDTOMapper(ModuleTypeDTOMapper):
    """
    Java class 'org.openhab.core.automation.dto.TriggerTypeDTOMapper'
    
        Extends:
            org.openhab.core.automation.dto.ModuleTypeDTOMapper
    
      Constructors:
        * TriggerTypeDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, types: typing.Union[java.util.Collection[org.openhab.core.automation.type.TriggerType], typing.Sequence[org.openhab.core.automation.type.TriggerType]]) -> java.util.List[TriggerTypeDTO]: ...
    @classmethod
    @typing.overload
    def map(cls, triggerType: org.openhab.core.automation.type.CompositeTriggerType) -> 'CompositeTriggerTypeDTO': ...
    @classmethod
    @typing.overload
    def map(cls, triggerType: org.openhab.core.automation.type.TriggerType) -> TriggerTypeDTO: ...
    @classmethod
    @typing.overload
    def map(cls, triggerTypeDto: 'CompositeTriggerTypeDTO') -> org.openhab.core.automation.type.TriggerType: ...

class CompositeActionTypeDTO(ActionTypeDTO):
    """
    Java class 'org.openhab.core.automation.dto.CompositeActionTypeDTO'
    
        Extends:
            org.openhab.core.automation.dto.ActionTypeDTO
    
      Constructors:
        * CompositeActionTypeDTO()
    
      Attributes:
        children (java.util.List): field
    
    """
    children: java.util.List = ...
    def __init__(self): ...

class CompositeConditionTypeDTO(ConditionTypeDTO):
    """
    Java class 'org.openhab.core.automation.dto.CompositeConditionTypeDTO'
    
        Extends:
            org.openhab.core.automation.dto.ConditionTypeDTO
    
      Constructors:
        * CompositeConditionTypeDTO()
    
      Attributes:
        children (java.util.List): field
    
    """
    children: java.util.List = ...
    def __init__(self): ...

class CompositeTriggerTypeDTO(TriggerTypeDTO):
    """
    Java class 'org.openhab.core.automation.dto.CompositeTriggerTypeDTO'
    
        Extends:
            org.openhab.core.automation.dto.TriggerTypeDTO
    
      Constructors:
        * CompositeTriggerTypeDTO()
    
      Attributes:
        children (java.util.List): field
    
    """
    children: java.util.List = ...
    def __init__(self): ...
