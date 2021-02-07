import java.lang
import java.util
import javax.ws.rs.core
import org.openhab.core.binding
import org.openhab.core.config.core
import org.openhab.core.io.rest
import org.openhab.core.io.rest.core.config
import typing


class BindingResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.core.internal.binding.BindingResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * BindingResource(org.openhab.core.binding.BindingInfoRegistry, org.openhab.core.io.rest.core.config.ConfigurationService, org.openhab.core.config.core.ConfigDescriptionRegistry, org.openhab.core.io.rest.LocaleService)
    
      Attributes:
        PATH_BINDINGS (java.lang.String): final static field
    
    """
    PATH_BINDINGS: typing.ClassVar[java.lang.String] = ...
    def __init__(self, bindingInfoRegistry: org.openhab.core.binding.BindingInfoRegistry, configurationService: org.openhab.core.io.rest.core.config.ConfigurationService, configDescRegistry: org.openhab.core.config.core.ConfigDescriptionRegistry, localeService: org.openhab.core.io.rest.LocaleService): ...
    def getAll(self, language: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getConfiguration(self, bindingId: java.lang.String) -> javax.ws.rs.core.Response: ...
    def updateConfiguration(self, bindingId: java.lang.String, configuration: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> javax.ws.rs.core.Response: ...
