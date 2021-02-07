import com.google.gson
import java.io
import java.lang
import java.lang.reflect
import java.util
import org.openhab.core.automation
import org.openhab.core.automation.parser
import org.openhab.core.automation.template
import org.openhab.core.automation.type
import typing


_AbstractGSONParser__T = typing.TypeVar('_AbstractGSONParser__T')  # <T>
class AbstractGSONParser(org.openhab.core.automation.parser.Parser[_AbstractGSONParser__T], typing.Generic[_AbstractGSONParser__T]):
    """
    Java class 'org.openhab.core.automation.internal.parser.gson.AbstractGSONParser'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.parser.Parser
    
      Constructors:
        * AbstractGSONParser()
    
    """
    def __init__(self): ...
    def serialize(self, dataObjects: java.util.Set[_AbstractGSONParser__T], writer: java.io.OutputStreamWriter) -> None: ...

class ActionInstanceCreator(com.google.gson.InstanceCreator[org.openhab.core.automation.type.CompositeActionType]):
    """
    Java class 'org.openhab.core.automation.internal.parser.gson.ActionInstanceCreator'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            com.google.gson.InstanceCreator
    
      Constructors:
        * ActionInstanceCreator()
    
    """
    def __init__(self): ...
    @typing.overload
    def createInstance(self, type: java.lang.reflect.Type) -> typing.Any: ...
    @typing.overload
    def createInstance(self, type: java.lang.reflect.Type) -> org.openhab.core.automation.type.CompositeActionType: ...

class ConditionInstanceCreator(com.google.gson.InstanceCreator[org.openhab.core.automation.type.CompositeConditionType]):
    """
    Java class 'org.openhab.core.automation.internal.parser.gson.ConditionInstanceCreator'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            com.google.gson.InstanceCreator
    
      Constructors:
        * ConditionInstanceCreator()
    
    """
    def __init__(self): ...
    @typing.overload
    def createInstance(self, type: java.lang.reflect.Type) -> typing.Any: ...
    @typing.overload
    def createInstance(self, type: java.lang.reflect.Type) -> org.openhab.core.automation.type.CompositeConditionType: ...

class ModuleTypeParsingContainer(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.internal.parser.gson.ModuleTypeParsingContainer'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ModuleTypeParsingContainer()
    
      Attributes:
        triggers (java.util.List): field
        conditions (java.util.List): field
        actions (java.util.List): field
    
    """
    triggers: java.util.List = ...
    conditions: java.util.List = ...
    actions: java.util.List = ...
    def __init__(self): ...

class TriggerInstanceCreator(com.google.gson.InstanceCreator[org.openhab.core.automation.type.CompositeTriggerType]):
    """
    Java class 'org.openhab.core.automation.internal.parser.gson.TriggerInstanceCreator'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            com.google.gson.InstanceCreator
    
      Constructors:
        * TriggerInstanceCreator()
    
    """
    def __init__(self): ...
    @typing.overload
    def createInstance(self, type: java.lang.reflect.Type) -> typing.Any: ...
    @typing.overload
    def createInstance(self, type: java.lang.reflect.Type) -> org.openhab.core.automation.type.CompositeTriggerType: ...

class ModuleTypeGSONParser(AbstractGSONParser[org.openhab.core.automation.type.ModuleType]):
    """
    Java class 'org.openhab.core.automation.internal.parser.gson.ModuleTypeGSONParser'
    
        Extends:
            org.openhab.core.automation.internal.parser.gson.AbstractGSONParser
    
      Constructors:
        * ModuleTypeGSONParser()
    
    """
    def __init__(self): ...
    def parse(self, reader: java.io.InputStreamReader) -> java.util.Set[org.openhab.core.automation.type.ModuleType]: ...
    def serialize(self, dataObjects: java.util.Set[org.openhab.core.automation.type.ModuleType], writer: java.io.OutputStreamWriter) -> None: ...

class RuleGSONParser(AbstractGSONParser[org.openhab.core.automation.Rule]):
    """
    Java class 'org.openhab.core.automation.internal.parser.gson.RuleGSONParser'
    
        Extends:
            org.openhab.core.automation.internal.parser.gson.AbstractGSONParser
    
      Constructors:
        * RuleGSONParser()
    
    """
    def __init__(self): ...
    def parse(self, reader: java.io.InputStreamReader) -> java.util.Set[org.openhab.core.automation.Rule]: ...

class TemplateGSONParser(AbstractGSONParser[org.openhab.core.automation.template.Template]):
    """
    Java class 'org.openhab.core.automation.internal.parser.gson.TemplateGSONParser'
    
        Extends:
            org.openhab.core.automation.internal.parser.gson.AbstractGSONParser
    
      Constructors:
        * TemplateGSONParser()
    
    """
    def __init__(self): ...
    def parse(self, reader: java.io.InputStreamReader) -> java.util.Set[org.openhab.core.automation.template.Template]: ...
