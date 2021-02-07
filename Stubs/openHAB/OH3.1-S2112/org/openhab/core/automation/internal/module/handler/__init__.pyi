import java.lang
import java.lang.reflect
import java.util
import org.openhab.core.automation
import org.openhab.core.automation.handler
import org.openhab.core.automation.type
import org.openhab.core.ephemeris
import org.openhab.core.events
import org.openhab.core.items
import org.openhab.core.scheduler
import org.osgi.framework
import org.slf4j
import typing


class AnnotationActionHandler(org.openhab.core.automation.handler.BaseActionModuleHandler):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.AnnotationActionHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseActionModuleHandler
    
      Constructors:
        * AnnotationActionHandler(org.openhab.core.automation.Action, org.openhab.core.automation.type.ActionType, java.lang.reflect.Method, java.lang.Object)
    
    """
    def __init__(self, module: org.openhab.core.automation.Action, mt: org.openhab.core.automation.type.ActionType, method: java.lang.reflect.Method, actionProvider: typing.Any): ...
    def execute(self, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> java.util.Map[java.lang.String, typing.Any]: ...

class ChannelEventTriggerHandler(org.openhab.core.automation.handler.BaseTriggerModuleHandler, org.openhab.core.events.EventSubscriber, org.openhab.core.events.EventFilter):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.ChannelEventTriggerHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseTriggerModuleHandler
    
        Interfaces:
            org.openhab.core.events.EventSubscriber,
            org.openhab.core.events.EventFilter
    
      Constructors:
        * ChannelEventTriggerHandler(org.openhab.core.automation.Trigger, org.osgi.framework.BundleContext)
    
      Attributes:
        MODULE_TYPE_ID (java.lang.String): final static field
        CFG_CHANNEL_EVENT (java.lang.String): final static field
        CFG_CHANNEL (java.lang.String): final static field
        TOPIC (java.lang.String): final static field
    
    """
    MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    CFG_CHANNEL_EVENT: typing.ClassVar[java.lang.String] = ...
    CFG_CHANNEL: typing.ClassVar[java.lang.String] = ...
    TOPIC: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Trigger, bundleContext: org.osgi.framework.BundleContext): ...
    def apply(self, event: org.openhab.core.events.Event) -> bool: ...
    def dispose(self) -> None: ...
    def getEventFilter(self) -> org.openhab.core.events.EventFilter: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def receive(self, event: org.openhab.core.events.Event) -> None: ...

