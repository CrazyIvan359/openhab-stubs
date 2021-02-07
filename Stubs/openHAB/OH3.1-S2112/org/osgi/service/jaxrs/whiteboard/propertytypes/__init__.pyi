import java.lang
import java.lang.annotation
import typing


class JSONRequired(java.lang.annotation.Annotation):
    """
    Java class 'org.osgi.service.jaxrs.whiteboard.propertytypes.JSONRequired'
    
        Interfaces:
            java.lang.annotation.Annotation
    
      Attributes:
        FILTER (java.lang.String): final static field
    
    """
    FILTER: typing.ClassVar[java.lang.String] = ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def osgi_jaxrs_extension_select(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class JaxrsApplicationBase(java.lang.annotation.Annotation):
    """
    Java class 'org.osgi.service.jaxrs.whiteboard.propertytypes.JaxrsApplicationBase'
    
        Interfaces:
            java.lang.annotation.Annotation
    
      Attributes:
        PREFIX_ (java.lang.String): final static field
    
    """
    PREFIX_: typing.ClassVar[java.lang.String] = ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def value(self) -> java.lang.String: ...

class JaxrsApplicationSelect(java.lang.annotation.Annotation):
    """
    Java class 'org.osgi.service.jaxrs.whiteboard.propertytypes.JaxrsApplicationSelect'
    
        Interfaces:
            java.lang.annotation.Annotation
    
      Attributes:
        PREFIX_ (java.lang.String): final static field
    
    """
    PREFIX_: typing.ClassVar[java.lang.String] = ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def value(self) -> java.lang.String: ...

class JaxrsExtension(java.lang.annotation.Annotation):
    """
    Java class 'org.osgi.service.jaxrs.whiteboard.propertytypes.JaxrsExtension'
    
        Interfaces:
            java.lang.annotation.Annotation
    
      Attributes:
        PREFIX_ (java.lang.String): final static field
    
    """
    PREFIX_: typing.ClassVar[java.lang.String] = ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class JaxrsExtensionSelect(java.lang.annotation.Annotation):
    """
    Java class 'org.osgi.service.jaxrs.whiteboard.propertytypes.JaxrsExtensionSelect'
    
        Interfaces:
            java.lang.annotation.Annotation
    
      Attributes:
        PREFIX_ (java.lang.String): final static field
    
    """
    PREFIX_: typing.ClassVar[java.lang.String] = ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def value(self) -> typing.List[java.lang.String]: ...

class JaxrsMediaType(java.lang.annotation.Annotation):
    """
    Java class 'org.osgi.service.jaxrs.whiteboard.propertytypes.JaxrsMediaType'
    
        Interfaces:
            java.lang.annotation.Annotation
    
      Attributes:
        PREFIX_ (java.lang.String): final static field
    
    """
    PREFIX_: typing.ClassVar[java.lang.String] = ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def value(self) -> typing.List[java.lang.String]: ...

class JaxrsName(java.lang.annotation.Annotation):
    """
    Java class 'org.osgi.service.jaxrs.whiteboard.propertytypes.JaxrsName'
    
        Interfaces:
            java.lang.annotation.Annotation
    
      Attributes:
        PREFIX_ (java.lang.String): final static field
    
    """
    PREFIX_: typing.ClassVar[java.lang.String] = ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def value(self) -> java.lang.String: ...

class JaxrsResource(java.lang.annotation.Annotation):
    """
    Java class 'org.osgi.service.jaxrs.whiteboard.propertytypes.JaxrsResource'
    
        Interfaces:
            java.lang.annotation.Annotation
    
      Attributes:
        PREFIX_ (java.lang.String): final static field
    
    """
    PREFIX_: typing.ClassVar[java.lang.String] = ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class JaxrsWhiteboardTarget(java.lang.annotation.Annotation):
    """
    Java class 'org.osgi.service.jaxrs.whiteboard.propertytypes.JaxrsWhiteboardTarget'
    
        Interfaces:
            java.lang.annotation.Annotation
    
      Attributes:
        PREFIX_ (java.lang.String): final static field
    
    """
    PREFIX_: typing.ClassVar[java.lang.String] = ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def value(self) -> java.lang.String: ...
