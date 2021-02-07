import java.lang
import org.osgi.framework
import typing


class TransformationException(java.lang.Exception):
    """
    Java class 'org.openhab.core.transform.TransformationException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * TransformationException(java.lang.String)
        * TransformationException(java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, message: java.lang.String): ...
    @typing.overload
    def __init__(self, message: java.lang.String, cause: java.lang.Throwable): ...

class TransformationHelper(java.lang.Object):
    """
    Java class 'org.openhab.core.transform.TransformationHelper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * TransformationHelper()
    
      Attributes:
        FUNCTION_VALUE_DELIMITER (java.lang.String): final static field
    
    """
    FUNCTION_VALUE_DELIMITER: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    @classmethod
    def getTransformationService(cls, context: org.osgi.framework.BundleContext, transformationType: java.lang.String) -> 'TransformationService': ...
    @classmethod
    def isTransform(cls, pattern: java.lang.String) -> bool: ...
    @classmethod
    @typing.overload
    def transform(cls, service: 'TransformationService', function: java.lang.String, format: java.lang.String, state: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def transform(cls, context: org.osgi.framework.BundleContext, stateDescPattern: java.lang.String, state: java.lang.String) -> java.lang.String: ...

class TransformationService(java.lang.Object):
    """
    @NonNullByDefault public interface TransformationService
    
        A TransformationProcessor transforms a given input and returns the transformed result. Transformations could make sense
        in various situations, for example:
    
          - extract certain informations from a weather forecast website
          - extract the status of your TV which provides it's status on a webpage
          - postprocess the output from a serial device to be human readable
    
        One could provide his own processors by providing a new implementation of this Interface.
    
    
    """
    TRANSFORM_FOLDER_NAME: typing.ClassVar[java.lang.String] = ...
    TRANSFORM_PROFILE_SCOPE: typing.ClassVar[java.lang.String] = ...
    def transform(self, function: java.lang.String, source: java.lang.String) -> java.lang.String: ...

_AbstractFileTransformationService__T = typing.TypeVar('_AbstractFileTransformationService__T')  # <T>
class AbstractFileTransformationService(TransformationService, typing.Generic[_AbstractFileTransformationService__T]):
    """
    Java class 'org.openhab.core.transform.AbstractFileTransformationService'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.transform.TransformationService
    
      Constructors:
        * AbstractFileTransformationService()
    
    """
    def __init__(self): ...
    def transform(self, filename: java.lang.String, source: java.lang.String) -> java.lang.String: ...
