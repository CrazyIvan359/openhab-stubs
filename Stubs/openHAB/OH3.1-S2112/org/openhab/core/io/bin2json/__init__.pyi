import java.lang
import typing


class ConversionException(java.lang.Exception):
    """
    Java class 'org.openhab.core.io.bin2json.ConversionException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * ConversionException(java.lang.Throwable)
        * ConversionException(java.lang.String, java.lang.Throwable)
        * ConversionException(java.lang.String)
        * ConversionException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, message: java.lang.String): ...
    @typing.overload
    def __init__(self, message: java.lang.String, cause: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, cause: java.lang.Throwable): ...
