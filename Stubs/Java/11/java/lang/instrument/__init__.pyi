import java.lang
import java.security
import java.util
import java.util.jar
import typing


class ClassDefinition(java.lang.Object):
    """
    Java class 'java.lang.instrument.ClassDefinition'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ClassDefinition(java.lang.Class, byte[])
    
    """
    def __init__(self, class_: typing.Type[typing.Any], byteArray: typing.List[int]): ...
    def getDefinitionClass(self) -> typing.Type[typing.Any]: ...
    def getDefinitionClassFile(self) -> typing.List[int]: ...

class ClassFileTransformer(java.lang.Object):
    """
    public interface ClassFileTransformer
    
        A transformer of class files. An agent registers an implementation of this interface using the
        :meth:`~java.lang.instrument.Instrumentation.addTransformer` method so that the transformer's
        :meth:`~java.lang.instrument.ClassFileTransformer.transform` method is invoked when classes are loaded,
        :meth:`~java.lang.instrument.Instrumentation.redefineClasses`, or
        :meth:`~java.lang.instrument.Instrumentation.retransformClasses`. The implementation should override one of the
        :code:`transform` methods defined here. Transformers are invoked before the class is defined by the Java virtual
        machine.
    
        There are two kinds of transformers, determined by the :code:`canRetransform` parameter of
        :meth:`~java.lang.instrument.Instrumentation.addTransformer`:
    
          - *retransformation capable* transformers that were added with :code:`canRetransform` as true
          - *retransformation incapable* transformers that were added with :code:`canRetransform` as false or where added with
            :meth:`~java.lang.instrument.Instrumentation.addTransformer`
    
    
        Once a transformer has been registered with :meth:`~java.lang.instrument.Instrumentation.addTransformer`, the
        transformer will be called for every new class definition and every class redefinition. Retransformation capable
        transformers will also be called on every class retransformation. The request for a new class definition is made with
        :meth:`~java.lang.ClassLoader.defineClass` or its native equivalents. The request for a class redefinition is made with
        :meth:`~java.lang.instrument.Instrumentation.redefineClasses` or its native equivalents. The request for a class
        retransformation is made with :meth:`~java.lang.instrument.Instrumentation.retransformClasses` or its native
        equivalents. The transformer is called during the processing of the request, before the class file bytes have been
        verified or applied. When there are multiple transformers, transformations are composed by chaining the
        :code:`transform` calls. That is, the byte array returned by one call to :code:`transform` becomes the input (via the
        :code:`classfileBuffer` parameter) to the next call.
    
        Transformations are applied in the following order:
    
          - Retransformation incapable transformers
          - Retransformation incapable native transformers
          - Retransformation capable transformers
          - Retransformation capable native transformers
    
    
        For retransformations, the retransformation incapable transformers are not called, instead the result of the previous
        transformation is reused. In all other cases, this method is called. Within each of these groupings, transformers are
        called in the order registered. Native transformers are provided by the :code:`ClassFileLoadHook` event in the Java
        Virtual Machine Tool Interface).
    
        The input (via the :code:`classfileBuffer` parameter) to the first transformer is:
    
          - for new class definition, the bytes passed to :code:`ClassLoader.defineClass`
          - for class redefinition, :code:`definitions.getDefinitionClassFile()` where :code:`definitions` is the parameter to
            :meth:`~java.lang.instrument.Instrumentation.redefineClasses`
          - for class retransformation, the bytes passed to the new class definition or, if redefined, the last redefinition, with
            all transformations made by retransformation incapable transformers reapplied automatically and unaltered; for details
            see :meth:`~java.lang.instrument.Instrumentation.retransformClasses`
    
    
        If the implementing method determines that no transformations are needed, it should return :code:`null`. Otherwise, it
        should create a new :code:`byte[]` array, copy the input :code:`classfileBuffer` into it, along with all desired
        transformations, and return the new array. The input :code:`classfileBuffer` must not be modified.
    
        In the retransform and redefine cases, the transformer must support the redefinition semantics: if a class that the
        transformer changed during initial definition is later retransformed or redefined, the transformer must insure that the
        second class output class file is a legal redefinition of the first output class file.
    
        If the transformer throws an exception (which it doesn't catch), subsequent transformers will still be called and the
        load, redefine or retransform will still be attempted. Thus, throwing an exception has the same effect as returning
        :code:`null`. To prevent unexpected behavior when unchecked exceptions are generated in transformer code, a transformer
        can catch :code:`Throwable`. If the transformer believes the :code:`classFileBuffer` does not represent a validly
        formatted class file, it should throw an :code:`IllegalClassFormatException`; while this has the same effect as
        returning null. it facilitates the logging or debugging of format corruptions.
    
        Note the term *class file* is used as defined in section 3.1 of "The Java™ Virtual Machine Specification", to mean a
        sequence of bytes in class file format, whether or not they reside in a file.
    
        Since:
            1.5
    
        Also see:
            :class:`~java.lang.instrument.Instrumentation`
    
    
    """
    @typing.overload
    def transform(self, classLoader: java.lang.ClassLoader, string: java.lang.String, class2: typing.Type[typing.Any], protectionDomain: java.security.ProtectionDomain, byteArray: typing.List[int]) -> typing.List[int]: ...
    @typing.overload
    def transform(self, module: java.lang.Module, classLoader: java.lang.ClassLoader, string: java.lang.String, class2: typing.Type[typing.Any], protectionDomain: java.security.ProtectionDomain, byteArray: typing.List[int]) -> typing.List[int]: ...

