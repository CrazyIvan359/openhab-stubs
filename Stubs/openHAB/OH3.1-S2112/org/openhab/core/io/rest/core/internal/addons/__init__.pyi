import java.lang
import javax.ws.rs.core
import org.openhab.core.events
import org.openhab.core.io.rest
import typing


class AddonResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.core.internal.addons.AddonResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * AddonResource(org.openhab.core.events.EventPublisher, org.openhab.core.io.rest.LocaleService)
    
      Attributes:
        PATH_ADDONS (java.lang.String): final static field
    
    """
    PATH_ADDONS: typing.ClassVar[java.lang.String] = ...
    def __init__(self, eventPublisher: org.openhab.core.events.EventPublisher, localeService: org.openhab.core.io.rest.LocaleService): ...
    def getAddon(self, language: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getById(self, language: java.lang.String, addonId: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getTypes(self, language: java.lang.String) -> javax.ws.rs.core.Response: ...
    def installAddon(self, addonId: java.lang.String) -> javax.ws.rs.core.Response: ...
    def installAddonByURL(self, url: java.lang.String) -> javax.ws.rs.core.Response: ...
    def uninstallAddon(self, addonId: java.lang.String) -> javax.ws.rs.core.Response: ...
