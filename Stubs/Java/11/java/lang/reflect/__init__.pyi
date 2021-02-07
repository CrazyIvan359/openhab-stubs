import java.io
import java.lang
import java.lang.annotation
import java.security
import typing


class AnnotatedElement(java.lang.Object):
    """
    public interface AnnotatedElement
    
        Represents an annotated element of the program currently running in this VM. This interface allows annotations to be
        read reflectively. All annotations returned by methods in this interface are immutable and serializable. The arrays
        returned by methods of this interface may be modified by callers without affecting the arrays returned to other callers.
    
        The :meth:`~java.lang.reflect.AnnotatedElement.getAnnotationsByType` and
        :meth:`~java.lang.reflect.AnnotatedElement.getDeclaredAnnotationsByType` methods support multiple annotations of the
        same type on an element. If the argument to either method is a repeatable annotation type (JLS 9.6), then the method
        will "look through" a container annotation (JLS 9.7), if present, and return any annotations inside the container.
        Container annotations may be generated at compile-time to wrap multiple annotations of the argument type.
    
        The terms *directly present*, *indirectly present*, *present*, and *associated* are used throughout this interface to
        describe precisely which annotations are returned by methods:
    
          - An annotation *A* is *directly present* on an element *E* if *E* has a :code:`RuntimeVisibleAnnotations` or
            :code:`RuntimeVisibleParameterAnnotations` or :code:`RuntimeVisibleTypeAnnotations` attribute, and the attribute
            contains *A*.
          - An annotation *A* is *indirectly present* on an element *E* if *E* has a :code:`RuntimeVisibleAnnotations` or
            :code:`RuntimeVisibleParameterAnnotations` or :code:`RuntimeVisibleTypeAnnotations` attribute, and *A* 's type is
            repeatable, and the attribute contains exactly one annotation whose value element contains *A* and whose type is the
            containing annotation type of *A* 's type.
          - An annotation *A* is present on an element *E* if either:
    
              - *A* is directly present on *E*; or
              - No annotation of *A* 's type is directly present on *E*, and *E* is a class, and *A* 's type is inheritable, and *A* is
                present on the superclass of *E*.
    
          - An annotation *A* is *associated* with an element *E* if either:
    
              - *A* is directly or indirectly present on *E*; or
              - No annotation of *A* 's type is directly or indirectly present on *E*, and *E* is a class, and *A*'s type is
                inheritable, and *A* is associated with the superclass of *E*.
    
    
    
        The table below summarizes which kind of annotation presence different methods in this interface examine.
    
        For an invocation of :code:`get[Declared]AnnotationsByType( Class < T >)`, the order of annotations which are directly
        or indirectly present on an element *E* is computed as if indirectly present annotations on *E* are directly present on
        *E* in place of their container annotation, in the order in which they appear in the value element of the container
        annotation.
    
        There are several compatibility concerns to keep in mind if an annotation type *T* is originally *not* repeatable and
        later modified to be repeatable. The containing annotation type for *T* is *TC*.
    
          - Modifying *T* to be repeatable is source and binary compatible with existing uses of *T* and with existing uses of *TC*.
            That is, for source compatibility, source code with annotations of type *T* or of type *TC* will still compile. For
            binary compatibility, class files with annotations of type *T* or of type *TC* (or with other kinds of uses of type *T*
            or of type *TC*) will link against the modified version of *T* if they linked against the earlier version. (An
            annotation type *TC* may informally serve as an acting containing annotation type before *T* is modified to be formally
            repeatable. Alternatively, when *T* is made repeatable, *TC* can be introduced as a new type.)
          - If an annotation type *TC* is present on an element, and *T* is modified to be repeatable with *TC* as its containing
            annotation type then:
    
              - The change to *T* is behaviorally compatible with respect to the :code:`get[Declared]Annotation(Class<T>)` (called with
                an argument of *T* or *TC*) and :code:`get[Declared]Annotations()` methods because the results of the methods will not
                change due to *TC* becoming the containing annotation type for *T*.
              - The change to *T* changes the results of the :code:`get[Declared]AnnotationsByType(Class<T>)` methods called with an
                argument of *T*, because those methods will now recognize an annotation of type *TC* as a container annotation for *T*
                and will "look through" it to expose annotations of type *T*.
    
          - If an annotation of type *T* is present on an element and *T* is made repeatable and more annotations of type *T* are
            added to the element:
    
              - The addition of the annotations of type *T* is both source compatible and binary compatible.
              - The addition of the annotations of type *T* changes the results of the :code:`get[Declared]Annotation(Class<T>)` methods
                and :code:`get[Declared]Annotations()` methods, because those methods will now only see a container annotation on the
                element and not see an annotation of type *T*.
              - The addition of the annotations of type *T* changes the results of the :code:`get[Declared]AnnotationsByType(Class<T>)`
                methods, because their results will expose the additional annotations of type *T* whereas previously they exposed only a
                single annotation of type *T*.
    
    
    
        If an annotation returned by a method in this interface contains (directly or indirectly) a
        :class:`~java.lang.Class`-valued member referring to a class that is not accessible in this VM, attempting to read the
        class by calling the relevant Class-returning method on the returned annotation will result in a
        :class:`~java.lang.TypeNotPresentException`.
    
        Similarly, attempting to read an enum-valued member will result in a :class:`~java.lang.EnumConstantNotPresentException`
        if the enum constant in the annotation is no longer present in the enum type.
    
        If an annotation type *T* is (meta-)annotated with an :code:`@Repeatable` annotation whose value element indicates a
        type *TC*, but *TC* does not declare a :code:`value()` method with a return type of *T*:code:`[]`, then an exception of
        type :class:`~java.lang.annotation.AnnotationFormatError` is thrown.
    
        Finally, attempting to read a member whose definition has evolved incompatibly will result in a
        :class:`~java.lang.annotation.AnnotationTypeMismatchException` or an
        :class:`~java.lang.annotation.IncompleteAnnotationException`.
    
        Since:
            1.5
    
        Also see:
            :class:`~java.lang.EnumConstantNotPresentException`, :class:`~java.lang.TypeNotPresentException`,
            :class:`~java.lang.annotation.AnnotationFormatError`, :class:`~java.lang.annotation.AnnotationTypeMismatchException`,
            :class:`~java.lang.annotation.IncompleteAnnotationException`
    
    
    """
    _getAnnotation__T = typing.TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: typing.Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    def getAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    _getAnnotationsByType__T = typing.TypeVar('_getAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotationsByType(self, class_: typing.Type[_getAnnotationsByType__T]) -> typing.List[_getAnnotationsByType__T]: ...
    _getDeclaredAnnotation__T = typing.TypeVar('_getDeclaredAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotation(self, class_: typing.Type[_getDeclaredAnnotation__T]) -> _getDeclaredAnnotation__T: ...
    def getDeclaredAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    _getDeclaredAnnotationsByType__T = typing.TypeVar('_getDeclaredAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotationsByType(self, class_: typing.Type[_getDeclaredAnnotationsByType__T]) -> typing.List[_getDeclaredAnnotationsByType__T]: ...
    def isAnnotationPresent(self, class_: typing.Type[java.lang.annotation.Annotation]) -> bool: ...

class Array(java.lang.Object):
    """
    Java class 'java.lang.reflect.Array'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def get(cls, object: typing.Any, int: int) -> typing.Any: ...
    @classmethod
    def getBoolean(cls, object: typing.Any, int: int) -> bool: ...
    @classmethod
    def getByte(cls, object: typing.Any, int: int) -> int: ...
    @classmethod
    def getChar(cls, object: typing.Any, int: int) -> str: ...
    @classmethod
    def getDouble(cls, object: typing.Any, int: int) -> float: ...
    @classmethod
    def getFloat(cls, object: typing.Any, int: int) -> float: ...
    @classmethod
    def getInt(cls, object: typing.Any, int: int) -> int: ...
    @classmethod
    def getLength(cls, object: typing.Any) -> int: ...
    @classmethod
    def getLong(cls, object: typing.Any, int: int) -> int: ...
    @classmethod
    def getShort(cls, object: typing.Any, int: int) -> int: ...
    @classmethod
    @typing.overload
    def newInstance(cls, class_: typing.Type[typing.Any], int: int) -> typing.Any: ...
    @classmethod
    @typing.overload
    def newInstance(cls, class_: typing.Type[typing.Any], intArray: typing.List[int]) -> typing.Any: ...
    @classmethod
    def set(cls, object: typing.Any, int: int, object2: typing.Any) -> None: ...
    @classmethod
    def setBoolean(cls, object: typing.Any, int: int, boolean: bool) -> None: ...
    @classmethod
    def setByte(cls, object: typing.Any, int: int, byte: int) -> None: ...
    @classmethod
    def setChar(cls, object: typing.Any, int: int, char: str) -> None: ...
    @classmethod
    def setDouble(cls, object: typing.Any, int: int, double: float) -> None: ...
    @classmethod
    def setFloat(cls, object: typing.Any, int: int, float: float) -> None: ...
    @classmethod
    def setInt(cls, object: typing.Any, int: int, int2: int) -> None: ...
    @classmethod
    def setLong(cls, object: typing.Any, int: int, long: int) -> None: ...
    @classmethod
    def setShort(cls, object: typing.Any, int: int, short: int) -> None: ...

class GenericSignatureFormatError(java.lang.ClassFormatError):
    """
    Java class 'java.lang.reflect.GenericSignatureFormatError'
    
        Extends:
            java.lang.ClassFormatError
    
      Constructors:
        * GenericSignatureFormatError()
        * GenericSignatureFormatError(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: java.lang.String): ...

class InaccessibleObjectException(java.lang.RuntimeException):
    """
    Java class 'java.lang.reflect.InaccessibleObjectException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * InaccessibleObjectException()
        * InaccessibleObjectException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: java.lang.String): ...

class InvocationHandler(java.lang.Object):
    """
    public interface InvocationHandler
    
        :code:`InvocationHandler` is the interface implemented by the *invocation handler* of a proxy instance.
    
        Each proxy instance has an associated invocation handler. When a method is invoked on a proxy instance, the method
        invocation is encoded and dispatched to the :code:`invoke` method of its invocation handler.
    
        Since:
            1.3
    
        Also see:
            :class:`~java.lang.reflect.Proxy`
    
    
    """
    def invoke(self, object: typing.Any, method: 'Method', objectArray: typing.List[typing.Any]) -> typing.Any: ...

class InvocationTargetException(java.lang.ReflectiveOperationException):
    """
    Java class 'java.lang.reflect.InvocationTargetException'
    
        Extends:
            java.lang.ReflectiveOperationException
    
      Constructors:
        * InvocationTargetException(java.lang.Throwable, java.lang.String)
        * InvocationTargetException(java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable, string: java.lang.String): ...
    def getCause(self) -> java.lang.Throwable: ...
    def getTargetException(self) -> java.lang.Throwable: ...

class MalformedParameterizedTypeException(java.lang.RuntimeException):
    """
    Java class 'java.lang.reflect.MalformedParameterizedTypeException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * MalformedParameterizedTypeException()
        * MalformedParameterizedTypeException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: java.lang.String): ...

class MalformedParametersException(java.lang.RuntimeException):
    """
    Java class 'java.lang.reflect.MalformedParametersException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * MalformedParametersException()
        * MalformedParametersException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: java.lang.String): ...

class Member(java.lang.Object):
    """
    public interface Member
    
        Member is an interface that reflects identifying information about a single member (a field or a method) or a
        constructor.
    
        Since:
            1.1
    
        Also see:
            :class:`~java.lang.Class`, :class:`~java.lang.reflect.Field`, :class:`~java.lang.reflect.Method`,
            :class:`~java.lang.reflect.Constructor`
    
    
    """
    PUBLIC: typing.ClassVar[int] = ...
    DECLARED: typing.ClassVar[int] = ...
    def getDeclaringClass(self) -> typing.Type[typing.Any]: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> java.lang.String: ...
    def isSynthetic(self) -> bool: ...

class Modifier(java.lang.Object):
    """
    Java class 'java.lang.reflect.Modifier'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Modifier()
    
      Attributes:
        PUBLIC (int): final static field
        PRIVATE (int): final static field
        PROTECTED (int): final static field
        STATIC (int): final static field
        FINAL (int): final static field
        SYNCHRONIZED (int): final static field
        VOLATILE (int): final static field
        TRANSIENT (int): final static field
        NATIVE (int): final static field
        INTERFACE (int): final static field
        ABSTRACT (int): final static field
        STRICT (int): final static field
    
    """
    PUBLIC: typing.ClassVar[int] = ...
    PRIVATE: typing.ClassVar[int] = ...
    PROTECTED: typing.ClassVar[int] = ...
    STATIC: typing.ClassVar[int] = ...
    FINAL: typing.ClassVar[int] = ...
    SYNCHRONIZED: typing.ClassVar[int] = ...
    VOLATILE: typing.ClassVar[int] = ...
    TRANSIENT: typing.ClassVar[int] = ...
    NATIVE: typing.ClassVar[int] = ...
    INTERFACE: typing.ClassVar[int] = ...
    ABSTRACT: typing.ClassVar[int] = ...
    STRICT: typing.ClassVar[int] = ...
    def __init__(self): ...
    @classmethod
    def classModifiers(cls) -> int: ...
    @classmethod
    def constructorModifiers(cls) -> int: ...
    @classmethod
    def fieldModifiers(cls) -> int: ...
    @classmethod
    def interfaceModifiers(cls) -> int: ...
    @classmethod
    def isAbstract(cls, int: int) -> bool: ...
    @classmethod
    def isFinal(cls, int: int) -> bool: ...
    @classmethod
    def isInterface(cls, int: int) -> bool: ...
    @classmethod
    def isNative(cls, int: int) -> bool: ...
    @classmethod
    def isPrivate(cls, int: int) -> bool: ...
    @classmethod
    def isProtected(cls, int: int) -> bool: ...
    @classmethod
    def isPublic(cls, int: int) -> bool: ...
    @classmethod
    def isStatic(cls, int: int) -> bool: ...
    @classmethod
    def isStrict(cls, int: int) -> bool: ...
    @classmethod
    def isSynchronized(cls, int: int) -> bool: ...
    @classmethod
    def isTransient(cls, int: int) -> bool: ...
    @classmethod
    def isVolatile(cls, int: int) -> bool: ...
    @classmethod
    def methodModifiers(cls) -> int: ...
    @classmethod
    def parameterModifiers(cls) -> int: ...
    @typing.overload
    def toString(self) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def toString(cls, int: int) -> java.lang.String: ...

class Proxy(java.io.Serializable):
    """
    Java class 'java.lang.reflect.Proxy'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
    """
    @classmethod
    def getInvocationHandler(cls, object: typing.Any) -> InvocationHandler: ...
    @classmethod
    def getProxyClass(cls, classLoader: java.lang.ClassLoader, classArray: typing.List[typing.Type[typing.Any]]) -> typing.Type[typing.Any]: ...
    @classmethod
    def isProxyClass(cls, class_: typing.Type[typing.Any]) -> bool: ...
    @classmethod
    def newProxyInstance(cls, classLoader: java.lang.ClassLoader, classArray: typing.List[typing.Type[typing.Any]], invocationHandler: InvocationHandler) -> typing.Any: ...

class ReflectPermission(java.security.BasicPermission):
    """
    Java class 'java.lang.reflect.ReflectPermission'
    
        Extends:
            java.security.BasicPermission
    
      Constructors:
        * ReflectPermission(java.lang.String)
        * ReflectPermission(java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, string: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, string2: java.lang.String): ...

class Type(java.lang.Object):
    """
    public interface Type
    
        Type is the common superinterface for all types in the Java programming language. These include raw types, parameterized
        types, array types, type variables and primitive types.
    
        Since:
            1.5
    
    
    """
    def getTypeName(self) -> java.lang.String: ...

class UndeclaredThrowableException(java.lang.RuntimeException):
    """
    Java class 'java.lang.reflect.UndeclaredThrowableException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * UndeclaredThrowableException(java.lang.Throwable)
        * UndeclaredThrowableException(java.lang.Throwable, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable, string: java.lang.String): ...
    def getCause(self) -> java.lang.Throwable: ...
    def getUndeclaredThrowable(self) -> java.lang.Throwable: ...

class AccessibleObject(AnnotatedElement):
    """
    Java class 'java.lang.reflect.AccessibleObject'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.lang.reflect.AnnotatedElement
    
    """
    def canAccess(self, object: typing.Any) -> bool: ...
    _getAnnotation__T = typing.TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: typing.Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    def getAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    _getAnnotationsByType__T = typing.TypeVar('_getAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotationsByType(self, class_: typing.Type[_getAnnotationsByType__T]) -> typing.List[_getAnnotationsByType__T]: ...
    _getDeclaredAnnotation__T = typing.TypeVar('_getDeclaredAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotation(self, class_: typing.Type[_getDeclaredAnnotation__T]) -> _getDeclaredAnnotation__T: ...
    def getDeclaredAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    _getDeclaredAnnotationsByType__T = typing.TypeVar('_getDeclaredAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotationsByType(self, class_: typing.Type[_getDeclaredAnnotationsByType__T]) -> typing.List[_getDeclaredAnnotationsByType__T]: ...
    def isAccessible(self) -> bool: ...
    def isAnnotationPresent(self, class_: typing.Type[java.lang.annotation.Annotation]) -> bool: ...
    @classmethod
    @typing.overload
    def setAccessible(cls, accessibleObjectArray: typing.List['AccessibleObject'], boolean: bool) -> None: ...
    @typing.overload
    def setAccessible(self, boolean: bool) -> None: ...
    def trySetAccessible(self) -> bool: ...

class AnnotatedType(AnnotatedElement):
    """
    Java class 'java.lang.reflect.AnnotatedType'
    
        Interfaces:
            java.lang.reflect.AnnotatedElement
    
    """
    def getAnnotatedOwnerType(self) -> 'AnnotatedType': ...
    def getType(self) -> Type: ...

class GenericArrayType(Type):
    """
    Java class 'java.lang.reflect.GenericArrayType'
    
        Interfaces:
            java.lang.reflect.Type
    
    """
    def getGenericComponentType(self) -> Type: ...

class GenericDeclaration(AnnotatedElement):
    """
    Java class 'java.lang.reflect.GenericDeclaration'
    
        Interfaces:
            java.lang.reflect.AnnotatedElement
    
    """
    def getTypeParameters(self) -> typing.List['TypeVariable'[typing.Any]]: ...

class Parameter(AnnotatedElement):
    """
    Java class 'java.lang.reflect.Parameter'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.lang.reflect.AnnotatedElement
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getAnnotatedType(self) -> AnnotatedType: ...
    _getAnnotation__T = typing.TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: typing.Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    def getAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    _getAnnotationsByType__T = typing.TypeVar('_getAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotationsByType(self, class_: typing.Type[_getAnnotationsByType__T]) -> typing.List[_getAnnotationsByType__T]: ...
    _getDeclaredAnnotation__T = typing.TypeVar('_getDeclaredAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotation(self, class_: typing.Type[_getDeclaredAnnotation__T]) -> _getDeclaredAnnotation__T: ...
    def getDeclaredAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    _getDeclaredAnnotationsByType__T = typing.TypeVar('_getDeclaredAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotationsByType(self, class_: typing.Type[_getDeclaredAnnotationsByType__T]) -> typing.List[_getDeclaredAnnotationsByType__T]: ...
    def getDeclaringExecutable(self) -> 'Executable': ...
    def getModifiers(self) -> int: ...
    def getName(self) -> java.lang.String: ...
    def getParameterizedType(self) -> Type: ...
    def getType(self) -> typing.Type[typing.Any]: ...
    def hashCode(self) -> int: ...
    def isImplicit(self) -> bool: ...
    def isNamePresent(self) -> bool: ...
    def isSynthetic(self) -> bool: ...
    def isVarArgs(self) -> bool: ...
    def toString(self) -> java.lang.String: ...

class ParameterizedType(Type):
    """
    Java class 'java.lang.reflect.ParameterizedType'
    
        Interfaces:
            java.lang.reflect.Type
    
    """
    def getActualTypeArguments(self) -> typing.List[Type]: ...
    def getOwnerType(self) -> Type: ...
    def getRawType(self) -> Type: ...

_TypeVariable__D = typing.TypeVar('_TypeVariable__D', bound=GenericDeclaration)  # <D>
class TypeVariable(Type, AnnotatedElement, typing.Generic[_TypeVariable__D]):
    """
    Java class 'java.lang.reflect.TypeVariable'
    
        Interfaces:
            java.lang.reflect.Type, java.lang.reflect.AnnotatedElement
    
    """
    def getAnnotatedBounds(self) -> typing.List[AnnotatedType]: ...
    def getBounds(self) -> typing.List[Type]: ...
    def getGenericDeclaration(self) -> _TypeVariable__D: ...
    def getName(self) -> java.lang.String: ...

class WildcardType(Type):
    """
    Java class 'java.lang.reflect.WildcardType'
    
        Interfaces:
            java.lang.reflect.Type
    
    """
    def getLowerBounds(self) -> typing.List[Type]: ...
    def getUpperBounds(self) -> typing.List[Type]: ...

class AnnotatedArrayType(AnnotatedType):
    """
    Java class 'java.lang.reflect.AnnotatedArrayType'
    
        Interfaces:
            java.lang.reflect.AnnotatedType
    
    """
    def getAnnotatedGenericComponentType(self) -> AnnotatedType: ...
    def getAnnotatedOwnerType(self) -> AnnotatedType: ...

class AnnotatedParameterizedType(AnnotatedType):
    """
    Java class 'java.lang.reflect.AnnotatedParameterizedType'
    
        Interfaces:
            java.lang.reflect.AnnotatedType
    
    """
    def getAnnotatedActualTypeArguments(self) -> typing.List[AnnotatedType]: ...
    def getAnnotatedOwnerType(self) -> AnnotatedType: ...

class AnnotatedTypeVariable(AnnotatedType):
    """
    Java class 'java.lang.reflect.AnnotatedTypeVariable'
    
        Interfaces:
            java.lang.reflect.AnnotatedType
    
    """
    def getAnnotatedBounds(self) -> typing.List[AnnotatedType]: ...
    def getAnnotatedOwnerType(self) -> AnnotatedType: ...

class AnnotatedWildcardType(AnnotatedType):
    """
    Java class 'java.lang.reflect.AnnotatedWildcardType'
    
        Interfaces:
            java.lang.reflect.AnnotatedType
    
    """
    def getAnnotatedLowerBounds(self) -> typing.List[AnnotatedType]: ...
    def getAnnotatedOwnerType(self) -> AnnotatedType: ...
    def getAnnotatedUpperBounds(self) -> typing.List[AnnotatedType]: ...

class Executable(AccessibleObject, Member, GenericDeclaration):
    """
    Java class 'java.lang.reflect.Executable'
    
        Extends:
            java.lang.reflect.AccessibleObject
    
        Interfaces:
            java.lang.reflect.Member, java.lang.reflect.GenericDeclaration
    
    """
    def getAnnotatedExceptionTypes(self) -> typing.List[AnnotatedType]: ...
    def getAnnotatedParameterTypes(self) -> typing.List[AnnotatedType]: ...
    def getAnnotatedReceiverType(self) -> AnnotatedType: ...
    def getAnnotatedReturnType(self) -> AnnotatedType: ...
    _getAnnotation__T = typing.TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: typing.Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    _getAnnotationsByType__T = typing.TypeVar('_getAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotationsByType(self, class_: typing.Type[_getAnnotationsByType__T]) -> typing.List[_getAnnotationsByType__T]: ...
    def getDeclaredAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    def getDeclaringClass(self) -> typing.Type[typing.Any]: ...
    def getExceptionTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getGenericExceptionTypes(self) -> typing.List[Type]: ...
    def getGenericParameterTypes(self) -> typing.List[Type]: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> java.lang.String: ...
    def getParameterAnnotations(self) -> typing.List[typing.List[java.lang.annotation.Annotation]]: ...
    def getParameterCount(self) -> int: ...
    def getParameterTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getParameters(self) -> typing.List[Parameter]: ...
    def getTypeParameters(self) -> typing.List[TypeVariable[typing.Any]]: ...
    def isSynthetic(self) -> bool: ...
    def isVarArgs(self) -> bool: ...
    def toGenericString(self) -> java.lang.String: ...

class Field(AccessibleObject, Member):
    """
    Java class 'java.lang.reflect.Field'
    
        Extends:
            java.lang.reflect.AccessibleObject
    
        Interfaces:
            java.lang.reflect.Member
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, object: typing.Any) -> typing.Any: ...
    def getAnnotatedType(self) -> AnnotatedType: ...
    _getAnnotation__T = typing.TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: typing.Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    _getAnnotationsByType__T = typing.TypeVar('_getAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotationsByType(self, class_: typing.Type[_getAnnotationsByType__T]) -> typing.List[_getAnnotationsByType__T]: ...
    def getBoolean(self, object: typing.Any) -> bool: ...
    def getByte(self, object: typing.Any) -> int: ...
    def getChar(self, object: typing.Any) -> str: ...
    def getDeclaredAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    def getDeclaringClass(self) -> typing.Type[typing.Any]: ...
    def getDouble(self, object: typing.Any) -> float: ...
    def getFloat(self, object: typing.Any) -> float: ...
    def getGenericType(self) -> Type: ...
    def getInt(self, object: typing.Any) -> int: ...
    def getLong(self, object: typing.Any) -> int: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> java.lang.String: ...
    def getShort(self, object: typing.Any) -> int: ...
    def getType(self) -> typing.Type[typing.Any]: ...
    def hashCode(self) -> int: ...
    def isEnumConstant(self) -> bool: ...
    def isSynthetic(self) -> bool: ...
    def set(self, object: typing.Any, object2: typing.Any) -> None: ...
    @classmethod
    @typing.overload
    def setAccessible(cls, accessibleObjectArray: typing.List[AccessibleObject], boolean: bool) -> None: ...
    @typing.overload
    def setAccessible(self, boolean: bool) -> None: ...
    def setBoolean(self, object: typing.Any, boolean: bool) -> None: ...
    def setByte(self, object: typing.Any, byte: int) -> None: ...
    def setChar(self, object: typing.Any, char: str) -> None: ...
    def setDouble(self, object: typing.Any, double: float) -> None: ...
    def setFloat(self, object: typing.Any, float: float) -> None: ...
    def setInt(self, object: typing.Any, int: int) -> None: ...
    def setLong(self, object: typing.Any, long: int) -> None: ...
    def setShort(self, object: typing.Any, short: int) -> None: ...
    def toGenericString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

_Constructor__T = typing.TypeVar('_Constructor__T')  # <T>
class Constructor(Executable, typing.Generic[_Constructor__T]):
    """
    Java class 'java.lang.reflect.Constructor'
    
        Extends:
            java.lang.reflect.Executable
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getAnnotatedReceiverType(self) -> AnnotatedType: ...
    def getAnnotatedReturnType(self) -> AnnotatedType: ...
    _getAnnotation__T = typing.TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: typing.Type[java.lang.annotation.Annotation]) -> java.lang.annotation.Annotation: ...
    def getDeclaredAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    def getDeclaringClass(self) -> typing.Type[_Constructor__T]: ...
    def getExceptionTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getGenericExceptionTypes(self) -> typing.List[Type]: ...
    def getGenericParameterTypes(self) -> typing.List[Type]: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> java.lang.String: ...
    def getParameterAnnotations(self) -> typing.List[typing.List[java.lang.annotation.Annotation]]: ...
    def getParameterCount(self) -> int: ...
    def getParameterTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getTypeParameters(self) -> typing.List[TypeVariable['Constructor'[_Constructor__T]]]: ...
    def hashCode(self) -> int: ...
    def isSynthetic(self) -> bool: ...
    def isVarArgs(self) -> bool: ...
    def newInstance(self, objectArray: typing.List[typing.Any]) -> _Constructor__T: ...
    @classmethod
    @typing.overload
    def setAccessible(cls, accessibleObjectArray: typing.List[AccessibleObject], boolean: bool) -> None: ...
    @typing.overload
    def setAccessible(self, boolean: bool) -> None: ...
    def toGenericString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class Method(Executable):
    """
    Java class 'java.lang.reflect.Method'
    
        Extends:
            java.lang.reflect.Executable
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getAnnotatedReturnType(self) -> AnnotatedType: ...
    _getAnnotation__T = typing.TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: typing.Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    def getDeclaredAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    def getDeclaringClass(self) -> typing.Type[typing.Any]: ...
    def getDefaultValue(self) -> typing.Any: ...
    def getExceptionTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getGenericExceptionTypes(self) -> typing.List[Type]: ...
    def getGenericParameterTypes(self) -> typing.List[Type]: ...
    def getGenericReturnType(self) -> Type: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> java.lang.String: ...
    def getParameterAnnotations(self) -> typing.List[typing.List[java.lang.annotation.Annotation]]: ...
    def getParameterCount(self) -> int: ...
    def getParameterTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getReturnType(self) -> typing.Type[typing.Any]: ...
    def getTypeParameters(self) -> typing.List[TypeVariable['Method']]: ...
    def hashCode(self) -> int: ...
    def invoke(self, object: typing.Any, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def isBridge(self) -> bool: ...
    def isDefault(self) -> bool: ...
    def isSynthetic(self) -> bool: ...
    def isVarArgs(self) -> bool: ...
    @classmethod
    @typing.overload
    def setAccessible(cls, accessibleObjectArray: typing.List[AccessibleObject], boolean: bool) -> None: ...
    @typing.overload
    def setAccessible(self, boolean: bool) -> None: ...
    def toGenericString(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...