class IllegalClassFormatException(java.lang.Exception):
    """
    Java class 'java.lang.instrument.IllegalClassFormatException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * IllegalClassFormatException()
        * IllegalClassFormatException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: java.lang.String): ...

class Instrumentation(java.lang.Object):
    """
    public interface Instrumentation
    
        This class provides services needed to instrument Java programming language code. Instrumentation is the addition of
        byte-codes to methods for the purpose of gathering data to be utilized by tools. Since the changes are purely additive,
        these tools do not modify application state or behavior. Examples of such benign tools include monitoring agents,
        profilers, coverage analyzers, and event loggers.
    
        There are two ways to obtain an instance of the :code:`Instrumentation` interface:
    
          1.  
            When a JVM is launched in a way that indicates an agent class. In that case an :code:`Instrumentation` instance is
            passed to the :code:`premain` method of the agent class.
          2.  
            When a JVM provides a mechanism to start agents sometime after the JVM is launched. In that case an
            :code:`Instrumentation` instance is passed to the :code:`agentmain` method of the agent code.
    
    
        These mechanisms are described in the :class:`~java.lang.instrument.package`.
    
        Once an agent acquires an :code:`Instrumentation` instance, the agent may call methods on the instance at any time.
    
        Since:
            1.5
    
    
    """
    @typing.overload
    def addTransformer(self, classFileTransformer: ClassFileTransformer) -> None: ...
    @typing.overload
    def addTransformer(self, classFileTransformer: ClassFileTransformer, boolean: bool) -> None: ...
    def appendToBootstrapClassLoaderSearch(self, jarFile: java.util.jar.JarFile) -> None: ...
    def appendToSystemClassLoaderSearch(self, jarFile: java.util.jar.JarFile) -> None: ...
    def getAllLoadedClasses(self) -> typing.List[typing.Type]: ...
    def getInitiatedClasses(self, classLoader: java.lang.ClassLoader) -> typing.List[typing.Type]: ...
    def getObjectSize(self, object: typing.Any) -> int: ...
    def isModifiableClass(self, class_: typing.Type[typing.Any]) -> bool: ...
    def isModifiableModule(self, module: java.lang.Module) -> bool: ...
    def isNativeMethodPrefixSupported(self) -> bool: ...
    def isRedefineClassesSupported(self) -> bool: ...
    def isRetransformClassesSupported(self) -> bool: ...
    def redefineClasses(self, classDefinitionArray: typing.List[ClassDefinition]) -> None: ...
    def redefineModule(self, module: java.lang.Module, set: java.util.Set[java.lang.Module], map: typing.Union[java.util.Map[java.lang.String, java.util.Set[java.lang.Module]], typing.Mapping[java.lang.String, java.util.Set[java.lang.Module]]], map2: typing.Union[java.util.Map[java.lang.String, java.util.Set[java.lang.Module]], typing.Mapping[java.lang.String, java.util.Set[java.lang.Module]]], set2: java.util.Set[typing.Type[typing.Any]], map3: typing.Union[java.util.Map[typing.Type[typing.Any], java.util.List[typing.Type[typing.Any]]], typing.Mapping[typing.Type[typing.Any], java.util.List[typing.Type[typing.Any]]]]) -> None: ...
    def removeTransformer(self, classFileTransformer: ClassFileTransformer) -> bool: ...
    def retransformClasses(self, classArray: typing.List[typing.Type[typing.Any]]) -> None: ...
    def setNativeMethodPrefix(self, classFileTransformer: ClassFileTransformer, string: java.lang.String) -> None: ...

class UnmodifiableClassException(java.lang.Exception):
    """
    Java class 'java.lang.instrument.UnmodifiableClassException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * UnmodifiableClassException()
        * UnmodifiableClassException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: java.lang.String): ...

class UnmodifiableModuleException(java.lang.RuntimeException):
    """
    Java class 'java.lang.instrument.UnmodifiableModuleException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * UnmodifiableModuleException()
        * UnmodifiableModuleException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: java.lang.String): ...
