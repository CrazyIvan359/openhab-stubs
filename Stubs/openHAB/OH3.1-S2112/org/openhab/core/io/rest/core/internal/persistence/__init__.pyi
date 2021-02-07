import java.lang
import javax.ws.rs.core
import org.openhab.core.i18n
import org.openhab.core.io.rest
import org.openhab.core.items
import org.openhab.core.persistence
import typing


class PersistenceResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.core.internal.persistence.PersistenceResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * PersistenceResource(org.openhab.core.items.ItemRegistry, org.openhab.core.io.rest.LocaleService, org.openhab.core.persistence.PersistenceServiceRegistry, org.openhab.core.i18n.TimeZoneProvider)
    
      Attributes:
        PATH_PERSISTENCE (java.lang.String): final static field
    
    """
    PATH_PERSISTENCE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, itemRegistry: org.openhab.core.items.ItemRegistry, localeService: org.openhab.core.io.rest.LocaleService, persistenceServiceRegistry: org.openhab.core.persistence.PersistenceServiceRegistry, timeZoneProvider: org.openhab.core.i18n.TimeZoneProvider): ...
    def httpDeletePersistenceServiceItem(self, headers: javax.ws.rs.core.HttpHeaders, serviceId: java.lang.String, itemName: java.lang.String, startTime: java.lang.String, endTime: java.lang.String) -> javax.ws.rs.core.Response: ...
    def httpGetPersistenceItemData(self, headers: javax.ws.rs.core.HttpHeaders, serviceId: java.lang.String, itemName: java.lang.String, startTime: java.lang.String, endTime: java.lang.String, pageNumber: int, pageLength: int, boundary: bool) -> javax.ws.rs.core.Response: ...
    def httpGetPersistenceServiceItems(self, headers: javax.ws.rs.core.HttpHeaders, serviceId: java.lang.String) -> javax.ws.rs.core.Response: ...
    def httpGetPersistenceServices(self, headers: javax.ws.rs.core.HttpHeaders, language: java.lang.String) -> javax.ws.rs.core.Response: ...
    def httpPutPersistenceItemData(self, headers: javax.ws.rs.core.HttpHeaders, serviceId: java.lang.String, itemName: java.lang.String, time: java.lang.String, value: java.lang.String) -> javax.ws.rs.core.Response: ...
