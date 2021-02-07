import java.lang
import org.eclipse.emf.common.notify
import org.eclipse.emf.ecore
import org.eclipse.emf.ecore.impl
import org.eclipse.emf.ecore.resource.impl
import org.eclipse.xtext.xbase.impl
import org.openhab.core.model.script.script
import typing


class AbstractUnitImpl(org.eclipse.emf.ecore.impl.MinimalEObjectImpl.Container, org.openhab.core.model.script.script.AbstractUnit):
    """
    Java class 'org.openhab.core.model.script.script.impl.AbstractUnitImpl'
    
        Extends:
            org.eclipse.emf.ecore.impl.MinimalEObjectImpl$Container
    
        Interfaces:
            org.openhab.core.model.script.script.AbstractUnit
    
    """
    @typing.overload
    def eGet(self, eStructuralFeature: org.eclipse.emf.ecore.EStructuralFeature) -> typing.Any: ...
    @typing.overload
    def eGet(self, eStructuralFeature: org.eclipse.emf.ecore.EStructuralFeature, boolean: bool) -> typing.Any: ...
    @typing.overload
    def eGet(self, eStructuralFeature: org.eclipse.emf.ecore.EStructuralFeature, boolean: bool, boolean2: bool) -> typing.Any: ...
    @typing.overload
    def eGet(self, featureID: int, resolve: bool, coreType: bool) -> typing.Any: ...
    @typing.overload
    def eIsSet(self, eStructuralFeature: org.eclipse.emf.ecore.EStructuralFeature) -> bool: ...
    @typing.overload
    def eIsSet(self, featureID: int) -> bool: ...
    @typing.overload
    def eSet(self, eStructuralFeature: org.eclipse.emf.ecore.EStructuralFeature, object: typing.Any) -> None: ...
    @typing.overload
    def eSet(self, featureID: int, newValue: typing.Any) -> None: ...
    @typing.overload
    def eUnset(self, eStructuralFeature: org.eclipse.emf.ecore.EStructuralFeature) -> None: ...
    @typing.overload
    def eUnset(self, featureID: int) -> None: ...
    def getValue(self) -> java.lang.String: ...
    def setValue(self, newValue: java.lang.String) -> None: ...
    def toString(self) -> java.lang.String: ...

class QuantityLiteralImpl(org.eclipse.xtext.xbase.impl.XExpressionImpl, org.openhab.core.model.script.script.QuantityLiteral):
    """
    Java class 'org.openhab.core.model.script.script.impl.QuantityLiteralImpl'
    
        Extends:
            org.eclipse.xtext.xbase.impl.XExpressionImpl
    
        Interfaces:
            org.openhab.core.model.script.script.QuantityLiteral
    
    """
    def basicSetUnit(self, newUnit: org.openhab.core.model.script.script.AbstractUnit, msgs: org.eclipse.emf.common.notify.NotificationChain) -> org.eclipse.emf.common.notify.NotificationChain: ...
    @typing.overload
    def eGet(self, eStructuralFeature: org.eclipse.emf.ecore.EStructuralFeature) -> typing.Any: ...
    @typing.overload
    def eGet(self, eStructuralFeature: org.eclipse.emf.ecore.EStructuralFeature, boolean: bool) -> typing.Any: ...
    @typing.overload
    def eGet(self, eStructuralFeature: org.eclipse.emf.ecore.EStructuralFeature, boolean: bool, boolean2: bool) -> typing.Any: ...
    @typing.overload
    def eGet(self, featureID: int, resolve: bool, coreType: bool) -> typing.Any: ...
    @typing.overload
    def eInverseRemove(self, internalEObject: org.eclipse.emf.ecore.InternalEObject, int2: int, class_: typing.Type[typing.Any], notificationChain: org.eclipse.emf.common.notify.NotificationChain) -> org.eclipse.emf.common.notify.NotificationChain: ...
    @typing.overload
    def eInverseRemove(self, otherEnd: org.eclipse.emf.ecore.InternalEObject, featureID: int, msgs: org.eclipse.emf.common.notify.NotificationChain) -> org.eclipse.emf.common.notify.NotificationChain: ...
    @typing.overload
    def eIsSet(self, eStructuralFeature: org.eclipse.emf.ecore.EStructuralFeature) -> bool: ...
    @typing.overload
    def eIsSet(self, featureID: int) -> bool: ...
    @typing.overload
    def eSet(self, eStructuralFeature: org.eclipse.emf.ecore.EStructuralFeature, object: typing.Any) -> None: ...
    @typing.overload
    def eSet(self, featureID: int, newValue: typing.Any) -> None: ...
    @typing.overload
    def eUnset(self, eStructuralFeature: org.eclipse.emf.ecore.EStructuralFeature) -> None: ...
    @typing.overload
    def eUnset(self, featureID: int) -> None: ...
    def getUnit(self) -> org.openhab.core.model.script.script.AbstractUnit: ...
    def getValue(self) -> java.lang.String: ...
    def setUnit(self, newUnit: org.openhab.core.model.script.script.AbstractUnit) -> None: ...
    def setValue(self, newValue: java.lang.String) -> None: ...
    def toString(self) -> java.lang.String: ...

