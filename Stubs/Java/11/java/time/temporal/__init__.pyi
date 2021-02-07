import java
import java.io
import java.lang
import java.time
import java.time.chrono
import java.time.format
import java.util
import java.util.function
import typing


class IsoFields(java.lang.Object):
    """
    Java class 'java.time.temporal.IsoFields'
    
        Extends:
            java.lang.Object
    
      Attributes:
        DAY_OF_QUARTER (java.time.temporal.TemporalField): final static field
        QUARTER_OF_YEAR (java.time.temporal.TemporalField): final static field
        WEEK_OF_WEEK_BASED_YEAR (java.time.temporal.TemporalField): final static field
        WEEK_BASED_YEAR (java.time.temporal.TemporalField): final static field
        WEEK_BASED_YEARS (java.time.temporal.TemporalUnit): final static field
        QUARTER_YEARS (java.time.temporal.TemporalUnit): final static field
    
    """
    DAY_OF_QUARTER: typing.ClassVar['TemporalField'] = ...
    QUARTER_OF_YEAR: typing.ClassVar['TemporalField'] = ...
    WEEK_OF_WEEK_BASED_YEAR: typing.ClassVar['TemporalField'] = ...
    WEEK_BASED_YEAR: typing.ClassVar['TemporalField'] = ...
    WEEK_BASED_YEARS: typing.ClassVar['TemporalUnit'] = ...
    QUARTER_YEARS: typing.ClassVar['TemporalUnit'] = ...

class JulianFields(java.lang.Object):
    """
    Java class 'java.time.temporal.JulianFields'
    
        Extends:
            java.lang.Object
    
      Attributes:
        JULIAN_DAY (java.time.temporal.TemporalField): final static field
        MODIFIED_JULIAN_DAY (java.time.temporal.TemporalField): final static field
        RATA_DIE (java.time.temporal.TemporalField): final static field
    
    """
    JULIAN_DAY: typing.ClassVar['TemporalField'] = ...
    MODIFIED_JULIAN_DAY: typing.ClassVar['TemporalField'] = ...
    RATA_DIE: typing.ClassVar['TemporalField'] = ...

class TemporalAccessor(java.lang.Object):
    """
    public interface TemporalAccessor
    
        Framework-level interface defining read-only access to a temporal object, such as a date, time, offset or some
        combination of these.
    
        This is the base interface type for date, time and offset objects. It is implemented by those classes that can provide
        information as :class:`~java.time.temporal.TemporalField` or :class:`~java.time.temporal.TemporalQuery`.
    
        Most date and time information can be represented as a number. These are modeled using :code:`TemporalField` with the
        number held using a :code:`long` to handle large values. Year, month and day-of-month are simple examples of fields, but
        they also include instant and offsets. See :class:`~java.time.temporal.ChronoField` for the standard set of fields.
    
        Two pieces of date/time information cannot be represented by numbers, the :class:`~java.time.chrono.Chronology` and the
        :class:`~java.time.ZoneId`. These can be accessed via :meth:`~java.time.temporal.TemporalAccessor.query` using the
        static methods defined on :class:`~java.time.temporal.TemporalQuery`.
    
        A sub-interface, :class:`~java.time.temporal.Temporal`, extends this definition to one that also supports adjustment and
        manipulation on more complete temporal objects.
    
        This interface is a framework-level interface that should not be widely used in application code. Instead, applications
        should create and pass around instances of concrete types, such as :code:`LocalDate`. There are many reasons for this,
        part of which is that implementations of this interface may be in calendar systems other than ISO. See
        :class:`~java.time.chrono.ChronoLocalDate` for a fuller discussion of the issues.
    
        Implementation Requirements:
            This interface places no restrictions on the mutability of implementations, however immutability is strongly
            recommended.
    
        Since:
            1.8
    
    
    """
    def get(self, temporalField: 'TemporalField') -> int: ...
    def getLong(self, temporalField: 'TemporalField') -> int: ...
    def isSupported(self, temporalField: 'TemporalField') -> bool: ...
    _query__R = typing.TypeVar('_query__R')  # <R>
    def query(self, temporalQuery: typing.Union['TemporalQuery'[_query__R], typing.Callable[[], _query__R]]) -> _query__R: ...
    def range(self, temporalField: 'TemporalField') -> 'ValueRange': ...

