import java.lang
import java.security
import java.util
import org
import org.osgi.framework
import typing


class Configuration(java.lang.Object):
    """
    Java class 'org.osgi.service.cm.Configuration'
    
    """
    def addAttributes(self, configurationAttributeArray: typing.List['Configuration.ConfigurationAttribute']) -> None: ...
    def delete(self) -> None: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAttributes(self) -> java.util.Set['Configuration.ConfigurationAttribute']: ...
    def getBundleLocation(self) -> java.lang.String: ...
    def getChangeCount(self) -> int: ...
    def getFactoryPid(self) -> java.lang.String: ...
    def getPid(self) -> java.lang.String: ...
    def getProcessedProperties(self, serviceReference: org.osgi.framework.ServiceReference[typing.Any]) -> java.util.Dictionary[java.lang.String, typing.Any]: ...
    def getProperties(self) -> java.util.Dictionary[java.lang.String, typing.Any]: ...
    def hashCode(self) -> int: ...
    def removeAttributes(self, configurationAttributeArray: typing.List['Configuration.ConfigurationAttribute']) -> None: ...
    def setBundleLocation(self, string: java.lang.String) -> None: ...
    @typing.overload
    def update(self) -> None: ...
    @typing.overload
    def update(self, dictionary: java.util.Dictionary[java.lang.String, typing.Any]) -> None: ...
    def updateIfDifferent(self, dictionary: java.util.Dictionary[java.lang.String, typing.Any]) -> bool: ...
    class ConfigurationAttribute(java.lang.Enum[org.osgi.service.cm.Configuration.ConfigurationAttribute]):
        """
        Java class 'org.osgi.service.cm.Configuration$ConfigurationAttribute'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            READ_ONLY (org.osgi.service.cm.Configuration$ConfigurationAttribute): final static enum constant
        
        """
        READ_ONLY: typing.ClassVar['Configuration.ConfigurationAttribute'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @typing.overload
        def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
        @classmethod
        @typing.overload
        def valueOf(cls, string: java.lang.String) -> 'Configuration.ConfigurationAttribute': ...
        @classmethod
        def values(cls) -> typing.List['Configuration.ConfigurationAttribute']: ...

class ConfigurationAdmin(java.lang.Object):
    """
    Java class 'org.osgi.service.cm.ConfigurationAdmin'
    
      Attributes:
        SERVICE_FACTORYPID (java.lang.String): final static field
        SERVICE_BUNDLELOCATION (java.lang.String): final static field
    
    """
    SERVICE_FACTORYPID: typing.ClassVar[java.lang.String] = ...
    SERVICE_BUNDLELOCATION: typing.ClassVar[java.lang.String] = ...
    @typing.overload
    def createFactoryConfiguration(self, string: java.lang.String) -> Configuration: ...
    @typing.overload
    def createFactoryConfiguration(self, string: java.lang.String, string2: java.lang.String) -> Configuration: ...
    @typing.overload
    def getConfiguration(self, string: java.lang.String) -> Configuration: ...
    @typing.overload
    def getConfiguration(self, string: java.lang.String, string2: java.lang.String) -> Configuration: ...
    @typing.overload
    def getFactoryConfiguration(self, string: java.lang.String, string2: java.lang.String) -> Configuration: ...
    @typing.overload
    def getFactoryConfiguration(self, string: java.lang.String, string2: java.lang.String, string3: java.lang.String) -> Configuration: ...
    def listConfigurations(self, string: java.lang.String) -> typing.List[Configuration]: ...

class ConfigurationConstants(java.lang.Object):
    """
    Java class 'org.osgi.service.cm.ConfigurationConstants'
    
        Extends:
            java.lang.Object
    
      Attributes:
        CONFIGURATION_ADMIN_IMPLEMENTATION (java.lang.String): final static field
        CONFIGURATION_ADMIN_SPECIFICATION_VERSION (java.lang.String): final static field
    
    """
    CONFIGURATION_ADMIN_IMPLEMENTATION: typing.ClassVar[java.lang.String] = ...
    CONFIGURATION_ADMIN_SPECIFICATION_VERSION: typing.ClassVar[java.lang.String] = ...

class ConfigurationEvent(java.lang.Object):
    """
    Java class 'org.osgi.service.cm.ConfigurationEvent'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConfigurationEvent(org.osgi.framework.ServiceReference, int, java.lang.String, java.lang.String)
    
      Attributes:
        CM_UPDATED (int): final static field
        CM_DELETED (int): final static field
        CM_LOCATION_CHANGED (int): final static field
    
    """
    CM_UPDATED: typing.ClassVar[int] = ...
    CM_DELETED: typing.ClassVar[int] = ...
    CM_LOCATION_CHANGED: typing.ClassVar[int] = ...
    def __init__(self, serviceReference: org.osgi.framework.ServiceReference[ConfigurationAdmin], int: int, string: java.lang.String, string2: java.lang.String): ...
    def getFactoryPid(self) -> java.lang.String: ...
    def getPid(self) -> java.lang.String: ...
    def getReference(self) -> org.osgi.framework.ServiceReference[ConfigurationAdmin]: ...
    def getType(self) -> int: ...

class ConfigurationException(java.lang.Exception):
    """
    Java class 'org.osgi.service.cm.ConfigurationException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * ConfigurationException(java.lang.String, java.lang.String)
        * ConfigurationException(java.lang.String, java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, string: java.lang.String, string2: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, string2: java.lang.String, throwable: java.lang.Throwable): ...
    def getCause(self) -> java.lang.Throwable: ...
    def getProperty(self) -> java.lang.String: ...
    def getReason(self) -> java.lang.String: ...
    def initCause(self, throwable: java.lang.Throwable) -> java.lang.Throwable: ...

class ConfigurationListener(java.lang.Object):
    """
    Java class 'org.osgi.service.cm.ConfigurationListener'
    
    """
    def configurationEvent(self, configurationEvent: ConfigurationEvent) -> None: ...

class ConfigurationPermission(java.security.BasicPermission):
    """
    Java class 'org.osgi.service.cm.ConfigurationPermission'
    
        Extends:
            java.security.BasicPermission
    
      Constructors:
        * ConfigurationPermission(java.lang.String, java.lang.String)
    
      Attributes:
        CONFIGURE (java.lang.String): final static field
        TARGET (java.lang.String): final static field
        ATTRIBUTE (java.lang.String): final static field
    
    """
    CONFIGURE: typing.ClassVar[java.lang.String] = ...
    TARGET: typing.ClassVar[java.lang.String] = ...
    ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, string: java.lang.String, string2: java.lang.String): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getActions(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def implies(self, permission: java.security.Permission) -> bool: ...
    def newPermissionCollection(self) -> java.security.PermissionCollection: ...

class ConfigurationPlugin(java.lang.Object):
    """
    Java class 'org.osgi.service.cm.ConfigurationPlugin'
    
      Attributes:
        CM_TARGET (java.lang.String): final static field
        CM_RANKING (java.lang.String): final static field
    
    """
    CM_TARGET: typing.ClassVar[java.lang.String] = ...
    CM_RANKING: typing.ClassVar[java.lang.String] = ...
    def modifyConfiguration(self, serviceReference: org.osgi.framework.ServiceReference[typing.Any], dictionary: java.util.Dictionary[java.lang.String, typing.Any]) -> None: ...

class ManagedService(java.lang.Object):
    """
    Java class 'org.osgi.service.cm.ManagedService'
    
    """
    def updated(self, dictionary: java.util.Dictionary[java.lang.String, typing.Any]) -> None: ...

class ManagedServiceFactory(java.lang.Object):
    """
    Java class 'org.osgi.service.cm.ManagedServiceFactory'
    
    """
    def deleted(self, string: java.lang.String) -> None: ...
    def getName(self) -> java.lang.String: ...
    def updated(self, string: java.lang.String, dictionary: java.util.Dictionary[java.lang.String, typing.Any]) -> None: ...

class ReadOnlyConfigurationException(java.lang.RuntimeException):
    """
    Java class 'org.osgi.service.cm.ReadOnlyConfigurationException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * ReadOnlyConfigurationException(java.lang.String)
    
    """
    def __init__(self, string: java.lang.String): ...

class SynchronousConfigurationListener(ConfigurationListener):
    """
    Java class 'org.osgi.service.cm.SynchronousConfigurationListener'
    
        Interfaces:
            org.osgi.service.cm.ConfigurationListener
    
    """
