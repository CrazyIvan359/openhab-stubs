import java.lang
import java.time
import java.time.temporal
import java.util
import java.util.concurrent
import typing


class CronJob(java.lang.Object):
    """
    @NonNullByDefault public interface CronJob
    
        Runnable that can be passed data and can throw a checked exception.
    
    
    """
    CRON: typing.ClassVar[java.lang.String] = ...
    def run(self, data: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...

class CronScheduler(java.lang.Object):
    """
    Java class 'org.openhab.core.scheduler.CronScheduler'
    
    """
    @typing.overload
    def schedule(self, cronJob: CronJob, config: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]], cronExpression: java.lang.String) -> 'ScheduledCompletableFuture'[None]: ...
    @typing.overload
    def schedule(self, runnable: 'SchedulerRunnable', cronExpression: java.lang.String) -> 'ScheduledCompletableFuture'[None]: ...

class PeriodicScheduler(java.lang.Object):
    """
    @NonNullByDefault public interface PeriodicScheduler
    
        Scheduler that runs the same job at the given periods.
    
    
    """
    _schedule__T = typing.TypeVar('_schedule__T')  # <T>
    def schedule(self, runnable: 'SchedulerRunnable', delays: typing.List[java.time.Duration]) -> 'ScheduledCompletableFuture'[_schedule__T]: ...

_ScheduledCompletableFuture__T = typing.TypeVar('_ScheduledCompletableFuture__T')  # <T>
class ScheduledCompletableFuture(java.util.concurrent.ScheduledFuture[_ScheduledCompletableFuture__T], typing.Generic[_ScheduledCompletableFuture__T]):
    """
    Java class 'org.openhab.core.scheduler.ScheduledCompletableFuture'
    
        Interfaces:
            java.util.concurrent.ScheduledFuture
    
    """
    def getPromise(self) -> java.util.concurrent.CompletableFuture[_ScheduledCompletableFuture__T]: ...

class Scheduler(java.lang.Object):
    """
    @NonNullByDefault public interface Scheduler
    
        A Scheduler service provides timed semantics to CompletableFutures. A Scheduler can delay a CompletableFutures, it can
        resolve a CompletableFutures at a certain time, or it can provide a timeout to a CompletableFutures.
    
        This scheduler has a millisecond resolution.
    
    
    """
    @typing.overload
    def after(self, delay: java.time.Duration) -> ScheduledCompletableFuture[java.time.Instant]: ...
    _after_1__T = typing.TypeVar('_after_1__T')  # <T>
    @typing.overload
    def after(self, callable: typing.Union[java.util.concurrent.Callable[_after_1__T], typing.Callable[[], _after_1__T]], delay: java.time.Duration) -> ScheduledCompletableFuture[_after_1__T]: ...
    @typing.overload
    def at(self, instant: java.time.Instant) -> ScheduledCompletableFuture[java.time.Instant]: ...
    _at_1__T = typing.TypeVar('_at_1__T')  # <T>
    @typing.overload
    def at(self, callable: typing.Union[java.util.concurrent.Callable[_at_1__T], typing.Callable[[], _at_1__T]], instant: java.time.Instant) -> ScheduledCompletableFuture[_at_1__T]: ...
    @typing.overload
    def at(self, runnable: 'SchedulerRunnable', instant: java.time.Instant) -> ScheduledCompletableFuture[None]: ...
    _before__T = typing.TypeVar('_before__T')  # <T>
    def before(self, promise: java.util.concurrent.CompletableFuture[_before__T], timeout: java.time.Duration) -> ScheduledCompletableFuture[_before__T]: ...
    _schedule__T = typing.TypeVar('_schedule__T')  # <T>
    def schedule(self, callable: 'SchedulerRunnable', temporalAdjuster: java.time.temporal.TemporalAdjuster) -> ScheduledCompletableFuture[_schedule__T]: ...

class SchedulerRunnable(java.lang.Object):
    """
    public interface SchedulerRunnable
    
        Runnable that can throw checked exceptions.
    
    
    """
    def run(self) -> None: ...

class SchedulerTemporalAdjuster(java.time.temporal.TemporalAdjuster):
    """
    Java class 'org.openhab.core.scheduler.SchedulerTemporalAdjuster'
    
        Interfaces:
            java.time.temporal.TemporalAdjuster
    
    """
    def isDone(self, temporal: java.time.temporal.Temporal) -> bool: ...