class TemporalAdjuster(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface TemporalAdjuster
    
        Strategy for adjusting a temporal object.
    
        Adjusters are a key tool for modifying temporal objects. They exist to externalize the process of adjustment, permitting
        different approaches, as per the strategy design pattern. Examples might be an adjuster that sets the date avoiding
        weekends, or one that sets the date to the last day of the month.
    
        There are two equivalent ways of using a :code:`TemporalAdjuster`. The first is to invoke the method on this interface
        directly. The second is to use :meth:`~java.time.temporal.Temporal.with`:
    
        .. code-block: java
        
           // these two lines are equivalent, but the second approach is recommended
           temporal = thisAdjuster.adjustInto(temporal);
           temporal = temporal.with(thisAdjuster);
         
        It is recommended to use the second approach, :code:`with(TemporalAdjuster)`, as it is a lot clearer to read in code.
    
        The :class:`~java.time.temporal.TemporalAdjusters` class contains a standard set of adjusters, available as static
        methods. These include:
    
          - finding the first or last day of the month
          - finding the first day of next month
          - finding the first or last day of the year
          - finding the first day of next year
          - finding the first or last day-of-week within a month, such as "first Wednesday in June"
          - finding the next or previous day-of-week, such as "next Thursday"
    
    
        Implementation Requirements:
            This interface places no restrictions on the mutability of implementations, however immutability is strongly
            recommended.
    
        Since:
            1.8
    
        Also see:
            :class:`~java.time.temporal.TemporalAdjusters`
    
    
    """
    def adjustInto(self, temporal: 'Temporal') -> 'Temporal': ...

class TemporalAdjusters(java.lang.Object):
    """
    Java class 'java.time.temporal.TemporalAdjusters'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def dayOfWeekInMonth(cls, int: int, dayOfWeek: java.time.DayOfWeek) -> TemporalAdjuster: ...
    @classmethod
    def firstDayOfMonth(cls) -> TemporalAdjuster: ...
    @classmethod
    def firstDayOfNextMonth(cls) -> TemporalAdjuster: ...
    @classmethod
    def firstDayOfNextYear(cls) -> TemporalAdjuster: ...
    @classmethod
    def firstDayOfYear(cls) -> TemporalAdjuster: ...
    @classmethod
    def firstInMonth(cls, dayOfWeek: java.time.DayOfWeek) -> TemporalAdjuster: ...
    @classmethod
    def lastDayOfMonth(cls) -> TemporalAdjuster: ...
    @classmethod
    def lastDayOfYear(cls) -> TemporalAdjuster: ...
    @classmethod
    def lastInMonth(cls, dayOfWeek: java.time.DayOfWeek) -> TemporalAdjuster: ...
    @classmethod
    def next(cls, dayOfWeek: java.time.DayOfWeek) -> TemporalAdjuster: ...
    @classmethod
    def nextOrSame(cls, dayOfWeek: java.time.DayOfWeek) -> TemporalAdjuster: ...
    @classmethod
    def ofDateAdjuster(cls, unaryOperator: typing.Union[java.util.function.UnaryOperator[java.time.LocalDate], typing.Callable[[], java.time.LocalDate]]) -> TemporalAdjuster: ...
    @classmethod
    def previous(cls, dayOfWeek: java.time.DayOfWeek) -> TemporalAdjuster: ...
    @classmethod
    def previousOrSame(cls, dayOfWeek: java.time.DayOfWeek) -> TemporalAdjuster: ...

class TemporalAmount(java.lang.Object):
    """
    public interface TemporalAmount
    
        Framework-level interface defining an amount of time, such as "6 hours", "8 days" or "2 years and 3 months".
    
        This is the base interface type for amounts of time. An amount is distinct from a date or time-of-day in that it is not
        tied to any specific point on the time-line.
    
        The amount can be thought of as a :code:`Map` of :class:`~java.time.temporal.TemporalUnit` to :code:`long`, exposed via
        :meth:`~java.time.temporal.TemporalAmount.getUnits` and :meth:`~java.time.temporal.TemporalAmount.get`. A simple case
        might have a single unit-value pair, such as "6 hours". A more complex case may have multiple unit-value pairs, such as
        "7 years, 3 months and 5 days".
    
        There are two common implementations. :class:`~java.time.Period` is a date-based implementation, storing years, months
        and days. :class:`~java.time.Duration` is a time-based implementation, storing seconds and nanoseconds, but providing
        some access using other duration based units such as minutes, hours and fixed 24-hour days.
    
        This interface is a framework-level interface that should not be widely used in application code. Instead, applications
        should create and pass around instances of concrete types, such as :code:`Period` and :code:`Duration`.
    
        Implementation Requirements:
            This interface places no restrictions on the mutability of implementations, however immutability is strongly
            recommended.
    
        Since:
            1.8
    
    
    """
    def addTo(self, temporal: 'Temporal') -> 'Temporal': ...
    def get(self, temporalUnit: 'TemporalUnit') -> int: ...
    def getUnits(self) -> java.util.List['TemporalUnit']: ...
    def subtractFrom(self, temporal: 'Temporal') -> 'Temporal': ...

class TemporalField(java.lang.Object):
    """
    public interface TemporalField
    
        A field of date-time, such as month-of-year or hour-of-minute.
    
        Date and time is expressed using fields which partition the time-line into something meaningful for humans.
        Implementations of this interface represent those fields.
    
        The most commonly used units are defined in :class:`~java.time.temporal.ChronoField`. Further fields are supplied in
        :class:`~java.time.temporal.IsoFields`, :class:`~java.time.temporal.WeekFields` and
        :class:`~java.time.temporal.JulianFields`. Fields can also be written by application code by implementing this
        interface.
    
        The field works using double dispatch. Client code calls methods on a date-time like :code:`LocalDateTime` which check
        if the field is a :code:`ChronoField`. If it is, then the date-time must handle it. Otherwise, the method call is
        re-dispatched to the matching method in this interface.
    
        Implementation Requirements:
            This interface must be implemented with care to ensure other classes operate correctly. All implementations that can be
            instantiated must be final, immutable and thread-safe. Implementations should be :code:`Serializable` where possible. An
            enum is as effective implementation choice.
    
        Since:
            1.8
    
    
    """
    _adjustInto__R = typing.TypeVar('_adjustInto__R', bound='Temporal')  # <R>
    def adjustInto(self, r: _adjustInto__R, long: int) -> _adjustInto__R: ...
    def getBaseUnit(self) -> 'TemporalUnit': ...
    def getDisplayName(self, locale: java.util.Locale) -> java.lang.String: ...
    def getFrom(self, temporalAccessor: TemporalAccessor) -> int: ...
    def getRangeUnit(self) -> 'TemporalUnit': ...
    def isDateBased(self) -> bool: ...
    def isSupportedBy(self, temporalAccessor: TemporalAccessor) -> bool: ...
    def isTimeBased(self) -> bool: ...
    def range(self) -> 'ValueRange': ...
    def rangeRefinedBy(self, temporalAccessor: TemporalAccessor) -> 'ValueRange': ...
    def resolve(self, map: typing.Union[java.util.Map['TemporalField', int], typing.Mapping['TemporalField', int]], temporalAccessor: TemporalAccessor, resolverStyle: java.time.format.ResolverStyle) -> TemporalAccessor: ...
    def toString(self) -> java.lang.String: ...

class TemporalQueries(java.lang.Object):
    """
    Java class 'java.time.temporal.TemporalQueries'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def chronology(cls) -> 'TemporalQuery'[java.time.chrono.Chronology]: ...
    @classmethod
    def localDate(cls) -> 'TemporalQuery'[java.time.LocalDate]: ...
    @classmethod
    def localTime(cls) -> 'TemporalQuery'[java.time.LocalTime]: ...
    @classmethod
    def offset(cls) -> 'TemporalQuery'[java.time.ZoneOffset]: ...
    @classmethod
    def precision(cls) -> 'TemporalQuery'['TemporalUnit']: ...
    @classmethod
    def zone(cls) -> 'TemporalQuery'[java.time.ZoneId]: ...
    @classmethod
    def zoneId(cls) -> 'TemporalQuery'[java.time.ZoneId]: ...

_TemporalQuery__R = typing.TypeVar('_TemporalQuery__R')  # <R>
class TemporalQuery(java.lang.Object, typing.Generic[_TemporalQuery__R]):
    """
    :class:`~java.lang.FunctionalInterface` public interface TemporalQuery<R>
    
        Strategy for querying a temporal object.
    
        Queries are a key tool for extracting information from temporal objects. They exist to externalize the process of
        querying, permitting different approaches, as per the strategy design pattern. Examples might be a query that checks if
        the date is the day before February 29th in a leap year, or calculates the number of days to your next birthday.
    
        The :class:`~java.time.temporal.TemporalField` interface provides another mechanism for querying temporal objects. That
        interface is limited to returning a :code:`long`. By contrast, queries can return any type.
    
        There are two equivalent ways of using a :code:`TemporalQuery`. The first is to invoke the method on this interface
        directly. The second is to use :meth:`~java.time.temporal.TemporalAccessor.query`:
    
        .. code-block: java
        
           // these two lines are equivalent, but the second approach is recommended
           temporal = thisQuery.queryFrom(temporal);
           temporal = temporal.query(thisQuery);
         
        It is recommended to use the second approach, :code:`query(TemporalQuery)`, as it is a lot clearer to read in code.
    
        The most common implementations are method references, such as :code:`LocalDate::from` and :code:`ZoneId::from`.
        Additional common queries are provided as static methods in :class:`~java.time.temporal.TemporalQueries`.
    
        Implementation Requirements:
            This interface places no restrictions on the mutability of implementations, however immutability is strongly
            recommended.
    
        Since:
            1.8
    
    
    """
    def queryFrom(self, temporalAccessor: TemporalAccessor) -> _TemporalQuery__R: ...

class TemporalUnit(java.lang.Object):
    """
    public interface TemporalUnit
    
        A unit of date-time, such as Days or Hours.
    
        Measurement of time is built on units, such as years, months, days, hours, minutes and seconds. Implementations of this
        interface represent those units.
    
        An instance of this interface represents the unit itself, rather than an amount of the unit. See
        :class:`~java.time.Period` for a class that represents an amount in terms of the common units.
    
        The most commonly used units are defined in :class:`~java.time.temporal.ChronoUnit`. Further units are supplied in
        :class:`~java.time.temporal.IsoFields`. Units can also be written by application code by implementing this interface.
    
        The unit works using double dispatch. Client code calls methods on a date-time like :code:`LocalDateTime` which check if
        the unit is a :code:`ChronoUnit`. If it is, then the date-time must handle it. Otherwise, the method call is
        re-dispatched to the matching method in this interface.
    
        Implementation Requirements:
            This interface must be implemented with care to ensure other classes operate correctly. All implementations that can be
            instantiated must be final, immutable and thread-safe. It is recommended to use an enum where possible.
    
        Since:
            1.8
    
    
    """
    _addTo__R = typing.TypeVar('_addTo__R', bound='Temporal')  # <R>
    def addTo(self, r: _addTo__R, long: int) -> _addTo__R: ...
    def between(self, temporal: 'Temporal', temporal2: 'Temporal') -> int: ...
    def getDuration(self) -> java.time.Duration: ...
    def isDateBased(self) -> bool: ...
    def isDurationEstimated(self) -> bool: ...
    def isSupportedBy(self, temporal: 'Temporal') -> bool: ...
    def isTimeBased(self) -> bool: ...
    def toString(self) -> java.lang.String: ...

class UnsupportedTemporalTypeException(java.time.DateTimeException):
    """
    Java class 'java.time.temporal.UnsupportedTemporalTypeException'
    
        Extends:
            java.time.DateTimeException
    
      Constructors:
        * UnsupportedTemporalTypeException(java.lang.String)
        * UnsupportedTemporalTypeException(java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, string: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, throwable: java.lang.Throwable): ...

class ValueRange(java.io.Serializable):
    """
    Java class 'java.time.temporal.ValueRange'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
    """
    def checkValidIntValue(self, long: int, temporalField: TemporalField) -> int: ...
    def checkValidValue(self, long: int, temporalField: TemporalField) -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getLargestMinimum(self) -> int: ...
    def getMaximum(self) -> int: ...
    def getMinimum(self) -> int: ...
    def getSmallestMaximum(self) -> int: ...
    def hashCode(self) -> int: ...
    def isFixed(self) -> bool: ...
    def isIntValue(self) -> bool: ...
    def isValidIntValue(self, long: int) -> bool: ...
    def isValidValue(self, long: int) -> bool: ...
    @classmethod
    @typing.overload
    def of(cls, long: int, long2: int) -> 'ValueRange': ...
    @classmethod
    @typing.overload
    def of(cls, long: int, long2: int, long3: int) -> 'ValueRange': ...
    @classmethod
    @typing.overload
    def of(cls, long: int, long2: int, long3: int, long4: int) -> 'ValueRange': ...
    def toString(self) -> java.lang.String: ...

class WeekFields(java.io.Serializable):
    """
    Java class 'java.time.temporal.WeekFields'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Attributes:
        ISO (java.time.temporal.WeekFields): final static field
        SUNDAY_START (java.time.temporal.WeekFields): final static field
        WEEK_BASED_YEARS (java.time.temporal.TemporalUnit): final static field
    
    """
    ISO: typing.ClassVar['WeekFields'] = ...
    SUNDAY_START: typing.ClassVar['WeekFields'] = ...
    WEEK_BASED_YEARS: typing.ClassVar[TemporalUnit] = ...
    def dayOfWeek(self) -> TemporalField: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getFirstDayOfWeek(self) -> java.time.DayOfWeek: ...
    def getMinimalDaysInFirstWeek(self) -> int: ...
    def hashCode(self) -> int: ...
    @classmethod
    @typing.overload
    def of(cls, dayOfWeek: java.time.DayOfWeek, int: int) -> 'WeekFields': ...
    @classmethod
    @typing.overload
    def of(cls, locale: java.util.Locale) -> 'WeekFields': ...
    def toString(self) -> java.lang.String: ...
    def weekBasedYear(self) -> TemporalField: ...
    def weekOfMonth(self) -> TemporalField: ...
    def weekOfWeekBasedYear(self) -> TemporalField: ...
    def weekOfYear(self) -> TemporalField: ...

class ChronoField(java.lang.Enum[java.time.temporal.ChronoField], TemporalField):
    """
    Java class 'java.time.temporal.ChronoField'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            java.time.temporal.TemporalField
    
      Attributes:
        NANO_OF_SECOND (java.time.temporal.ChronoField): final static enum constant
        NANO_OF_DAY (java.time.temporal.ChronoField): final static enum constant
        MICRO_OF_SECOND (java.time.temporal.ChronoField): final static enum constant
        MICRO_OF_DAY (java.time.temporal.ChronoField): final static enum constant
        MILLI_OF_SECOND (java.time.temporal.ChronoField): final static enum constant
        MILLI_OF_DAY (java.time.temporal.ChronoField): final static enum constant
        SECOND_OF_MINUTE (java.time.temporal.ChronoField): final static enum constant
        SECOND_OF_DAY (java.time.temporal.ChronoField): final static enum constant
        MINUTE_OF_HOUR (java.time.temporal.ChronoField): final static enum constant
        MINUTE_OF_DAY (java.time.temporal.ChronoField): final static enum constant
        HOUR_OF_AMPM (java.time.temporal.ChronoField): final static enum constant
        CLOCK_HOUR_OF_AMPM (java.time.temporal.ChronoField): final static enum constant
        HOUR_OF_DAY (java.time.temporal.ChronoField): final static enum constant
        CLOCK_HOUR_OF_DAY (java.time.temporal.ChronoField): final static enum constant
        AMPM_OF_DAY (java.time.temporal.ChronoField): final static enum constant
        DAY_OF_WEEK (java.time.temporal.ChronoField): final static enum constant
        ALIGNED_DAY_OF_WEEK_IN_MONTH (java.time.temporal.ChronoField): final static enum constant
        ALIGNED_DAY_OF_WEEK_IN_YEAR (java.time.temporal.ChronoField): final static enum constant
        DAY_OF_MONTH (java.time.temporal.ChronoField): final static enum constant
        DAY_OF_YEAR (java.time.temporal.ChronoField): final static enum constant
        EPOCH_DAY (java.time.temporal.ChronoField): final static enum constant
        ALIGNED_WEEK_OF_MONTH (java.time.temporal.ChronoField): final static enum constant
        ALIGNED_WEEK_OF_YEAR (java.time.temporal.ChronoField): final static enum constant
        MONTH_OF_YEAR (java.time.temporal.ChronoField): final static enum constant
        PROLEPTIC_MONTH (java.time.temporal.ChronoField): final static enum constant
        YEAR_OF_ERA (java.time.temporal.ChronoField): final static enum constant
        YEAR (java.time.temporal.ChronoField): final static enum constant
        ERA (java.time.temporal.ChronoField): final static enum constant
        INSTANT_SECONDS (java.time.temporal.ChronoField): final static enum constant
        OFFSET_SECONDS (java.time.temporal.ChronoField): final static enum constant
    
    """
    NANO_OF_SECOND: typing.ClassVar['ChronoField'] = ...
    NANO_OF_DAY: typing.ClassVar['ChronoField'] = ...
    MICRO_OF_SECOND: typing.ClassVar['ChronoField'] = ...
    MICRO_OF_DAY: typing.ClassVar['ChronoField'] = ...
    MILLI_OF_SECOND: typing.ClassVar['ChronoField'] = ...
    MILLI_OF_DAY: typing.ClassVar['ChronoField'] = ...
    SECOND_OF_MINUTE: typing.ClassVar['ChronoField'] = ...
    SECOND_OF_DAY: typing.ClassVar['ChronoField'] = ...
    MINUTE_OF_HOUR: typing.ClassVar['ChronoField'] = ...
    MINUTE_OF_DAY: typing.ClassVar['ChronoField'] = ...
    HOUR_OF_AMPM: typing.ClassVar['ChronoField'] = ...
    CLOCK_HOUR_OF_AMPM: typing.ClassVar['ChronoField'] = ...
    HOUR_OF_DAY: typing.ClassVar['ChronoField'] = ...
    CLOCK_HOUR_OF_DAY: typing.ClassVar['ChronoField'] = ...
    AMPM_OF_DAY: typing.ClassVar['ChronoField'] = ...
    DAY_OF_WEEK: typing.ClassVar['ChronoField'] = ...
    ALIGNED_DAY_OF_WEEK_IN_MONTH: typing.ClassVar['ChronoField'] = ...
    ALIGNED_DAY_OF_WEEK_IN_YEAR: typing.ClassVar['ChronoField'] = ...
    DAY_OF_MONTH: typing.ClassVar['ChronoField'] = ...
    DAY_OF_YEAR: typing.ClassVar['ChronoField'] = ...
    EPOCH_DAY: typing.ClassVar['ChronoField'] = ...
    ALIGNED_WEEK_OF_MONTH: typing.ClassVar['ChronoField'] = ...
    ALIGNED_WEEK_OF_YEAR: typing.ClassVar['ChronoField'] = ...
    MONTH_OF_YEAR: typing.ClassVar['ChronoField'] = ...
    PROLEPTIC_MONTH: typing.ClassVar['ChronoField'] = ...
    YEAR_OF_ERA: typing.ClassVar['ChronoField'] = ...
    YEAR: typing.ClassVar['ChronoField'] = ...
    ERA: typing.ClassVar['ChronoField'] = ...
    INSTANT_SECONDS: typing.ClassVar['ChronoField'] = ...
    OFFSET_SECONDS: typing.ClassVar['ChronoField'] = ...
    _adjustInto__R = typing.TypeVar('_adjustInto__R', bound='Temporal')  # <R>
    def adjustInto(self, r: _adjustInto__R, long: int) -> _adjustInto__R: ...
    def checkValidIntValue(self, long: int) -> int: ...
    def checkValidValue(self, long: int) -> int: ...
    def getBaseUnit(self) -> TemporalUnit: ...
    def getDisplayName(self, locale: java.util.Locale) -> java.lang.String: ...
    def getFrom(self, temporalAccessor: TemporalAccessor) -> int: ...
    def getRangeUnit(self) -> TemporalUnit: ...
    def isDateBased(self) -> bool: ...
    def isSupportedBy(self, temporalAccessor: TemporalAccessor) -> bool: ...
    def isTimeBased(self) -> bool: ...
    def range(self) -> ValueRange: ...
    def rangeRefinedBy(self, temporalAccessor: TemporalAccessor) -> ValueRange: ...
    def toString(self) -> java.lang.String: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, string: java.lang.String) -> 'ChronoField': ...
    @classmethod
    def values(cls) -> typing.List['ChronoField']: ...

