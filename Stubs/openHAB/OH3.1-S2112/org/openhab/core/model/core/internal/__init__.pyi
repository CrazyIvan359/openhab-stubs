import java.io
import java.lang
import java.util
import java.util.function
import org.eclipse.emf.ecore
import org.openhab.core.model.core
import org.osgi.framework
import typing


class ModelCoreActivator(org.osgi.framework.BundleActivator):
    """
    Java class 'org.openhab.core.model.core.internal.ModelCoreActivator'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.osgi.framework.BundleActivator
    
      Constructors:
        * ModelCoreActivator()
    
    """
    def __init__(self): ...
    def start(self, bundleContext: org.osgi.framework.BundleContext) -> None: ...
    def stop(self, bundleContext: org.osgi.framework.BundleContext) -> None: ...

class ModelRepositoryImpl(org.openhab.core.model.core.ModelRepository):
    """
    Java class 'org.openhab.core.model.core.internal.ModelRepositoryImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.core.ModelRepository
    
      Constructors:
        * ModelRepositoryImpl(org.openhab.core.model.core.SafeEMF)
    
    """
    def __init__(self, safeEmf: org.openhab.core.model.core.SafeEMF): ...
    def addModelRepositoryChangeListener(self, listener: org.openhab.core.model.core.ModelRepositoryChangeListener) -> None: ...
    def addOrRefreshModel(self, name: java.lang.String, originalInputStream: java.io.InputStream) -> bool: ...
    def getAllModelNamesOfType(self, modelType: java.lang.String) -> java.lang.Iterable[java.lang.String]: ...
    def getModel(self, name: java.lang.String) -> org.eclipse.emf.ecore.EObject: ...
    def reloadAllModelsOfType(self, modelType: java.lang.String) -> None: ...
    def removeAllModelsOfType(self, modelType: java.lang.String) -> java.util.Set[java.lang.String]: ...
    def removeModel(self, name: java.lang.String) -> bool: ...
    def removeModelRepositoryChangeListener(self, listener: org.openhab.core.model.core.ModelRepositoryChangeListener) -> None: ...

class SafeEMFImpl(org.openhab.core.model.core.SafeEMF):
    """
    Java class 'org.openhab.core.model.core.internal.SafeEMFImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.core.SafeEMF
    
      Constructors:
        * SafeEMFImpl()
    
    """
    def __init__(self): ...
    _call_0__T = typing.TypeVar('_call_0__T')  # <T>
    @typing.overload
    def call(self, func: typing.Union[java.util.function.Supplier[_call_0__T], typing.Callable[[], _call_0__T]]) -> _call_0__T: ...
    @typing.overload
    def call(self, func: java.lang.Runnable) -> None: ...
