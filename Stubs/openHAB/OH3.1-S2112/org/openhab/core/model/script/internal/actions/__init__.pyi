import java.time
import org.openhab.core.model.script.actions
import org.openhab.core.scheduler


class TimerImpl(org.openhab.core.model.script.actions.Timer):
    """
    Java class 'org.openhab.core.model.script.internal.actions.TimerImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.model.script.actions.Timer
    
      Constructors:
        * TimerImpl(org.openhab.core.scheduler.Scheduler, java.time.ZonedDateTime, org.openhab.core.scheduler.SchedulerRunnable)
    
    """
    def __init__(self, scheduler: org.openhab.core.scheduler.Scheduler, startTime: java.time.ZonedDateTime, runnable: org.openhab.core.scheduler.SchedulerRunnable): ...
    def cancel(self) -> bool: ...
    def hasTerminated(self) -> bool: ...
    def isActive(self) -> bool: ...
    def isRunning(self) -> bool: ...
    def reschedule(self, newTime: java.time.ZonedDateTime) -> bool: ...