class ChronoUnit(java.lang.Enum[java.time.temporal.ChronoUnit], TemporalUnit):
    """
    Java class 'java.time.temporal.ChronoUnit'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            java.time.temporal.TemporalUnit
    
      Attributes:
        NANOS (java.time.temporal.ChronoUnit): final static enum constant
        MICROS (java.time.temporal.ChronoUnit): final static enum constant
        MILLIS (java.time.temporal.ChronoUnit): final static enum constant
        SECONDS (java.time.temporal.ChronoUnit): final static enum constant
        MINUTES (java.time.temporal.ChronoUnit): final static enum constant
        HOURS (java.time.temporal.ChronoUnit): final static enum constant
        HALF_DAYS (java.time.temporal.ChronoUnit): final static enum constant
        DAYS (java.time.temporal.ChronoUnit): final static enum constant
        WEEKS (java.time.temporal.ChronoUnit): final static enum constant
        MONTHS (java.time.temporal.ChronoUnit): final static enum constant
        YEARS (java.time.temporal.ChronoUnit): final static enum constant
        DECADES (java.time.temporal.ChronoUnit): final static enum constant
        CENTURIES (java.time.temporal.ChronoUnit): final static enum constant
        MILLENNIA (java.time.temporal.ChronoUnit): final static enum constant
        ERAS (java.time.temporal.ChronoUnit): final static enum constant
        FOREVER (java.time.temporal.ChronoUnit): final static enum constant
    
    """
    NANOS: typing.ClassVar['ChronoUnit'] = ...
    MICROS: typing.ClassVar['ChronoUnit'] = ...
    MILLIS: typing.ClassVar['ChronoUnit'] = ...
    SECONDS: typing.ClassVar['ChronoUnit'] = ...
    MINUTES: typing.ClassVar['ChronoUnit'] = ...
    HOURS: typing.ClassVar['ChronoUnit'] = ...
    HALF_DAYS: typing.ClassVar['ChronoUnit'] = ...
    DAYS: typing.ClassVar['ChronoUnit'] = ...
    WEEKS: typing.ClassVar['ChronoUnit'] = ...
    MONTHS: typing.ClassVar['ChronoUnit'] = ...
    YEARS: typing.ClassVar['ChronoUnit'] = ...
    DECADES: typing.ClassVar['ChronoUnit'] = ...
    CENTURIES: typing.ClassVar['ChronoUnit'] = ...
    MILLENNIA: typing.ClassVar['ChronoUnit'] = ...
    ERAS: typing.ClassVar['ChronoUnit'] = ...
    FOREVER: typing.ClassVar['ChronoUnit'] = ...
    _addTo__R = typing.TypeVar('_addTo__R', bound='Temporal')  # <R>
    def addTo(self, r: _addTo__R, long: int) -> _addTo__R: ...
    def between(self, temporal: 'Temporal', temporal2: 'Temporal') -> int: ...
    def getDuration(self) -> java.time.Duration: ...
    def isDateBased(self) -> bool: ...
    def isDurationEstimated(self) -> bool: ...
    def isSupportedBy(self, temporal: 'Temporal') -> bool: ...
    def isTimeBased(self) -> bool: ...
    def toString(self) -> java.lang.String: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, string: java.lang.String) -> 'ChronoUnit': ...
    @classmethod
    def values(cls) -> typing.List['ChronoUnit']: ...

class Temporal(TemporalAccessor):
    """
    Java class 'java.time.temporal.Temporal'
    
        Interfaces:
            java.time.temporal.TemporalAccessor
    
    """
    @typing.overload
    def isSupported(self, temporalUnit: TemporalUnit) -> bool: ...
    @typing.overload
    def isSupported(self, temporalField: TemporalField) -> bool: ...
    @typing.overload
    def minus(self, temporalAmount: TemporalAmount) -> 'Temporal': ...
    @typing.overload
    def minus(self, long: int, temporalUnit: TemporalUnit) -> 'Temporal': ...
    @typing.overload
    def plus(self, long: int, temporalUnit: TemporalUnit) -> 'Temporal': ...
    @typing.overload
    def plus(self, temporalAmount: TemporalAmount) -> 'Temporal': ...
    def until(self, temporal: 'Temporal', temporalUnit: TemporalUnit) -> int: ...
