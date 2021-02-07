import java.lang
import java.math
import java.time
import java.util
import javax.measure
import org
import org.openhab.core.items
import org.openhab.core.types
import typing


class DateTimeGroupFunction(org.openhab.core.items.GroupFunction):
    """
    Java class 'org.openhab.core.library.types.DateTimeGroupFunction'
    
        Interfaces:
            org.openhab.core.items.GroupFunction
    
    """
    class Earliest(org.openhab.core.items.GroupFunction):
        """
        Java class 'org.openhab.core.library.types.DateTimeGroupFunction$Earliest'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                org.openhab.core.items.GroupFunction
        
          Constructors:
            * Earliest()
        
        """
        def __init__(self): ...
        def calculate(self, items: java.util.Set[org.openhab.core.items.Item]) -> org.openhab.core.types.State: ...
        def getParameters(self) -> typing.List[org.openhab.core.types.State]: ...
        _getStateAs__T = typing.TypeVar('_getStateAs__T', bound=org.openhab.core.types.State)  # <T>
        def getStateAs(self, items: java.util.Set[org.openhab.core.items.Item], stateClass: typing.Type[_getStateAs__T]) -> _getStateAs__T: ...
    class Latest(org.openhab.core.items.GroupFunction):
        """
        Java class 'org.openhab.core.library.types.DateTimeGroupFunction$Latest'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                org.openhab.core.items.GroupFunction
        
          Constructors:
            * Latest()
        
        """
        def __init__(self): ...
        def calculate(self, items: java.util.Set[org.openhab.core.items.Item]) -> org.openhab.core.types.State: ...
        def getParameters(self) -> typing.List[org.openhab.core.types.State]: ...
        _getStateAs__T = typing.TypeVar('_getStateAs__T', bound=org.openhab.core.types.State)  # <T>
        def getStateAs(self, items: java.util.Set[org.openhab.core.items.Item], stateClass: typing.Type[_getStateAs__T]) -> _getStateAs__T: ...

class DateTimeType(org.openhab.core.types.PrimitiveType, org.openhab.core.types.State, org.openhab.core.types.Command):
    """
    Java class 'org.openhab.core.library.types.DateTimeType'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.types.PrimitiveType,
            org.openhab.core.types.State, org.openhab.core.types.Command
    
      Constructors:
        * DateTimeType(java.time.ZonedDateTime)
        * DateTimeType()
        * DateTimeType(java.lang.String)
    
      Attributes:
        DATE_PATTERN (java.lang.String): final static field
        DATE_PATTERN_WITH_TZ (java.lang.String): final static field
        DATE_PATTERN_WITH_TZ_AND_MS (java.lang.String): final static field
        DATE_PATTERN_WITH_TZ_AND_MS_GENERAL (java.lang.String): final static field
        DATE_PATTERN_WITH_TZ_AND_MS_ISO (java.lang.String): final static field
    
    """
    DATE_PATTERN: typing.ClassVar[java.lang.String] = ...
    DATE_PATTERN_WITH_TZ: typing.ClassVar[java.lang.String] = ...
    DATE_PATTERN_WITH_TZ_AND_MS: typing.ClassVar[java.lang.String] = ...
    DATE_PATTERN_WITH_TZ_AND_MS_GENERAL: typing.ClassVar[java.lang.String] = ...
    DATE_PATTERN_WITH_TZ_AND_MS_ISO: typing.ClassVar[java.lang.String] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, zonedValue: java.lang.String): ...
    @typing.overload
    def __init__(self, zoned: java.time.ZonedDateTime): ...
    def equals(self, obj: typing.Any) -> bool: ...
    @typing.overload
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    @typing.overload
    def format(self, locale: java.util.Locale, pattern: java.lang.String) -> java.lang.String: ...
    def getZonedDateTime(self) -> java.time.ZonedDateTime: ...
    def hashCode(self) -> int: ...
    def toFullString(self) -> java.lang.String: ...
    def toLocaleZone(self) -> 'DateTimeType': ...
    def toString(self) -> java.lang.String: ...
    @typing.overload
    def toZone(self, zone: java.lang.String) -> 'DateTimeType': ...
    @typing.overload
    def toZone(self, zoneId: java.time.ZoneId) -> 'DateTimeType': ...
    @classmethod
    def valueOf(cls, value: java.lang.String) -> 'DateTimeType': ...

