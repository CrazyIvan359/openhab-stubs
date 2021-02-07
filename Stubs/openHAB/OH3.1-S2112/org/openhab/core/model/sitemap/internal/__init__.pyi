import java.lang
import java.util
import org.openhab.core.model.core
import org.openhab.core.model.sitemap
import org.openhab.core.model.sitemap.sitemap


class SitemapProviderImpl(org.openhab.core.model.sitemap.SitemapProvider, org.openhab.core.model.core.ModelRepositoryChangeListener):
    """
    Java class 'org.openhab.core.model.sitemap.internal.SitemapProviderImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.sitemap.SitemapProvider,
            org.openhab.core.model.core.ModelRepositoryChangeListener
    
      Constructors:
        * SitemapProviderImpl(org.openhab.core.model.core.ModelRepository)
    
    """
    def __init__(self, modelRepo: org.openhab.core.model.core.ModelRepository): ...
    def addModelChangeListener(self, listener: org.openhab.core.model.core.ModelRepositoryChangeListener) -> None: ...
    def getSitemap(self, sitemapName: java.lang.String) -> org.openhab.core.model.sitemap.sitemap.Sitemap: ...
    def getSitemapNames(self) -> java.util.Set[java.lang.String]: ...
    def modelChanged(self, modelName: java.lang.String, type: org.openhab.core.model.core.EventType) -> None: ...
    def removeModelChangeListener(self, listener: org.openhab.core.model.core.ModelRepositoryChangeListener) -> None: ...
