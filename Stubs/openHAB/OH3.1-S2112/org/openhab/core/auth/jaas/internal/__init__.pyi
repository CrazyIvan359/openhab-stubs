import java.lang
import java.util
import javax.security.auth
import javax.security.auth.callback
import javax.security.auth.login
import javax.security.auth.spi
import org.openhab.core.auth
import typing


class JaasAuthenticationProvider(org.openhab.core.auth.AuthenticationProvider):
    """
    Java class 'org.openhab.core.auth.jaas.internal.JaasAuthenticationProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.auth.AuthenticationProvider
    
      Constructors:
        * JaasAuthenticationProvider()
    
    """
    def __init__(self): ...
    def authenticate(self, credentials: org.openhab.core.auth.Credentials) -> org.openhab.core.auth.Authentication: ...
    def supports(self, type: typing.Type[org.openhab.core.auth.Credentials]) -> bool: ...

class ManagedUserLoginConfiguration(javax.security.auth.login.Configuration):
    """
    Java class 'org.openhab.core.auth.jaas.internal.ManagedUserLoginConfiguration'
    
        Extends:
            javax.security.auth.login.Configuration
    
      Constructors:
        * ManagedUserLoginConfiguration()
    
    """
    def __init__(self): ...
    def getAppConfigurationEntry(self, name: java.lang.String) -> typing.List[javax.security.auth.login.AppConfigurationEntry]: ...

class ManagedUserLoginModule(javax.security.auth.spi.LoginModule):
    """
    Java class 'org.openhab.core.auth.jaas.internal.ManagedUserLoginModule'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            javax.security.auth.spi.LoginModule
    
      Constructors:
        * ManagedUserLoginModule()
    
    """
    def __init__(self): ...
    def abort(self) -> bool: ...
    def commit(self) -> bool: ...
    def initialize(self, subject: javax.security.auth.Subject, callbackHandler: javax.security.auth.callback.CallbackHandler, sharedState: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]], options: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def login(self) -> bool: ...
    def logout(self) -> bool: ...
