import java.lang
import java.util
import org.openhab.core.auth
import org.openhab.core.common.registry
import org.openhab.core.storage
import org.osgi.framework
import typing


class AuthenticationManagerImpl(org.openhab.core.auth.AuthenticationManager):
    """
    Java class 'org.openhab.core.internal.auth.AuthenticationManagerImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.auth.AuthenticationManager
    
      Constructors:
        * AuthenticationManagerImpl()
    
    """
    def __init__(self): ...
    def addAuthenticationProvider(self, provider: org.openhab.core.auth.AuthenticationProvider) -> None: ...
    def authenticate(self, credentials: org.openhab.core.auth.Credentials) -> org.openhab.core.auth.Authentication: ...
    def removeAuthenticationProvider(self, provider: org.openhab.core.auth.AuthenticationProvider) -> None: ...

class ManagedUserProvider(org.openhab.core.common.registry.DefaultAbstractManagedProvider[org.openhab.core.auth.User, java.lang.String]):
    """
    Java class 'org.openhab.core.internal.auth.ManagedUserProvider'
    
        Extends:
            org.openhab.core.common.registry.DefaultAbstractManagedProvider
    
      Constructors:
        * ManagedUserProvider(org.openhab.core.storage.StorageService)
    
    """
    def __init__(self, storageService: org.openhab.core.storage.StorageService): ...

class UserRegistryImpl(org.openhab.core.common.registry.AbstractRegistry[org.openhab.core.auth.User, java.lang.String, org.openhab.core.auth.UserProvider], org.openhab.core.auth.UserRegistry):
    """
    Java class 'org.openhab.core.internal.auth.UserRegistryImpl'
    
        Extends:
            org.openhab.core.common.registry.AbstractRegistry
    
        Interfaces:
            org.openhab.core.auth.UserRegistry
    
      Constructors:
        * UserRegistryImpl(org.osgi.framework.BundleContext, java.util.Map)
    
    """
    def __init__(self, context: org.osgi.framework.BundleContext, properties: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]): ...
    def addUserApiToken(self, user: org.openhab.core.auth.User, name: java.lang.String, scope: java.lang.String) -> java.lang.String: ...
    def addUserSession(self, user: org.openhab.core.auth.User, session: org.openhab.core.auth.UserSession) -> None: ...
    def authenticate(self, credentials: org.openhab.core.auth.Credentials) -> org.openhab.core.auth.Authentication: ...
    def changePassword(self, user: org.openhab.core.auth.User, newPassword: java.lang.String) -> None: ...
    def clearSessions(self, user: org.openhab.core.auth.User) -> None: ...
    def register(self, username: java.lang.String, password: java.lang.String, roles: java.util.Set[java.lang.String]) -> org.openhab.core.auth.User: ...
    def removeUserApiToken(self, user: org.openhab.core.auth.User, userApiToken: org.openhab.core.auth.UserApiToken) -> None: ...
    def removeUserSession(self, user: org.openhab.core.auth.User, session: org.openhab.core.auth.UserSession) -> None: ...
    def supports(self, type: typing.Type[org.openhab.core.auth.Credentials]) -> bool: ...
