import java
import java.lang
import java.lang.reflect
import typing


class Annotation(java.lang.Object):
    """
    public interface Annotation
    
        The common interface extended by all annotation types. Note that an interface that manually extends this one does *not*
        define an annotation type. Also note that this interface does not itself define an annotation type. More information
        about annotation types can be found in section 9.6 of "The Java™ Language Specification". The
        :class:`~java.lang.reflect.AnnotatedElement` interface discusses compatibility concerns when evolving an annotation type
        from being non-repeatable to being repeatable.
    
        Since:
            1.5
    
    
    """
    def annotationType(self) -> typing.Type['Annotation']: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class AnnotationFormatError(java.lang.Error):
    """
    Java class 'java.lang.annotation.AnnotationFormatError'
    
        Extends:
            java.lang.Error
    
      Constructors:
        * AnnotationFormatError(java.lang.String)
        * AnnotationFormatError(java.lang.String, java.lang.Throwable)
        * AnnotationFormatError(java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, string: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class AnnotationTypeMismatchException(java.lang.RuntimeException):
    """
    Java class 'java.lang.annotation.AnnotationTypeMismatchException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * AnnotationTypeMismatchException(java.lang.reflect.Method, java.lang.String)
    
    """
    def __init__(self, method: java.lang.reflect.Method, string: java.lang.String): ...
    def element(self) -> java.lang.reflect.Method: ...
    def foundType(self) -> java.lang.String: ...

class ElementType(java.lang.Enum[java.lang.annotation.ElementType]):
    """
    Java class 'java.lang.annotation.ElementType'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        TYPE (java.lang.annotation.ElementType): final static enum constant
        FIELD (java.lang.annotation.ElementType): final static enum constant
        METHOD (java.lang.annotation.ElementType): final static enum constant
        PARAMETER (java.lang.annotation.ElementType): final static enum constant
        CONSTRUCTOR (java.lang.annotation.ElementType): final static enum constant
        LOCAL_VARIABLE (java.lang.annotation.ElementType): final static enum constant
        ANNOTATION_TYPE (java.lang.annotation.ElementType): final static enum constant
        PACKAGE (java.lang.annotation.ElementType): final static enum constant
        TYPE_PARAMETER (java.lang.annotation.ElementType): final static enum constant
        TYPE_USE (java.lang.annotation.ElementType): final static enum constant
        MODULE (java.lang.annotation.ElementType): final static enum constant
    
    """
    TYPE: typing.ClassVar['ElementType'] = ...
    FIELD: typing.ClassVar['ElementType'] = ...
    METHOD: typing.ClassVar['ElementType'] = ...
    PARAMETER: typing.ClassVar['ElementType'] = ...
    CONSTRUCTOR: typing.ClassVar['ElementType'] = ...
    LOCAL_VARIABLE: typing.ClassVar['ElementType'] = ...
    ANNOTATION_TYPE: typing.ClassVar['ElementType'] = ...
    PACKAGE: typing.ClassVar['ElementType'] = ...
    TYPE_PARAMETER: typing.ClassVar['ElementType'] = ...
    TYPE_USE: typing.ClassVar['ElementType'] = ...
    MODULE: typing.ClassVar['ElementType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, string: java.lang.String) -> 'ElementType': ...
    @classmethod
    def values(cls) -> typing.List['ElementType']: ...

class IncompleteAnnotationException(java.lang.RuntimeException):
    """
    Java class 'java.lang.annotation.IncompleteAnnotationException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * IncompleteAnnotationException(java.lang.Class, java.lang.String)
    
    """
    def __init__(self, class_: typing.Type[Annotation], string: java.lang.String): ...
    def annotationType(self) -> typing.Type[Annotation]: ...
    def elementName(self) -> java.lang.String: ...

class RetentionPolicy(java.lang.Enum[java.lang.annotation.RetentionPolicy]):
    """
    Java class 'java.lang.annotation.RetentionPolicy'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        SOURCE (java.lang.annotation.RetentionPolicy): final static enum constant
        CLASS (java.lang.annotation.RetentionPolicy): final static enum constant
        RUNTIME (java.lang.annotation.RetentionPolicy): final static enum constant
    
    """
    SOURCE: typing.ClassVar['RetentionPolicy'] = ...
    CLASS: typing.ClassVar['RetentionPolicy'] = ...
    RUNTIME: typing.ClassVar['RetentionPolicy'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, string: java.lang.String) -> 'RetentionPolicy': ...
    @classmethod
    def values(cls) -> typing.List['RetentionPolicy']: ...

class Documented(Annotation):
    """
    Java class 'java.lang.annotation.Documented'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class Inherited(Annotation):
    """
    Java class 'java.lang.annotation.Inherited'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class Native(Annotation):
    """
    Java class 'java.lang.annotation.Native'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class Repeatable(Annotation):
    """
    Java class 'java.lang.annotation.Repeatable'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def value(self) -> typing.Type[Annotation]: ...

class Retention(Annotation):
    """
    Java class 'java.lang.annotation.Retention'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def value(self) -> RetentionPolicy: ...

class Target(Annotation):
    """
    Java class 'java.lang.annotation.Target'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def value(self) -> typing.List[ElementType]: ...
