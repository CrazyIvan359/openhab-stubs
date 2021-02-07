import java.lang
import java.util
import java.util.function
import javax.ws.rs.core
import org.openhab.core.items
import org.openhab.core.items.dto
import org.openhab.core.types
import typing


class EnrichedItemDTO(org.openhab.core.items.dto.ItemDTO):
    """
    Java class 'org.openhab.core.io.rest.core.item.EnrichedItemDTO'
    
        Extends:
            org.openhab.core.items.dto.ItemDTO
    
      Constructors:
        * EnrichedItemDTO(org.openhab.core.items.dto.ItemDTO, java.lang.String, java.lang.String, java.lang.String, org.openhab.core.types.StateDescription, org.openhab.core.types.CommandDescription)
    
      Attributes:
        link (java.lang.String): field
        state (java.lang.String): field
        transformedState (java.lang.String): field
        stateDescription (org.openhab.core.types.StateDescription): field
        commandDescription (org.openhab.core.types.CommandDescription): field
        metadata (java.util.Map): field
        editable (java.lang.Boolean): field
    
    """
    link: java.lang.String = ...
    state: java.lang.String = ...
    transformedState: java.lang.String = ...
    stateDescription: org.openhab.core.types.StateDescription = ...
    commandDescription: org.openhab.core.types.CommandDescription = ...
    metadata: java.util.Map = ...
    editable: bool = ...
    def __init__(self, itemDTO: org.openhab.core.items.dto.ItemDTO, link: java.lang.String, state: java.lang.String, transformedState: java.lang.String, stateDescription: org.openhab.core.types.StateDescription, commandDescription: org.openhab.core.types.CommandDescription): ...

class EnrichedItemDTOMapper(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.core.item.EnrichedItemDTOMapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * EnrichedItemDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    def map(cls, item: org.openhab.core.items.Item, drillDown: bool, itemFilter: typing.Union[java.util.function.Predicate[org.openhab.core.items.Item], typing.Callable[[], org.openhab.core.items.Item]], uriBuilder: javax.ws.rs.core.UriBuilder, locale: java.util.Locale) -> EnrichedItemDTO: ...

class EnrichedGroupItemDTO(EnrichedItemDTO):
    """
    Java class 'org.openhab.core.io.rest.core.item.EnrichedGroupItemDTO'
    
        Extends:
            org.openhab.core.io.rest.core.item.EnrichedItemDTO
    
      Constructors:
        * EnrichedGroupItemDTO(org.openhab.core.items.dto.ItemDTO, org.openhab.core.io.rest.core.item.EnrichedItemDTO[], java.lang.String, java.lang.String, java.lang.String, org.openhab.core.types.StateDescription)
    
      Attributes:
        members ([Lorg.openhab.core.io.rest.core.item.EnrichedItemDTO;): field
        groupType (java.lang.String): field
        function (org.openhab.core.items.dto.GroupFunctionDTO): field
    
    """
    members: typing.List[EnrichedItemDTO] = ...
    groupType: java.lang.String = ...
    function: org.openhab.core.items.dto.GroupFunctionDTO = ...
    def __init__(self, itemDTO: org.openhab.core.items.dto.ItemDTO, members: typing.List[EnrichedItemDTO], link: java.lang.String, state: java.lang.String, transformedState: java.lang.String, stateDescription: org.openhab.core.types.StateDescription): ...
