import java.lang
import java.util
import javax.ws.rs.core
import org.openhab.core.config.core
import org.openhab.core.io.rest
import org.openhab.core.io.rest.core.config
import org.openhab.core.io.rest.core.service
import org.osgi.framework
import typing


class ConfigurableServiceResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.core.internal.service.ConfigurableServiceResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * ConfigurableServiceResource(org.osgi.framework.BundleContext, org.openhab.core.io.rest.core.config.ConfigurationService, org.openhab.core.config.core.ConfigDescriptionRegistry)
    
      Attributes:
        PATH_SERVICES (java.lang.String): final static field
    
    """
    PATH_SERVICES: typing.ClassVar[java.lang.String] = ...
    def __init__(self, bundleContext: org.osgi.framework.BundleContext, configurationService: org.openhab.core.io.rest.core.config.ConfigurationService, configDescRegistry: org.openhab.core.config.core.ConfigDescriptionRegistry): ...
    def deleteConfiguration(self, serviceId: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getAll(self) -> java.util.List[org.openhab.core.io.rest.core.service.ConfigurableServiceDTO]: ...
    def getById(self, serviceId: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getConfiguration(self, serviceId: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getMultiConfigServicesByFactoryPid(self, serviceId: java.lang.String) -> java.util.List[org.openhab.core.io.rest.core.service.ConfigurableServiceDTO]: ...
    def updateConfiguration(self, serviceId: java.lang.String, configuration: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> javax.ws.rs.core.Response: ...
