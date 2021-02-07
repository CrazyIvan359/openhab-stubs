import java.lang
import java.math
import java.util
import org
import typing


class CommandDescription(java.lang.Object):
    """
    @NonNullByDefault public interface CommandDescription
    
        The :class:`~org.openhab.core.types.CommandDescription` groups state command properties.
    
    
    """
    def getCommandOptions(self) -> java.util.List['CommandOption']: ...

class CommandDescriptionBuilder(java.lang.Object):
    """
    Java class 'org.openhab.core.types.CommandDescriptionBuilder'
    
        Extends:
            java.lang.Object
    
    """
    def build(self) -> CommandDescription: ...
    @classmethod
    def create(cls) -> 'CommandDescriptionBuilder': ...
    def withCommandOption(self, commandOption: 'CommandOption') -> 'CommandDescriptionBuilder': ...
    def withCommandOptions(self, commandOptions: java.util.List['CommandOption']) -> 'CommandDescriptionBuilder': ...

class CommandDescriptionProvider(java.lang.Object):
    """
    @NonNullByDefault public interface CommandDescriptionProvider
    
        Implementations provide an item specific, localized :class:`~org.openhab.core.types.CommandDescription`.
    
    
    """
    def getCommandDescription(self, itemName: java.lang.String, locale: java.util.Locale) -> CommandDescription: ...

