import java.lang
import java.security
import java.util
import org.openhab.core.common.registry
import typing


class Authentication(java.lang.Object):
    """
    Java class 'org.openhab.core.auth.Authentication'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Authentication(java.lang.String, java.lang.String[], java.lang.String)
        * Authentication(java.lang.String, java.lang.String[])
    
    """
    @typing.overload
    def __init__(self, username: java.lang.String, roles: typing.List[java.lang.String]): ...
    @typing.overload
    def __init__(self, username: java.lang.String, roles: typing.List[java.lang.String], scope: java.lang.String): ...
    def getRoles(self) -> java.util.Set[java.lang.String]: ...
    def getScope(self) -> java.lang.String: ...
    def getUsername(self) -> java.lang.String: ...

class AuthenticationManager(java.lang.Object):
    """
    public interface AuthenticationManager
    
        Authentication manager is main entry point for all places which are interested in securing requests and verifying their
        originator.
    
    
    """
    def authenticate(self, credentials: 'Credentials') -> Authentication: ...

class AuthenticationProvider(java.lang.Object):
    """
    @NonNullByDefault public interface AuthenticationProvider
    
        Realizations of this type are responsible for checking validity of various credentials and giving back authentication
        which defines access scope for authenticated user or system.
    
    
    """
    def authenticate(self, credentials: 'Credentials') -> Authentication: ...
    def supports(self, type: typing.Type['Credentials']) -> bool: ...

class Credentials(java.lang.Object):
    """
    public interface Credentials
    
        Marker interface for credentials which can be handled by authentication providers.
    
    
    """

class PendingToken(java.lang.Object):
    """
    Java class 'org.openhab.core.auth.PendingToken'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PendingToken(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String)
    
    """
    def __init__(self, authorizationCode: java.lang.String, clientId: java.lang.String, redirectUri: java.lang.String, scope: java.lang.String, codeChallenge: java.lang.String, codeChallengeMethod: java.lang.String): ...
    def getAuthorizationCode(self) -> java.lang.String: ...
    def getClientId(self) -> java.lang.String: ...
    def getCodeChallenge(self) -> java.lang.String: ...
    def getCodeChallengeMethod(self) -> java.lang.String: ...
    def getRedirectUri(self) -> java.lang.String: ...
    def getScope(self) -> java.lang.String: ...

class Role(java.lang.Object):
    """
    public interface Role
    
        Interface defining constants for roles within the framework.
    
    
    """
    ADMIN: typing.ClassVar[java.lang.String] = ...
    USER: typing.ClassVar[java.lang.String] = ...

