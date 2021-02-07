import java.lang
import java.time
import java.util
import org
import org.openhab.core.items
import org.openhab.core.persistence.config
import org.openhab.core.persistence.strategy
import org.openhab.core.types
import typing


class FilterCriteria(java.lang.Object):
    """
    Java class 'org.openhab.core.persistence.FilterCriteria'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * FilterCriteria()
    
    """
    def __init__(self): ...
    def getBeginDate(self) -> java.time.ZonedDateTime: ...
    def getEndDate(self) -> java.time.ZonedDateTime: ...
    def getItemName(self) -> java.lang.String: ...
    def getOperator(self) -> 'FilterCriteria.Operator': ...
    def getOrdering(self) -> 'FilterCriteria.Ordering': ...
    def getPageNumber(self) -> int: ...
    def getPageSize(self) -> int: ...
    def getState(self) -> org.openhab.core.types.State: ...
    def setBeginDate(self, beginDate: java.time.ZonedDateTime) -> 'FilterCriteria': ...
    def setEndDate(self, endDate: java.time.ZonedDateTime) -> 'FilterCriteria': ...
    def setItemName(self, itemName: java.lang.String) -> 'FilterCriteria': ...
    def setOperator(self, operator: 'FilterCriteria.Operator') -> 'FilterCriteria': ...
    def setOrdering(self, ordering: 'FilterCriteria.Ordering') -> 'FilterCriteria': ...
    def setPageNumber(self, pageNumber: int) -> 'FilterCriteria': ...
    def setPageSize(self, pageSize: int) -> 'FilterCriteria': ...
    def setState(self, state: org.openhab.core.types.State) -> 'FilterCriteria': ...
    class Operator(java.lang.Enum[org.openhab.core.persistence.FilterCriteria.Operator]):
        """
        Java class 'org.openhab.core.persistence.FilterCriteria$Operator'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            EQ (org.openhab.core.persistence.FilterCriteria$Operator): final static enum constant
            NEQ (org.openhab.core.persistence.FilterCriteria$Operator): final static enum constant
            GT (org.openhab.core.persistence.FilterCriteria$Operator): final static enum constant
            LT (org.openhab.core.persistence.FilterCriteria$Operator): final static enum constant
            GTE (org.openhab.core.persistence.FilterCriteria$Operator): final static enum constant
            LTE (org.openhab.core.persistence.FilterCriteria$Operator): final static enum constant
        
        """
        EQ: typing.ClassVar['FilterCriteria.Operator'] = ...
        NEQ: typing.ClassVar['FilterCriteria.Operator'] = ...
        GT: typing.ClassVar['FilterCriteria.Operator'] = ...
        LT: typing.ClassVar['FilterCriteria.Operator'] = ...
        GTE: typing.ClassVar['FilterCriteria.Operator'] = ...
        LTE: typing.ClassVar['FilterCriteria.Operator'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @typing.overload
        def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
        @classmethod
        @typing.overload
        def valueOf(cls, name: java.lang.String) -> 'FilterCriteria.Operator': ...
        @classmethod
        def values(cls) -> typing.List['FilterCriteria.Operator']: ...
    class Ordering(java.lang.Enum[org.openhab.core.persistence.FilterCriteria.Ordering]):
        """
        Java class 'org.openhab.core.persistence.FilterCriteria$Ordering'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            ASCENDING (org.openhab.core.persistence.FilterCriteria$Ordering): final static enum constant
            DESCENDING (org.openhab.core.persistence.FilterCriteria$Ordering): final static enum constant
        
        """
        ASCENDING: typing.ClassVar['FilterCriteria.Ordering'] = ...
        DESCENDING: typing.ClassVar['FilterCriteria.Ordering'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @typing.overload
        def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
        @classmethod
        @typing.overload
        def valueOf(cls, name: java.lang.String) -> 'FilterCriteria.Ordering': ...
        @classmethod
        def values(cls) -> typing.List['FilterCriteria.Ordering']: ...

class HistoricItem(java.lang.Object):
    """
    @NonNullByDefault public interface HistoricItem
    
        This interface is used by persistence services to represent an item with a certain state at a given point in time.
    
        Note that this interface does not extend :code:`Item` as the persistence services could not provide an implementation
        that correctly implement getAcceptedXTypes() and getGroupNames().
    
    
    """
    def getName(self) -> java.lang.String: ...
    def getState(self) -> org.openhab.core.types.State: ...
    def getTimestamp(self) -> java.time.ZonedDateTime: ...

class PersistenceFilter(java.lang.Object):
    """
    Java class 'org.openhab.core.persistence.PersistenceFilter'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PersistenceFilter()
    
    """
    def __init__(self): ...

class PersistenceItemConfiguration(java.lang.Object):
    """
    Java class 'org.openhab.core.persistence.PersistenceItemConfiguration'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PersistenceItemConfiguration(java.util.List, java.lang.String, java.util.List, java.util.List)
    
    """
    def __init__(self, items: java.util.List[org.openhab.core.persistence.config.PersistenceConfig], alias: java.lang.String, strategies: java.util.List[org.openhab.core.persistence.strategy.PersistenceStrategy], filters: java.util.List[PersistenceFilter]): ...
    def getAlias(self) -> java.lang.String: ...
    def getFilters(self) -> java.util.List[PersistenceFilter]: ...
    def getItems(self) -> java.util.List[org.openhab.core.persistence.config.PersistenceConfig]: ...
    def getStrategies(self) -> java.util.List[org.openhab.core.persistence.strategy.PersistenceStrategy]: ...
    def toString(self) -> java.lang.String: ...

class PersistenceItemInfo(java.lang.Object):
    """
    @NonNullByDefault public interface PersistenceItemInfo
    
        This class provides information about an item that is stored in a persistence service. It is used to return information
        about the item to the system
    
    
    """
    def getCount(self) -> int: ...
    def getEarliest(self) -> java.util.Date: ...
    def getLatest(self) -> java.util.Date: ...
    def getName(self) -> java.lang.String: ...

class PersistenceManager(java.lang.Object):
    """
    @NonNullByDefault public interface PersistenceManager
    
        A persistence manager service which could be used to start event handling or supply configuration for persistence
        services.
    
    
    """
    def addConfig(self, dbId: java.lang.String, config: 'PersistenceServiceConfiguration') -> None: ...
    def removeConfig(self, dbId: java.lang.String) -> None: ...

class PersistenceService(java.lang.Object):
    """
    @NonNullByDefault public interface PersistenceService
    
        A persistence service which can be used to store data from openHAB. This must not necessarily be a local database, a
        persistence service can also be cloud-based or a simply data-export facility (e.g. for sending data to an IoT (Internet
        of Things) service.
    
    
    """
    def getDefaultStrategies(self) -> java.util.List[org.openhab.core.persistence.strategy.PersistenceStrategy]: ...
    def getId(self) -> java.lang.String: ...
    def getLabel(self, locale: java.util.Locale) -> java.lang.String: ...
    @typing.overload
    def store(self, item: org.openhab.core.items.Item) -> None: ...
    @typing.overload
    def store(self, item: org.openhab.core.items.Item, alias: java.lang.String) -> None: ...

class PersistenceServiceConfiguration(java.lang.Object):
    """
    Java class 'org.openhab.core.persistence.PersistenceServiceConfiguration'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PersistenceServiceConfiguration(java.util.Collection, java.util.Collection, java.util.Collection)
    
    """
    def __init__(self, configs: typing.Union[java.util.Collection[PersistenceItemConfiguration], typing.Sequence[PersistenceItemConfiguration]], defaults: typing.Union[java.util.Collection[org.openhab.core.persistence.strategy.PersistenceStrategy], typing.Sequence[org.openhab.core.persistence.strategy.PersistenceStrategy]], strategies: typing.Union[java.util.Collection[org.openhab.core.persistence.strategy.PersistenceStrategy], typing.Sequence[org.openhab.core.persistence.strategy.PersistenceStrategy]]): ...
    def getConfigs(self) -> java.util.List[PersistenceItemConfiguration]: ...
    def getDefaults(self) -> java.util.List[org.openhab.core.persistence.strategy.PersistenceStrategy]: ...
    def getStrategies(self) -> java.util.List[org.openhab.core.persistence.strategy.PersistenceStrategy]: ...

class PersistenceServiceRegistry(java.lang.Object):
    """
    @NonNullByDefault public interface PersistenceServiceRegistry
    
        This is the interface for a central service that provides access to
        :class:`~org.openhab.core.persistence.PersistenceService`s.
    
    
    """
    def get(self, serviceId: java.lang.String) -> PersistenceService: ...
    def getAll(self) -> java.util.Set[PersistenceService]: ...
    def getDefault(self) -> PersistenceService: ...
    def getDefaultId(self) -> java.lang.String: ...

class QueryablePersistenceService(PersistenceService):
    """
    Java class 'org.openhab.core.persistence.QueryablePersistenceService'
    
        Interfaces:
            org.openhab.core.persistence.PersistenceService
    
    """
    def getItemInfo(self) -> java.util.Set[PersistenceItemInfo]: ...
    def query(self, filter: FilterCriteria) -> java.lang.Iterable[HistoricItem]: ...

class ModifiablePersistenceService(QueryablePersistenceService):
    """
    Java class 'org.openhab.core.persistence.ModifiablePersistenceService'
    
        Interfaces:
            org.openhab.core.persistence.QueryablePersistenceService
    
    """
    def remove(self, filter: FilterCriteria) -> bool: ...
    @typing.overload
    def store(self, item: org.openhab.core.items.Item, date: java.util.Date, state: org.openhab.core.types.State) -> None: ...
    @typing.overload
    def store(self, item: org.openhab.core.items.Item) -> None: ...
    @typing.overload
    def store(self, item: org.openhab.core.items.Item, alias: java.lang.String) -> None: ...
