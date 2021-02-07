import java.lang
import java.util
import org.openhab.core.config.core


class MetadataConfigDescriptionProvider(java.lang.Object):
    """
    @NonNullByDefault public interface MetadataConfigDescriptionProvider
    
        A :class:`~org.openhab.core.config.core.metadata.MetadataConfigDescriptionProvider` implementation can be registered as
        an OSGi service in order to give guidance to UIs what metadata namespaces should be available and what metadata
        properties are expected.
    
        It will be tracked by the framework and the given information will be translated into config descriptions.
    
        Every extension which deals with specific metadata (in its own namespace) is expected to provide an implementation of
        this interface.
    
    
    """
    def getDescription(self, locale: java.util.Locale) -> java.lang.String: ...
    def getNamespace(self) -> java.lang.String: ...
    def getParameterOptions(self, locale: java.util.Locale) -> java.util.List[org.openhab.core.config.core.ParameterOption]: ...
    def getParameters(self, value: java.lang.String, locale: java.util.Locale) -> java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]: ...
