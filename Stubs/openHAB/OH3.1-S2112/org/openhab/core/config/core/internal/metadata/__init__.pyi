import java.net
import java.util
import org.openhab.core.config.core


class MetadataConfigDescriptionProviderImpl(org.openhab.core.config.core.ConfigDescriptionProvider):
    """
    Java class 'org.openhab.core.config.core.internal.metadata.MetadataConfigDescriptionProviderImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.core.ConfigDescriptionProvider
    
      Constructors:
        * MetadataConfigDescriptionProviderImpl()
    
    """
    def __init__(self): ...
    def getConfigDescription(self, uri: java.net.URI, locale: java.util.Locale) -> org.openhab.core.config.core.ConfigDescription: ...
    def getConfigDescriptions(self, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.config.core.ConfigDescription]: ...