class DecimalType(java.lang.Number, org.openhab.core.types.PrimitiveType, org.openhab.core.types.State, org.openhab.core.types.Command, java.lang.Comparable[org.openhab.core.library.types.DecimalType]):
    """
    Java class 'org.openhab.core.library.types.DecimalType'
    
        Extends:
            java.lang.Number
    
        Interfaces:
            org.openhab.core.types.PrimitiveType,
            org.openhab.core.types.State, org.openhab.core.types.Command,
            java.lang.Comparable
    
      Constructors:
        * DecimalType(double)
        * DecimalType(long)
        * DecimalType(java.math.BigDecimal)
        * DecimalType()
        * DecimalType(java.lang.String)
    
      Attributes:
        ZERO (org.openhab.core.library.types.DecimalType): final static field
    
    """
    ZERO: typing.ClassVar['DecimalType'] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, value: float): ...
    @typing.overload
    def __init__(self, value: java.lang.String): ...
    @typing.overload
    def __init__(self, value: java.math.BigDecimal): ...
    @typing.overload
    def __init__(self, value: int): ...
    @typing.overload
    def compareTo(self, object: typing.Any) -> int: ...
    @typing.overload
    def compareTo(self, o: 'DecimalType') -> int: ...
    def doubleValue(self) -> float: ...
    def equals(self, obj: typing.Any) -> bool: ...
    def floatValue(self) -> float: ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def intValue(self) -> int: ...
    def longValue(self) -> int: ...
    def toBigDecimal(self) -> java.math.BigDecimal: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    @classmethod
    def valueOf(cls, value: java.lang.String) -> 'DecimalType': ...

class IncreaseDecreaseType(java.lang.Enum[org.openhab.core.library.types.IncreaseDecreaseType], org.openhab.core.types.PrimitiveType, org.openhab.core.types.Command):
    """
    Java class 'org.openhab.core.library.types.IncreaseDecreaseType'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            org.openhab.core.types.PrimitiveType,
            org.openhab.core.types.Command
    
      Attributes:
        INCREASE (org.openhab.core.library.types.IncreaseDecreaseType): final static enum constant
        DECREASE (org.openhab.core.library.types.IncreaseDecreaseType): final static enum constant
    
    """
    INCREASE: typing.ClassVar['IncreaseDecreaseType'] = ...
    DECREASE: typing.ClassVar['IncreaseDecreaseType'] = ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'IncreaseDecreaseType': ...
    @classmethod
    def values(cls) -> typing.List['IncreaseDecreaseType']: ...

class NextPreviousType(java.lang.Enum[org.openhab.core.library.types.NextPreviousType], org.openhab.core.types.PrimitiveType, org.openhab.core.types.Command):
    """
    Java class 'org.openhab.core.library.types.NextPreviousType'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            org.openhab.core.types.PrimitiveType,
            org.openhab.core.types.Command
    
      Attributes:
        NEXT (org.openhab.core.library.types.NextPreviousType): final static enum constant
        PREVIOUS (org.openhab.core.library.types.NextPreviousType): final static enum constant
    
    """
    NEXT: typing.ClassVar['NextPreviousType'] = ...
    PREVIOUS: typing.ClassVar['NextPreviousType'] = ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'NextPreviousType': ...
    @classmethod
    def values(cls) -> typing.List['NextPreviousType']: ...

class OnOffType(java.lang.Enum[org.openhab.core.library.types.OnOffType], org.openhab.core.types.PrimitiveType, org.openhab.core.types.State, org.openhab.core.types.Command):
    """
    Java class 'org.openhab.core.library.types.OnOffType'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            org.openhab.core.types.PrimitiveType,
            org.openhab.core.types.State, org.openhab.core.types.Command
    
      Attributes:
        ON (org.openhab.core.library.types.OnOffType): final static enum constant
        OFF (org.openhab.core.library.types.OnOffType): final static enum constant
    
    """
    ON: typing.ClassVar['OnOffType'] = ...
    OFF: typing.ClassVar['OnOffType'] = ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'OnOffType': ...
    @classmethod
    def values(cls) -> typing.List['OnOffType']: ...

class OpenClosedType(java.lang.Enum[org.openhab.core.library.types.OpenClosedType], org.openhab.core.types.PrimitiveType, org.openhab.core.types.State, org.openhab.core.types.Command):
    """
    Java class 'org.openhab.core.library.types.OpenClosedType'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            org.openhab.core.types.PrimitiveType,
            org.openhab.core.types.State, org.openhab.core.types.Command
    
      Attributes:
        OPEN (org.openhab.core.library.types.OpenClosedType): final static enum constant
        CLOSED (org.openhab.core.library.types.OpenClosedType): final static enum constant
    
    """
    OPEN: typing.ClassVar['OpenClosedType'] = ...
    CLOSED: typing.ClassVar['OpenClosedType'] = ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'OpenClosedType': ...
    @classmethod
    def values(cls) -> typing.List['OpenClosedType']: ...