class CompareConditionHandler(org.openhab.core.automation.handler.BaseConditionModuleHandler):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.CompareConditionHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseConditionModuleHandler
    
      Constructors:
        * CompareConditionHandler(org.openhab.core.automation.Condition)
    
      Attributes:
        MODULE_TYPE (java.lang.String): final static field
        INPUT_LEFT_OBJECT (java.lang.String): final static field
        INPUT_LEFT_FIELD (java.lang.String): final static field
        RIGHT_OP (java.lang.String): final static field
        OPERATOR (java.lang.String): final static field
        logger (org.slf4j.Logger): final field
    
    """
    MODULE_TYPE: typing.ClassVar[java.lang.String] = ...
    INPUT_LEFT_OBJECT: typing.ClassVar[java.lang.String] = ...
    INPUT_LEFT_FIELD: typing.ClassVar[java.lang.String] = ...
    RIGHT_OP: typing.ClassVar[java.lang.String] = ...
    OPERATOR: typing.ClassVar[java.lang.String] = ...
    logger: org.slf4j.Logger = ...
    def __init__(self, module: org.openhab.core.automation.Condition): ...
    def isSatisfied(self, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> bool: ...

class DayOfWeekConditionHandler(org.openhab.core.automation.handler.BaseConditionModuleHandler):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.DayOfWeekConditionHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseConditionModuleHandler
    
      Constructors:
        * DayOfWeekConditionHandler(org.openhab.core.automation.Condition)
    
      Attributes:
        MODULE_TYPE_ID (java.lang.String): final static field
        MODULE_CONTEXT_NAME (java.lang.String): final static field
        CFG_DAYS (java.lang.String): final static field
    
    """
    MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    MODULE_CONTEXT_NAME: typing.ClassVar[java.lang.String] = ...
    CFG_DAYS: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Condition): ...
    def isSatisfied(self, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> bool: ...

class EphemerisConditionHandler(org.openhab.core.automation.handler.BaseModuleHandler[org.openhab.core.automation.Condition], org.openhab.core.automation.handler.ConditionHandler):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.EphemerisConditionHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseModuleHandler
    
        Interfaces:
            org.openhab.core.automation.handler.ConditionHandler
    
      Constructors:
        * EphemerisConditionHandler(org.openhab.core.automation.Condition, org.openhab.core.ephemeris.EphemerisManager)
    
      Attributes:
        HOLIDAY_MODULE_TYPE_ID (java.lang.String): final static field
        WEEKEND_MODULE_TYPE_ID (java.lang.String): final static field
        WEEKDAY_MODULE_TYPE_ID (java.lang.String): final static field
        DAYSET_MODULE_TYPE_ID (java.lang.String): final static field
    
    """
    HOLIDAY_MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    WEEKEND_MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    WEEKDAY_MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    DAYSET_MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    def __init__(self, condition: org.openhab.core.automation.Condition, ephemerisManager: org.openhab.core.ephemeris.EphemerisManager): ...
    def isSatisfied(self, inputs: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> bool: ...

class GenericCronTriggerHandler(org.openhab.core.automation.handler.BaseTriggerModuleHandler, org.openhab.core.scheduler.SchedulerRunnable):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.GenericCronTriggerHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseTriggerModuleHandler
    
        Interfaces:
            org.openhab.core.scheduler.SchedulerRunnable
    
      Constructors:
        * GenericCronTriggerHandler(org.openhab.core.automation.Trigger, org.openhab.core.scheduler.CronScheduler)
    
      Attributes:
        MODULE_TYPE_ID (java.lang.String): final static field
        CALLBACK_CONTEXT_NAME (java.lang.String): final static field
        MODULE_CONTEXT_NAME (java.lang.String): final static field
        CFG_CRON_EXPRESSION (java.lang.String): final static field
    
    """
    MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    CALLBACK_CONTEXT_NAME: typing.ClassVar[java.lang.String] = ...
    MODULE_CONTEXT_NAME: typing.ClassVar[java.lang.String] = ...
    CFG_CRON_EXPRESSION: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Trigger, scheduler: org.openhab.core.scheduler.CronScheduler): ...
    def dispose(self) -> None: ...
    def run(self) -> None: ...
    def setCallback(self, callback: org.openhab.core.automation.ModuleHandlerCallback) -> None: ...

class GenericEventConditionHandler(org.openhab.core.automation.handler.BaseConditionModuleHandler):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.GenericEventConditionHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseConditionModuleHandler
    
      Constructors:
        * GenericEventConditionHandler(org.openhab.core.automation.Condition)
    
      Attributes:
        MODULETYPE_ID (java.lang.String): final static field
        logger (org.slf4j.Logger): final field
    
    """
    MODULETYPE_ID: typing.ClassVar[java.lang.String] = ...
    logger: org.slf4j.Logger = ...
    def __init__(self, module: org.openhab.core.automation.Condition): ...
    def isSatisfied(self, inputs: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> bool: ...

class GenericEventTriggerHandler(org.openhab.core.automation.handler.BaseTriggerModuleHandler, org.openhab.core.events.EventSubscriber, org.openhab.core.events.EventFilter):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.GenericEventTriggerHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseTriggerModuleHandler
    
        Interfaces:
            org.openhab.core.events.EventSubscriber,
            org.openhab.core.events.EventFilter
    
      Constructors:
        * GenericEventTriggerHandler(org.openhab.core.automation.Trigger, org.osgi.framework.BundleContext)
    
      Attributes:
        MODULE_TYPE_ID (java.lang.String): final static field
    
    """
    MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Trigger, bundleContext: org.osgi.framework.BundleContext): ...
    def apply(self, event: org.openhab.core.events.Event) -> bool: ...
    def dispose(self) -> None: ...
    def getEventFilter(self) -> org.openhab.core.events.EventFilter: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def getTopic(self) -> java.lang.String: ...
    def receive(self, event: org.openhab.core.events.Event) -> None: ...
    def setTopic(self, topic: java.lang.String) -> None: ...

