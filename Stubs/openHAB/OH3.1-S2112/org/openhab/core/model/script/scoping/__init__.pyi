import java.lang
import org.eclipse.xtext.naming
import org.eclipse.xtext.xbase.scoping
import org.eclipse.xtext.xbase.scoping.batch
import org.openhab.core.types
import typing


class AbstractScriptScopeProvider(org.eclipse.xtext.xbase.scoping.batch.XbaseBatchScopeProvider):
    """
    Java class 'org.openhab.core.model.script.scoping.AbstractScriptScopeProvider'
    
        Extends:
            org.eclipse.xtext.xbase.scoping.batch.XbaseBatchScopeProvider
    
      Constructors:
        * AbstractScriptScopeProvider()
    
    """
    def __init__(self): ...

class ActionClassLoader(java.lang.ClassLoader):
    """
    Java class 'org.openhab.core.model.script.scoping.ActionClassLoader'
    
        Extends:
            java.lang.ClassLoader
    
      Constructors:
        * ActionClassLoader(java.lang.ClassLoader)
    
    """
    def __init__(self, cl: java.lang.ClassLoader): ...
    def loadClass(self, name: java.lang.String) -> typing.Type[typing.Any]: ...

class ScriptImplicitlyImportedTypes(org.eclipse.xtext.xbase.scoping.batch.ImplicitlyImportedFeatures):
    """
    Java class 'org.openhab.core.model.script.scoping.ScriptImplicitlyImportedTypes'
    
        Extends:
            org.eclipse.xtext.xbase.scoping.batch.ImplicitlyImportedFeatures
    
      Constructors:
        * ScriptImplicitlyImportedTypes()
    
    """
    def __init__(self): ...

class ScriptImportSectionNamespaceScopeProvider(org.eclipse.xtext.xbase.scoping.XImportSectionNamespaceScopeProvider):
    """
    Java class 'org.openhab.core.model.script.scoping.ScriptImportSectionNamespaceScopeProvider'
    
        Extends:
            org.eclipse.xtext.xbase.scoping.XImportSectionNamespaceScopeProvider
    
      Constructors:
        * ScriptImportSectionNamespaceScopeProvider()
    
      Attributes:
        CORE_LIBRARY_UNITS_PACKAGE (org.eclipse.xtext.naming.QualifiedName): final static field
        CORE_LIBRARY_TYPES_PACKAGE (org.eclipse.xtext.naming.QualifiedName): final static field
        CORE_LIBRARY_ITEMS_PACKAGE (org.eclipse.xtext.naming.QualifiedName): final static field
        CORE_ITEMS_PACKAGE (org.eclipse.xtext.naming.QualifiedName): final static field
        CORE_PERSISTENCE_PACKAGE (org.eclipse.xtext.naming.QualifiedName): final static field
        MODEL_SCRIPT_ACTIONS_PACKAGE (org.eclipse.xtext.naming.QualifiedName): final static field
        TIME_PACKAGE (org.eclipse.xtext.naming.QualifiedName): final static field
        QUANTITY_PACKAGE (org.eclipse.xtext.naming.QualifiedName): final static field
    
    """
    CORE_LIBRARY_UNITS_PACKAGE: typing.ClassVar[org.eclipse.xtext.naming.QualifiedName] = ...
    CORE_LIBRARY_TYPES_PACKAGE: typing.ClassVar[org.eclipse.xtext.naming.QualifiedName] = ...
    CORE_LIBRARY_ITEMS_PACKAGE: typing.ClassVar[org.eclipse.xtext.naming.QualifiedName] = ...
    CORE_ITEMS_PACKAGE: typing.ClassVar[org.eclipse.xtext.naming.QualifiedName] = ...
    CORE_PERSISTENCE_PACKAGE: typing.ClassVar[org.eclipse.xtext.naming.QualifiedName] = ...
    MODEL_SCRIPT_ACTIONS_PACKAGE: typing.ClassVar[org.eclipse.xtext.naming.QualifiedName] = ...
    TIME_PACKAGE: typing.ClassVar[org.eclipse.xtext.naming.QualifiedName] = ...
    QUANTITY_PACKAGE: typing.ClassVar[org.eclipse.xtext.naming.QualifiedName] = ...
    def __init__(self): ...

class StateAndCommandProvider(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.scoping.StateAndCommandProvider'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * StateAndCommandProvider()
    
    """
    def __init__(self): ...
    def getAllCommands(self) -> java.lang.Iterable[org.openhab.core.types.Command]: ...
    def getAllStates(self) -> java.lang.Iterable[org.openhab.core.types.State]: ...
    def getAllTypes(self) -> java.lang.Iterable[org.openhab.core.types.Type]: ...

class ScriptScopeProvider(AbstractScriptScopeProvider):
    """
    Java class 'org.openhab.core.model.script.scoping.ScriptScopeProvider'
    
        Extends:
            org.openhab.core.model.script.scoping.AbstractScriptScopeProvider
    
      Constructors:
        * ScriptScopeProvider()
    
    """
    def __init__(self): ...