class PlayPauseType(java.lang.Enum[org.openhab.core.library.types.PlayPauseType], org.openhab.core.types.PrimitiveType, org.openhab.core.types.State, org.openhab.core.types.Command):
    """
    Java class 'org.openhab.core.library.types.PlayPauseType'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            org.openhab.core.types.PrimitiveType,
            org.openhab.core.types.State, org.openhab.core.types.Command
    
      Attributes:
        PLAY (org.openhab.core.library.types.PlayPauseType): final static enum constant
        PAUSE (org.openhab.core.library.types.PlayPauseType): final static enum constant
    
    """
    PLAY: typing.ClassVar['PlayPauseType'] = ...
    PAUSE: typing.ClassVar['PlayPauseType'] = ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'PlayPauseType': ...
    @classmethod
    def values(cls) -> typing.List['PlayPauseType']: ...

class PointType(org.openhab.core.types.ComplexType, org.openhab.core.types.Command, org.openhab.core.types.State):
    """
    Java class 'org.openhab.core.library.types.PointType'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.types.ComplexType,
            org.openhab.core.types.Command, org.openhab.core.types.State
    
      Constructors:
        * PointType(org.openhab.core.library.types.StringType, org.openhab.core.library.types.StringType, org.openhab.core.library.types.StringType)
        * PointType(org.openhab.core.library.types.StringType, org.openhab.core.library.types.StringType)
        * PointType(org.openhab.core.library.types.DecimalType, org.openhab.core.library.types.DecimalType, org.openhab.core.library.types.DecimalType)
        * PointType(java.lang.String)
        * PointType()
        * PointType(org.openhab.core.library.types.DecimalType, org.openhab.core.library.types.DecimalType)
    
      Attributes:
        LOCATION_PATTERN (java.lang.String): final static field
        EARTH_GRAVITATIONAL_CONSTANT (double): final static field
        WGS84_A (double): final static field
        KEY_LATITUDE (java.lang.String): final static field
        KEY_LONGITUDE (java.lang.String): final static field
        KEY_ALTITUDE (java.lang.String): final static field
    
    """
    LOCATION_PATTERN: typing.ClassVar[java.lang.String] = ...
    EARTH_GRAVITATIONAL_CONSTANT: typing.ClassVar[float] = ...
    WGS84_A: typing.ClassVar[float] = ...
    KEY_LATITUDE: typing.ClassVar[java.lang.String] = ...
    KEY_LONGITUDE: typing.ClassVar[java.lang.String] = ...
    KEY_ALTITUDE: typing.ClassVar[java.lang.String] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, value: java.lang.String): ...
    @typing.overload
    def __init__(self, latitude: DecimalType, longitude: DecimalType): ...
    @typing.overload
    def __init__(self, latitude: DecimalType, longitude: DecimalType, altitude: DecimalType): ...
    @typing.overload
    def __init__(self, latitude: 'StringType', longitude: 'StringType'): ...
    @typing.overload
    def __init__(self, latitude: 'StringType', longitude: 'StringType', altitude: 'StringType'): ...
    def distanceFrom(self, otherPoint: 'PointType') -> DecimalType: ...
    def equals(self, obj: typing.Any) -> bool: ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def getAltitude(self) -> DecimalType: ...
    def getConstituents(self) -> java.util.SortedMap[java.lang.String, org.openhab.core.types.PrimitiveType]: ...
    def getGravity(self) -> DecimalType: ...
    def getLatitude(self) -> DecimalType: ...
    def getLongitude(self) -> DecimalType: ...
    def hashCode(self) -> int: ...
    def setAltitude(self, altitude: DecimalType) -> None: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    @classmethod
    def valueOf(cls, value: java.lang.String) -> 'PointType': ...

