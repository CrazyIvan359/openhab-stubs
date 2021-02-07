import java.lang
import java.net
import java.util
import org.openhab.core.addon


class SampleAddonService(org.openhab.core.addon.AddonService):
    """
    Java class 'org.openhab.core.addon.sample.internal.SampleAddonService'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.addon.AddonService
    
      Constructors:
        * SampleAddonService()
    
    """
    def __init__(self): ...
    def getAddon(self, id: java.lang.String, locale: java.util.Locale) -> org.openhab.core.addon.Addon: ...
    def getAddonId(self, extensionURI: java.net.URI) -> java.lang.String: ...
    def getAddons(self, locale: java.util.Locale) -> java.util.List[org.openhab.core.addon.Addon]: ...
    def getTypes(self, locale: java.util.Locale) -> java.util.List[org.openhab.core.addon.AddonType]: ...
    def install(self, id: java.lang.String) -> None: ...
    def uninstall(self, id: java.lang.String) -> None: ...
