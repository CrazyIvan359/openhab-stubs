import java.lang
import java.net
import java.util
import org.openhab.core.events
import typing


class Addon(java.lang.Object):
    """
    Java class 'org.openhab.core.addon.Addon'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Addon(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, boolean)
        * Addon(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, boolean, java.lang.String, java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, id: java.lang.String, type: java.lang.String, label: java.lang.String, version: java.lang.String, link: java.lang.String, installed: bool): ...
    @typing.overload
    def __init__(self, id: java.lang.String, type: java.lang.String, label: java.lang.String, version: java.lang.String, link: java.lang.String, installed: bool, description: java.lang.String, backgroundColor: java.lang.String, imageLink: java.lang.String): ...
    def getBackgroundColor(self) -> java.lang.String: ...
    def getDescription(self) -> java.lang.String: ...
    def getId(self) -> java.lang.String: ...
    def getImageLink(self) -> java.lang.String: ...
    def getLabel(self) -> java.lang.String: ...
    def getLink(self) -> java.lang.String: ...
    def getType(self) -> java.lang.String: ...
    def getVersion(self) -> java.lang.String: ...
    def isInstalled(self) -> bool: ...
    def setInstalled(self, installed: bool) -> None: ...

class AddonEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.addon.AddonEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
      Constructors:
        * AddonEvent(java.lang.String, java.lang.String, java.lang.String)
        * AddonEvent(java.lang.String, java.lang.String, java.lang.String, java.lang.String)
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    @typing.overload
    def __init__(self, topic: java.lang.String, payload: java.lang.String, id: java.lang.String): ...
    @typing.overload
    def __init__(self, topic: java.lang.String, payload: java.lang.String, id: java.lang.String, msg: java.lang.String): ...
    def getType(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class AddonEventFactory(org.openhab.core.events.AbstractEventFactory):
    """
    Java class 'org.openhab.core.addon.AddonEventFactory'
    
        Extends:
            org.openhab.core.events.AbstractEventFactory
    
      Constructors:
        * AddonEventFactory()
    
    """
    def __init__(self): ...
    @classmethod
    def createAddonFailureEvent(cls, id: java.lang.String, msg: java.lang.String) -> AddonEvent: ...
    @classmethod
    def createAddonInstalledEvent(cls, id: java.lang.String) -> AddonEvent: ...
    @classmethod
    def createAddonUninstalledEvent(cls, id: java.lang.String) -> AddonEvent: ...

class AddonService(java.lang.Object):
    """
    public interface AddonService
    
        Classes implementing this interface can be registered as an OSGi service in order to provide functionality for managing
        add-ons, such as listing, installing and uninstalling them. The REST API offers an uri that exposes this functionality.
    
    
    """
    def getAddon(self, id: java.lang.String, locale: java.util.Locale) -> Addon: ...
    def getAddonId(self, addonURI: java.net.URI) -> java.lang.String: ...
    def getAddons(self, locale: java.util.Locale) -> java.util.List[Addon]: ...
    def getTypes(self, locale: java.util.Locale) -> java.util.List['AddonType']: ...
    def install(self, id: java.lang.String) -> None: ...
    def uninstall(self, id: java.lang.String) -> None: ...

class AddonType(java.lang.Object):
    """
    Java class 'org.openhab.core.addon.AddonType'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * AddonType(java.lang.String, java.lang.String)
    
    """
    def __init__(self, id: java.lang.String, label: java.lang.String): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getId(self) -> java.lang.String: ...
    def getLabel(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
