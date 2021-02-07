import java.lang
import java.util
import java.util.stream
import org.openhab.core.ui.tiles
import typing


class TileService(org.openhab.core.ui.tiles.TileProvider):
    """
    Java class 'org.openhab.core.ui.internal.tiles.TileService'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.ui.tiles.TileProvider
    
      Constructors:
        * TileService(java.util.Map)
    
    """
    def __init__(self, properties: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]): ...
    def getTiles(self) -> java.util.stream.Stream[org.openhab.core.ui.tiles.Tile]: ...
