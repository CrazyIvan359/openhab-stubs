import java.lang
import java.util
import org.osgi.resource
import typing


class HostedCapability(org.osgi.resource.Capability):
    """
    Java class 'org.osgi.service.resolver.HostedCapability'
    
        Interfaces:
            org.osgi.resource.Capability
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getDeclaredCapability(self) -> org.osgi.resource.Capability: ...
    def getResource(self) -> org.osgi.resource.Resource: ...
    def hashCode(self) -> int: ...

class ResolutionException(java.lang.Exception):
    """
    Java class 'org.osgi.service.resolver.ResolutionException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * ResolutionException(java.lang.Throwable)
        * ResolutionException(java.lang.String)
        * ResolutionException(java.lang.String, java.lang.Throwable, java.util.Collection)
    
    """
    @typing.overload
    def __init__(self, string: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, throwable: java.lang.Throwable, collection: typing.Union[java.util.Collection[org.osgi.resource.Requirement], typing.Sequence[org.osgi.resource.Requirement]]): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...
    def getUnresolvedRequirements(self) -> java.util.Collection[org.osgi.resource.Requirement]: ...

class ResolveContext(java.lang.Object):
    """
    Java class 'org.osgi.service.resolver.ResolveContext'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ResolveContext()
    
    """
    def __init__(self): ...
    def findProviders(self, requirement: org.osgi.resource.Requirement) -> java.util.List[org.osgi.resource.Capability]: ...
    def getMandatoryResources(self) -> java.util.Collection[org.osgi.resource.Resource]: ...
    def getOptionalResources(self) -> java.util.Collection[org.osgi.resource.Resource]: ...
    def getWirings(self) -> java.util.Map[org.osgi.resource.Resource, org.osgi.resource.Wiring]: ...
    def insertHostedCapability(self, list: java.util.List[org.osgi.resource.Capability], hostedCapability: HostedCapability) -> int: ...
    def isEffective(self, requirement: org.osgi.resource.Requirement) -> bool: ...

class Resolver(java.lang.Object):
    """
    Java class 'org.osgi.service.resolver.Resolver'
    
    """
    def resolve(self, resolveContext: ResolveContext) -> java.util.Map[org.osgi.resource.Resource, java.util.List[org.osgi.resource.Wire]]: ...
