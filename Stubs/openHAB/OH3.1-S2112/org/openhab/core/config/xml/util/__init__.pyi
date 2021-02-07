import com.thoughtworks.xstream.converters
import com.thoughtworks.xstream.io
import java.lang
import java.net
import java.util
import typing


class ConverterAssertion(java.lang.Object):
    """
    Java class 'org.openhab.core.config.xml.util.ConverterAssertion'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def assertEndOfType(cls, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader) -> None: ...
    @classmethod
    def assertNeitherNullNorEmpty(cls, propertyName: java.lang.String, property: java.lang.String) -> None: ...
    @classmethod
    def assertNoAttribute(cls, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader) -> None: ...

class ConverterAttributeMapValidator(java.lang.Object):
    """
    Java class 'org.openhab.core.config.xml.util.ConverterAttributeMapValidator'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConverterAttributeMapValidator(java.lang.String[][])
        * ConverterAttributeMapValidator(java.util.Map)
    
    """
    @typing.overload
    def __init__(self, validationMaskTemplate: typing.List[typing.List[java.lang.String]]): ...
    @typing.overload
    def __init__(self, validationMaskTemplate: typing.Union[java.util.Map[java.lang.String, bool], typing.Mapping[java.lang.String, bool]]): ...
    @typing.overload
    def readValidatedAttributes(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader) -> java.util.Map[java.lang.String, java.lang.String]: ...
    @classmethod
    @typing.overload
    def readValidatedAttributes(cls, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, validationMaskTemplate: typing.Union[java.util.Map[java.lang.String, bool], typing.Mapping[java.lang.String, bool]]) -> java.util.Map[java.lang.String, java.lang.String]: ...

class ConverterValueMap(java.lang.Object):
    """
    Java class 'org.openhab.core.config.xml.util.ConverterValueMap'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConverterValueMap(com.thoughtworks.xstream.io.HierarchicalStreamReader, com.thoughtworks.xstream.converters.UnmarshallingContext)
        * ConverterValueMap(com.thoughtworks.xstream.io.HierarchicalStreamReader, int, com.thoughtworks.xstream.converters.UnmarshallingContext)
    
      Raises:
        com.thoughtworks.xstream.converters.ConversionException: from java
    
    """
    @typing.overload
    def __init__(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, context: com.thoughtworks.xstream.converters.UnmarshallingContext): ...
    @typing.overload
    def __init__(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, numberOfValues: int, context: com.thoughtworks.xstream.converters.UnmarshallingContext): ...
    @typing.overload
    def getBoolean(self, nodeName: java.lang.String) -> bool: ...
    @typing.overload
    def getBoolean(self, nodeName: java.lang.String, defaultValue: bool) -> bool: ...
    @typing.overload
    def getInteger(self, nodeName: java.lang.String) -> int: ...
    @typing.overload
    def getInteger(self, nodeName: java.lang.String, defaultValue: int) -> int: ...
    @typing.overload
    def getObject(self, nodeName: java.lang.String) -> typing.Any: ...
    @typing.overload
    def getObject(self, nodeName: java.lang.String, defaultValue: typing.Any) -> typing.Any: ...
    @typing.overload
    def getString(self, nodeName: java.lang.String) -> java.lang.String: ...
    @typing.overload
    def getString(self, nodeName: java.lang.String, defaultValue: java.lang.String) -> java.lang.String: ...
    def getValueMap(self) -> java.util.Map[java.lang.String, typing.Any]: ...
    @classmethod
    def readValueMap(cls, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, numberOfValues: int, context: com.thoughtworks.xstream.converters.UnmarshallingContext) -> java.util.Map[java.lang.String, typing.Any]: ...

_GenericUnmarshaller__T = typing.TypeVar('_GenericUnmarshaller__T')  # <T>
class GenericUnmarshaller(com.thoughtworks.xstream.converters.Converter, typing.Generic[_GenericUnmarshaller__T]):
    """
    Java class 'org.openhab.core.config.xml.util.GenericUnmarshaller'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            com.thoughtworks.xstream.converters.Converter
    
      Constructors:
        * GenericUnmarshaller(java.lang.Class)
    
    """
    def __init__(self, clazz: typing.Type[_GenericUnmarshaller__T]): ...
    def canConvert(self, paramClass: typing.Type) -> bool: ...
    def getResultType(self) -> typing.Type[typing.Any]: ...
    def marshal(self, value: typing.Any, writer: com.thoughtworks.xstream.io.HierarchicalStreamWriter, context: com.thoughtworks.xstream.converters.MarshallingContext) -> None: ...

class NodeIterator(java.util.Iterator[typing.Any]):
    """
    Java class 'org.openhab.core.config.xml.util.NodeIterator'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.util.Iterator
    
      Constructors:
        * NodeIterator(java.util.List)
    
    """
    def __init__(self, nodes: java.util.List[typing.Any]): ...
    def assertEndOfType(self) -> None: ...
    def hasNext(self) -> bool: ...
    @typing.overload
    def next(self) -> typing.Any: ...
    @typing.overload
    def next(self, nodeName: java.lang.String, required: bool) -> typing.Any: ...
    def nextAttribute(self, nodeName: java.lang.String, attributeName: java.lang.String, required: bool) -> java.lang.String: ...
    def nextList(self, nodeName: java.lang.String, required: bool) -> java.util.List[typing.Any]: ...
    def nextValue(self, nodeName: java.lang.String, required: bool) -> typing.Any: ...
    def remove(self) -> None: ...
    def revert(self) -> None: ...

class NodeName(java.lang.Object):
    """
    public interface NodeName
    
        The :class:`~org.openhab.core.config.xml.util.NodeName` interface defines common features for all :code:`Node`* classes.
    
        Each :code:`Node`* class has to return its node name.
    
    
    """
    def getNodeName(self) -> java.lang.String: ...

_XmlDocumentReader__T = typing.TypeVar('_XmlDocumentReader__T')  # <T>
class XmlDocumentReader(java.lang.Object, typing.Generic[_XmlDocumentReader__T]):
    """
    Java class 'org.openhab.core.config.xml.util.XmlDocumentReader'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * XmlDocumentReader()
    
    """
    def __init__(self): ...
    def readFromXML(self, xmlURL: java.net.URL) -> _XmlDocumentReader__T: ...

class NodeAttributes(NodeName):
    """
    Java class 'org.openhab.core.config.xml.util.NodeAttributes'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.xml.util.NodeName
    
      Constructors:
        * NodeAttributes(java.lang.String, java.util.Map)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
    """
    def __init__(self, nodeName: java.lang.String, attributes: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]): ...
    def getAttribute(self, name: java.lang.String) -> java.lang.String: ...
    def getAttributes(self) -> java.util.Map[java.lang.String, java.lang.String]: ...
    def getNodeName(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class NodeAttributesConverter(GenericUnmarshaller[NodeAttributes]):
    """
    Java class 'org.openhab.core.config.xml.util.NodeAttributesConverter'
    
        Extends:
            org.openhab.core.config.xml.util.GenericUnmarshaller
    
      Constructors:
        * NodeAttributesConverter()
    
    """
    def __init__(self): ...
    def unmarshal(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, context: com.thoughtworks.xstream.converters.UnmarshallingContext) -> typing.Any: ...

class NodeList(NodeName):
    """
    Java class 'org.openhab.core.config.xml.util.NodeList'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.xml.util.NodeName
    
      Constructors:
        * NodeList(java.lang.String, java.util.Map, java.util.List)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
    """
    def __init__(self, nodeName: java.lang.String, attributes: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]], list: java.util.List[typing.Any]): ...
    @typing.overload
    def getAttributes(self, nodeName: java.lang.String, attributeName: java.lang.String) -> java.util.List[java.lang.String]: ...
    @typing.overload
    def getAttributes(self, nodeName: java.lang.String, attributeName: java.lang.String, formattedText: java.lang.String) -> java.util.List[java.lang.String]: ...
    @typing.overload
    def getAttributes(self) -> java.util.Map[java.lang.String, java.lang.String]: ...
    def getList(self) -> java.util.List[typing.Any]: ...
    def getNodeName(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class NodeListConverter(GenericUnmarshaller[NodeList]):
    """
    Java class 'org.openhab.core.config.xml.util.NodeListConverter'
    
        Extends:
            org.openhab.core.config.xml.util.GenericUnmarshaller
    
      Constructors:
        * NodeListConverter()
    
    """
    def __init__(self): ...
    def unmarshal(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, context: com.thoughtworks.xstream.converters.UnmarshallingContext) -> typing.Any: ...

class NodeValue(NodeName):
    """
    Java class 'org.openhab.core.config.xml.util.NodeValue'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.xml.util.NodeName
    
      Constructors:
        * NodeValue(java.lang.String, java.util.Map, java.lang.Object)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
    """
    def __init__(self, nodeName: java.lang.String, attributes: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]], value: typing.Any): ...
    def getAttributes(self) -> java.util.Map[java.lang.String, java.lang.String]: ...
    def getNodeName(self) -> java.lang.String: ...
    def getValue(self) -> typing.Any: ...
    def toString(self) -> java.lang.String: ...

class NodeValueConverter(GenericUnmarshaller[NodeValue]):
    """
    Java class 'org.openhab.core.config.xml.util.NodeValueConverter'
    
        Extends:
            org.openhab.core.config.xml.util.GenericUnmarshaller
    
      Constructors:
        * NodeValueConverter()
    
    """
    def __init__(self): ...
    def unmarshal(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, context: com.thoughtworks.xstream.converters.UnmarshallingContext) -> typing.Any: ...
