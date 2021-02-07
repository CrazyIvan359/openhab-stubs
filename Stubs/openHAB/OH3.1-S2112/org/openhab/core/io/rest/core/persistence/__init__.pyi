import java.lang
import java.util
import org.openhab.core.persistence.dto
import typing


class ItemHistoryListDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.core.persistence.ItemHistoryListDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ItemHistoryListDTO()
        * ItemHistoryListDTO(java.util.Collection)
    
      Attributes:
        item (java.util.List): final field
    
    """
    item: java.util.List = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, list: typing.Union[java.util.Collection[org.openhab.core.persistence.dto.ItemHistoryDTO], typing.Sequence[org.openhab.core.persistence.dto.ItemHistoryDTO]]): ...
