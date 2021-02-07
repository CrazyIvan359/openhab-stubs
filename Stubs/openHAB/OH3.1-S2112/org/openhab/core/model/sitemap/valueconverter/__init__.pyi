import java.lang
import org.eclipse.xtext.common.services
import org.eclipse.xtext.conversion


class SitemapConverters(org.eclipse.xtext.common.services.DefaultTerminalConverters):
    """
    Java class 'org.openhab.core.model.sitemap.valueconverter.SitemapConverters'
    
        Extends:
            org.eclipse.xtext.common.services.DefaultTerminalConverters
    
      Constructors:
        * SitemapConverters()
    
    """
    def __init__(self): ...
    def Command(self) -> org.eclipse.xtext.conversion.IValueConverter[java.lang.String]: ...
    def Icon(self) -> org.eclipse.xtext.conversion.IValueConverter[java.lang.String]: ...
    @classmethod
    def containsWhiteSpace(cls, string: java.lang.String) -> bool: ...