_QuantityType__T = typing.TypeVar('_QuantityType__T', bound=javax.measure.Quantity)  # <T>
class QuantityType(java.lang.Number, org.openhab.core.types.PrimitiveType, org.openhab.core.types.State, org.openhab.core.types.Command, java.lang.Comparable[org.openhab.core.library.types.QuantityType[_QuantityType__T]], typing.Generic[_QuantityType__T]):
    """
    Java class 'org.openhab.core.library.types.QuantityType'
    
        Extends:
            java.lang.Number
    
        Interfaces:
            org.openhab.core.types.PrimitiveType,
            org.openhab.core.types.State, org.openhab.core.types.Command,
            java.lang.Comparable
    
      Constructors:
        * QuantityType(java.lang.String)
        * QuantityType()
        * QuantityType(java.lang.Number, javax.measure.Unit)
    
      Attributes:
        ZERO (org.openhab.core.library.types.QuantityType): final static field
        ONE (org.openhab.core.library.types.QuantityType): final static field
    
    """
    ZERO: typing.ClassVar['QuantityType'] = ...
    ONE: typing.ClassVar['QuantityType'] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, value: java.lang.Number, unit: javax.measure.Unit[_QuantityType__T]): ...
    @typing.overload
    def __init__(self, value: java.lang.String): ...
    def add(self, state: 'QuantityType'[_QuantityType__T]) -> 'QuantityType'[_QuantityType__T]: ...
    @typing.overload
    def compareTo(self, object: typing.Any) -> int: ...
    @typing.overload
    def compareTo(self, o: 'QuantityType'[_QuantityType__T]) -> int: ...
    @typing.overload
    def divide(self, value: java.math.BigDecimal) -> 'QuantityType'[typing.Any]: ...
    @typing.overload
    def divide(self, state: 'QuantityType'[typing.Any]) -> 'QuantityType'[typing.Any]: ...
    def doubleValue(self) -> float: ...
    def equals(self, obj: typing.Any) -> bool: ...
    def floatValue(self) -> float: ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def getDimension(self) -> javax.measure.Dimension: ...
    def getUnit(self) -> javax.measure.Unit[_QuantityType__T]: ...
    def hashCode(self) -> int: ...
    def intValue(self) -> int: ...
    def longValue(self) -> int: ...
    @typing.overload
    def multiply(self, value: java.math.BigDecimal) -> 'QuantityType'[typing.Any]: ...
    @typing.overload
    def multiply(self, state: 'QuantityType'[typing.Any]) -> 'QuantityType'[typing.Any]: ...
    def negate(self) -> 'QuantityType'[_QuantityType__T]: ...
    def offset(self, offset: 'QuantityType'[_QuantityType__T], unit: javax.measure.Unit[_QuantityType__T]) -> 'QuantityType'[_QuantityType__T]: ...
    def subtract(self, state: 'QuantityType'[_QuantityType__T]) -> 'QuantityType'[_QuantityType__T]: ...
    def toBigDecimal(self) -> java.math.BigDecimal: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    @typing.overload
    def toUnit(self, targetUnit: java.lang.String) -> 'QuantityType'[_QuantityType__T]: ...
    @typing.overload
    def toUnit(self, targetUnit: javax.measure.Unit[typing.Any]) -> 'QuantityType'[_QuantityType__T]: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=javax.measure.Quantity)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, value: float, unit: javax.measure.Unit[_valueOf_0__T]) -> 'QuantityType'[_valueOf_0__T]: ...
    @classmethod
    @typing.overload
    def valueOf(cls, value: java.lang.String) -> 'QuantityType'[javax.measure.Quantity[typing.Any]]: ...

