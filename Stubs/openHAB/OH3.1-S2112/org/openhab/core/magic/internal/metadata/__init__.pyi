import java.lang
import java.util
import org.openhab.core.config.core
import org.openhab.core.config.core.metadata
import org.openhab.core.items


class MagicMetadataProvider(org.openhab.core.config.core.metadata.MetadataConfigDescriptionProvider):
    """
    Java class 'org.openhab.core.magic.internal.metadata.MagicMetadataProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.core.metadata.MetadataConfigDescriptio
            nProvider
    
      Constructors:
        * MagicMetadataProvider()
    
    """
    def __init__(self): ...
    def getDescription(self, locale: java.util.Locale) -> java.lang.String: ...
    def getNamespace(self) -> java.lang.String: ...
    def getParameterOptions(self, locale: java.util.Locale) -> java.util.List[org.openhab.core.config.core.ParameterOption]: ...
    def getParameters(self, value: java.lang.String, locale: java.util.Locale) -> java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]: ...

class MagicMetadataProvider2(org.openhab.core.config.core.metadata.MetadataConfigDescriptionProvider):
    """
    Java class 'org.openhab.core.magic.internal.metadata.MagicMetadataProvider2'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.core.metadata.MetadataConfigDescriptio
            nProvider
    
      Constructors:
        * MagicMetadataProvider2()
    
    """
    def __init__(self): ...
    def getDescription(self, locale: java.util.Locale) -> java.lang.String: ...
    def getNamespace(self) -> java.lang.String: ...
    def getParameterOptions(self, locale: java.util.Locale) -> java.util.List[org.openhab.core.config.core.ParameterOption]: ...
    def getParameters(self, value: java.lang.String, locale: java.util.Locale) -> java.util.List[org.openhab.core.config.core.ConfigDescriptionParameter]: ...

class MagicMetadataUsingService(java.lang.Object):
    """
    Java class 'org.openhab.core.magic.internal.metadata.MagicMetadataUsingService'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MagicMetadataUsingService(org.openhab.core.items.MetadataRegistry)
    
    """
    def __init__(self, metadataRegistry: org.openhab.core.items.MetadataRegistry): ...
    def deactivate(self) -> None: ...
