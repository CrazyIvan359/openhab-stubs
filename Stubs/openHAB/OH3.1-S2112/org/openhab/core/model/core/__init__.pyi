import java.io
import java.lang
import java.util
import java.util.function
import org
import org.eclipse.emf.ecore
import typing


class EventType(java.lang.Enum[org.openhab.core.model.core.EventType]):
    """
    Java class 'org.openhab.core.model.core.EventType'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        ADDED (org.openhab.core.model.core.EventType): final static enum constant
        REMOVED (org.openhab.core.model.core.EventType): final static enum constant
        MODIFIED (org.openhab.core.model.core.EventType): final static enum constant
    
    """
    ADDED: typing.ClassVar['EventType'] = ...
    REMOVED: typing.ClassVar['EventType'] = ...
    MODIFIED: typing.ClassVar['EventType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'EventType': ...
    @classmethod
    def values(cls) -> typing.List['EventType']: ...

class ModelCoreConstants(java.lang.Object):
    """
    Java class 'org.openhab.core.model.core.ModelCoreConstants'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ModelCoreConstants()
    
      Attributes:
        SERVICE_PID (java.lang.String): final static field
    
    """
    SERVICE_PID: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...

class ModelParser(java.lang.Object):
    """
    public interface ModelParser
    
        This interface has to be implemented by services that register an EMF model parser
    
    
    """
    def getExtension(self) -> java.lang.String: ...

class ModelRepository(java.lang.Object):
    """
    @NonNullByDefault public interface ModelRepository
    
        The model repository stores the configuration files (EMF models). It takes care of loading these resources and serving
        them to clients. By this abstraction, the clients do not need to know where the models come from.
    
    
    """
    def addModelRepositoryChangeListener(self, listener: 'ModelRepositoryChangeListener') -> None: ...
    def addOrRefreshModel(self, name: java.lang.String, inputStream: java.io.InputStream) -> bool: ...
    def getAllModelNamesOfType(self, modelType: java.lang.String) -> java.lang.Iterable[java.lang.String]: ...
    def getModel(self, name: java.lang.String) -> org.eclipse.emf.ecore.EObject: ...
    def reloadAllModelsOfType(self, modelType: java.lang.String) -> None: ...
    def removeAllModelsOfType(self, modelType: java.lang.String) -> java.util.Set[java.lang.String]: ...
    def removeModel(self, name: java.lang.String) -> bool: ...
    def removeModelRepositoryChangeListener(self, listener: 'ModelRepositoryChangeListener') -> None: ...

class ModelRepositoryChangeListener(java.lang.Object):
    """
    @NonNullByDefault public interface ModelRepositoryChangeListener
    
    
    
    """
    def modelChanged(self, modelName: java.lang.String, type: EventType) -> None: ...

class SafeEMF(java.lang.Object):
    """
    public interface SafeEMF
    
        Service interface to execute EMF methods in a single based thread.
    
    
    """
    _call_0__T = typing.TypeVar('_call_0__T')  # <T>
    @typing.overload
    def call(self, func: typing.Union[java.util.function.Supplier[_call_0__T], typing.Callable[[], _call_0__T]]) -> _call_0__T: ...
    @typing.overload
    def call(self, func: java.lang.Runnable) -> None: ...
