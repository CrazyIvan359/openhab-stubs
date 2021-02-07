import com.google.gson
import java.io
import java.lang
import java.lang.reflect
import java.util
import org.openhab.core.storage
import typing


_JsonStorage__T = typing.TypeVar('_JsonStorage__T')  # <T>
class JsonStorage(org.openhab.core.storage.Storage[_JsonStorage__T], typing.Generic[_JsonStorage__T]):
    """
    Java class 'org.openhab.core.storage.json.internal.JsonStorage'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.storage.Storage
    
      Constructors:
        * JsonStorage(java.io.File, java.lang.ClassLoader, int, int, int)
    
    """
    def __init__(self, file: java.io.File, classLoader: java.lang.ClassLoader, maxBackupFiles: int, writeDelay: int, maxDeferredPeriod: int): ...
    def containsKey(self, key: java.lang.String) -> bool: ...
    def deferredCommit(self) -> None: ...
    def flush(self) -> None: ...
    def get(self, key: java.lang.String) -> _JsonStorage__T: ...
    def getKeys(self) -> java.util.Collection[java.lang.String]: ...
    def getValues(self) -> java.util.Collection[_JsonStorage__T]: ...
    def put(self, key: java.lang.String, value: _JsonStorage__T) -> _JsonStorage__T: ...
    def remove(self, key: java.lang.String) -> _JsonStorage__T: ...

class JsonStorageService(org.openhab.core.storage.StorageService):
    """
    Java class 'org.openhab.core.storage.json.internal.JsonStorageService'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.storage.StorageService
    
      Constructors:
        * JsonStorageService()
    
    """
    def __init__(self): ...
    _getStorage_0__T = typing.TypeVar('_getStorage_0__T')  # <T>
    @typing.overload
    def getStorage(self, name: java.lang.String) -> org.openhab.core.storage.Storage[_getStorage_0__T]: ...
    _getStorage_1__T = typing.TypeVar('_getStorage_1__T')  # <T>
    @typing.overload
    def getStorage(self, name: java.lang.String, classLoader: java.lang.ClassLoader) -> org.openhab.core.storage.Storage[_getStorage_1__T]: ...

class StorageEntry(java.lang.Object):
    """
    Java class 'org.openhab.core.storage.json.internal.StorageEntry'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * StorageEntry(java.lang.String, java.lang.Object)
    
    """
    def __init__(self, entityClassName: java.lang.String, value: typing.Any): ...
    def getEntityClassName(self) -> java.lang.String: ...
    def getValue(self) -> typing.Any: ...

class StorageEntryMapDeserializer(com.google.gson.JsonDeserializer[java.util.Map[java.lang.String, StorageEntry]]):
    """
    Java class 'org.openhab.core.storage.json.internal.StorageEntryMapDeserializer'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            com.google.gson.JsonDeserializer
    
      Constructors:
        * StorageEntryMapDeserializer()
    
    """
    def __init__(self): ...
    @typing.overload
    def deserialize(self, jsonElement: com.google.gson.JsonElement, type: java.lang.reflect.Type, jsonDeserializationContext: com.google.gson.JsonDeserializationContext) -> typing.Any: ...
    @typing.overload
    def deserialize(self, json: com.google.gson.JsonElement, typeOfT: java.lang.reflect.Type, context: com.google.gson.JsonDeserializationContext) -> java.util.Map[java.lang.String, StorageEntry]: ...
