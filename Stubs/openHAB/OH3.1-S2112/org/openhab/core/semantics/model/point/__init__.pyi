import java.lang
import java.util.stream
import org.openhab.core.semantics.model
import typing


class Alarm(org.openhab.core.semantics.model.Point):
    """
    Java class 'org.openhab.core.semantics.model.point.Alarm'
    
        Interfaces:
            org.openhab.core.semantics.model.Point
    
    """

class Control(org.openhab.core.semantics.model.Point):
    """
    Java class 'org.openhab.core.semantics.model.point.Control'
    
        Interfaces:
            org.openhab.core.semantics.model.Point
    
    """

class Measurement(org.openhab.core.semantics.model.Point):
    """
    Java class 'org.openhab.core.semantics.model.point.Measurement'
    
        Interfaces:
            org.openhab.core.semantics.model.Point
    
    """

class Points(java.lang.Object):
    """
    Java class 'org.openhab.core.semantics.model.point.Points'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Points()
    
    """
    def __init__(self): ...
    @classmethod
    def stream(cls) -> java.util.stream.Stream[typing.Type[org.openhab.core.semantics.model.Point]]: ...

class Setpoint(org.openhab.core.semantics.model.Point):
    """
    Java class 'org.openhab.core.semantics.model.point.Setpoint'
    
        Interfaces:
            org.openhab.core.semantics.model.Point
    
    """

class Status(org.openhab.core.semantics.model.Point):
    """
    Java class 'org.openhab.core.semantics.model.point.Status'
    
        Interfaces:
            org.openhab.core.semantics.model.Point
    
    """

class LowBattery(Status):
    """
    Java class 'org.openhab.core.semantics.model.point.LowBattery'
    
        Interfaces:
            org.openhab.core.semantics.model.point.Status
    
    """

class OpenLevel(Status):
    """
    Java class 'org.openhab.core.semantics.model.point.OpenLevel'
    
        Interfaces:
            org.openhab.core.semantics.model.point.Status
    
    """

class OpenState(Status):
    """
    Java class 'org.openhab.core.semantics.model.point.OpenState'
    
        Interfaces:
            org.openhab.core.semantics.model.point.Status
    
    """

class Switch(Control):
    """
    Java class 'org.openhab.core.semantics.model.point.Switch'
    
        Interfaces:
            org.openhab.core.semantics.model.point.Control
    
    """

class Tampered(Status):
    """
    Java class 'org.openhab.core.semantics.model.point.Tampered'
    
        Interfaces:
            org.openhab.core.semantics.model.point.Status
    
    """

class Tilt(Status):
    """
    Java class 'org.openhab.core.semantics.model.point.Tilt'
    
        Interfaces:
            org.openhab.core.semantics.model.point.Status
    
    """
