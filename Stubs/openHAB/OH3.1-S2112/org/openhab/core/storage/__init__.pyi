import java.lang
import java.util
import java.util.stream
import typing


_Storage__T = typing.TypeVar('_Storage__T')  # <T>
class Storage(java.lang.Object, typing.Generic[_Storage__T]):
    """
    @NonNullByDefault public interface Storage<T>
    
        A :class:`~org.openhab.core.storage.Storage` is the generic way to store key-value pairs in OHC. Each storage
        implementation can store its data differently, e.g in-memory or in-database.
    
    
    """
    def containsKey(self, key: java.lang.String) -> bool: ...
    def get(self, key: java.lang.String) -> _Storage__T: ...
    def getKeys(self) -> java.util.Collection[java.lang.String]: ...
    def getValues(self) -> java.util.Collection[_Storage__T]: ...
    def put(self, key: java.lang.String, value: _Storage__T) -> _Storage__T: ...
    def remove(self, key: java.lang.String) -> _Storage__T: ...
    def stream(self) -> java.util.stream.Stream[java.util.Map.Entry[java.lang.String, _Storage__T]]: ...

class StorageService(java.lang.Object):
    """
    @NonNullByDefault public interface StorageService
    
        The :class:`~org.openhab.core.storage.StorageService` provides instances of :class:`~org.openhab.core.storage.Storage`s
        which are meant as a means for generic storage of key-value pairs. You can think of different
        :class:`~org.openhab.core.storage.StorageService`s that store these key-value pairs differently. One can think of e.g
        in-memory or in-database :class:`~org.openhab.core.storage.Storage`s and many more. This
        :class:`~org.openhab.core.storage.StorageService` decides which kind of :class:`~org.openhab.core.storage.Storage` is
        returned on request. It is meant to be injected into service consumers with the need for storing generic key-value pairs
        like the ManagedXXXProviders.
    
    
    """
    _getStorage_0__T = typing.TypeVar('_getStorage_0__T')  # <T>
    @typing.overload
    def getStorage(self, name: java.lang.String) -> Storage[_getStorage_0__T]: ...
    _getStorage_1__T = typing.TypeVar('_getStorage_1__T')  # <T>
    @typing.overload
    def getStorage(self, name: java.lang.String, classLoader: java.lang.ClassLoader) -> Storage[_getStorage_1__T]: ...

_DeletableStorage__T = typing.TypeVar('_DeletableStorage__T')  # <T>
class DeletableStorage(Storage[_DeletableStorage__T], typing.Generic[_DeletableStorage__T]):
    """
    Java class 'org.openhab.core.storage.DeletableStorage'
    
        Interfaces:
            org.openhab.core.storage.Storage
    
    """
    def delete(self) -> None: ...

class DeletableStorageService(StorageService):
    """
    Java class 'org.openhab.core.storage.DeletableStorageService'
    
        Interfaces:
            org.openhab.core.storage.StorageService
    
    """
    _getStorage_0__T = typing.TypeVar('_getStorage_0__T')  # <T>
    @typing.overload
    def getStorage(self, name: java.lang.String) -> DeletableStorage[_getStorage_0__T]: ...
    _getStorage_1__T = typing.TypeVar('_getStorage_1__T')  # <T>
    @typing.overload
    def getStorage(self, name: java.lang.String, classLoader: java.lang.ClassLoader) -> DeletableStorage[_getStorage_1__T]: ...
    @typing.overload
    def getStorage(self, string: java.lang.String) -> Storage: ...
    @typing.overload
    def getStorage(self, string: java.lang.String, classLoader: java.lang.ClassLoader) -> Storage: ...