class CommandOption(java.lang.Object):
    """
    Java class 'org.openhab.core.types.CommandOption'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * CommandOption(java.lang.String, java.lang.String)
    
    """
    def __init__(self, command: java.lang.String, label: java.lang.String): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getCommand(self) -> java.lang.String: ...
    def getLabel(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class EventDescription(java.lang.Object):
    """
    Java class 'org.openhab.core.types.EventDescription'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * EventDescription(java.util.List)
    
    """
    def __init__(self, options: java.util.List['EventOption']): ...
    def getOptions(self) -> java.util.List['EventOption']: ...
    def toString(self) -> java.lang.String: ...

class EventOption(java.lang.Object):
    """
    Java class 'org.openhab.core.types.EventOption'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * EventOption(java.lang.String, java.lang.String)
    
    """
    def __init__(self, value: java.lang.String, label: java.lang.String): ...
    def getLabel(self) -> java.lang.String: ...
    def getValue(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class EventType(java.lang.Enum[org.openhab.core.types.EventType]):
    """
    Java class 'org.openhab.core.types.EventType'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        COMMAND (org.openhab.core.types.EventType): final static enum constant
        UPDATE (org.openhab.core.types.EventType): final static enum constant
    
    """
    COMMAND: typing.ClassVar['EventType'] = ...
    UPDATE: typing.ClassVar['EventType'] = ...
    def toString(self) -> java.lang.String: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'EventType': ...
    @classmethod
    def values(cls) -> typing.List['EventType']: ...

class StateDescription(java.lang.Object):
    """
    Java class 'org.openhab.core.types.StateDescription'
    
        Extends:
            java.lang.Object
    
    """
    def equals(self, obj: typing.Any) -> bool: ...
    def getMaximum(self) -> java.math.BigDecimal: ...
    def getMinimum(self) -> java.math.BigDecimal: ...
    def getOptions(self) -> java.util.List['StateOption']: ...
    def getPattern(self) -> java.lang.String: ...
    def getStep(self) -> java.math.BigDecimal: ...
    def hashCode(self) -> int: ...
    def isReadOnly(self) -> bool: ...
    def toString(self) -> java.lang.String: ...

class StateDescriptionFragment(java.lang.Object):
    """
    @NonNullByDefault public interface StateDescriptionFragment
    
        A :class:`~org.openhab.core.types.StateDescriptionFragment` will deliver only the parts of a
        :class:`~org.openhab.core.types.StateDescription` it knows of. All other methods should return :code:`null` to indicate
        an unknown value.
    
    
    """
    def getMaximum(self) -> java.math.BigDecimal: ...
    def getMinimum(self) -> java.math.BigDecimal: ...
    def getOptions(self) -> java.util.List['StateOption']: ...
    def getPattern(self) -> java.lang.String: ...
    def getStep(self) -> java.math.BigDecimal: ...
    def isReadOnly(self) -> bool: ...
    def toStateDescription(self) -> StateDescription: ...

class StateDescriptionFragmentBuilder(java.lang.Object):
    """
    Java class 'org.openhab.core.types.StateDescriptionFragmentBuilder'
    
        Extends:
            java.lang.Object
    
    """
    def build(self) -> StateDescriptionFragment: ...
    @classmethod
    @typing.overload
    def create(cls) -> 'StateDescriptionFragmentBuilder': ...
    @classmethod
    @typing.overload
    def create(cls, legacy: StateDescription) -> 'StateDescriptionFragmentBuilder': ...
    @classmethod
    @typing.overload
    def create(cls, fragment: StateDescriptionFragment) -> 'StateDescriptionFragmentBuilder': ...
    def withMaximum(self, maximum: java.math.BigDecimal) -> 'StateDescriptionFragmentBuilder': ...
    def withMinimum(self, minimum: java.math.BigDecimal) -> 'StateDescriptionFragmentBuilder': ...
    def withOption(self, option: 'StateOption') -> 'StateDescriptionFragmentBuilder': ...
    def withOptions(self, options: java.util.List['StateOption']) -> 'StateDescriptionFragmentBuilder': ...
    def withPattern(self, pattern: java.lang.String) -> 'StateDescriptionFragmentBuilder': ...
    def withReadOnly(self, readOnly: bool) -> 'StateDescriptionFragmentBuilder': ...
    def withStep(self, step: java.math.BigDecimal) -> 'StateDescriptionFragmentBuilder': ...

class StateDescriptionFragmentProvider(java.lang.Object):
    """
    @NonNullByDefault public interface StateDescriptionFragmentProvider
    
        Provide a :class:`~org.openhab.core.types.StateDescriptionFragment` for the current
        :class:`~org.openhab.core.types.StateDescription`. Use the
        :class:`~org.openhab.core.types.StateDescriptionFragmentBuilder` to create a
        :class:`~org.openhab.core.types.StateDescriptionFragment` with only the parts known.
    
    
    """
    def getRank(self) -> int: ...
    def getStateDescriptionFragment(self, itemName: java.lang.String, locale: java.util.Locale) -> StateDescriptionFragment: ...

class StateOption(java.lang.Object):
    """
    Java class 'org.openhab.core.types.StateOption'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * StateOption(java.lang.String, java.lang.String)
    
    """
    def __init__(self, value: java.lang.String, label: java.lang.String): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getLabel(self) -> java.lang.String: ...
    def getValue(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class Type(java.lang.Object):
    """
    @NonNullByDefault public interface Type
    
        This is a parent interface for all states and commands. It was introduced as many states can be commands at the same
        time and vice versa. E.g a light can have the state ON or OFF and one can also send ON and OFF as commands to the
        device. This duality is captured by this marker interface and allows implementing classes to be both state and command
        at the same time.
    
    
    """
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def toFullString(self) -> java.lang.String: ...

class TypeParser(java.lang.Object):
    """
    Java class 'org.openhab.core.types.TypeParser'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def parseCommand(cls, types: java.util.List[typing.Type['Command']], s: java.lang.String) -> 'Command': ...
    @classmethod
    def parseState(cls, types: java.util.List[typing.Type['State']], s: java.lang.String) -> 'State': ...
    @classmethod
    def parseType(cls, typeName: java.lang.String, input: java.lang.String) -> Type: ...

class Command(Type):
    """
    Java class 'org.openhab.core.types.Command'
    
        Interfaces:
            org.openhab.core.types.Type
    
    """

class ComplexType(Type):
    """
    Java class 'org.openhab.core.types.ComplexType'
    
        Interfaces:
            org.openhab.core.types.Type
    
    """
    def getConstituents(self) -> java.util.SortedMap[java.lang.String, 'PrimitiveType']: ...

class PrimitiveType(Type):
    """
    Java class 'org.openhab.core.types.PrimitiveType'
    
        Interfaces:
            org.openhab.core.types.Type
    
    """

class State(Type):
    """
    Java class 'org.openhab.core.types.State'
    
        Interfaces:
            org.openhab.core.types.Type
    
    """

class RefreshType(java.lang.Enum[org.openhab.core.types.RefreshType], PrimitiveType, Command):
    """
    Java class 'org.openhab.core.types.RefreshType'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            org.openhab.core.types.PrimitiveType,
            org.openhab.core.types.Command
    
      Attributes:
        REFRESH (org.openhab.core.types.RefreshType): final static enum constant
    
    """
    REFRESH: typing.ClassVar['RefreshType'] = ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'RefreshType': ...
    @classmethod
    def values(cls) -> typing.List['RefreshType']: ...

class UnDefType(java.lang.Enum[org.openhab.core.types.UnDefType], PrimitiveType, State):
    """
    Java class 'org.openhab.core.types.UnDefType'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            org.openhab.core.types.PrimitiveType,
            org.openhab.core.types.State
    
      Attributes:
        UNDEF (org.openhab.core.types.UnDefType): final static enum constant
        NULL (org.openhab.core.types.UnDefType): final static enum constant
    
    """
    UNDEF: typing.ClassVar['UnDefType'] = ...
    NULL: typing.ClassVar['UnDefType'] = ...
    def format(self, pattern: java.lang.String) -> java.lang.String: ...
    def toFullString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'UnDefType': ...
    @classmethod
    def values(cls) -> typing.List['UnDefType']: ...
