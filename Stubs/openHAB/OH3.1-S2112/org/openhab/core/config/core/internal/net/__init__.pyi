import java.lang
import java.net
import java.util
import org.openhab.core.config.core


class NetworkConfigOptionProvider(org.openhab.core.config.core.ConfigOptionProvider):
    """
    Java class 'org.openhab.core.config.core.internal.net.NetworkConfigOptionProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.core.ConfigOptionProvider
    
      Constructors:
        * NetworkConfigOptionProvider()
    
    """
    def __init__(self): ...
    def getParameterOptions(self, uri: java.net.URI, param: java.lang.String, context: java.lang.String, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.config.core.ParameterOption]: ...
