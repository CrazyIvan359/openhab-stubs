import java.lang
import java.util
import org.osgi.framework.wiring
import typing


class ResolverHook(java.lang.Object):
    """
    Java class 'org.osgi.framework.hooks.resolver.ResolverHook'
    
    """
    def end(self) -> None: ...
    def filterMatches(self, bundleRequirement: org.osgi.framework.wiring.BundleRequirement, collection: typing.Union[java.util.Collection[org.osgi.framework.wiring.BundleCapability], typing.Sequence[org.osgi.framework.wiring.BundleCapability]]) -> None: ...
    def filterResolvable(self, collection: typing.Union[java.util.Collection[org.osgi.framework.wiring.BundleRevision], typing.Sequence[org.osgi.framework.wiring.BundleRevision]]) -> None: ...
    def filterSingletonCollisions(self, bundleCapability: org.osgi.framework.wiring.BundleCapability, collection: typing.Union[java.util.Collection[org.osgi.framework.wiring.BundleCapability], typing.Sequence[org.osgi.framework.wiring.BundleCapability]]) -> None: ...

class ResolverHookFactory(java.lang.Object):
    """
    Java class 'org.osgi.framework.hooks.resolver.ResolverHookFactory'
    
    """
    def begin(self, collection: typing.Union[java.util.Collection[org.osgi.framework.wiring.BundleRevision], typing.Sequence[org.osgi.framework.wiring.BundleRevision]]) -> ResolverHook: ...
