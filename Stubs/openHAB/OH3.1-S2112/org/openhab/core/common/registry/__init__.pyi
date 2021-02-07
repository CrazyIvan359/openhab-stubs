import java.lang
import java.util
import java.util.stream
import org.openhab.core.storage
import typing


_Identifiable__T = typing.TypeVar('_Identifiable__T')  # <T>
class Identifiable(java.lang.Object, typing.Generic[_Identifiable__T]):
    """
    @NonNullByDefault public interface Identifiable<@NonNull T>
    
        Interface for classes that instances provide an identifier.
    
    
    """
    def getUID(self) -> _Identifiable__T: ...

_Provider__E = typing.TypeVar('_Provider__E')  # <E>
class Provider(java.lang.Object, typing.Generic[_Provider__E]):
    """
    @NonNullByDefault public interface Provider<@NonNull E>
    
        A :class:`~org.openhab.core.common.registry.Provider` provides elements of a determined type and the subinterfaces are
        registered as OSGi services. Providers are tracked by :class:`~org.openhab.core.common.registry.Registry` services,
        which collect all elements from different providers of the same type.
    
    
    """
    def addProviderChangeListener(self, listener: 'ProviderChangeListener'[_Provider__E]) -> None: ...
    def getAll(self) -> java.util.Collection[_Provider__E]: ...
    def removeProviderChangeListener(self, listener: 'ProviderChangeListener'[_Provider__E]) -> None: ...

_ProviderChangeListener__E = typing.TypeVar('_ProviderChangeListener__E')  # <E>
class ProviderChangeListener(java.lang.Object, typing.Generic[_ProviderChangeListener__E]):
    """
    @NonNullByDefault public interface ProviderChangeListener<@NonNull E>
    
        :class:`~org.openhab.core.common.registry.ProviderChangeListener` can be added to
        :class:`~org.openhab.core.common.registry.Provider` services, to listen for changes. The
        :class:`~org.openhab.core.common.registry.AbstractRegistry` implements a
        :class:`~org.openhab.core.common.registry.ProviderChangeListener` and subscribes itself to every added
        :class:`~org.openhab.core.common.registry.Provider`.
    
    
    """
    def added(self, provider: Provider[_ProviderChangeListener__E], element: _ProviderChangeListener__E) -> None: ...
    def removed(self, provider: Provider[_ProviderChangeListener__E], element: _ProviderChangeListener__E) -> None: ...
    def updated(self, provider: Provider[_ProviderChangeListener__E], oldelement: _ProviderChangeListener__E, element: _ProviderChangeListener__E) -> None: ...

_Registry__E = typing.TypeVar('_Registry__E', bound=Identifiable)  # <E>
_Registry__K = typing.TypeVar('_Registry__K')  # <K>
class Registry(java.lang.Object, typing.Generic[_Registry__E, _Registry__K]):
    """
    @NonNullByDefault public interface Registry<@NonNull E extends :class:`~org.openhab.core.common.registry.Identifiable`<@NonNull K>,​@NonNull K>
    
        The :class:`~org.openhab.core.common.registry.Registry` interface represents a registry for elements of the type E. The
        concrete sub interfaces are registered as OSGi services.
    
    
    """
    def add(self, element: _Registry__E) -> _Registry__E: ...
    def addRegistryChangeListener(self, listener: 'RegistryChangeListener'[_Registry__E]) -> None: ...
    def get(self, key: _Registry__K) -> _Registry__E: ...
    def getAll(self) -> java.util.Collection[_Registry__E]: ...
    def remove(self, key: _Registry__K) -> _Registry__E: ...
    def removeRegistryChangeListener(self, listener: 'RegistryChangeListener'[_Registry__E]) -> None: ...
    def stream(self) -> java.util.stream.Stream[_Registry__E]: ...
    def update(self, element: _Registry__E) -> _Registry__E: ...

_RegistryChangeListener__E = typing.TypeVar('_RegistryChangeListener__E')  # <E>
class RegistryChangeListener(java.lang.Object, typing.Generic[_RegistryChangeListener__E]):
    """
    @NonNullByDefault public interface RegistryChangeListener<E>
    
        :class:`~org.openhab.core.common.registry.RegistryChangeListener` can be added to
        :class:`~org.openhab.core.common.registry.Registry` services, to listen for changes.
    
    
    """
    def added(self, element: _RegistryChangeListener__E) -> None: ...
    def removed(self, element: _RegistryChangeListener__E) -> None: ...
    def updated(self, oldElement: _RegistryChangeListener__E, element: _RegistryChangeListener__E) -> None: ...

_AbstractProvider__E = typing.TypeVar('_AbstractProvider__E')  # <E>
class AbstractProvider(Provider[_AbstractProvider__E], typing.Generic[_AbstractProvider__E]):
    """
    Java class 'org.openhab.core.common.registry.AbstractProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.common.registry.Provider
    
      Constructors:
        * AbstractProvider()
    
    """
    def __init__(self): ...
    def addProviderChangeListener(self, listener: ProviderChangeListener[_AbstractProvider__E]) -> None: ...
    def removeProviderChangeListener(self, listener: ProviderChangeListener[_AbstractProvider__E]) -> None: ...

