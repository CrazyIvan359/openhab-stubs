import java.lang
import java.util
import org
import org.openhab.core.common.registry
import org.openhab.core.config.core.dto
import typing


class UIComponent(java.lang.Object):
    """
    Java class 'org.openhab.core.ui.components.UIComponent'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * UIComponent(java.lang.String)
    
    """
    def __init__(self, componentType: java.lang.String): ...
    def addComponent(self, slotName: java.lang.String, subComponent: 'UIComponent') -> None: ...
    def addConfig(self, key: java.lang.String, value: typing.Any) -> None: ...
    def addSlot(self, slotName: java.lang.String) -> java.util.List['UIComponent']: ...
    def getConfig(self) -> java.util.Map[java.lang.String, typing.Any]: ...
    def getSlot(self, slotName: java.lang.String) -> java.util.List['UIComponent']: ...
    def getSlots(self) -> java.util.Map[java.lang.String, java.util.List['UIComponent']]: ...
    def getType(self) -> java.lang.String: ...

class UIComponentRegistry(org.openhab.core.common.registry.Registry[org.openhab.core.ui.components.RootUIComponent, java.lang.String]):
    """
    Java class 'org.openhab.core.ui.components.UIComponentRegistry'
    
        Interfaces:
            org.openhab.core.common.registry.Registry
    
    """

class UIComponentRegistryFactory(java.lang.Object):
    """
    @NonNullByDefault public interface UIComponentRegistryFactory
    
        A factory for :class:`~org.openhab.core.ui.components.UIComponentRegistry` instances based on the namespace.
    
    
    """
    def getRegistry(self, namespace: java.lang.String) -> UIComponentRegistry: ...

class RootUIComponent(UIComponent, org.openhab.core.common.registry.Identifiable[java.lang.String]):
    """
    Java class 'org.openhab.core.ui.components.RootUIComponent'
    
        Extends:
            org.openhab.core.ui.components.UIComponent
    
        Interfaces:
            org.openhab.core.common.registry.Identifiable
    
      Constructors:
        * RootUIComponent(java.lang.String)
        * RootUIComponent(java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, name: java.lang.String): ...
    @typing.overload
    def __init__(self, uid: java.lang.String, name: java.lang.String): ...
    def addTag(self, tag: java.lang.String) -> None: ...
    @typing.overload
    def addTags(self, tags: typing.List[java.lang.String]) -> None: ...
    @typing.overload
    def addTags(self, tags: typing.Union[java.util.Collection[java.lang.String], typing.Sequence[java.lang.String]]) -> None: ...
    def getProps(self) -> org.openhab.core.config.core.dto.ConfigDescriptionDTO: ...
    def getTags(self) -> java.util.Set[java.lang.String]: ...
    def getTimestamp(self) -> java.util.Date: ...
    @typing.overload
    def getUID(self) -> typing.Any: ...
    @typing.overload
    def getUID(self) -> java.lang.String: ...
    def hasTag(self, tag: java.lang.String) -> bool: ...
    def removeAllTags(self) -> None: ...
    def removeTag(self, tag: java.lang.String) -> None: ...
    def setProps(self, props: org.openhab.core.config.core.dto.ConfigDescriptionDTO) -> None: ...
    def setTimestamp(self, date: java.util.Date) -> None: ...
    def updateTimestamp(self) -> None: ...
