import org.eclipse.xtext.validation
import org.openhab.core.model.sitemap.sitemap
import typing


class AbstractSitemapValidator(org.eclipse.xtext.validation.AbstractDeclarativeValidator):
    """
    Java class 'org.openhab.core.model.sitemap.validation.AbstractSitemapValidator'
    
        Extends:
            org.eclipse.xtext.validation.AbstractDeclarativeValidator
    
      Constructors:
        * AbstractSitemapValidator()
    
    """
    def __init__(self): ...

class SitemapValidator(AbstractSitemapValidator):
    """
    Java class 'org.openhab.core.model.sitemap.validation.SitemapValidator'
    
        Extends:
            org.openhab.core.model.sitemap.validation.AbstractSitemapValidator
    
      Constructors:
        * SitemapValidator()
    
    """
    def __init__(self): ...
    def checkFramesInFrame(self, frame: org.openhab.core.model.sitemap.sitemap.Frame) -> None: ...
    @typing.overload
    def checkFramesInWidgetList(self, widget: org.openhab.core.model.sitemap.sitemap.LinkableWidget) -> None: ...
    @typing.overload
    def checkFramesInWidgetList(self, sitemap: org.openhab.core.model.sitemap.sitemap.Sitemap) -> None: ...
    def checkSetpoints(self, sp: org.openhab.core.model.sitemap.sitemap.Setpoint) -> None: ...
