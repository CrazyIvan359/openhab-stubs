import java.lang
import java.net
import java.util
import org.openhab.core.common
import org.openhab.core.config.core
import org.openhab.core.items
import org.openhab.core.persistence
import org.openhab.core.scheduler
import org.openhab.core.service
import org.openhab.core.types
import typing


class PersistItemsJob(org.openhab.core.scheduler.SchedulerRunnable):
    """
    Java class 'org.openhab.core.persistence.internal.PersistItemsJob'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.scheduler.SchedulerRunnable
    
      Constructors:
        * PersistItemsJob(org.openhab.core.persistence.internal.PersistenceManagerImpl, java.lang.String, java.lang.String)
    
    """
    def __init__(self, manager: 'PersistenceManagerImpl', dbId: java.lang.String, strategyName: java.lang.String): ...
    def run(self) -> None: ...

class PersistenceManagerImpl(org.openhab.core.items.ItemRegistryChangeListener, org.openhab.core.persistence.PersistenceManager, org.openhab.core.items.StateChangeListener, org.openhab.core.service.ReadyService.ReadyTracker):
    """
    Java class 'org.openhab.core.persistence.internal.PersistenceManagerImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.items.ItemRegistryChangeListener,
            org.openhab.core.persistence.PersistenceManager,
            org.openhab.core.items.StateChangeListener,
            org.openhab.core.service.ReadyService.ReadyTracker
    
      Constructors:
        * PersistenceManagerImpl(org.openhab.core.scheduler.CronScheduler, org.openhab.core.items.ItemRegistry, org.openhab.core.common.SafeCaller, org.openhab.core.service.ReadyService)
    
    """
    def __init__(self, scheduler: org.openhab.core.scheduler.CronScheduler, itemRegistry: org.openhab.core.items.ItemRegistry, safeCaller: org.openhab.core.common.SafeCaller, readyService: org.openhab.core.service.ReadyService): ...
    def addConfig(self, dbId: java.lang.String, config: org.openhab.core.persistence.PersistenceServiceConfiguration) -> None: ...
    @typing.overload
    def added(self, object: typing.Any) -> None: ...
    @typing.overload
    def added(self, item: org.openhab.core.items.Item) -> None: ...
    def allItemsChanged(self, oldItemNames: typing.Union[java.util.Collection[java.lang.String], typing.Sequence[java.lang.String]]) -> None: ...
    def onReadyMarkerAdded(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
    def onReadyMarkerRemoved(self, readyMarker: org.openhab.core.service.ReadyMarker) -> None: ...
    def removeConfig(self, dbId: java.lang.String) -> None: ...
    @typing.overload
    def removed(self, object: typing.Any) -> None: ...
    @typing.overload
    def removed(self, item: org.openhab.core.items.Item) -> None: ...
    def stateChanged(self, item: org.openhab.core.items.Item, oldState: org.openhab.core.types.State, newState: org.openhab.core.types.State) -> None: ...
    def stateUpdated(self, item: org.openhab.core.items.Item, state: org.openhab.core.types.State) -> None: ...
    @typing.overload
    def updated(self, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def updated(self, oldItem: org.openhab.core.items.Item, item: org.openhab.core.items.Item) -> None: ...

class PersistenceServiceRegistryImpl(org.openhab.core.config.core.ConfigOptionProvider, org.openhab.core.persistence.PersistenceServiceRegistry):
    """
    Java class 'org.openhab.core.persistence.internal.PersistenceServiceRegistryImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.core.ConfigOptionProvider,
            org.openhab.core.persistence.PersistenceServiceRegistry
    
      Constructors:
        * PersistenceServiceRegistryImpl()
    
    """
    def __init__(self): ...
    def addPersistenceService(self, persistenceService: org.openhab.core.persistence.PersistenceService) -> None: ...
    def get(self, serviceId: java.lang.String) -> org.openhab.core.persistence.PersistenceService: ...
    def getAll(self) -> java.util.Set[org.openhab.core.persistence.PersistenceService]: ...
    def getDefault(self) -> org.openhab.core.persistence.PersistenceService: ...
    def getDefaultId(self) -> java.lang.String: ...
    def getParameterOptions(self, uri: java.net.URI, param: java.lang.String, context: java.lang.String, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.config.core.ParameterOption]: ...
    def removePersistenceService(self, persistenceService: org.openhab.core.persistence.PersistenceService) -> None: ...
