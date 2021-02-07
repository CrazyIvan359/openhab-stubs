import java.lang
import java.time
import java.time.temporal
import java.util
import java.util.concurrent
import org.openhab.core.scheduler
import typing


class CronSchedulerImpl(org.openhab.core.scheduler.CronScheduler):
    """
    Java class 'org.openhab.core.internal.scheduler.CronSchedulerImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.scheduler.CronScheduler
    
      Constructors:
        * CronSchedulerImpl(org.openhab.core.scheduler.Scheduler)
    
    """
    def __init__(self, scheduler: org.openhab.core.scheduler.Scheduler): ...
    @typing.overload
    def schedule(self, job: org.openhab.core.scheduler.CronJob, config: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]], cronExpression: java.lang.String) -> org.openhab.core.scheduler.ScheduledCompletableFuture[None]: ...
    @typing.overload
    def schedule(self, runnable: org.openhab.core.scheduler.SchedulerRunnable, cronExpression: java.lang.String) -> org.openhab.core.scheduler.ScheduledCompletableFuture[None]: ...

class DelegatedSchedulerImpl(org.openhab.core.scheduler.Scheduler):
    """
    Java class 'org.openhab.core.internal.scheduler.DelegatedSchedulerImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.scheduler.Scheduler
    
      Constructors:
        * DelegatedSchedulerImpl(org.openhab.core.internal.scheduler.SchedulerImpl)
    
    """
    def __init__(self, scheduler: 'SchedulerImpl'): ...
    @typing.overload
    def after(self, delay: java.time.Duration) -> org.openhab.core.scheduler.ScheduledCompletableFuture[java.time.Instant]: ...
    _after_1__T = typing.TypeVar('_after_1__T')  # <T>
    @typing.overload
    def after(self, callable: typing.Union[java.util.concurrent.Callable[_after_1__T], typing.Callable[[], _after_1__T]], delay: java.time.Duration) -> org.openhab.core.scheduler.ScheduledCompletableFuture[_after_1__T]: ...
    @typing.overload
    def at(self, runnable: org.openhab.core.scheduler.SchedulerRunnable, instant: java.time.Instant) -> org.openhab.core.scheduler.ScheduledCompletableFuture[None]: ...
    @typing.overload
    def at(self, instant: java.time.Instant) -> org.openhab.core.scheduler.ScheduledCompletableFuture[java.time.Instant]: ...
    _at_2__T = typing.TypeVar('_at_2__T')  # <T>
    @typing.overload
    def at(self, callable: typing.Union[java.util.concurrent.Callable[_at_2__T], typing.Callable[[], _at_2__T]], instant: java.time.Instant) -> org.openhab.core.scheduler.ScheduledCompletableFuture[_at_2__T]: ...
    _before__T = typing.TypeVar('_before__T')  # <T>
    def before(self, promise: java.util.concurrent.CompletableFuture[_before__T], timeout: java.time.Duration) -> org.openhab.core.scheduler.ScheduledCompletableFuture[_before__T]: ...
    _schedule__T = typing.TypeVar('_schedule__T')  # <T>
    def schedule(self, runnable: org.openhab.core.scheduler.SchedulerRunnable, temporalAdjuster: java.time.temporal.TemporalAdjuster) -> org.openhab.core.scheduler.ScheduledCompletableFuture[_schedule__T]: ...

class PeriodicSchedulerImpl(org.openhab.core.scheduler.PeriodicScheduler):
    """
    Java class 'org.openhab.core.internal.scheduler.PeriodicSchedulerImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.scheduler.PeriodicScheduler
    
      Constructors:
        * PeriodicSchedulerImpl(org.openhab.core.scheduler.Scheduler)
    
    """
    def __init__(self, scheduler: org.openhab.core.scheduler.Scheduler): ...
    _schedule__T = typing.TypeVar('_schedule__T')  # <T>
    def schedule(self, runnable: org.openhab.core.scheduler.SchedulerRunnable, delays: typing.List[java.time.Duration]) -> org.openhab.core.scheduler.ScheduledCompletableFuture[_schedule__T]: ...

class SchedulerImpl(org.openhab.core.scheduler.Scheduler):
    """
    Java class 'org.openhab.core.internal.scheduler.SchedulerImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.scheduler.Scheduler
    
      Constructors:
        * SchedulerImpl()
    
    """
    def __init__(self): ...
    @typing.overload
    def after(self, duration: java.time.Duration) -> org.openhab.core.scheduler.ScheduledCompletableFuture[java.time.Instant]: ...
    _after_1__T = typing.TypeVar('_after_1__T')  # <T>
    @typing.overload
    def after(self, callable: typing.Union[java.util.concurrent.Callable[_after_1__T], typing.Callable[[], _after_1__T]], duration: java.time.Duration) -> org.openhab.core.scheduler.ScheduledCompletableFuture[_after_1__T]: ...
    @typing.overload
    def at(self, runnable: org.openhab.core.scheduler.SchedulerRunnable, instant: java.time.Instant) -> org.openhab.core.scheduler.ScheduledCompletableFuture[None]: ...
    @typing.overload
    def at(self, instant: java.time.Instant) -> org.openhab.core.scheduler.ScheduledCompletableFuture[java.time.Instant]: ...
    _at_2__T = typing.TypeVar('_at_2__T')  # <T>
    @typing.overload
    def at(self, callable: typing.Union[java.util.concurrent.Callable[_at_2__T], typing.Callable[[], _at_2__T]], instant: java.time.Instant) -> org.openhab.core.scheduler.ScheduledCompletableFuture[_at_2__T]: ...
    _before__T = typing.TypeVar('_before__T')  # <T>
    def before(self, promise: java.util.concurrent.CompletableFuture[_before__T], timeout: java.time.Duration) -> org.openhab.core.scheduler.ScheduledCompletableFuture[_before__T]: ...
    _schedule__T = typing.TypeVar('_schedule__T')  # <T>
    def schedule(self, runnable: org.openhab.core.scheduler.SchedulerRunnable, temporalAdjuster: java.time.temporal.TemporalAdjuster) -> org.openhab.core.scheduler.ScheduledCompletableFuture[_schedule__T]: ...