class GroupCommandTriggerHandler(org.openhab.core.automation.handler.BaseTriggerModuleHandler, org.openhab.core.events.EventSubscriber, org.openhab.core.events.EventFilter):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.GroupCommandTriggerHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseTriggerModuleHandler
    
        Interfaces:
            org.openhab.core.events.EventSubscriber,
            org.openhab.core.events.EventFilter
    
      Constructors:
        * GroupCommandTriggerHandler(org.openhab.core.automation.Trigger, org.osgi.framework.BundleContext)
    
      Attributes:
        MODULE_TYPE_ID (java.lang.String): final static field
        CFG_GROUPNAME (java.lang.String): final static field
        CFG_COMMAND (java.lang.String): final static field
    
    """
    MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    CFG_GROUPNAME: typing.ClassVar[java.lang.String] = ...
    CFG_COMMAND: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Trigger, bundleContext: org.osgi.framework.BundleContext): ...
    def apply(self, event: org.openhab.core.events.Event) -> bool: ...
    def dispose(self) -> None: ...
    def getEventFilter(self) -> org.openhab.core.events.EventFilter: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def receive(self, event: org.openhab.core.events.Event) -> None: ...
    def setItemRegistry(self, itemRegistry: org.openhab.core.items.ItemRegistry) -> None: ...
    def unsetItemRegistry(self, itemRegistry: org.openhab.core.items.ItemRegistry) -> None: ...

class GroupStateTriggerHandler(org.openhab.core.automation.handler.BaseTriggerModuleHandler, org.openhab.core.events.EventSubscriber, org.openhab.core.events.EventFilter):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.GroupStateTriggerHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseTriggerModuleHandler
    
        Interfaces:
            org.openhab.core.events.EventSubscriber,
            org.openhab.core.events.EventFilter
    
      Constructors:
        * GroupStateTriggerHandler(org.openhab.core.automation.Trigger, org.osgi.framework.BundleContext)
    
      Attributes:
        UPDATE_MODULE_TYPE_ID (java.lang.String): final static field
        CHANGE_MODULE_TYPE_ID (java.lang.String): final static field
        CFG_GROUPNAME (java.lang.String): final static field
        CFG_STATE (java.lang.String): final static field
        CFG_PREVIOUS_STATE (java.lang.String): final static field
    
    """
    UPDATE_MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    CHANGE_MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    CFG_GROUPNAME: typing.ClassVar[java.lang.String] = ...
    CFG_STATE: typing.ClassVar[java.lang.String] = ...
    CFG_PREVIOUS_STATE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Trigger, bundleContext: org.osgi.framework.BundleContext): ...
    def apply(self, event: org.openhab.core.events.Event) -> bool: ...
    def dispose(self) -> None: ...
    def getEventFilter(self) -> org.openhab.core.events.EventFilter: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def receive(self, event: org.openhab.core.events.Event) -> None: ...
    def setItemRegistry(self, itemRegistry: org.openhab.core.items.ItemRegistry) -> None: ...
    def unsetItemRegistry(self, itemRegistry: org.openhab.core.items.ItemRegistry) -> None: ...