class RawType(org.openhab.core.types.PrimitiveType, org.openhab.core.types.State):
    """
    Java class 'org.openhab.core.library.types.RawType'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.types.PrimitiveType,
            org.openhab.core.types.State
    
      Constructors:
        * RawType(byte[], java.lang.String)
    
      Attributes:
        DEFAULT_MIME_TYPE (java.lang.String): final static field
    
    """
    DEFAULT_MIME_TYPE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, bytes: typing.List[int], mimeType: java.lang.String): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def getBytes(self) -> typing.List[int]: ...
    def getMimeType(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    @classmethod
    def valueOf(cls, value: java.lang.String) -> 'RawType': ...

class RewindFastforwardType(java.lang.Enum[org.openhab.core.library.types.RewindFastforwardType], org.openhab.core.types.PrimitiveType, org.openhab.core.types.State, org.openhab.core.types.Command):
    """
    Java class 'org.openhab.core.library.types.RewindFastforwardType'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            org.openhab.core.types.PrimitiveType,
            org.openhab.core.types.State, org.openhab.core.types.Command
    
      Attributes:
        REWIND (org.openhab.core.library.types.RewindFastforwardType): final static enum constant
        FASTFORWARD (org.openhab.core.library.types.RewindFastforwardType): final static enum constant
    
    """
    REWIND: typing.ClassVar['RewindFastforwardType'] = ...
    FASTFORWARD: typing.ClassVar['RewindFastforwardType'] = ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'RewindFastforwardType': ...
    @classmethod
    def values(cls) -> typing.List['RewindFastforwardType']: ...

class StopMoveType(java.lang.Enum[org.openhab.core.library.types.StopMoveType], org.openhab.core.types.PrimitiveType, org.openhab.core.types.Command):
    """
    Java class 'org.openhab.core.library.types.StopMoveType'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            org.openhab.core.types.PrimitiveType,
            org.openhab.core.types.Command
    
      Attributes:
        STOP (org.openhab.core.library.types.StopMoveType): final static enum constant
        MOVE (org.openhab.core.library.types.StopMoveType): final static enum constant
    
    """
    STOP: typing.ClassVar['StopMoveType'] = ...
    MOVE: typing.ClassVar['StopMoveType'] = ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'StopMoveType': ...
    @classmethod
    def values(cls) -> typing.List['StopMoveType']: ...

class StringListType(org.openhab.core.types.Command, org.openhab.core.types.State):
    """
    Java class 'org.openhab.core.library.types.StringListType'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.types.Command, org.openhab.core.types.State
    
      Constructors:
        * StringListType(java.lang.String)
        * StringListType(java.lang.String[])
        * StringListType(org.openhab.core.library.types.StringType[])
        * StringListType(java.util.List)
        * StringListType()
    
      Attributes:
        DELIMITER (java.lang.String): final static field
        ESCAPED_DELIMITER (java.lang.String): final static field
        REGEX_SPLITTER (java.lang.String): final static field
    
    """
    DELIMITER: typing.ClassVar[java.lang.String] = ...
    ESCAPED_DELIMITER: typing.ClassVar[java.lang.String] = ...
    REGEX_SPLITTER: typing.ClassVar[java.lang.String] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, serialized: java.lang.String): ...
    @typing.overload
    def __init__(self, rows: typing.List[java.lang.String]): ...
    @typing.overload
    def __init__(self, rows: java.util.List[java.lang.String]): ...
    @typing.overload
    def __init__(self, rows: typing.List['StringType']): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def getValue(self, index: int) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    @classmethod
    def valueOf(cls, value: java.lang.String) -> 'StringListType': ...

class StringType(org.openhab.core.types.PrimitiveType, org.openhab.core.types.State, org.openhab.core.types.Command):
    """
    Java class 'org.openhab.core.library.types.StringType'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.types.PrimitiveType,
            org.openhab.core.types.State, org.openhab.core.types.Command
    
      Constructors:
        * StringType(java.lang.String)
        * StringType()
    
      Attributes:
        EMPTY (org.openhab.core.library.types.StringType): final static field
    
    """
    EMPTY: typing.ClassVar['StringType'] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, value: java.lang.String): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    @classmethod
    def valueOf(cls, value: java.lang.String) -> 'StringType': ...

class UpDownType(java.lang.Enum[org.openhab.core.library.types.UpDownType], org.openhab.core.types.PrimitiveType, org.openhab.core.types.State, org.openhab.core.types.Command):
    """
    Java class 'org.openhab.core.library.types.UpDownType'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            org.openhab.core.types.PrimitiveType,
            org.openhab.core.types.State, org.openhab.core.types.Command
    
      Attributes:
        UP (org.openhab.core.library.types.UpDownType): final static enum constant
        DOWN (org.openhab.core.library.types.UpDownType): final static enum constant
    
    """
    UP: typing.ClassVar['UpDownType'] = ...
    DOWN: typing.ClassVar['UpDownType'] = ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'UpDownType': ...
    @classmethod
    def values(cls) -> typing.List['UpDownType']: ...

class PercentType(DecimalType):
    """
    Java class 'org.openhab.core.library.types.PercentType'
    
        Extends:
            org.openhab.core.library.types.DecimalType
    
      Constructors:
        * PercentType(java.lang.String)
        * PercentType(int)
        * PercentType()
        * PercentType(java.math.BigDecimal)
    
      Attributes:
        ZERO (org.openhab.core.library.types.PercentType): final static field
        HUNDRED (org.openhab.core.library.types.PercentType): final static field
    
    """
    ZERO: typing.ClassVar['PercentType'] = ...
    HUNDRED: typing.ClassVar['PercentType'] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, value: int): ...
    @typing.overload
    def __init__(self, value: java.lang.String): ...
    @typing.overload
    def __init__(self, value: java.math.BigDecimal): ...
    @classmethod
    @typing.overload
    def valueOf(cls, value: java.lang.String) -> DecimalType: ...
    @classmethod
    @typing.overload
    def valueOf(cls, value: java.lang.String) -> 'PercentType': ...

