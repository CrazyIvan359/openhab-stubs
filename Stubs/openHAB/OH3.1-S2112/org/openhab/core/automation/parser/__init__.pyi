import java.io
import java.lang
import java.util
import typing


_Parser__T = typing.TypeVar('_Parser__T')  # <T>
class Parser(java.lang.Object, typing.Generic[_Parser__T]):
    """
    @NonNullByDefault public interface Parser<T>
    
        This interface provides opportunity to plug different parsers, for example JSON, GSON or other.
    
    
    """
    PARSER_TYPE: typing.ClassVar[java.lang.String] = ...
    PARSER_MODULE_TYPE: typing.ClassVar[java.lang.String] = ...
    PARSER_TEMPLATE: typing.ClassVar[java.lang.String] = ...
    PARSER_RULE: typing.ClassVar[java.lang.String] = ...
    FORMAT: typing.ClassVar[java.lang.String] = ...
    FORMAT_JSON: typing.ClassVar[java.lang.String] = ...
    def parse(self, reader: java.io.InputStreamReader) -> java.util.Set[_Parser__T]: ...
    def serialize(self, dataObjects: java.util.Set[_Parser__T], writer: java.io.OutputStreamWriter) -> None: ...

class ParsingException(java.lang.Exception):
    """
    Java class 'org.openhab.core.automation.parser.ParsingException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * ParsingException(org.openhab.core.automation.parser.ParsingNestedException)
        * ParsingException(java.util.List)
    
    """
    @typing.overload
    def __init__(self, exceptions: java.util.List['ParsingNestedException']): ...
    @typing.overload
    def __init__(self, e: 'ParsingNestedException'): ...
    def getMessage(self) -> java.lang.String: ...
    def getStackTrace(self) -> typing.List[java.lang.StackTraceElement]: ...

class ParsingNestedException(java.lang.Exception):
    """
    Java class 'org.openhab.core.automation.parser.ParsingNestedException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * ParsingNestedException(int, java.lang.String, java.lang.String, java.lang.Throwable)
        * ParsingNestedException(int, java.lang.String, java.lang.Throwable)
    
      Attributes:
        MODULE_TYPE (int): final static field
        TEMPLATE (int): final static field
        RULE (int): final static field
    
    """
    MODULE_TYPE: typing.ClassVar[int] = ...
    TEMPLATE: typing.ClassVar[int] = ...
    RULE: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, type: int, id: java.lang.String, msg: java.lang.String, t: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, type: int, id: java.lang.String, t: java.lang.Throwable): ...
    def getMessage(self) -> java.lang.String: ...
