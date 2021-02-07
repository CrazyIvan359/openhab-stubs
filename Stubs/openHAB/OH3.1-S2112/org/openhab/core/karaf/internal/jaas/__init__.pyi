import java.lang
import java.security
import java.util
import javax.security.auth.login
import org.apache.karaf.jaas.boot.principal
import org.apache.karaf.jaas.config
import org.apache.karaf.jaas.modules
import org.openhab.core.auth
import typing


class ManagedUserBackingEngine(org.apache.karaf.jaas.modules.BackingEngine):
    """
    Java class 'org.openhab.core.karaf.internal.jaas.ManagedUserBackingEngine'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.apache.karaf.jaas.modules.BackingEngine
    
      Constructors:
        * ManagedUserBackingEngine(org.openhab.core.auth.UserRegistry)
    
    """
    def __init__(self, userRegistry: org.openhab.core.auth.UserRegistry): ...
    def addGroup(self, username: java.lang.String, group: java.lang.String) -> None: ...
    def addGroupRole(self, group: java.lang.String, role: java.lang.String) -> None: ...
    def addRole(self, username: java.lang.String, role: java.lang.String) -> None: ...
    def addUser(self, username: java.lang.String, password: java.lang.String) -> None: ...
    def createGroup(self, group: java.lang.String) -> None: ...
    def deleteGroup(self, username: java.lang.String, group: java.lang.String) -> None: ...
    def deleteGroupRole(self, group: java.lang.String, role: java.lang.String) -> None: ...
    def deleteRole(self, username: java.lang.String, role: java.lang.String) -> None: ...
    def deleteUser(self, username: java.lang.String) -> None: ...
    @typing.overload
    def listGroups(self, user: org.apache.karaf.jaas.boot.principal.UserPrincipal) -> java.util.List[org.apache.karaf.jaas.boot.principal.GroupPrincipal]: ...
    @typing.overload
    def listGroups(self) -> java.util.Map[org.apache.karaf.jaas.boot.principal.GroupPrincipal, java.lang.String]: ...
    def listRoles(self, principal: java.security.Principal) -> java.util.List[org.apache.karaf.jaas.boot.principal.RolePrincipal]: ...
    def listUsers(self) -> java.util.List[org.apache.karaf.jaas.boot.principal.UserPrincipal]: ...
    def lookupUser(self, username: java.lang.String) -> org.apache.karaf.jaas.boot.principal.UserPrincipal: ...

class ManagedUserBackingEngineFactory(org.apache.karaf.jaas.modules.BackingEngineFactory):
    """
    Java class 'org.openhab.core.karaf.internal.jaas.ManagedUserBackingEngineFactory'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.apache.karaf.jaas.modules.BackingEngineFactory
    
      Constructors:
        * ManagedUserBackingEngineFactory(org.openhab.core.auth.UserRegistry)
    
    """
    def __init__(self, userRegistry: org.openhab.core.auth.UserRegistry): ...
    def build(self, options: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> org.apache.karaf.jaas.modules.BackingEngine: ...
    def getModuleClass(self) -> java.lang.String: ...

class ManagedUserRealm(org.apache.karaf.jaas.config.JaasRealm):
    """
    Java class 'org.openhab.core.karaf.internal.jaas.ManagedUserRealm'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.apache.karaf.jaas.config.JaasRealm
    
      Constructors:
        * ManagedUserRealm()
    
      Attributes:
        REALM_NAME (java.lang.String): final static field
        MODULE_CLASS (java.lang.String): final static field
    
    """
    REALM_NAME: typing.ClassVar[java.lang.String] = ...
    MODULE_CLASS: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    def getEntries(self) -> typing.List[javax.security.auth.login.AppConfigurationEntry]: ...
    def getName(self) -> java.lang.String: ...
    def getRank(self) -> int: ...
