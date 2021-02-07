import java.lang
import java.util
import org.openhab.core.items
import typing


class GroupFunctionDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.items.dto.GroupFunctionDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * GroupFunctionDTO()
    
      Attributes:
        name (java.lang.String): field
        params ([Ljava.lang.String;): field
    
    """
    name: java.lang.String = ...
    params: typing.List[java.lang.String] = ...
    def __init__(self): ...

class ItemDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.items.dto.ItemDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ItemDTO()
    
      Attributes:
        type (java.lang.String): field
        name (java.lang.String): field
        label (java.lang.String): field
        category (java.lang.String): field
        tags (java.util.Set): field
        groupNames (java.util.List): field
    
    """
    type: java.lang.String = ...
    name: java.lang.String = ...
    label: java.lang.String = ...
    category: java.lang.String = ...
    tags: java.util.Set = ...
    groupNames: java.util.List = ...
    def __init__(self): ...

class ItemDTOMapper(java.lang.Object):
    """
    Java class 'org.openhab.core.items.dto.ItemDTOMapper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ItemDTOMapper()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def map(cls, itemDTO: ItemDTO, itemBuilderFactory: org.openhab.core.items.ItemBuilderFactory) -> org.openhab.core.items.Item: ...
    @classmethod
    @typing.overload
    def map(cls, item: org.openhab.core.items.Item) -> ItemDTO: ...
    @classmethod
    @typing.overload
    def mapFunction(cls, baseItem: org.openhab.core.items.Item, function: GroupFunctionDTO) -> org.openhab.core.items.GroupFunction: ...
    @classmethod
    @typing.overload
    def mapFunction(cls, function: org.openhab.core.items.GroupFunction) -> GroupFunctionDTO: ...

class MetadataDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.items.dto.MetadataDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MetadataDTO()
    
      Attributes:
        value (java.lang.String): field
        config (java.util.Map): field
    
    """
    value: java.lang.String = ...
    config: java.util.Map = ...
    def __init__(self): ...

class GroupItemDTO(ItemDTO):
    """
    Java class 'org.openhab.core.items.dto.GroupItemDTO'
    
        Extends:
            org.openhab.core.items.dto.ItemDTO
    
      Constructors:
        * GroupItemDTO()
    
      Attributes:
        groupType (java.lang.String): field
        function (org.openhab.core.items.dto.GroupFunctionDTO): field
    
    """
    groupType: java.lang.String = ...
    function: GroupFunctionDTO = ...
    def __init__(self): ...