class SecurityException(java.lang.Exception):
    """
    Java class 'org.openhab.core.auth.SecurityException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * SecurityException(java.lang.String)
        * SecurityException(java.lang.Throwable)
        * SecurityException(java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, message: java.lang.String): ...
    @typing.overload
    def __init__(self, message: java.lang.String, cause: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, cause: java.lang.Throwable): ...

class User(java.security.Principal, org.openhab.core.common.registry.Identifiable[java.lang.String]):
    """
    @NonNullByDefault public interface User extends :class:`~org.openhab.core.auth.https:.docs.oracle.com.en.java.javase.11.docs.api.java.base.java.security.Principal?is`, :class:`~org.openhab.core.common.registry.Identifiable`<:class:`~org.openhab.core.auth.https:.docs.oracle.com.en.java.javase.11.docs.api.java.base.java.lang.String?is`>
    
        A user represents an individual, physical person using the system.
    
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getRoles(self) -> java.util.Set[java.lang.String]: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class UserApiToken(java.lang.Object):
    """
    Java class 'org.openhab.core.auth.UserApiToken'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * UserApiToken(java.lang.String, java.lang.String, java.lang.String)
    
    """
    def __init__(self, name: java.lang.String, apiToken: java.lang.String, scope: java.lang.String): ...
    def getApiToken(self) -> java.lang.String: ...
    def getCreatedTime(self) -> java.util.Date: ...
    def getName(self) -> java.lang.String: ...
    def getScope(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class UserProvider(org.openhab.core.common.registry.Provider[User]):
    """
    @NonNullByDefault public interface UserProvider extends :class:`~org.openhab.core.common.registry.Provider`<:class:`~org.openhab.core.auth.User`>
    
        A interface for a :class:`~org.openhab.core.common.registry.Provider` of :class:`~org.openhab.core.auth.User` entities
    
    
    """

class UserSession(java.lang.Object):
    """
    Java class 'org.openhab.core.auth.UserSession'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * UserSession(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String)
    
    """
    def __init__(self, sessionId: java.lang.String, refreshToken: java.lang.String, clientId: java.lang.String, redirectUri: java.lang.String, scope: java.lang.String): ...
    def getClientId(self) -> java.lang.String: ...
    def getCreatedTime(self) -> java.util.Date: ...
    def getLastRefreshTime(self) -> java.util.Date: ...
    def getRedirectUri(self) -> java.lang.String: ...
    def getRefreshToken(self) -> java.lang.String: ...
    def getScope(self) -> java.lang.String: ...
    def getSessionId(self) -> java.lang.String: ...
    def hasSessionCookie(self) -> bool: ...
    def setLastRefreshTime(self, lastRefreshTime: java.util.Date) -> None: ...
    def setSessionCookie(self, sessionCookie: bool) -> None: ...

class AuthenticationException(SecurityException):
    """
    Java class 'org.openhab.core.auth.AuthenticationException'
    
        Extends:
            org.openhab.core.auth.SecurityException
    
      Constructors:
        * AuthenticationException(java.lang.String)
        * AuthenticationException(java.lang.Throwable)
        * AuthenticationException(java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, message: java.lang.String): ...
    @typing.overload
    def __init__(self, message: java.lang.String, cause: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, cause: java.lang.Throwable): ...

class GenericUser(User):
    """
    Java class 'org.openhab.core.auth.GenericUser'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.auth.User
    
      Constructors:
        * GenericUser(java.lang.String, java.util.Set)
        * GenericUser(java.lang.String)
    
    """
    @typing.overload
    def __init__(self, name: java.lang.String): ...
    @typing.overload
    def __init__(self, name: java.lang.String, roles: java.util.Set[java.lang.String]): ...
    def getName(self) -> java.lang.String: ...
    def getRoles(self) -> java.util.Set[java.lang.String]: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    @typing.overload
    def getUID(self) -> java.lang.String: ...

class ManagedUser(User):
    """
    Java class 'org.openhab.core.auth.ManagedUser'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.auth.User
    
      Constructors:
        * ManagedUser(java.lang.String, java.lang.String, java.lang.String)
    
    """
    def __init__(self, name: java.lang.String, passwordSalt: java.lang.String, passwordHash: java.lang.String): ...
    def getApiTokens(self) -> java.util.List[UserApiToken]: ...
    def getName(self) -> java.lang.String: ...
    def getPasswordHash(self) -> java.lang.String: ...
    def getPasswordSalt(self) -> java.lang.String: ...
    def getPendingToken(self) -> PendingToken: ...
    def getRoles(self) -> java.util.Set[java.lang.String]: ...
    def getSessions(self) -> java.util.List[UserSession]: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    @typing.overload
    def getUID(self) -> java.lang.String: ...
    def setApiTokens(self, apiTokens: java.util.List[UserApiToken]) -> None: ...
    def setName(self, name: java.lang.String) -> None: ...
    def setPasswordHash(self, passwordHash: java.lang.String) -> None: ...
    def setPasswordSalt(self, passwordSalt: java.lang.String) -> None: ...
    def setPendingToken(self, pendingToken: PendingToken) -> None: ...
    def setRoles(self, roles: java.util.Set[java.lang.String]) -> None: ...
    def setSessions(self, sessions: java.util.List[UserSession]) -> None: ...
    def toString(self) -> java.lang.String: ...

class UserApiTokenCredentials(Credentials):
    """
    Java class 'org.openhab.core.auth.UserApiTokenCredentials'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.auth.Credentials
    
      Constructors:
        * UserApiTokenCredentials(java.lang.String)
    
    """
    def __init__(self, userApiToken: java.lang.String): ...
    def getApiToken(self) -> java.lang.String: ...

class UserRegistry(org.openhab.core.common.registry.Registry[User, java.lang.String], AuthenticationProvider):
    """
    Java class 'org.openhab.core.auth.UserRegistry'
    
        Interfaces:
            org.openhab.core.common.registry.Registry,
            org.openhab.core.auth.AuthenticationProvider
    
    """
    def addUserApiToken(self, user: User, name: java.lang.String, scope: java.lang.String) -> java.lang.String: ...
    def addUserSession(self, user: User, session: UserSession) -> None: ...
    def changePassword(self, user: User, newPassword: java.lang.String) -> None: ...
    def clearSessions(self, user: User) -> None: ...
    def register(self, username: java.lang.String, password: java.lang.String, roles: java.util.Set[java.lang.String]) -> User: ...
    def removeUserApiToken(self, user: User, apiToken: UserApiToken) -> None: ...
    def removeUserSession(self, user: User, session: UserSession) -> None: ...

class UsernamePasswordCredentials(Credentials):
    """
    Java class 'org.openhab.core.auth.UsernamePasswordCredentials'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.auth.Credentials
    
      Constructors:
        * UsernamePasswordCredentials(java.lang.String, java.lang.String)
    
    """
    def __init__(self, username: java.lang.String, password: java.lang.String): ...
    def getPassword(self) -> java.lang.String: ...
    def getUsername(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class UnsupportedCredentialsException(AuthenticationException):
    """
    Java class 'org.openhab.core.auth.UnsupportedCredentialsException'
    
        Extends:
            org.openhab.core.auth.AuthenticationException
    
      Constructors:
        * UnsupportedCredentialsException(java.lang.String)
        * UnsupportedCredentialsException(java.lang.Throwable)
        * UnsupportedCredentialsException(java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, message: java.lang.String): ...
    @typing.overload
    def __init__(self, message: java.lang.String, cause: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, cause: java.lang.Throwable): ...
