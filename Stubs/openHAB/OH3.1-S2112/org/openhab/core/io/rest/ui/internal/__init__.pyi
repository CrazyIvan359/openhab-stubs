import java.lang
import javax.ws.rs.core
import org.openhab.core.io.rest
import org.openhab.core.ui.components
import org.openhab.core.ui.tiles
import typing


class UIResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.ui.internal.UIResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * UIResource(org.openhab.core.ui.components.UIComponentRegistryFactory, org.openhab.core.ui.tiles.TileProvider)
    
      Attributes:
        PATH_UI (java.lang.String): final static field
    
    """
    PATH_UI: typing.ClassVar[java.lang.String] = ...
    def __init__(self, componentRegistryFactory: org.openhab.core.ui.components.UIComponentRegistryFactory, tileProvider: org.openhab.core.ui.tiles.TileProvider): ...
    def addComponent(self, namespace: java.lang.String, component: org.openhab.core.ui.components.RootUIComponent) -> javax.ws.rs.core.Response: ...
    def deleteComponent(self, namespace: java.lang.String, componentUID: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getAll(self) -> javax.ws.rs.core.Response: ...
    def getAllComponents(self, namespace: java.lang.String, summary: bool) -> javax.ws.rs.core.Response: ...
    def getComponentByUID(self, namespace: java.lang.String, componentUID: java.lang.String) -> javax.ws.rs.core.Response: ...
    def updateComponent(self, namespace: java.lang.String, componentUID: java.lang.String, component: org.openhab.core.ui.components.RootUIComponent) -> javax.ws.rs.core.Response: ...
