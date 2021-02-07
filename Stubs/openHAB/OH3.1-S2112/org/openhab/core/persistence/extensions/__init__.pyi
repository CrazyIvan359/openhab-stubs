import java.lang
import java.time
import org.openhab.core.items
import org.openhab.core.library.types
import org.openhab.core.persistence
import typing


class PersistenceExtensions(java.lang.Object):
    """
    Java class 'org.openhab.core.persistence.extensions.PersistenceExtensions'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PersistenceExtensions(org.openhab.core.persistence.PersistenceServiceRegistry)
    
    """
    def __init__(self, registry: org.openhab.core.persistence.PersistenceServiceRegistry): ...
    @classmethod
    @typing.overload
    def averageSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime) -> org.openhab.core.library.types.DecimalType: ...
    @classmethod
    @typing.overload
    def averageSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime, serviceId: java.lang.String) -> org.openhab.core.library.types.DecimalType: ...
    @classmethod
    @typing.overload
    def changedSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime) -> bool: ...
    @classmethod
    @typing.overload
    def changedSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime, serviceId: java.lang.String) -> bool: ...
    @classmethod
    @typing.overload
    def deltaSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime) -> org.openhab.core.library.types.DecimalType: ...
    @classmethod
    @typing.overload
    def deltaSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime, serviceId: java.lang.String) -> org.openhab.core.library.types.DecimalType: ...
    @classmethod
    @typing.overload
    def deviationSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime) -> org.openhab.core.library.types.DecimalType: ...
    @classmethod
    @typing.overload
    def deviationSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime, serviceId: java.lang.String) -> org.openhab.core.library.types.DecimalType: ...
    @classmethod
    @typing.overload
    def evolutionRate(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime) -> org.openhab.core.library.types.DecimalType: ...
    @classmethod
    @typing.overload
    def evolutionRate(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime, serviceId: java.lang.String) -> org.openhab.core.library.types.DecimalType: ...
    @classmethod
    @typing.overload
    def historicState(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime) -> org.openhab.core.persistence.HistoricItem: ...
    @classmethod
    @typing.overload
    def historicState(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime, serviceId: java.lang.String) -> org.openhab.core.persistence.HistoricItem: ...
    @classmethod
    @typing.overload
    def lastUpdate(cls, item: org.openhab.core.items.Item) -> java.time.ZonedDateTime: ...
    @classmethod
    @typing.overload
    def lastUpdate(cls, item: org.openhab.core.items.Item, serviceId: java.lang.String) -> java.time.ZonedDateTime: ...
    @classmethod
    @typing.overload
    def maximumSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime) -> org.openhab.core.persistence.HistoricItem: ...
    @classmethod
    @typing.overload
    def maximumSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime, serviceId: java.lang.String) -> org.openhab.core.persistence.HistoricItem: ...
    @classmethod
    @typing.overload
    def minimumSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime) -> org.openhab.core.persistence.HistoricItem: ...
    @classmethod
    @typing.overload
    def minimumSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime, serviceId: java.lang.String) -> org.openhab.core.persistence.HistoricItem: ...
    @classmethod
    @typing.overload
    def persist(cls, item: org.openhab.core.items.Item) -> None: ...
    @classmethod
    @typing.overload
    def persist(cls, item: org.openhab.core.items.Item, serviceId: java.lang.String) -> None: ...
    @classmethod
    @typing.overload
    def previousState(cls, item: org.openhab.core.items.Item) -> org.openhab.core.persistence.HistoricItem: ...
    @classmethod
    @typing.overload
    def previousState(cls, item: org.openhab.core.items.Item, skipEqual: bool) -> org.openhab.core.persistence.HistoricItem: ...
    @classmethod
    @typing.overload
    def previousState(cls, item: org.openhab.core.items.Item, skipEqual: bool, serviceId: java.lang.String) -> org.openhab.core.persistence.HistoricItem: ...
    @classmethod
    @typing.overload
    def sumSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime) -> org.openhab.core.library.types.DecimalType: ...
    @classmethod
    @typing.overload
    def sumSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime, serviceId: java.lang.String) -> org.openhab.core.library.types.DecimalType: ...
    @classmethod
    @typing.overload
    def updatedSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime) -> bool: ...
    @classmethod
    @typing.overload
    def updatedSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime, serviceId: java.lang.String) -> bool: ...
    @classmethod
    @typing.overload
    def varianceSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime) -> org.openhab.core.library.types.DecimalType: ...
    @classmethod
    @typing.overload
    def varianceSince(cls, item: org.openhab.core.items.Item, timestamp: java.time.ZonedDateTime, serviceId: java.lang.String) -> org.openhab.core.library.types.DecimalType: ...
