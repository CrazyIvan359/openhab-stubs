import java.lang
import java.security
import java.util
import org.osgi.framework
import typing


class Coordination(java.lang.Object):
    """
    Java class 'org.osgi.service.coordinator.Coordination'
    
      Attributes:
        TIMEOUT (java.lang.Exception): final static field
        RELEASED (java.lang.Exception): final static field
        ORPHANED (java.lang.Exception): final static field
    
    """
    TIMEOUT: typing.ClassVar[java.lang.Exception] = ...
    RELEASED: typing.ClassVar[java.lang.Exception] = ...
    ORPHANED: typing.ClassVar[java.lang.Exception] = ...
    def addParticipant(self, participant: 'Participant') -> None: ...
    def end(self) -> None: ...
    def extendTimeout(self, long: int) -> int: ...
    def fail(self, throwable: java.lang.Throwable) -> bool: ...
    def getBundle(self) -> org.osgi.framework.Bundle: ...
    def getEnclosingCoordination(self) -> 'Coordination': ...
    def getFailure(self) -> java.lang.Throwable: ...
    def getId(self) -> int: ...
    def getName(self) -> java.lang.String: ...
    def getParticipants(self) -> java.util.List['Participant']: ...
    def getThread(self) -> java.lang.Thread: ...
    def getVariables(self) -> java.util.Map[typing.Type[typing.Any], typing.Any]: ...
    def isTerminated(self) -> bool: ...
    def join(self, long: int) -> None: ...
    def push(self) -> 'Coordination': ...

class CoordinationException(java.lang.RuntimeException):
    """
    Java class 'org.osgi.service.coordinator.CoordinationException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * CoordinationException(java.lang.String, org.osgi.service.coordinator.Coordination, int, java.lang.Throwable)
        * CoordinationException(java.lang.String, org.osgi.service.coordinator.Coordination, int)
    
      Attributes:
        UNKNOWN (int): final static field
        DEADLOCK_DETECTED (int): final static field
        FAILED (int): final static field
        PARTIALLY_ENDED (int): final static field
        ALREADY_ENDED (int): final static field
        ALREADY_PUSHED (int): final static field
        LOCK_INTERRUPTED (int): final static field
        WRONG_THREAD (int): final static field
    
    """
    UNKNOWN: typing.ClassVar[int] = ...
    DEADLOCK_DETECTED: typing.ClassVar[int] = ...
    FAILED: typing.ClassVar[int] = ...
    PARTIALLY_ENDED: typing.ClassVar[int] = ...
    ALREADY_ENDED: typing.ClassVar[int] = ...
    ALREADY_PUSHED: typing.ClassVar[int] = ...
    LOCK_INTERRUPTED: typing.ClassVar[int] = ...
    WRONG_THREAD: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, string: java.lang.String, coordination: Coordination, int: int): ...
    @typing.overload
    def __init__(self, string: java.lang.String, coordination: Coordination, int: int, throwable: java.lang.Throwable): ...
    def getId(self) -> int: ...
    def getName(self) -> java.lang.String: ...
    def getType(self) -> int: ...

class CoordinationPermission(java.security.BasicPermission):
    """
    Java class 'org.osgi.service.coordinator.CoordinationPermission'
    
        Extends:
            java.security.BasicPermission
    
      Constructors:
        * CoordinationPermission(java.lang.String, org.osgi.framework.Bundle, java.lang.String)
        * CoordinationPermission(java.lang.String, java.lang.String)
    
      Attributes:
        INITIATE (java.lang.String): final static field
        PARTICIPATE (java.lang.String): final static field
        ADMIN (java.lang.String): final static field
    
    """
    INITIATE: typing.ClassVar[java.lang.String] = ...
    PARTICIPATE: typing.ClassVar[java.lang.String] = ...
    ADMIN: typing.ClassVar[java.lang.String] = ...
    @typing.overload
    def __init__(self, string: java.lang.String, string2: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, bundle: org.osgi.framework.Bundle, string2: java.lang.String): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getActions(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def implies(self, permission: java.security.Permission) -> bool: ...
    def newPermissionCollection(self) -> java.security.PermissionCollection: ...

class Coordinator(java.lang.Object):
    """
    Java class 'org.osgi.service.coordinator.Coordinator'
    
    """
    def addParticipant(self, participant: 'Participant') -> bool: ...
    def begin(self, string: java.lang.String, long: int) -> Coordination: ...
    def create(self, string: java.lang.String, long: int) -> Coordination: ...
    def fail(self, throwable: java.lang.Throwable) -> bool: ...
    def getCoordination(self, long: int) -> Coordination: ...
    def getCoordinations(self) -> java.util.Collection[Coordination]: ...
    def peek(self) -> Coordination: ...
    def pop(self) -> Coordination: ...

class Participant(java.lang.Object):
    """
    Java class 'org.osgi.service.coordinator.Participant'
    
    """
    def ended(self, coordination: Coordination) -> None: ...
    def failed(self, coordination: Coordination) -> None: ...
