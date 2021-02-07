import java.lang
import java.util
import org.openhab.core.common.registry
import org.openhab.core.events
import org.openhab.core.i18n
import org.openhab.core.items
import org.openhab.core.items.dto
import org.openhab.core.items.events
import org.openhab.core.service
import org.openhab.core.storage
import org.openhab.core.types
import typing


class ExpireManager(org.openhab.core.events.EventSubscriber, org.openhab.core.common.registry.RegistryChangeListener[org.openhab.core.items.Item]):
    """
    Java class 'org.openhab.core.internal.items.ExpireManager'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.events.EventSubscriber,
            org.openhab.core.common.registry.RegistryChangeListener
    
      Constructors:
        * ExpireManager(java.util.Map, org.openhab.core.events.EventPublisher, org.openhab.core.items.MetadataRegistry, org.openhab.core.items.ItemRegistry)
    
    """
    def __init__(self, configuration: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]], eventPublisher: org.openhab.core.events.EventPublisher, metadataRegistry: org.openhab.core.items.MetadataRegistry, itemRegistry: org.openhab.core.items.ItemRegistry): ...
    @typing.overload
    def added(self, object: typing.Any) -> None: ...
    @typing.overload
    def added(self, item: org.openhab.core.items.Item) -> None: ...
    def getEventFilter(self) -> org.openhab.core.events.EventFilter: ...
    def getSubscribedEventTypes(self) -> java.util.Set[java.lang.String]: ...
    def receive(self, event: org.openhab.core.events.Event) -> None: ...
    @typing.overload
    def removed(self, object: typing.Any) -> None: ...
    @typing.overload
    def removed(self, item: org.openhab.core.items.Item) -> None: ...
    @typing.overload
    def updated(self, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def updated(self, oldItem: org.openhab.core.items.Item, item: org.openhab.core.items.Item) -> None: ...

class GroupFunctionHelper(java.lang.Object):
    """
    Java class 'org.openhab.core.internal.items.GroupFunctionHelper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * GroupFunctionHelper()
    
    """
    def __init__(self): ...
    def createGroupFunction(self, function: org.openhab.core.items.dto.GroupFunctionDTO, baseItem: org.openhab.core.items.Item) -> org.openhab.core.items.GroupFunction: ...

class ItemBuilderFactoryImpl(org.openhab.core.items.ItemBuilderFactory):
    """
    Java class 'org.openhab.core.internal.items.ItemBuilderFactoryImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.items.ItemBuilderFactory
    
      Constructors:
        * ItemBuilderFactoryImpl(org.openhab.core.items.ItemFactory)
    
    """
    def __init__(self, coreItemFactory: org.openhab.core.items.ItemFactory): ...
    @typing.overload
    def newItemBuilder(self, itemType: java.lang.String, itemName: java.lang.String) -> org.openhab.core.items.ItemBuilder: ...
    @typing.overload
    def newItemBuilder(self, item: org.openhab.core.items.Item) -> org.openhab.core.items.ItemBuilder: ...

class ItemBuilderImpl(org.openhab.core.items.ItemBuilder):
    """
    Java class 'org.openhab.core.internal.items.ItemBuilderImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.items.ItemBuilder
    
      Constructors:
        * ItemBuilderImpl(java.util.Set, org.openhab.core.items.Item)
        * ItemBuilderImpl(java.util.Set, java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, itemFactories: java.util.Set[org.openhab.core.items.ItemFactory], itemType: java.lang.String, itemName: java.lang.String): ...
    @typing.overload
    def __init__(self, itemFactories: java.util.Set[org.openhab.core.items.ItemFactory], item: org.openhab.core.items.Item): ...
    def build(self) -> org.openhab.core.items.Item: ...
    def withBaseItem(self, item: org.openhab.core.items.Item) -> org.openhab.core.items.ItemBuilder: ...
    def withCategory(self, category: java.lang.String) -> org.openhab.core.items.ItemBuilder: ...
    def withGroupFunction(self, function: org.openhab.core.items.GroupFunction) -> org.openhab.core.items.ItemBuilder: ...
    def withGroups(self, groups: typing.Union[java.util.Collection[java.lang.String], typing.Sequence[java.lang.String]]) -> org.openhab.core.items.ItemBuilder: ...
    def withLabel(self, label: java.lang.String) -> org.openhab.core.items.ItemBuilder: ...
    def withTags(self, tags: java.util.Set[java.lang.String]) -> org.openhab.core.items.ItemBuilder: ...

class ItemRegistryImpl(org.openhab.core.common.registry.AbstractRegistry[org.openhab.core.items.Item, java.lang.String, org.openhab.core.items.ItemProvider], org.openhab.core.items.ItemRegistry):
    """
    Java class 'org.openhab.core.internal.items.ItemRegistryImpl'
    
        Extends:
            org.openhab.core.common.registry.AbstractRegistry
    
        Interfaces:
            org.openhab.core.items.ItemRegistry
    
      Constructors:
        * ItemRegistryImpl(org.openhab.core.items.MetadataRegistry)
    
    """
    def __init__(self, metadataRegistry: org.openhab.core.items.MetadataRegistry): ...
    def addRegistryHook(self, hook: org.openhab.core.items.RegistryHook[org.openhab.core.items.Item]) -> None: ...
    @typing.overload
    def added(self, provider: org.openhab.core.common.registry.Provider, object: typing.Any) -> None: ...
    @typing.overload
    def added(self, provider: org.openhab.core.common.registry.Provider, identifiable: org.openhab.core.common.registry.Identifiable) -> None: ...
    @typing.overload
    def added(self, provider: org.openhab.core.common.registry.Provider[org.openhab.core.items.Item], element: org.openhab.core.items.Item) -> None: ...
    def getItem(self, name: java.lang.String) -> org.openhab.core.items.Item: ...
    def getItemByPattern(self, name: java.lang.String) -> org.openhab.core.items.Item: ...
    @typing.overload
    def getItems(self) -> java.util.Collection[org.openhab.core.items.Item]: ...
    @typing.overload
    def getItems(self, pattern: java.lang.String) -> java.util.Collection[org.openhab.core.items.Item]: ...
    _getItemsByTag_0__T = typing.TypeVar('_getItemsByTag_0__T', bound=org.openhab.core.items.Item)  # <T>
    @typing.overload
    def getItemsByTag(self, typeFilter: typing.Type[_getItemsByTag_0__T], tags: typing.List[java.lang.String]) -> java.util.Collection[_getItemsByTag_0__T]: ...
    @typing.overload
    def getItemsByTag(self, tags: typing.List[java.lang.String]) -> java.util.Collection[org.openhab.core.items.Item]: ...
    def getItemsByTagAndType(self, type: java.lang.String, tags: typing.List[java.lang.String]) -> java.util.Collection[org.openhab.core.items.Item]: ...
    def getItemsOfType(self, type: java.lang.String) -> java.util.Collection[org.openhab.core.items.Item]: ...
    @typing.overload
    def remove(self, key: typing.Any) -> org.openhab.core.common.registry.Identifiable: ...
    @typing.overload
    def remove(self, itemName: java.lang.String, recursive: bool) -> org.openhab.core.items.Item: ...
    def removeRegistryHook(self, hook: org.openhab.core.items.RegistryHook[org.openhab.core.items.Item]) -> None: ...
    @typing.overload
    def removed(self, provider: org.openhab.core.common.registry.Provider, object: typing.Any) -> None: ...
    @typing.overload
    def removed(self, provider: org.openhab.core.common.registry.Provider, identifiable: org.openhab.core.common.registry.Identifiable) -> None: ...
    @typing.overload
    def removed(self, provider: org.openhab.core.common.registry.Provider[org.openhab.core.items.Item], element: org.openhab.core.items.Item) -> None: ...
    def setCommandDescriptionService(self, commandDescriptionService: org.openhab.core.service.CommandDescriptionService) -> None: ...
    def unsetCommandDescriptionService(self, commandDescriptionService: org.openhab.core.service.CommandDescriptionService) -> None: ...

class ItemStateConverterImpl(org.openhab.core.items.ItemStateConverter):
    """
    Java class 'org.openhab.core.internal.items.ItemStateConverterImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.items.ItemStateConverter
    
      Constructors:
        * ItemStateConverterImpl(org.openhab.core.i18n.UnitProvider)
    
    """
    def __init__(self, unitProvider: org.openhab.core.i18n.UnitProvider): ...
    def convertToAcceptedState(self, state: org.openhab.core.types.State, item: org.openhab.core.items.Item) -> org.openhab.core.types.State: ...

class ItemUpdater(org.openhab.core.items.events.AbstractItemEventSubscriber):
    """
    Java class 'org.openhab.core.internal.items.ItemUpdater'
    
        Extends:
            org.openhab.core.items.events.AbstractItemEventSubscriber
    
      Constructors:
        * ItemUpdater(org.openhab.core.items.ItemRegistry)
    
    """
    def __init__(self, itemRegistry: org.openhab.core.items.ItemRegistry): ...

class ManagedMetadataProviderImpl(org.openhab.core.common.registry.AbstractManagedProvider[org.openhab.core.items.Metadata, org.openhab.core.items.MetadataKey, org.openhab.core.items.Metadata], org.openhab.core.items.ManagedMetadataProvider):
    """
    Java class 'org.openhab.core.internal.items.ManagedMetadataProviderImpl'
    
        Extends:
            org.openhab.core.common.registry.AbstractManagedProvider
    
        Interfaces:
            org.openhab.core.items.ManagedMetadataProvider
    
      Constructors:
        * ManagedMetadataProviderImpl(org.openhab.core.storage.StorageService)
    
    """
    def __init__(self, storageService: org.openhab.core.storage.StorageService): ...
    def removeItemMetadata(self, name: java.lang.String) -> None: ...

class MetadataCommandDescriptionProvider(org.openhab.core.types.CommandDescriptionProvider):
    """
    Java class 'org.openhab.core.internal.items.MetadataCommandDescriptionProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.types.CommandDescriptionProvider
    
      Constructors:
        * MetadataCommandDescriptionProvider(org.openhab.core.items.MetadataRegistry, java.util.Map)
    
      Attributes:
        COMMANDDESCRIPTION_METADATA_NAMESPACE (java.lang.String): final static field
    
    """
    COMMANDDESCRIPTION_METADATA_NAMESPACE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, metadataRegistry: org.openhab.core.items.MetadataRegistry, properties: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]): ...
    def getCommandDescription(self, itemName: java.lang.String, locale: java.util.Locale) -> org.openhab.core.types.CommandDescription: ...

class MetadataRegistryImpl(org.openhab.core.common.registry.AbstractRegistry[org.openhab.core.items.Metadata, org.openhab.core.items.MetadataKey, org.openhab.core.items.MetadataProvider], org.openhab.core.items.MetadataRegistry):
    """
    Java class 'org.openhab.core.internal.items.MetadataRegistryImpl'
    
        Extends:
            org.openhab.core.common.registry.AbstractRegistry
    
        Interfaces:
            org.openhab.core.items.MetadataRegistry
    
      Constructors:
        * MetadataRegistryImpl()
    
    """
    def __init__(self): ...
    def isInternalNamespace(self, namespace: java.lang.String) -> bool: ...
    def removeItemMetadata(self, itemName: java.lang.String) -> None: ...

class MetadataStateDescriptionFragmentProvider(org.openhab.core.types.StateDescriptionFragmentProvider):
    """
    Java class 'org.openhab.core.internal.items.MetadataStateDescriptionFragmentProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.types.StateDescriptionFragmentProvider
    
      Constructors:
        * MetadataStateDescriptionFragmentProvider(org.openhab.core.items.MetadataRegistry, java.util.Map)
    
      Attributes:
        STATEDESCRIPTION_METADATA_NAMESPACE (java.lang.String): final static field
    
    """
    STATEDESCRIPTION_METADATA_NAMESPACE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, metadataRegistry: org.openhab.core.items.MetadataRegistry, properties: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]): ...
    def getRank(self) -> int: ...
    def getStateDescriptionFragment(self, itemName: java.lang.String, locale: java.util.Locale) -> org.openhab.core.types.StateDescriptionFragment: ...