_AbstractRegistry__E = typing.TypeVar('_AbstractRegistry__E', bound=Identifiable)  # <E>
_AbstractRegistry__K = typing.TypeVar('_AbstractRegistry__K')  # <K>
_AbstractRegistry__P = typing.TypeVar('_AbstractRegistry__P', bound=Provider)  # <P>
class AbstractRegistry(ProviderChangeListener[_AbstractRegistry__E], Registry[_AbstractRegistry__E, _AbstractRegistry__K], typing.Generic[_AbstractRegistry__E, _AbstractRegistry__K, _AbstractRegistry__P]):
    """
    Java class 'org.openhab.core.common.registry.AbstractRegistry'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.common.registry.ProviderChangeListener,
            org.openhab.core.common.registry.Registry
    
    """
    def add(self, element: _AbstractRegistry__E) -> _AbstractRegistry__E: ...
    def addRegistryChangeListener(self, listener: RegistryChangeListener[_AbstractRegistry__E]) -> None: ...
    @typing.overload
    def added(self, provider: Provider, object: typing.Any) -> None: ...
    @typing.overload
    def added(self, provider: Provider[_AbstractRegistry__E], element: _AbstractRegistry__E) -> None: ...
    def get(self, key: _AbstractRegistry__K) -> _AbstractRegistry__E: ...
    def getAll(self) -> java.util.Collection[_AbstractRegistry__E]: ...
    def getProvider(self, element: _AbstractRegistry__E) -> Provider[_AbstractRegistry__E]: ...
    def remove(self, key: _AbstractRegistry__K) -> _AbstractRegistry__E: ...
    def removeRegistryChangeListener(self, listener: RegistryChangeListener[_AbstractRegistry__E]) -> None: ...
    @typing.overload
    def removed(self, provider: Provider, object: typing.Any) -> None: ...
    @typing.overload
    def removed(self, provider: Provider[_AbstractRegistry__E], element: _AbstractRegistry__E) -> None: ...
    def stream(self) -> java.util.stream.Stream[_AbstractRegistry__E]: ...
    def update(self, element: _AbstractRegistry__E) -> _AbstractRegistry__E: ...
    @typing.overload
    def updated(self, provider: Provider, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def updated(self, provider: Provider[_AbstractRegistry__E], oldElement: _AbstractRegistry__E, element: _AbstractRegistry__E) -> None: ...
    def waitForCompletedAsyncActivationTasks(self) -> None: ...

_ManagedProvider__E = typing.TypeVar('_ManagedProvider__E', bound=Identifiable)  # <E>
_ManagedProvider__K = typing.TypeVar('_ManagedProvider__K')  # <K>
class ManagedProvider(Provider[_ManagedProvider__E], typing.Generic[_ManagedProvider__E, _ManagedProvider__K]):
    """
    Java class 'org.openhab.core.common.registry.ManagedProvider'
    
        Interfaces:
            org.openhab.core.common.registry.Provider
    
    """
    def add(self, element: _ManagedProvider__E) -> None: ...
    def get(self, key: _ManagedProvider__K) -> _ManagedProvider__E: ...
    def remove(self, key: _ManagedProvider__K) -> _ManagedProvider__E: ...
    def update(self, element: _ManagedProvider__E) -> _ManagedProvider__E: ...

_AbstractManagedProvider__E = typing.TypeVar('_AbstractManagedProvider__E', bound=Identifiable)  # <E>
_AbstractManagedProvider__K = typing.TypeVar('_AbstractManagedProvider__K')  # <K>
_AbstractManagedProvider__PE = typing.TypeVar('_AbstractManagedProvider__PE')  # <PE>
class AbstractManagedProvider(AbstractProvider[_AbstractManagedProvider__E], ManagedProvider[_AbstractManagedProvider__E, _AbstractManagedProvider__K], typing.Generic[_AbstractManagedProvider__E, _AbstractManagedProvider__K, _AbstractManagedProvider__PE]):
    """
    Java class 'org.openhab.core.common.registry.AbstractManagedProvider'
    
        Extends:
            org.openhab.core.common.registry.AbstractProvider
    
        Interfaces:
            org.openhab.core.common.registry.ManagedProvider
    
      Constructors:
        * AbstractManagedProvider(org.openhab.core.storage.StorageService)
    
    """
    def __init__(self, storageService: org.openhab.core.storage.StorageService): ...
    def add(self, element: _AbstractManagedProvider__E) -> None: ...
    def get(self, key: _AbstractManagedProvider__K) -> _AbstractManagedProvider__E: ...
    def getAll(self) -> java.util.Collection[_AbstractManagedProvider__E]: ...
    def remove(self, key: _AbstractManagedProvider__K) -> _AbstractManagedProvider__E: ...
    def update(self, element: _AbstractManagedProvider__E) -> _AbstractManagedProvider__E: ...

_DefaultAbstractManagedProvider__E = typing.TypeVar('_DefaultAbstractManagedProvider__E', bound=Identifiable)  # <E>
_DefaultAbstractManagedProvider__K = typing.TypeVar('_DefaultAbstractManagedProvider__K')  # <K>
class DefaultAbstractManagedProvider(AbstractManagedProvider[_DefaultAbstractManagedProvider__E, _DefaultAbstractManagedProvider__K, _DefaultAbstractManagedProvider__E], typing.Generic[_DefaultAbstractManagedProvider__E, _DefaultAbstractManagedProvider__K]):
    """
    Java class 'org.openhab.core.common.registry.DefaultAbstractManagedProvider'
    
        Extends:
            org.openhab.core.common.registry.AbstractManagedProvider
    
      Constructors:
        * DefaultAbstractManagedProvider(org.openhab.core.storage.StorageService)
    
    """
    def __init__(self, storageService: org.openhab.core.storage.StorageService): ...
