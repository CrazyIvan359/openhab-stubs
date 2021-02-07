import java.lang
import org.openhab.core.config.xml.util
import org.openhab.core.service
import org.osgi.framework
import org.osgi.util.tracker
import typing


_XmlDocumentBundleTracker__T = typing.TypeVar('_XmlDocumentBundleTracker__T')  # <T>
class XmlDocumentBundleTracker(org.osgi.util.tracker.BundleTracker[org.osgi.framework.Bundle], typing.Generic[_XmlDocumentBundleTracker__T]):
    """
    Java class 'org.openhab.core.config.xml.osgi.XmlDocumentBundleTracker'
    
        Extends:
            org.osgi.util.tracker.BundleTracker
    
      Constructors:
        * XmlDocumentBundleTracker(org.osgi.framework.BundleContext, java.lang.String, org.openhab.core.config.xml.util.XmlDocumentReader, org.openhab.core.config.xml.osgi.XmlDocumentProviderFactory, java.lang.String, org.openhab.core.service.ReadyService)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
      Attributes:
        THREAD_POOL_NAME (java.lang.String): final static field
    
    """
    THREAD_POOL_NAME: typing.ClassVar[java.lang.String] = ...
    def __init__(self, bundleContext: org.osgi.framework.BundleContext, xmlDirectory: java.lang.String, xmlDocumentTypeReader: org.openhab.core.config.xml.util.XmlDocumentReader[_XmlDocumentBundleTracker__T], xmlDocumentProviderFactory: 'XmlDocumentProviderFactory'[_XmlDocumentBundleTracker__T], readyMarkerKey: java.lang.String, readyService: org.openhab.core.service.ReadyService): ...
    @typing.overload
    def addingBundle(self, bundle: org.osgi.framework.Bundle, event: org.osgi.framework.BundleEvent) -> org.osgi.framework.Bundle: ...
    @typing.overload
    def addingBundle(self, bundle: org.osgi.framework.Bundle, bundleEvent: org.osgi.framework.BundleEvent) -> typing.Any: ...
    def close(self) -> None: ...
    def open(self) -> None: ...
    @typing.overload
    def removedBundle(self, bundle: org.osgi.framework.Bundle, event: org.osgi.framework.BundleEvent, object: org.osgi.framework.Bundle) -> None: ...
    @typing.overload
    def removedBundle(self, bundle: org.osgi.framework.Bundle, bundleEvent: org.osgi.framework.BundleEvent, object: typing.Any) -> None: ...
    def toString(self) -> java.lang.String: ...

_XmlDocumentProvider__T = typing.TypeVar('_XmlDocumentProvider__T')  # <T>
class XmlDocumentProvider(java.lang.Object, typing.Generic[_XmlDocumentProvider__T]):
    """
    @NonNullByDefault public interface XmlDocumentProvider<@NonNull T>
    
        The :class:`~org.openhab.core.config.xml.osgi.XmlDocumentProvider` is responsible managing any created objects by a
        :code:`ConfigDescriptionReader` for a certain module.
    
        Each instance of this class is assigned to exactly one module.
    
    
    """
    def addingFinished(self) -> None: ...
    def addingObject(self, object: _XmlDocumentProvider__T) -> None: ...
    def release(self) -> None: ...

_XmlDocumentProviderFactory__T = typing.TypeVar('_XmlDocumentProviderFactory__T')  # <T>
class XmlDocumentProviderFactory(java.lang.Object, typing.Generic[_XmlDocumentProviderFactory__T]):
    """
    @NonNullByDefault public interface XmlDocumentProviderFactory<@NonNull T>
    
        The :class:`~org.openhab.core.config.xml.osgi.XmlDocumentProviderFactory` is responsible to create
        :class:`~org.openhab.core.config.xml.osgi.XmlDocumentProvider` instances for any certain module. The factory is *not*
        responsible to clean-up any created providers.
    
        The :class:`~org.openhab.core.config.xml.osgi.XmlDocumentProviderFactory` is used by the
        :class:`~org.openhab.core.config.xml.osgi.XmlDocumentBundleTracker` to create for each module an own
        :class:`~org.openhab.core.config.xml.osgi.XmlDocumentProvider` instance to process any result objects from the XML
        conversion.
    
        Also see:
            :class:`~org.openhab.core.config.xml.osgi.XmlDocumentProvider`
    
    
    """
    def createDocumentProvider(self, bundle: org.osgi.framework.Bundle) -> XmlDocumentProvider[_XmlDocumentProviderFactory__T]: ...
