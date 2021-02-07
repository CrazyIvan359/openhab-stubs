import java.lang
import java.util
import org.openhab.core.types


class ItemHistoryDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.persistence.dto.ItemHistoryDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ItemHistoryDTO()
    
      Attributes:
        name (java.lang.String): field
        totalrecords (java.lang.String): field
        datapoints (java.lang.String): field
        data (java.util.List): field
    
    """
    name: java.lang.String = ...
    totalrecords: java.lang.String = ...
    datapoints: java.lang.String = ...
    data: java.util.List = ...
    def __init__(self): ...
    def addData(self, time: int, state: org.openhab.core.types.State) -> None: ...
    class HistoryDataBean(java.lang.Object):
        """
        Java class 'org.openhab.core.persistence.dto.ItemHistoryDTO$HistoryDataBean'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * HistoryDataBean()
        
          Attributes:
            time (java.lang.Long): field
            state (java.lang.String): field
        
        """
        time: int = ...
        state: java.lang.String = ...
        def __init__(self): ...

class PersistenceServiceDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.persistence.dto.PersistenceServiceDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PersistenceServiceDTO()
    
      Attributes:
        id (java.lang.String): field
        label (java.lang.String): field
        type (java.lang.String): field
    
    """
    id: java.lang.String = ...
    label: java.lang.String = ...
    type: java.lang.String = ...
    def __init__(self): ...
