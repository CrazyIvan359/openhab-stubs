import java.lang
import typing


class AudioStreamUtils(java.lang.Object):
    """
    Java class 'org.openhab.core.audio.utils.AudioStreamUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * AudioStreamUtils()
    
      Attributes:
        EXTENSION_SEPARATOR (java.lang.String): final static field
    
    """
    EXTENSION_SEPARATOR: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    @classmethod
    def getBaseName(cls, filename: java.lang.String) -> java.lang.String: ...
    @classmethod
    def getExtension(cls, filename: java.lang.String) -> java.lang.String: ...
    @classmethod
    def isExtension(cls, filename: java.lang.String, extension: java.lang.String) -> bool: ...