class ItemCommandActionHandler(org.openhab.core.automation.handler.BaseActionModuleHandler):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.ItemCommandActionHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseActionModuleHandler
    
      Constructors:
        * ItemCommandActionHandler(org.openhab.core.automation.Action)
    
      Attributes:
        ITEM_COMMAND_ACTION (java.lang.String): final static field
        ITEM_NAME (java.lang.String): final static field
        COMMAND (java.lang.String): final static field
    
    """
    ITEM_COMMAND_ACTION: typing.ClassVar[java.lang.String] = ...
    ITEM_NAME: typing.ClassVar[java.lang.String] = ...
    COMMAND: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Action): ...
    def dispose(self) -> None: ...
    def execute(self, inputs: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> java.util.Map[java.lang.String, typing.Any]: ...
    def setEventPublisher(self, eventPublisher: org.openhab.core.events.EventPublisher) -> None: ...
    def setItemRegistry(self, itemRegistry: org.openhab.core.items.ItemRegistry) -> None: ...
    def unsetEventPublisher(self, eventPublisher: org.openhab.core.events.EventPublisher) -> None: ...
    def unsetItemRegistry(self, itemRegistry: org.openhab.core.items.ItemRegistry) -> None: ...

class ItemCommandTriggerHandler(org.openhab.core.automation.handler.BaseTriggerModuleHandler, org.openhab.core.events.EventSubscriber, org.openhab.core.events.EventFilter):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.ItemCommandTriggerHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseTriggerModuleHandler
    
        Interfaces:
            org.openhab.core.events.EventSubscriber,
            org.openhab.core.events.EventFilter
    
      Constructors:
        * ItemCommandTriggerHandler(org.openhab.core.automation.Trigger, org.osgi.framework.BundleContext)
    
      Attributes:
        MODULE_TYPE_ID (java.lang.String): final static field
        CFG_ITEMNAME (java.lang.String): final static field
        CFG_COMMAND (java.lang.String): final static field
    
    """
    MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    CFG_ITEMNAME: typing.ClassVar[java.lang.String] = ...
    CFG_COMMAND: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Trigger, bundleContext: org.osgi.framework.BundleContext): ...
    def apply(self, event: org.openhab.core.events.Event) -> bool: ...
    def dispose(self) -> None: ...
    def getEventFilter(self) -> org.openhab.core.events.EventFilter: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def receive(self, event: org.openhab.core.events.Event) -> None: ...

class ItemStateConditionHandler(org.openhab.core.automation.handler.BaseConditionModuleHandler):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.ItemStateConditionHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseConditionModuleHandler
    
      Constructors:
        * ItemStateConditionHandler(org.openhab.core.automation.Condition)
    
      Attributes:
        ITEM_STATE_CONDITION (java.lang.String): final static field
    
    """
    ITEM_STATE_CONDITION: typing.ClassVar[java.lang.String] = ...
    def __init__(self, condition: org.openhab.core.automation.Condition): ...
    def dispose(self) -> None: ...
    def isSatisfied(self, inputs: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> bool: ...
    def setItemRegistry(self, itemRegistry: org.openhab.core.items.ItemRegistry) -> None: ...
    def unsetItemRegistry(self, itemRegistry: org.openhab.core.items.ItemRegistry) -> None: ...

class ItemStateTriggerHandler(org.openhab.core.automation.handler.BaseTriggerModuleHandler, org.openhab.core.events.EventSubscriber, org.openhab.core.events.EventFilter):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.ItemStateTriggerHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseTriggerModuleHandler
    
        Interfaces:
            org.openhab.core.events.EventSubscriber,
            org.openhab.core.events.EventFilter
    
      Constructors:
        * ItemStateTriggerHandler(org.openhab.core.automation.Trigger, org.osgi.framework.BundleContext)
    
      Attributes:
        UPDATE_MODULE_TYPE_ID (java.lang.String): final static field
        CHANGE_MODULE_TYPE_ID (java.lang.String): final static field
        CFG_ITEMNAME (java.lang.String): final static field
        CFG_STATE (java.lang.String): final static field
        CFG_PREVIOUS_STATE (java.lang.String): final static field
    
    """
    UPDATE_MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    CHANGE_MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    CFG_ITEMNAME: typing.ClassVar[java.lang.String] = ...
    CFG_STATE: typing.ClassVar[java.lang.String] = ...
    CFG_PREVIOUS_STATE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Trigger, bundleContext: org.osgi.framework.BundleContext): ...
    def apply(self, event: org.openhab.core.events.Event) -> bool: ...
    def dispose(self) -> None: ...
    def getEventFilter(self) -> org.openhab.core.events.EventFilter: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def receive(self, event: org.openhab.core.events.Event) -> None: ...

