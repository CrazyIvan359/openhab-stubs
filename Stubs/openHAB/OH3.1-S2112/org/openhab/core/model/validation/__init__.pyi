import org.eclipse.xtext.validation
import org.openhab.core.model.items


class AbstractItemsValidator(org.eclipse.xtext.validation.AbstractDeclarativeValidator):
    """
    Java class 'org.openhab.core.model.validation.AbstractItemsValidator'
    
        Extends:
            org.eclipse.xtext.validation.AbstractDeclarativeValidator
    
      Constructors:
        * AbstractItemsValidator()
    
    """
    def __init__(self): ...

class ItemsValidator(AbstractItemsValidator):
    """
    Java class 'org.openhab.core.model.validation.ItemsValidator'
    
        Extends:
            org.openhab.core.model.validation.AbstractItemsValidator
    
      Constructors:
        * ItemsValidator()
    
    """
    def __init__(self): ...
    def checkDiemension(self, item: org.openhab.core.model.items.ModelItem) -> None: ...
    def checkItemName(self, item: org.openhab.core.model.items.ModelItem) -> None: ...
