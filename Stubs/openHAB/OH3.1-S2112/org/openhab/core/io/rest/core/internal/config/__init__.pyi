import java.lang
import javax.ws.rs.core
import org.openhab.core.config.core
import org.openhab.core.io.rest
import typing


class ConfigDescriptionResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.core.internal.config.ConfigDescriptionResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * ConfigDescriptionResource(org.openhab.core.config.core.ConfigDescriptionRegistry, org.openhab.core.io.rest.LocaleService)
    
      Attributes:
        PATH_CONFIG_DESCRIPTIONS (java.lang.String): final static field
    
    """
    PATH_CONFIG_DESCRIPTIONS: typing.ClassVar[java.lang.String] = ...
    def __init__(self, configDescriptionRegistry: org.openhab.core.config.core.ConfigDescriptionRegistry, localeService: org.openhab.core.io.rest.LocaleService): ...
    def getAll(self, language: java.lang.String, scheme: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getByURI(self, language: java.lang.String, uri: java.lang.String) -> javax.ws.rs.core.Response: ...