class ScriptFactoryImpl(org.eclipse.emf.ecore.impl.EFactoryImpl, org.openhab.core.model.script.script.ScriptFactory):
    """
    Java class 'org.openhab.core.model.script.script.impl.ScriptFactoryImpl'
    
        Extends:
            org.eclipse.emf.ecore.impl.EFactoryImpl
    
        Interfaces:
            org.openhab.core.model.script.script.ScriptFactory
    
      Constructors:
        * ScriptFactoryImpl()
    
    """
    def __init__(self): ...
    @typing.overload
    def create(self, eClass: org.eclipse.emf.ecore.EClass) -> org.eclipse.emf.ecore.EObject: ...
    @typing.overload
    def create(self, eDataType: org.eclipse.emf.ecore.EDataType) -> org.eclipse.emf.ecore.resource.impl.BinaryResourceImpl.DataConverter[typing.Any]: ...
    def createAbstractUnit(self) -> org.openhab.core.model.script.script.AbstractUnit: ...
    def createIDUnit(self) -> org.openhab.core.model.script.script.IDUnit: ...
    def createQuantityLiteral(self) -> org.openhab.core.model.script.script.QuantityLiteral: ...
    def createScript(self) -> org.openhab.core.model.script.script.Script: ...
    def createSpecificUnit(self) -> org.openhab.core.model.script.script.SpecificUnit: ...
    def createStringUnit(self) -> org.openhab.core.model.script.script.StringUnit: ...
    @classmethod
    def getPackage(cls) -> org.openhab.core.model.script.script.ScriptPackage: ...
    def getScriptPackage(self) -> org.openhab.core.model.script.script.ScriptPackage: ...
    @classmethod
    def init(cls) -> org.openhab.core.model.script.script.ScriptFactory: ...

class ScriptImpl(org.eclipse.xtext.xbase.impl.XBlockExpressionImpl, org.openhab.core.model.script.script.Script):
    """
    Java class 'org.openhab.core.model.script.script.impl.ScriptImpl'
    
        Extends:
            org.eclipse.xtext.xbase.impl.XBlockExpressionImpl
    
        Interfaces:
            org.openhab.core.model.script.script.Script
    
    """

class ScriptPackageImpl(org.eclipse.emf.ecore.impl.EPackageImpl, org.openhab.core.model.script.script.ScriptPackage):
    """
    Java class 'org.openhab.core.model.script.script.impl.ScriptPackageImpl'
    
        Extends:
            org.eclipse.emf.ecore.impl.EPackageImpl
    
        Interfaces:
            org.openhab.core.model.script.script.ScriptPackage
    
    """
    def createPackageContents(self) -> None: ...
    def getAbstractUnit(self) -> org.eclipse.emf.ecore.EClass: ...
    def getAbstractUnit_Value(self) -> org.eclipse.emf.ecore.EAttribute: ...
    def getIDUnit(self) -> org.eclipse.emf.ecore.EClass: ...
    def getQuantityLiteral(self) -> org.eclipse.emf.ecore.EClass: ...
    def getQuantityLiteral_Unit(self) -> org.eclipse.emf.ecore.EReference: ...
    def getQuantityLiteral_Value(self) -> org.eclipse.emf.ecore.EAttribute: ...
    def getScript(self) -> org.eclipse.emf.ecore.EClass: ...
    def getScriptFactory(self) -> org.openhab.core.model.script.script.ScriptFactory: ...
    def getSpecificUnit(self) -> org.eclipse.emf.ecore.EClass: ...
    def getStringUnit(self) -> org.eclipse.emf.ecore.EClass: ...
    @classmethod
    def init(cls) -> org.openhab.core.model.script.script.ScriptPackage: ...
    def initializePackageContents(self) -> None: ...

class IDUnitImpl(AbstractUnitImpl, org.openhab.core.model.script.script.IDUnit):
    """
    Java class 'org.openhab.core.model.script.script.impl.IDUnitImpl'
    
        Extends:
            org.openhab.core.model.script.script.impl.AbstractUnitImpl
    
        Interfaces:
            org.openhab.core.model.script.script.IDUnit
    
    """

class SpecificUnitImpl(AbstractUnitImpl, org.openhab.core.model.script.script.SpecificUnit):
    """
    Java class 'org.openhab.core.model.script.script.impl.SpecificUnitImpl'
    
        Extends:
            org.openhab.core.model.script.script.impl.AbstractUnitImpl
    
        Interfaces:
            org.openhab.core.model.script.script.SpecificUnit
    
    """

class StringUnitImpl(AbstractUnitImpl, org.openhab.core.model.script.script.StringUnit):
    """
    Java class 'org.openhab.core.model.script.script.impl.StringUnitImpl'
    
        Extends:
            org.openhab.core.model.script.script.impl.AbstractUnitImpl
    
        Interfaces:
            org.openhab.core.model.script.script.StringUnit
    
    """