class HSBType(PercentType, org.openhab.core.types.ComplexType, org.openhab.core.types.State, org.openhab.core.types.Command):
    """
    Java class 'org.openhab.core.library.types.HSBType'
    
        Extends:
            org.openhab.core.library.types.PercentType
    
        Interfaces:
            org.openhab.core.types.ComplexType,
            org.openhab.core.types.State, org.openhab.core.types.Command
    
      Constructors:
        * HSBType(org.openhab.core.library.types.DecimalType, org.openhab.core.library.types.PercentType, org.openhab.core.library.types.PercentType)
        * HSBType()
        * HSBType(java.lang.String)
    
      Attributes:
        KEY_HUE (java.lang.String): final static field
        KEY_SATURATION (java.lang.String): final static field
        KEY_BRIGHTNESS (java.lang.String): final static field
        BLACK (org.openhab.core.library.types.HSBType): final static field
        WHITE (org.openhab.core.library.types.HSBType): final static field
        RED (org.openhab.core.library.types.HSBType): final static field
        GREEN (org.openhab.core.library.types.HSBType): final static field
        BLUE (org.openhab.core.library.types.HSBType): final static field
    
    """
    KEY_HUE: typing.ClassVar[java.lang.String] = ...
    KEY_SATURATION: typing.ClassVar[java.lang.String] = ...
    KEY_BRIGHTNESS: typing.ClassVar[java.lang.String] = ...
    BLACK: typing.ClassVar['HSBType'] = ...
    WHITE: typing.ClassVar['HSBType'] = ...
    RED: typing.ClassVar['HSBType'] = ...
    GREEN: typing.ClassVar['HSBType'] = ...
    BLUE: typing.ClassVar['HSBType'] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, value: java.lang.String): ...
    @typing.overload
    def __init__(self, h: DecimalType, s: PercentType, b: PercentType): ...
    def equals(self, obj: typing.Any) -> bool: ...
    @classmethod
    def fromRGB(cls, r: int, g: int, b: int) -> 'HSBType': ...
    @classmethod
    def fromXY(cls, x: float, y: float) -> 'HSBType': ...
    def getBlue(self) -> PercentType: ...
    def getBrightness(self) -> PercentType: ...
    def getConstituents(self) -> java.util.SortedMap[java.lang.String, org.openhab.core.types.PrimitiveType]: ...
    def getGreen(self) -> PercentType: ...
    def getHue(self) -> DecimalType: ...
    def getRGB(self) -> int: ...
    def getRed(self) -> PercentType: ...
    def getSaturation(self) -> PercentType: ...
    def hashCode(self) -> int: ...
    def toFullString(self) -> java.lang.String: ...
    def toRGB(self) -> typing.List[PercentType]: ...
    def toString(self) -> java.lang.String: ...
    def toXY(self) -> typing.List[PercentType]: ...
    @classmethod
    @typing.overload
    def valueOf(cls, value: java.lang.String) -> DecimalType: ...
    @classmethod
    @typing.overload
    def valueOf(cls, value: java.lang.String) -> 'HSBType': ...
    @classmethod
    @typing.overload
    def valueOf(cls, value: java.lang.String) -> PercentType: ...

