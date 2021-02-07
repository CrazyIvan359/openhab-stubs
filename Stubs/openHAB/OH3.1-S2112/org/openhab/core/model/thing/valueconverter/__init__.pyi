import java.lang
import org.eclipse.xtext.common.services
import org.eclipse.xtext.conversion
import org.eclipse.xtext.nodemodel
import typing


class ThingValueConverters(org.eclipse.xtext.common.services.DefaultTerminalConverters):
    """
    Java class 'org.openhab.core.model.thing.valueconverter.ThingValueConverters'
    
        Extends:
            org.eclipse.xtext.common.services.DefaultTerminalConverters
    
      Constructors:
        * ThingValueConverters()
    
    """
    def __init__(self): ...
    def UID(self) -> org.eclipse.xtext.conversion.IValueConverter[java.lang.String]: ...
    def ValueType(self) -> org.eclipse.xtext.conversion.IValueConverter[typing.Any]: ...

class UIDtoStringConverter(org.eclipse.xtext.conversion.IValueConverter[java.lang.String]):
    """
    Java class 'org.openhab.core.model.thing.valueconverter.UIDtoStringConverter'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.eclipse.xtext.conversion.IValueConverter
    
      Constructors:
        * UIDtoStringConverter()
    
    """
    def __init__(self): ...
    @typing.overload
    def toString(self) -> java.lang.String: ...
    @typing.overload
    def toString(self, object: typing.Any) -> java.lang.String: ...
    @typing.overload
    def toString(self, string: java.lang.String) -> java.lang.String: ...
    @typing.overload
    def toValue(self, string: java.lang.String, iNode: org.eclipse.xtext.nodemodel.INode) -> typing.Any: ...
    @typing.overload
    def toValue(self, string: java.lang.String, iNode: org.eclipse.xtext.nodemodel.INode) -> java.lang.String: ...
