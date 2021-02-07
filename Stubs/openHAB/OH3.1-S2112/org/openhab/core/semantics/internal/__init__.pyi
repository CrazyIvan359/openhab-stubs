import java.lang
import java.util
import org.openhab.core.common.registry
import org.openhab.core.items
import org.openhab.core.semantics
import org.openhab.core.semantics.model
import typing


class SemanticsMetadataProvider(org.openhab.core.common.registry.AbstractProvider[org.openhab.core.items.Metadata], org.openhab.core.items.ItemRegistryChangeListener, org.openhab.core.items.MetadataProvider):
    """
    Java class 'org.openhab.core.semantics.internal.SemanticsMetadataProvider'
    
        Extends:
            org.openhab.core.common.registry.AbstractProvider
    
        Interfaces:
            org.openhab.core.items.ItemRegistryChangeListener,
            org.openhab.core.items.MetadataProvider
    
      Constructors:
        * SemanticsMetadataProvider(org.openhab.core.items.ItemRegistry)
    
      Attributes:
        NAMESPACE (java.lang.String): final static field
    
    """
    NAMESPACE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, itemRegistry: org.openhab.core.items.ItemRegistry): ...
    @typing.overload
    def added(self, object: typing.Any) -> None: ...
    @typing.overload
    def added(self, item: org.openhab.core.items.Item) -> None: ...
    def allItemsChanged(self, oldItemNames: typing.Union[java.util.Collection[java.lang.String], typing.Sequence[java.lang.String]]) -> None: ...
    def getAll(self) -> java.util.Collection[org.openhab.core.items.Metadata]: ...
    @typing.overload
    def removed(self, object: typing.Any) -> None: ...
    @typing.overload
    def removed(self, item: org.openhab.core.items.Item) -> None: ...
    @typing.overload
    def updated(self, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def updated(self, oldItem: org.openhab.core.items.Item, item: org.openhab.core.items.Item) -> None: ...

class SemanticsServiceImpl(org.openhab.core.semantics.SemanticsService):
    """
    Java class 'org.openhab.core.semantics.internal.SemanticsServiceImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.semantics.SemanticsService
    
      Constructors:
        * SemanticsServiceImpl(org.openhab.core.items.ItemRegistry, org.openhab.core.items.MetadataRegistry)
    
    """
    def __init__(self, itemRegistry: org.openhab.core.items.ItemRegistry, metadataRegistry: org.openhab.core.items.MetadataRegistry): ...
    @typing.overload
    def getItemsInLocation(self, locationType: typing.Type[org.openhab.core.semantics.model.Location]) -> java.util.Set[org.openhab.core.items.Item]: ...
    @typing.overload
    def getItemsInLocation(self, labelOrSynonym: java.lang.String, locale: java.util.Locale) -> java.util.Set[org.openhab.core.items.Item]: ...