class ArithmeticGroupFunction(org.openhab.core.items.GroupFunction):
    """
    Java class 'org.openhab.core.library.types.ArithmeticGroupFunction'
    
        Interfaces:
            org.openhab.core.items.GroupFunction
    
    """
    class And(org.openhab.core.items.GroupFunction):
        """
        Java class 'org.openhab.core.library.types.ArithmeticGroupFunction$And'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                org.openhab.core.items.GroupFunction
        
          Constructors:
            * And(org.openhab.core.types.State, org.openhab.core.types.State)
        
        """
        def __init__(self, activeValue: org.openhab.core.types.State, passiveValue: org.openhab.core.types.State): ...
        def calculate(self, items: java.util.Set[org.openhab.core.items.Item]) -> org.openhab.core.types.State: ...
        def getParameters(self) -> typing.List[org.openhab.core.types.State]: ...
        _getStateAs__T = typing.TypeVar('_getStateAs__T', bound=org.openhab.core.types.State)  # <T>
        def getStateAs(self, items: java.util.Set[org.openhab.core.items.Item], stateClass: typing.Type[_getStateAs__T]) -> _getStateAs__T: ...
    class Avg(org.openhab.core.items.GroupFunction):
        """
        Java class 'org.openhab.core.library.types.ArithmeticGroupFunction$Avg'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                org.openhab.core.items.GroupFunction
        
          Constructors:
            * Avg()
        
        """
        def __init__(self): ...
        def calculate(self, items: java.util.Set[org.openhab.core.items.Item]) -> org.openhab.core.types.State: ...
        def getParameters(self) -> typing.List[org.openhab.core.types.State]: ...
        _getStateAs__T = typing.TypeVar('_getStateAs__T', bound=org.openhab.core.types.State)  # <T>
        def getStateAs(self, items: java.util.Set[org.openhab.core.items.Item], stateClass: typing.Type[_getStateAs__T]) -> _getStateAs__T: ...
    class Count(org.openhab.core.items.GroupFunction):
        """
        Java class 'org.openhab.core.library.types.ArithmeticGroupFunction$Count'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                org.openhab.core.items.GroupFunction
        
          Constructors:
            * Count(org.openhab.core.types.State)
        
        """
        def __init__(self, regExpr: org.openhab.core.types.State): ...
        def calculate(self, items: java.util.Set[org.openhab.core.items.Item]) -> org.openhab.core.types.State: ...
        def getParameters(self) -> typing.List[org.openhab.core.types.State]: ...
        _getStateAs__T = typing.TypeVar('_getStateAs__T', bound=org.openhab.core.types.State)  # <T>
        def getStateAs(self, items: java.util.Set[org.openhab.core.items.Item], stateClass: typing.Type[_getStateAs__T]) -> _getStateAs__T: ...
    class Max(org.openhab.core.items.GroupFunction):
        """
        Java class 'org.openhab.core.library.types.ArithmeticGroupFunction$Max'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                org.openhab.core.items.GroupFunction
        
          Constructors:
            * Max()
        
        """
        def __init__(self): ...
        def calculate(self, items: java.util.Set[org.openhab.core.items.Item]) -> org.openhab.core.types.State: ...
        def getParameters(self) -> typing.List[org.openhab.core.types.State]: ...
        _getStateAs__T = typing.TypeVar('_getStateAs__T', bound=org.openhab.core.types.State)  # <T>
        def getStateAs(self, items: java.util.Set[org.openhab.core.items.Item], stateClass: typing.Type[_getStateAs__T]) -> _getStateAs__T: ...
    class Min(org.openhab.core.items.GroupFunction):
        """
        Java class 'org.openhab.core.library.types.ArithmeticGroupFunction$Min'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                org.openhab.core.items.GroupFunction
        
          Constructors:
            * Min()
        
        """
        def __init__(self): ...
        def calculate(self, items: java.util.Set[org.openhab.core.items.Item]) -> org.openhab.core.types.State: ...
        def getParameters(self) -> typing.List[org.openhab.core.types.State]: ...
        _getStateAs__T = typing.TypeVar('_getStateAs__T', bound=org.openhab.core.types.State)  # <T>
        def getStateAs(self, items: java.util.Set[org.openhab.core.items.Item], stateClass: typing.Type[_getStateAs__T]) -> _getStateAs__T: ...
    class NAnd(org.openhab.core.library.types.ArithmeticGroupFunction.And):
        """
        Java class 'org.openhab.core.library.types.ArithmeticGroupFunction$NAnd'
        
            Extends:
                org.openhab.core.library.types.ArithmeticGroupFunction$And
        
          Constructors:
            * NAnd(org.openhab.core.types.State, org.openhab.core.types.State)
        
        """
        def __init__(self, activeValue: org.openhab.core.types.State, passiveValue: org.openhab.core.types.State): ...
        def calculate(self, items: java.util.Set[org.openhab.core.items.Item]) -> org.openhab.core.types.State: ...
    class NOr(org.openhab.core.library.types.ArithmeticGroupFunction.Or):
        """
        Java class 'org.openhab.core.library.types.ArithmeticGroupFunction$NOr'
        
            Extends:
                org.openhab.core.library.types.ArithmeticGroupFunction$Or
        
          Constructors:
            * NOr(org.openhab.core.types.State, org.openhab.core.types.State)
        
        """
        def __init__(self, activeValue: org.openhab.core.types.State, passiveValue: org.openhab.core.types.State): ...
        def calculate(self, items: java.util.Set[org.openhab.core.items.Item]) -> org.openhab.core.types.State: ...
    class Or(org.openhab.core.items.GroupFunction):
        """
        Java class 'org.openhab.core.library.types.ArithmeticGroupFunction$Or'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                org.openhab.core.items.GroupFunction
        
          Constructors:
            * Or(org.openhab.core.types.State, org.openhab.core.types.State)
        
        """
        def __init__(self, activeValue: org.openhab.core.types.State, passiveValue: org.openhab.core.types.State): ...
        def calculate(self, items: java.util.Set[org.openhab.core.items.Item]) -> org.openhab.core.types.State: ...
        def getParameters(self) -> typing.List[org.openhab.core.types.State]: ...
        _getStateAs__T = typing.TypeVar('_getStateAs__T', bound=org.openhab.core.types.State)  # <T>
        def getStateAs(self, items: java.util.Set[org.openhab.core.items.Item], stateClass: typing.Type[_getStateAs__T]) -> _getStateAs__T: ...
    class Sum(org.openhab.core.items.GroupFunction):
        """
        Java class 'org.openhab.core.library.types.ArithmeticGroupFunction$Sum'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                org.openhab.core.items.GroupFunction
        
          Constructors:
            * Sum()
        
        """
        def __init__(self): ...
        def calculate(self, items: java.util.Set[org.openhab.core.items.Item]) -> org.openhab.core.types.State: ...
        def getParameters(self) -> typing.List[org.openhab.core.types.State]: ...
        _getStateAs__T = typing.TypeVar('_getStateAs__T', bound=org.openhab.core.types.State)  # <T>
        def getStateAs(self, items: java.util.Set[org.openhab.core.items.Item], stateClass: typing.Type[_getStateAs__T]) -> _getStateAs__T: ...

