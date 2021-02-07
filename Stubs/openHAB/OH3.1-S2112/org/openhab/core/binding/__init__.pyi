import java.lang
import java.net
import java.util
import org.openhab.core.common.registry
import typing


class BindingInfo(org.openhab.core.common.registry.Identifiable[java.lang.String]):
    """
    Java class 'org.openhab.core.binding.BindingInfo'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.common.registry.Identifiable
    
      Constructors:
        * BindingInfo(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.net.URI)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
      Attributes:
        DEFAULT_SERVICE_ID_PREFIX (java.lang.String): final static field
    
    """
    DEFAULT_SERVICE_ID_PREFIX: typing.ClassVar[java.lang.String] = ...
    def __init__(self, id: java.lang.String, name: java.lang.String, description: java.lang.String, author: java.lang.String, serviceId: java.lang.String, configDescriptionURI: java.net.URI): ...
    def getAuthor(self) -> java.lang.String: ...
    def getConfigDescriptionURI(self) -> java.net.URI: ...
    def getDescription(self) -> java.lang.String: ...
    def getName(self) -> java.lang.String: ...
    def getServiceId(self) -> java.lang.String: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    @typing.overload
    def getUID(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class BindingInfoProvider(java.lang.Object):
    """
    @NonNullByDefault public interface BindingInfoProvider
    
        The :class:`~org.openhab.core.binding.BindingInfoProvider` is a service interface providing
        :class:`~org.openhab.core.binding.BindingInfo` objects. All registered
        :class:`~org.openhab.core.binding.BindingInfoProvider` services are tracked by the
        :class:`~org.openhab.core.binding.BindingInfoRegistry` and provided as one common collection.
    
        Also see:
            :class:`~org.openhab.core.binding.BindingInfoRegistry`
    
    
    """
    def getBindingInfo(self, id: java.lang.String, locale: java.util.Locale) -> BindingInfo: ...
    def getBindingInfos(self, locale: java.util.Locale) -> java.util.Set[BindingInfo]: ...

class BindingInfoRegistry(java.lang.Object):
    """
    Java class 'org.openhab.core.binding.BindingInfoRegistry'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * BindingInfoRegistry()
    
    """
    def __init__(self): ...
    @typing.overload
    def getBindingInfo(self, id: java.lang.String) -> BindingInfo: ...
    @typing.overload
    def getBindingInfo(self, id: java.lang.String, locale: java.util.Locale) -> BindingInfo: ...
    @typing.overload
    def getBindingInfos(self) -> java.util.Set[BindingInfo]: ...
    @typing.overload
    def getBindingInfos(self, locale: java.util.Locale) -> java.util.Set[BindingInfo]: ...
