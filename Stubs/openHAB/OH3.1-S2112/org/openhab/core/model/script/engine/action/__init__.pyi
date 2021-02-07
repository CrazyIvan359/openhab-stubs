import java.lang
import java.lang.annotation
import typing


class ActionDoc(java.lang.annotation.Annotation):
    """
    Java class 'org.openhab.core.model.script.engine.action.ActionDoc'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def returns(self) -> java.lang.String: ...
    def text(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class ActionService(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.engine.action.ActionService'
    
    """
    def getActionClass(self) -> typing.Type[typing.Any]: ...
    def getActionClassName(self) -> java.lang.String: ...

class ParamDoc(java.lang.annotation.Annotation):
    """
    Java class 'org.openhab.core.model.script.engine.action.ParamDoc'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def name(self) -> java.lang.String: ...
    def text(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