class ItemStateUpdateActionHandler(org.openhab.core.automation.handler.BaseActionModuleHandler):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.ItemStateUpdateActionHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseActionModuleHandler
    
      Constructors:
        * ItemStateUpdateActionHandler(org.openhab.core.automation.Action, org.openhab.core.events.EventPublisher, org.openhab.core.items.ItemRegistry)
    
      Attributes:
        ITEM_STATE_UPDATE_ACTION (java.lang.String): final static field
        ITEM_NAME (java.lang.String): final static field
        STATE (java.lang.String): final static field
    
    """
    ITEM_STATE_UPDATE_ACTION: typing.ClassVar[java.lang.String] = ...
    ITEM_NAME: typing.ClassVar[java.lang.String] = ...
    STATE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Action, eventPublisher: org.openhab.core.events.EventPublisher, itemRegistry: org.openhab.core.items.ItemRegistry): ...
    def execute(self, inputs: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> java.util.Map[java.lang.String, typing.Any]: ...

class RuleEnablementActionHandler(org.openhab.core.automation.handler.BaseActionModuleHandler):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.RuleEnablementActionHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseActionModuleHandler
    
      Constructors:
        * RuleEnablementActionHandler(org.openhab.core.automation.Action)
    
      Attributes:
        UID (java.lang.String): final static field
    
    """
    UID: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Action): ...
    def execute(self, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> java.util.Map[java.lang.String, typing.Any]: ...

class RunRuleActionHandler(org.openhab.core.automation.handler.BaseActionModuleHandler):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.RunRuleActionHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseActionModuleHandler
    
      Constructors:
        * RunRuleActionHandler(org.openhab.core.automation.Action)
    
      Attributes:
        UID (java.lang.String): final static field
    
    """
    UID: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Action): ...
    def execute(self, context: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> java.util.Map[java.lang.String, typing.Any]: ...

class SystemTriggerHandler(org.openhab.core.automation.handler.BaseTriggerModuleHandler, org.openhab.core.events.EventSubscriber, org.openhab.core.events.EventFilter):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.SystemTriggerHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseTriggerModuleHandler
    
        Interfaces:
            org.openhab.core.events.EventSubscriber,
            org.openhab.core.events.EventFilter
    
      Constructors:
        * SystemTriggerHandler(org.openhab.core.automation.Trigger, org.osgi.framework.BundleContext)
    
      Attributes:
        STARTLEVEL_MODULE_TYPE_ID (java.lang.String): final static field
        CFG_STARTLEVEL (java.lang.String): final static field
        OUT_STARTLEVEL (java.lang.String): final static field
    
    """
    STARTLEVEL_MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    CFG_STARTLEVEL: typing.ClassVar[java.lang.String] = ...
    OUT_STARTLEVEL: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Trigger, bundleContext: org.osgi.framework.BundleContext): ...
    def apply(self, event: org.openhab.core.events.Event) -> bool: ...
    def dispose(self) -> None: ...
    def getEventFilter(self) -> org.openhab.core.events.EventFilter: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def receive(self, event: org.openhab.core.events.Event) -> None: ...
    def trigger(self) -> None: ...

