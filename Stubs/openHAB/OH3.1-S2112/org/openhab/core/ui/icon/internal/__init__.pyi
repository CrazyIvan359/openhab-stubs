import java.lang
import java.util
import javax.ws.rs.core
import org.openhab.core.i18n
import org.openhab.core.io.http.servlet
import org.openhab.core.io.rest
import org.openhab.core.ui.icon
import org.osgi.service.http
import typing


class CustomIconProvider(org.openhab.core.ui.icon.AbstractResourceIconProvider):
    """
    Java class 'org.openhab.core.ui.icon.internal.CustomIconProvider'
    
        Extends:
            org.openhab.core.ui.icon.AbstractResourceIconProvider
    
      Constructors:
        * CustomIconProvider(org.openhab.core.i18n.TranslationProvider)
    
    """
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    @typing.overload
    def getIconSets(self) -> java.util.Set[org.openhab.core.ui.icon.IconSet]: ...
    @typing.overload
    def getIconSets(self, locale: java.util.Locale) -> java.util.Set[org.openhab.core.ui.icon.IconSet]: ...

class IconServlet(org.openhab.core.io.http.servlet.OpenHABServlet):
    """
    Java class 'org.openhab.core.ui.icon.internal.IconServlet'
    
        Extends:
            org.openhab.core.io.http.servlet.OpenHABServlet
    
      Constructors:
        * IconServlet(org.osgi.service.http.HttpService, org.osgi.service.http.HttpContext)
    
    """
    def __init__(self, httpService: org.osgi.service.http.HttpService, httpContext: org.osgi.service.http.HttpContext): ...
    def addIconProvider(self, iconProvider: org.openhab.core.ui.icon.IconProvider) -> None: ...
    def removeIconProvider(self, iconProvider: org.openhab.core.ui.icon.IconProvider) -> None: ...

class IconSetResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.ui.icon.internal.IconSetResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * IconSetResource(org.openhab.core.io.rest.LocaleService)
    
      Attributes:
        PATH_ICONSETS (java.lang.String): final static field
    
    """
    PATH_ICONSETS: typing.ClassVar[java.lang.String] = ...
    def __init__(self, localeService: org.openhab.core.io.rest.LocaleService): ...
    def getAll(self, language: java.lang.String) -> javax.ws.rs.core.Response: ...
