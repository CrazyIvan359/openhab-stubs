import java.lang
import org.openhab.core.model.core


class SitemapRuntimeActivator(org.openhab.core.model.core.ModelParser):
    """
    Java class 'org.openhab.core.model.sitemap.runtime.internal.SitemapRuntimeActivator'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.core.ModelParser
    
      Constructors:
        * SitemapRuntimeActivator()
    
    """
    def __init__(self): ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def getExtension(self) -> java.lang.String: ...
