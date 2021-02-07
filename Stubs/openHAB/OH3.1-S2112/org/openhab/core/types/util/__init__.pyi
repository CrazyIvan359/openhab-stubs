import java.lang
import javax.measure
import typing


class UnitUtils(java.lang.Object):
    """
    Java class 'org.openhab.core.types.util.UnitUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * UnitUtils()
    
      Attributes:
        UNIT_PLACEHOLDER (java.lang.String): final static field
        UNIT_PERCENT_FORMAT_STRING (java.lang.String): final static field
    
    """
    UNIT_PLACEHOLDER: typing.ClassVar[java.lang.String] = ...
    UNIT_PERCENT_FORMAT_STRING: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    @classmethod
    def getDimensionName(cls, unit: javax.measure.Unit[typing.Any]) -> java.lang.String: ...
    @classmethod
    def isDifferentMeasurementSystem(cls, thisUnit: javax.measure.Unit[javax.measure.Quantity[typing.Any]], thatUnit: javax.measure.Unit[typing.Any]) -> bool: ...
    @classmethod
    def parseDimension(cls, dimension: java.lang.String) -> typing.Type[javax.measure.Quantity[typing.Any]]: ...
    @classmethod
    def parseUnit(cls, pattern: java.lang.String) -> javax.measure.Unit[typing.Any]: ...
