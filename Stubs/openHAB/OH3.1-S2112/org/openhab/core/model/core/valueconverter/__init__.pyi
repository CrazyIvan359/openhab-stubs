import java.lang
import org.eclipse.xtext.conversion
import org.eclipse.xtext.nodemodel
import typing


class ValueTypeToStringConverter(org.eclipse.xtext.conversion.IValueConverter[typing.Any]):
    """
    Java class 'org.openhab.core.model.core.valueconverter.ValueTypeToStringConverter'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.eclipse.xtext.conversion.IValueConverter
    
      Constructors:
        * ValueTypeToStringConverter()
    
    """
    def __init__(self): ...
    @typing.overload
    def toString(self) -> java.lang.String: ...
    @typing.overload
    def toString(self, value: typing.Any) -> java.lang.String: ...
    def toValue(self, string: java.lang.String, node: org.eclipse.xtext.nodemodel.INode) -> typing.Any: ...
