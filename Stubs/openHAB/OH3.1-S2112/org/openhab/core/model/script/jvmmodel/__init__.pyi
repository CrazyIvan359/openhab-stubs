import java.lang
import java.util
import org.eclipse.emf.ecore
import org.eclipse.xtext.xbase
import org.eclipse.xtext.xbase.jvmmodel
import org.eclipse.xtext.xbase.typesystem.computation
import org.openhab.core.items
import org.openhab.core.model.core
import typing


class ScriptItemRefresher(org.openhab.core.items.ItemRegistryChangeListener):
    """
    Java class 'org.openhab.core.model.script.jvmmodel.ScriptItemRefresher'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.items.ItemRegistryChangeListener
    
      Constructors:
        * ScriptItemRefresher()
    
    """
    def __init__(self): ...
    @typing.overload
    def added(self, object: typing.Any) -> None: ...
    @typing.overload
    def added(self, element: org.openhab.core.items.Item) -> None: ...
    def allItemsChanged(self, oldItemNames: typing.Union[java.util.Collection[java.lang.String], typing.Sequence[java.lang.String]]) -> None: ...
    @typing.overload
    def removed(self, object: typing.Any) -> None: ...
    @typing.overload
    def removed(self, element: org.openhab.core.items.Item) -> None: ...
    def setItemRegistry(self, itemRegistry: org.openhab.core.items.ItemRegistry) -> None: ...
    def setModelRepository(self, modelRepository: org.openhab.core.model.core.ModelRepository) -> None: ...
    def unsetItemRegistry(self, itemRegistry: org.openhab.core.items.ItemRegistry) -> None: ...
    def unsetModelRepository(self, modelRepository: org.openhab.core.model.core.ModelRepository) -> None: ...
    @typing.overload
    def updated(self, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def updated(self, oldElement: org.openhab.core.items.Item, element: org.openhab.core.items.Item) -> None: ...

class ScriptJvmModelInferrer(org.eclipse.xtext.xbase.jvmmodel.AbstractModelInferrer):
    """
    Java class 'org.openhab.core.model.script.jvmmodel.ScriptJvmModelInferrer'
    
        Extends:
            org.eclipse.xtext.xbase.jvmmodel.AbstractModelInferrer
    
      Constructors:
        * ScriptJvmModelInferrer()
    
      Attributes:
        VAR_TRIGGERING_ITEM (java.lang.String): final static field
        VAR_TRIGGERING_ITEM_NAME (java.lang.String): final static field
        VAR_PREVIOUS_STATE (java.lang.String): final static field
        VAR_NEW_STATE (java.lang.String): final static field
        VAR_RECEIVED_COMMAND (java.lang.String): final static field
        VAR_RECEIVED_EVENT (java.lang.String): final static field
    
    """
    VAR_TRIGGERING_ITEM: typing.ClassVar[java.lang.String] = ...
    VAR_TRIGGERING_ITEM_NAME: typing.ClassVar[java.lang.String] = ...
    VAR_PREVIOUS_STATE: typing.ClassVar[java.lang.String] = ...
    VAR_NEW_STATE: typing.ClassVar[java.lang.String] = ...
    VAR_RECEIVED_COMMAND: typing.ClassVar[java.lang.String] = ...
    VAR_RECEIVED_EVENT: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    def infer(self, script: org.eclipse.emf.ecore.EObject, acceptor: org.eclipse.xtext.xbase.jvmmodel.IJvmDeclaredTypeAcceptor, isPreIndexingPhase: bool) -> None: ...

class ScriptTypeComputer(org.eclipse.xtext.xbase.typesystem.computation.XbaseTypeComputer):
    """
    Java class 'org.openhab.core.model.script.jvmmodel.ScriptTypeComputer'
    
        Extends:
            org.eclipse.xtext.xbase.typesystem.computation.XbaseTypeComputer
    
      Constructors:
        * ScriptTypeComputer()
    
    """
    def __init__(self): ...
    def computeTypes(self, expression: org.eclipse.xtext.xbase.XExpression, state: org.eclipse.xtext.xbase.typesystem.computation.ITypeComputationState) -> None: ...
