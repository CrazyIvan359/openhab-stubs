import java.lang
import org.eclipse.emf.common.util
import org.eclipse.emf.ecore
import org.openhab.core.items
import org.openhab.core.library.types
import org.openhab.core.model.sitemap.sitemap
import org.openhab.core.types
import typing


class ItemUIProvider(java.lang.Object):
    """
    @NonNullByDefault public interface ItemUIProvider
    
        This interface describes the methods that need to be implemented by a provider that wants to define the appearance of an
        item in the UI.
    
    
    """
    def getCategory(self, itemName: java.lang.String) -> java.lang.String: ...
    def getDefaultWidget(self, itemType: typing.Type[org.openhab.core.items.Item], itemName: java.lang.String) -> org.openhab.core.model.sitemap.sitemap.Widget: ...
    def getLabel(self, itemName: java.lang.String) -> java.lang.String: ...
    def getWidget(self, itemName: java.lang.String) -> org.openhab.core.model.sitemap.sitemap.Widget: ...

class ItemUIRegistry(org.openhab.core.items.ItemRegistry, ItemUIProvider):
    """
    Java class 'org.openhab.core.ui.items.ItemUIRegistry'
    
        Interfaces:
            org.openhab.core.items.ItemRegistry,
            org.openhab.core.ui.items.ItemUIProvider
    
    """
    def convertState(self, widget: org.openhab.core.model.sitemap.sitemap.Widget, item: org.openhab.core.items.Item, state: org.openhab.core.types.State) -> org.openhab.core.types.State: ...
    def convertStateToLabelUnit(self, state: org.openhab.core.library.types.QuantityType[typing.Any], label: java.lang.String) -> org.openhab.core.types.State: ...
    @typing.overload
    def getCategory(self, itemName: java.lang.String) -> java.lang.String: ...
    @typing.overload
    def getCategory(self, w: org.openhab.core.model.sitemap.sitemap.Widget) -> java.lang.String: ...
    @typing.overload
    def getChildren(self, w: org.openhab.core.model.sitemap.sitemap.LinkableWidget) -> org.eclipse.emf.common.util.EList[org.openhab.core.model.sitemap.sitemap.Widget]: ...
    @typing.overload
    def getChildren(self, sitemap: org.openhab.core.model.sitemap.sitemap.Sitemap) -> org.eclipse.emf.common.util.EList[org.openhab.core.model.sitemap.sitemap.Widget]: ...
    def getItemState(self, itemName: java.lang.String) -> org.openhab.core.types.State: ...
    @typing.overload
    def getLabel(self, itemName: java.lang.String) -> java.lang.String: ...
    @typing.overload
    def getLabel(self, w: org.openhab.core.model.sitemap.sitemap.Widget) -> java.lang.String: ...
    def getLabelColor(self, w: org.openhab.core.model.sitemap.sitemap.Widget) -> java.lang.String: ...
    def getParent(self, w: org.openhab.core.model.sitemap.sitemap.Widget) -> org.eclipse.emf.ecore.EObject: ...
    def getState(self, w: org.openhab.core.model.sitemap.sitemap.Widget) -> org.openhab.core.types.State: ...
    def getUnitForWidget(self, widget: org.openhab.core.model.sitemap.sitemap.Widget) -> java.lang.String: ...
    def getValueColor(self, w: org.openhab.core.model.sitemap.sitemap.Widget) -> java.lang.String: ...
    def getVisiblity(self, w: org.openhab.core.model.sitemap.sitemap.Widget) -> bool: ...
    @typing.overload
    def getWidget(self, itemName: java.lang.String) -> org.openhab.core.model.sitemap.sitemap.Widget: ...
    @typing.overload
    def getWidget(self, sitemap: org.openhab.core.model.sitemap.sitemap.Sitemap, id: java.lang.String) -> org.openhab.core.model.sitemap.sitemap.Widget: ...
    def getWidgetId(self, w: org.openhab.core.model.sitemap.sitemap.Widget) -> java.lang.String: ...