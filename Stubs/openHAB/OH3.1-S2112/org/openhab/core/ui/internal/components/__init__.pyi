import java.lang
import java.util
import org.openhab.core.common.registry
import org.openhab.core.model.core
import org.openhab.core.model.sitemap
import org.openhab.core.model.sitemap.sitemap
import org.openhab.core.storage
import org.openhab.core.ui.components
import typing


class UIComponentProvider(org.openhab.core.common.registry.AbstractProvider[org.openhab.core.ui.components.RootUIComponent], org.openhab.core.common.registry.ManagedProvider[org.openhab.core.ui.components.RootUIComponent, java.lang.String]):
    """
    Java class 'org.openhab.core.ui.internal.components.UIComponentProvider'
    
        Extends:
            org.openhab.core.common.registry.AbstractProvider
    
        Interfaces:
            org.openhab.core.common.registry.ManagedProvider
    
      Constructors:
        * UIComponentProvider(java.lang.String, org.openhab.core.storage.StorageService)
    
    """
    def __init__(self, namespace: java.lang.String, storageService: org.openhab.core.storage.StorageService): ...
    @typing.overload
    def add(self, identifiable: org.openhab.core.common.registry.Identifiable) -> None: ...
    @typing.overload
    def add(self, element: org.openhab.core.ui.components.RootUIComponent) -> None: ...
    @typing.overload
    def get(self, object: typing.Any) -> org.openhab.core.common.registry.Identifiable: ...
    @typing.overload
    def get(self, key: java.lang.String) -> org.openhab.core.ui.components.RootUIComponent: ...
    def getAll(self) -> java.util.Collection[org.openhab.core.ui.components.RootUIComponent]: ...
    @typing.overload
    def remove(self, object: typing.Any) -> org.openhab.core.common.registry.Identifiable: ...
    @typing.overload
    def remove(self, key: java.lang.String) -> org.openhab.core.ui.components.RootUIComponent: ...
    @typing.overload
    def update(self, identifiable: org.openhab.core.common.registry.Identifiable) -> org.openhab.core.common.registry.Identifiable: ...
    @typing.overload
    def update(self, element: org.openhab.core.ui.components.RootUIComponent) -> org.openhab.core.ui.components.RootUIComponent: ...

class UIComponentRegistryFactoryImpl(org.openhab.core.ui.components.UIComponentRegistryFactory):
    """
    Java class 'org.openhab.core.ui.internal.components.UIComponentRegistryFactoryImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.ui.components.UIComponentRegistryFactory
    
      Constructors:
        * UIComponentRegistryFactoryImpl()
    
    """
    def __init__(self): ...
    @typing.overload
    def getRegistry(self, string: java.lang.String) -> org.openhab.core.ui.components.UIComponentRegistry: ...
    @typing.overload
    def getRegistry(self, namespace: java.lang.String) -> 'UIComponentRegistryImpl': ...

class UIComponentRegistryImpl(org.openhab.core.common.registry.AbstractRegistry[org.openhab.core.ui.components.RootUIComponent, java.lang.String, UIComponentProvider], org.openhab.core.ui.components.UIComponentRegistry):
    """
    Java class 'org.openhab.core.ui.internal.components.UIComponentRegistryImpl'
    
        Extends:
            org.openhab.core.common.registry.AbstractRegistry
    
        Interfaces:
            org.openhab.core.ui.components.UIComponentRegistry
    
      Constructors:
        * UIComponentRegistryImpl(java.lang.String, org.openhab.core.storage.StorageService)
    
    """
    def __init__(self, namespace: java.lang.String, storageService: org.openhab.core.storage.StorageService): ...

class UIComponentSitemapProvider(org.openhab.core.model.sitemap.SitemapProvider, org.openhab.core.common.registry.RegistryChangeListener[org.openhab.core.ui.components.RootUIComponent]):
    """
    Java class 'org.openhab.core.ui.internal.components.UIComponentSitemapProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.sitemap.SitemapProvider,
            org.openhab.core.common.registry.RegistryChangeListener
    
      Constructors:
        * UIComponentSitemapProvider()
    
      Attributes:
        SITEMAP_NAMESPACE (java.lang.String): final static field
    
    """
    SITEMAP_NAMESPACE: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    def addModelChangeListener(self, listener: org.openhab.core.model.core.ModelRepositoryChangeListener) -> None: ...
    @typing.overload
    def added(self, object: typing.Any) -> None: ...
    @typing.overload
    def added(self, element: org.openhab.core.ui.components.RootUIComponent) -> None: ...
    def getSitemap(self, sitemapName: java.lang.String) -> org.openhab.core.model.sitemap.sitemap.Sitemap: ...
    def getSitemapNames(self) -> java.util.Set[java.lang.String]: ...
    def removeModelChangeListener(self, listener: org.openhab.core.model.core.ModelRepositoryChangeListener) -> None: ...
    @typing.overload
    def removed(self, object: typing.Any) -> None: ...
    @typing.overload
    def removed(self, element: org.openhab.core.ui.components.RootUIComponent) -> None: ...
    @typing.overload
    def updated(self, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def updated(self, oldElement: org.openhab.core.ui.components.RootUIComponent, element: org.openhab.core.ui.components.RootUIComponent) -> None: ...
