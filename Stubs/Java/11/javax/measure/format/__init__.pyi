import java.lang
import javax.measure
import typing


class ParserException(javax.measure.MeasurementException):
    """
    Java class 'javax.measure.format.ParserException'
    
        Extends:
            javax.measure.MeasurementException
    
      Constructors:
        * ParserException(java.lang.Throwable)
        * ParserException(java.lang.CharSequence, int)
        * ParserException(java.lang.String, java.lang.CharSequence, int)
    
    """
    @typing.overload
    def __init__(self, charSequence: java.lang.CharSequence, int: int): ...
    @typing.overload
    def __init__(self, string: java.lang.String, charSequence: java.lang.CharSequence, int: int): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...
    def getParsedString(self) -> java.lang.String: ...
    def getPosition(self) -> int: ...

class UnitFormat(java.lang.Object):
    """
    Java class 'javax.measure.format.UnitFormat'
    
    """
    @typing.overload
    def format(self, unit: javax.measure.Unit[typing.Any], appendable: java.lang.Appendable) -> java.lang.Appendable: ...
    @typing.overload
    def format(self, unit: javax.measure.Unit[typing.Any]) -> java.lang.String: ...
    def isLocaleSensitive(self) -> bool: ...
    def label(self, unit: javax.measure.Unit[typing.Any], string: java.lang.String) -> None: ...
    def parse(self, charSequence: java.lang.CharSequence) -> javax.measure.Unit[typing.Any]: ...
