import org.eclipse.xtext.common.services
import org.eclipse.xtext.conversion
import typing


class ItemValueConverters(org.eclipse.xtext.common.services.DefaultTerminalConverters):
    """
    Java class 'org.openhab.core.model.internal.valueconverter.ItemValueConverters'
    
        Extends:
            org.eclipse.xtext.common.services.DefaultTerminalConverters
    
      Constructors:
        * ItemValueConverters()
    
    """
    def __init__(self): ...
    def ValueType(self) -> org.eclipse.xtext.conversion.IValueConverter[typing.Any]: ...
