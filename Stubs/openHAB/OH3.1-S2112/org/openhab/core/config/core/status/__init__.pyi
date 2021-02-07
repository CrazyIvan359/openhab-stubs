import java.lang
import java.util
import org
import typing


class ConfigStatusCallback(java.lang.Object):
    """
    public interface ConfigStatusCallback
    
        The :class:`~org.openhab.core.config.core.status.ConfigStatusCallback` interface is a callback interface to propagate a
        new configuration status for an entity.
    
    
    """
    def configUpdated(self, configStatusSource: 'ConfigStatusSource') -> None: ...

class ConfigStatusInfo(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.status.ConfigStatusInfo'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConfigStatusInfo()
        * ConfigStatusInfo(java.util.Collection)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, configStatusMessages: typing.Union[java.util.Collection['ConfigStatusMessage'], typing.Sequence['ConfigStatusMessage']]): ...
    @typing.overload
    def add(self, configStatusMessages: typing.Union[java.util.Collection['ConfigStatusMessage'], typing.Sequence['ConfigStatusMessage']]) -> None: ...
    @typing.overload
    def add(self, configStatusMessage: 'ConfigStatusMessage') -> None: ...
    def equals(self, obj: typing.Any) -> bool: ...
    @typing.overload
    def getConfigStatusMessages(self) -> java.util.Collection['ConfigStatusMessage']: ...
    @typing.overload
    def getConfigStatusMessages(self, parameterNames: typing.List[java.lang.String]) -> java.util.Collection['ConfigStatusMessage']: ...
    @typing.overload
    def getConfigStatusMessages(self, types: typing.Union[java.util.Collection['ConfigStatusMessage.Type'], typing.Sequence['ConfigStatusMessage.Type']], parameterNames: typing.Union[java.util.Collection[java.lang.String], typing.Sequence[java.lang.String]]) -> java.util.Collection['ConfigStatusMessage']: ...
    @typing.overload
    def getConfigStatusMessages(self, types: typing.List['ConfigStatusMessage.Type']) -> java.util.Collection['ConfigStatusMessage']: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class ConfigStatusMessage(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.status.ConfigStatusMessage'
    
        Extends:
            java.lang.Object
    
      Attributes:
        parameterName (java.lang.String): final field
        type (org.openhab.core.config.core.status.ConfigStatusMessage$Type): final field
        message (java.lang.String): final field
        statusCode (java.lang.Integer): final field
    
    """
    parameterName: java.lang.String = ...
    type: 'ConfigStatusMessage.Type' = ...
    message: java.lang.String = ...
    statusCode: int = ...
    def equals(self, obj: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    class Builder(java.lang.Object):
        """
        Java class 'org.openhab.core.config.core.status.ConfigStatusMessage$Builder'
        
            Extends:
                java.lang.Object
        
        """
        def build(self) -> 'ConfigStatusMessage': ...
        @classmethod
        def error(cls, parameterName: java.lang.String) -> 'ConfigStatusMessage.Builder': ...
        @classmethod
        def information(cls, parameterName: java.lang.String) -> 'ConfigStatusMessage.Builder': ...
        @classmethod
        def pending(cls, parameterName: java.lang.String) -> 'ConfigStatusMessage.Builder': ...
        @classmethod
        def warning(cls, parameterName: java.lang.String) -> 'ConfigStatusMessage.Builder': ...
        def withArguments(self, arguments: typing.List[typing.Any]) -> 'ConfigStatusMessage.Builder': ...
        def withMessageKeySuffix(self, messageKeySuffix: java.lang.String) -> 'ConfigStatusMessage.Builder': ...
        def withStatusCode(self, statusCode: int) -> 'ConfigStatusMessage.Builder': ...
    class Type(java.lang.Enum[org.openhab.core.config.core.status.ConfigStatusMessage.Type]):
        """
        Java class 'org.openhab.core.config.core.status.ConfigStatusMessage$Type'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            INFORMATION (org.openhab.core.config.core.status.ConfigStatusMessage$Type): final static enum constant
            WARNING (org.openhab.core.config.core.status.ConfigStatusMessage$Type): final static enum constant
            ERROR (org.openhab.core.config.core.status.ConfigStatusMessage$Type): final static enum constant
            PENDING (org.openhab.core.config.core.status.ConfigStatusMessage$Type): final static enum constant
        
        """
        INFORMATION: typing.ClassVar['ConfigStatusMessage.Type'] = ...
        WARNING: typing.ClassVar['ConfigStatusMessage.Type'] = ...
        ERROR: typing.ClassVar['ConfigStatusMessage.Type'] = ...
        PENDING: typing.ClassVar['ConfigStatusMessage.Type'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @typing.overload
        def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
        @classmethod
        @typing.overload
        def valueOf(cls, name: java.lang.String) -> 'ConfigStatusMessage.Type': ...
        @classmethod
        def values(cls) -> typing.List['ConfigStatusMessage.Type']: ...

class ConfigStatusProvider(java.lang.Object):
    """
    @NonNullByDefault public interface ConfigStatusProvider
    
        The :class:`~org.openhab.core.config.core.status.ConfigStatusProvider` can be implemented and registered as an *OSGi*
        service to provide status information for :class:`~org.openhab.core.config.core.Configuration`s of entities. The
        :class:`~org.openhab.core.config.core.status.ConfigStatusService` tracks each
        :class:`~org.openhab.core.config.core.status.ConfigStatusProvider` and provides the corresponding
        :class:`~org.openhab.core.config.core.status.ConfigStatusInfo` by the operation
        :meth:`~org.openhab.core.config.core.status.ConfigStatusService.getConfigStatus`.
    
    
    """
    def getConfigStatus(self) -> java.util.Collection[ConfigStatusMessage]: ...
    def setConfigStatusCallback(self, configStatusCallback: ConfigStatusCallback) -> None: ...
    def supportsEntity(self, entityId: java.lang.String) -> bool: ...

class ConfigStatusSource(java.lang.Object):
    """
    Java class 'org.openhab.core.config.core.status.ConfigStatusSource'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConfigStatusSource(java.lang.String)
    
      Attributes:
        entityId (java.lang.String): final field
    
    """
    entityId: java.lang.String = ...
    def __init__(self, entityId: java.lang.String): ...
    def getTopic(self) -> java.lang.String: ...

class ConfigStatusService(ConfigStatusCallback):
    """
    Java class 'org.openhab.core.config.core.status.ConfigStatusService'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.core.status.ConfigStatusCallback
    
      Constructors:
        * ConfigStatusService()
    
    """
    def __init__(self): ...
    def configUpdated(self, configStatusSource: ConfigStatusSource) -> None: ...
    def getConfigStatus(self, entityId: java.lang.String, locale: java.util.Locale) -> ConfigStatusInfo: ...
