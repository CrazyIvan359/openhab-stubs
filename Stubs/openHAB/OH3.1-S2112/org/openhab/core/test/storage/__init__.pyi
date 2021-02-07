import java.lang
import java.util
import org.openhab.core.storage
import typing


_VolatileStorage__T = typing.TypeVar('_VolatileStorage__T')  # <T>
class VolatileStorage(org.openhab.core.storage.Storage[_VolatileStorage__T], typing.Generic[_VolatileStorage__T]):
    """
    Java class 'org.openhab.core.test.storage.VolatileStorage'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.storage.Storage
    
      Constructors:
        * VolatileStorage()
    
    """
    def __init__(self): ...
    def containsKey(self, key: java.lang.String) -> bool: ...
    def get(self, key: java.lang.String) -> _VolatileStorage__T: ...
    def getKeys(self) -> java.util.Collection[java.lang.String]: ...
    def getValues(self) -> java.util.Collection[_VolatileStorage__T]: ...
    def put(self, key: java.lang.String, value: _VolatileStorage__T) -> _VolatileStorage__T: ...
    def remove(self, key: java.lang.String) -> _VolatileStorage__T: ...

class VolatileStorageService(org.openhab.core.storage.StorageService):
    """
    Java class 'org.openhab.core.test.storage.VolatileStorageService'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.storage.StorageService
    
      Constructors:
        * VolatileStorageService()
    
    """
    def __init__(self): ...
    _getStorage_0__T = typing.TypeVar('_getStorage_0__T')  # <T>
    @typing.overload
    def getStorage(self, name: java.lang.String, classLoader: java.lang.ClassLoader) -> org.openhab.core.storage.Storage[_getStorage_0__T]: ...
    _getStorage_1__T = typing.TypeVar('_getStorage_1__T')  # <T>
    @typing.overload
    def getStorage(self, name: java.lang.String) -> org.openhab.core.storage.Storage[_getStorage_1__T]: ...