class QuantityTypeArithmeticGroupFunction(org.openhab.core.items.GroupFunction):
    """
    Java class 'org.openhab.core.library.types.QuantityTypeArithmeticGroupFunction'
    
        Interfaces:
            org.openhab.core.items.GroupFunction
    
    """
    class Avg(org.openhab.core.library.types.QuantityTypeArithmeticGroupFunction.DimensionalGroupFunction):
        """
        Java class 'org.openhab.core.library.types.QuantityTypeArithmeticGroupFunction$Avg'
        
            Extends:
                org.openhab.core.library.types.QuantityTypeArithmeticGroupFunction$DimensionalGroupFunction
        
          Constructors:
            * Avg(java.lang.Class)
        
        """
        def __init__(self, dimension: typing.Type[javax.measure.Quantity[typing.Any]]): ...
        def calculate(self, items: java.util.Set[org.openhab.core.items.Item]) -> org.openhab.core.types.State: ...
    class DimensionalGroupFunction(org.openhab.core.items.GroupFunction):
        """
        Java class 'org.openhab.core.library.types.QuantityTypeArithmeticGroupFunction$DimensionalGroupFunction'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                org.openhab.core.items.GroupFunction
        
          Constructors:
            * DimensionalGroupFunction(java.lang.Class)
        
        """
        def __init__(self, dimension: typing.Type[javax.measure.Quantity[typing.Any]]): ...
        def getParameters(self) -> typing.List[org.openhab.core.types.State]: ...
        _getStateAs__T = typing.TypeVar('_getStateAs__T', bound=org.openhab.core.types.State)  # <T>
        def getStateAs(self, items: java.util.Set[org.openhab.core.items.Item], stateClass: typing.Type[_getStateAs__T]) -> _getStateAs__T: ...
    class Max(org.openhab.core.library.types.QuantityTypeArithmeticGroupFunction.DimensionalGroupFunction):
        """
        Java class 'org.openhab.core.library.types.QuantityTypeArithmeticGroupFunction$Max'
        
            Extends:
                org.openhab.core.library.types.QuantityTypeArithmeticGroupFunction$DimensionalGroupFunction
        
          Constructors:
            * Max(java.lang.Class)
        
        """
        def __init__(self, dimension: typing.Type[javax.measure.Quantity[typing.Any]]): ...
        def calculate(self, items: java.util.Set[org.openhab.core.items.Item]) -> org.openhab.core.types.State: ...
    class Min(org.openhab.core.library.types.QuantityTypeArithmeticGroupFunction.DimensionalGroupFunction):
        """
        Java class 'org.openhab.core.library.types.QuantityTypeArithmeticGroupFunction$Min'
        
            Extends:
                org.openhab.core.library.types.QuantityTypeArithmeticGroupFunction$DimensionalGroupFunction
        
          Constructors:
            * Min(java.lang.Class)
        
        """
        def __init__(self, dimension: typing.Type[javax.measure.Quantity[typing.Any]]): ...
        def calculate(self, items: java.util.Set[org.openhab.core.items.Item]) -> org.openhab.core.types.State: ...
    class Sum(org.openhab.core.library.types.QuantityTypeArithmeticGroupFunction.DimensionalGroupFunction):
        """
        Java class 'org.openhab.core.library.types.QuantityTypeArithmeticGroupFunction$Sum'
        
            Extends:
                org.openhab.core.library.types.QuantityTypeArithmeticGroupFunction$DimensionalGroupFunction
        
          Constructors:
            * Sum(java.lang.Class)
        
        """
        def __init__(self, dimension: typing.Type[javax.measure.Quantity[typing.Any]]): ...
        def calculate(self, items: java.util.Set[org.openhab.core.items.Item]) -> org.openhab.core.types.State: ...
