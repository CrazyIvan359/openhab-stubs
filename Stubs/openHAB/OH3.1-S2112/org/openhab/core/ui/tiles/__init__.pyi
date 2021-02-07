import java.lang
import java.util.stream


class Tile(java.lang.Object):
    """
    @NonNullByDefault public interface Tile
    
        A tile can be registered by an UI as a service in order to appear on the main openHAB UI.
    
    
    """
    def getImageUrl(self) -> java.lang.String: ...
    def getName(self) -> java.lang.String: ...
    def getOverlay(self) -> java.lang.String: ...
    def getUrl(self) -> java.lang.String: ...

class TileProvider(java.lang.Object):
    """
    @NonNullByDefault public interface TileProvider
    
        Interface for a component providing UI tiles.
    
    
    """
    def getTiles(self) -> java.util.stream.Stream[Tile]: ...

class ExternalServiceTile(Tile):
    """
    Java class 'org.openhab.core.ui.tiles.ExternalServiceTile'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.ui.tiles.Tile
    
    """
    def getImageUrl(self) -> java.lang.String: ...
    def getName(self) -> java.lang.String: ...
    def getOverlay(self) -> java.lang.String: ...
    def getUrl(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    class TileBuilder(java.lang.Object):
        """
        Java class 'org.openhab.core.ui.tiles.ExternalServiceTile$TileBuilder'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * TileBuilder()
        
        """
        def __init__(self): ...
        def build(self) -> 'ExternalServiceTile': ...
        def withImageUrl(self, imageUrl: java.lang.String) -> 'ExternalServiceTile.TileBuilder': ...
        def withName(self, name: java.lang.String) -> 'ExternalServiceTile.TileBuilder': ...
        def withOverlay(self, overlay: java.lang.String) -> 'ExternalServiceTile.TileBuilder': ...
        def withUrl(self, url: java.lang.String) -> 'ExternalServiceTile.TileBuilder': ...