class ThingStatusTriggerHandler(org.openhab.core.automation.handler.BaseTriggerModuleHandler, org.openhab.core.events.EventSubscriber, org.openhab.core.events.EventFilter):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.ThingStatusTriggerHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseTriggerModuleHandler
    
        Interfaces:
            org.openhab.core.events.EventSubscriber,
            org.openhab.core.events.EventFilter
    
      Constructors:
        * ThingStatusTriggerHandler(org.openhab.core.automation.Trigger, org.osgi.framework.BundleContext)
    
      Attributes:
        UPDATE_MODULE_TYPE_ID (java.lang.String): final static field
        CHANGE_MODULE_TYPE_ID (java.lang.String): final static field
        CFG_THING_UID (java.lang.String): final static field
        CFG_STATUS (java.lang.String): final static field
        CFG_PREVIOUS_STATUS (java.lang.String): final static field
        OUT_STATUS (java.lang.String): final static field
        OUT_NEW_STATUS (java.lang.String): final static field
        OUT_OLD_STATUS (java.lang.String): final static field
        OUT_EVENT (java.lang.String): final static field
    
    """
    UPDATE_MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    CHANGE_MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    CFG_THING_UID: typing.ClassVar[java.lang.String] = ...
    CFG_STATUS: typing.ClassVar[java.lang.String] = ...
    CFG_PREVIOUS_STATUS: typing.ClassVar[java.lang.String] = ...
    OUT_STATUS: typing.ClassVar[java.lang.String] = ...
    OUT_NEW_STATUS: typing.ClassVar[java.lang.String] = ...
    OUT_OLD_STATUS: typing.ClassVar[java.lang.String] = ...
    OUT_EVENT: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Trigger, bundleContext: org.osgi.framework.BundleContext): ...
    def apply(self, event: org.openhab.core.events.Event) -> bool: ...
    def dispose(self) -> None: ...
    def getEventFilter(self) -> org.openhab.core.events.EventFilter: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def receive(self, event: org.openhab.core.events.Event) -> None: ...

class TimeOfDayConditionHandler(org.openhab.core.automation.handler.BaseConditionModuleHandler):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.TimeOfDayConditionHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseConditionModuleHandler
    
      Constructors:
        * TimeOfDayConditionHandler(org.openhab.core.automation.Condition)
    
      Attributes:
        MODULE_TYPE_ID (java.lang.String): final static field
    
    """
    MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    def __init__(self, condition: org.openhab.core.automation.Condition): ...
    def isSatisfied(self, inputs: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> bool: ...

class TimeOfDayTriggerHandler(org.openhab.core.automation.handler.BaseTriggerModuleHandler, org.openhab.core.scheduler.SchedulerRunnable):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.TimeOfDayTriggerHandler'
    
        Extends:
            org.openhab.core.automation.handler.BaseTriggerModuleHandler
    
        Interfaces:
            org.openhab.core.scheduler.SchedulerRunnable
    
      Constructors:
        * TimeOfDayTriggerHandler(org.openhab.core.automation.Trigger, org.openhab.core.scheduler.CronScheduler)
    
      Attributes:
        MODULE_TYPE_ID (java.lang.String): final static field
        MODULE_CONTEXT_NAME (java.lang.String): final static field
        CFG_TIME (java.lang.String): final static field
    
    """
    MODULE_TYPE_ID: typing.ClassVar[java.lang.String] = ...
    MODULE_CONTEXT_NAME: typing.ClassVar[java.lang.String] = ...
    CFG_TIME: typing.ClassVar[java.lang.String] = ...
    def __init__(self, module: org.openhab.core.automation.Trigger, scheduler: org.openhab.core.scheduler.CronScheduler): ...
    def dispose(self) -> None: ...
    def run(self) -> None: ...
    def setCallback(self, callback: org.openhab.core.automation.ModuleHandlerCallback) -> None: ...

class TimerModuleHandlerFactory(org.openhab.core.automation.handler.BaseModuleHandlerFactory):
    """
    Java class 'org.openhab.core.automation.internal.module.handler.TimerModuleHandlerFactory'
    
        Extends:
            org.openhab.core.automation.handler.BaseModuleHandlerFactory
    
      Constructors:
        * TimerModuleHandlerFactory()
    
      Attributes:
        THREADPOOLNAME (java.lang.String): final static field
    
    """
    THREADPOOLNAME: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    def deactivate(self) -> None: ...
    def getTypes(self) -> java.util.Collection[java.lang.String]: ...
