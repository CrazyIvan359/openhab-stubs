import java.lang
import java.util
import org.openhab.core.common.registry
import org.openhab.core.items
import org.openhab.core.model.core
import org.openhab.core.model.item
import org.openhab.core.types
import typing


class GenericItemProvider(org.openhab.core.common.registry.AbstractProvider[org.openhab.core.items.Item], org.openhab.core.model.core.ModelRepositoryChangeListener, org.openhab.core.items.ItemProvider, org.openhab.core.types.StateDescriptionFragmentProvider):
    """
    Java class 'org.openhab.core.model.item.internal.GenericItemProvider'
    
        Extends:
            org.openhab.core.common.registry.AbstractProvider
    
        Interfaces:
            org.openhab.core.model.core.ModelRepositoryChangeListener,
            org.openhab.core.items.ItemProvider,
            org.openhab.core.types.StateDescriptionFragmentProvider
    
      Constructors:
        * GenericItemProvider(org.openhab.core.model.core.ModelRepository, org.openhab.core.model.item.internal.GenericMetadataProvider, java.util.Map)
    
    """
    def __init__(self, modelRepository: org.openhab.core.model.core.ModelRepository, genericMetadataProvider: 'GenericMetadataProvider', properties: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]): ...
    def addBindingConfigReader(self, reader: org.openhab.core.model.item.BindingConfigReader) -> None: ...
    def addItemFactory(self, factory: org.openhab.core.items.ItemFactory) -> None: ...
    def getAll(self) -> java.util.Collection[org.openhab.core.items.Item]: ...
    def getRank(self) -> int: ...
    def getStateDescriptionFragment(self, itemName: java.lang.String, locale: java.util.Locale) -> org.openhab.core.types.StateDescriptionFragment: ...
    def modelChanged(self, modelName: java.lang.String, type: org.openhab.core.model.core.EventType) -> None: ...
    def removeBindingConfigReader(self, reader: org.openhab.core.model.item.BindingConfigReader) -> None: ...
    def removeItemFactory(self, factory: org.openhab.core.items.ItemFactory) -> None: ...

class GenericMetadataProvider(org.openhab.core.common.registry.AbstractProvider[org.openhab.core.items.Metadata], org.openhab.core.items.MetadataProvider):
    """
    Java class 'org.openhab.core.model.item.internal.GenericMetadataProvider'
    
        Extends:
            org.openhab.core.common.registry.AbstractProvider
    
        Interfaces:
            org.openhab.core.items.MetadataProvider
    
      Constructors:
        * GenericMetadataProvider()
    
    """
    def __init__(self): ...
    def addMetadata(self, bindingType: java.lang.String, itemName: java.lang.String, value: java.lang.String, configuration: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def getAll(self) -> java.util.Collection[org.openhab.core.items.Metadata]: ...
    def removeMetadata(self, itemName: java.lang.String) -> None: ...
