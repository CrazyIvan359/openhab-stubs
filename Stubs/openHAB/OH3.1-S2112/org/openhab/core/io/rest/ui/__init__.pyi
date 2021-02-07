import java.lang


class TileDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.ui.TileDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * TileDTO(java.lang.String, java.lang.String, java.lang.String, java.lang.String)
    
      Attributes:
        name (java.lang.String): field
        url (java.lang.String): field
        overlay (java.lang.String): field
        imageUrl (java.lang.String): field
    
    """
    name: java.lang.String = ...
    url: java.lang.String = ...
    overlay: java.lang.String = ...
    imageUrl: java.lang.String = ...
    def __init__(self, name: java.lang.String, url: java.lang.String, overlay: java.lang.String, imageUrl: java.lang.String): ...
