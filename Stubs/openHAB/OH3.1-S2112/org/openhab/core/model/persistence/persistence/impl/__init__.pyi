import java.lang
import java.math
import org.eclipse.emf.common.notify
import org.eclipse.emf.common.util
import org.eclipse.emf.ecore
import org.eclipse.emf.ecore.impl
import org.eclipse.emf.ecore.resource.impl
import org.openhab.core.model.persistence.persistence
import typing


class AllConfigImpl(org.eclipse.emf.ecore.impl.MinimalEObjectImpl.Container, org.openhab.core.model.persistence.persistence.AllConfig):
    """
    Java class 'org.openhab.core.model.persistence.persistence.impl.AllConfigImpl'
    
        Extends:
            org.eclipse.emf.ecore.impl.MinimalEObjectImpl$Container
    
        Interfaces:
            org.openhab.core.model.persistence.persistence.AllConfig
    
    """

class FilterDetailsImpl(org.eclipse.emf.ecore.impl.MinimalEObjectImpl.Container, org.openhab.core.model.persistence.persistence.FilterDetails):
    """
    Java class 'org.openhab.core.model.persistence.persistence.impl.FilterDetailsImpl'
    
        Extends:
            org.eclipse.emf.ecore.impl.MinimalEObjectImpl$Container
    
        Interfaces:
            org.openhab.core.model.persistence.persistence.FilterDetails
    
    """

class FilterImpl(org.eclipse.emf.ecore.impl.MinimalEObjectImpl.Container, org.openhab.core.model.persistence.persistence.Filter):
    """
    Java class 'org.openhab.core.model.persistence.persistence.impl.FilterImpl'
    
        Extends:
            org.eclipse.emf.ecore.impl.MinimalEObjectImpl$Container
    
        Interfaces:
            org.openhab.core.model.persistence.persistence.Filter
    
    """
    def basicSetDefinition(self, newDefinition: org.openhab.core.model.persistence.persistence.FilterDetails, msgs: org.eclipse.emf.common.notify.NotificationChain) -> org.eclipse.emf.common.notify.NotificationChain: ...
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
    def getDefinition(self) -> org.openhab.core.model.persistence.persistence.FilterDetails: ...
    def getName(self) -> java.lang.String: ...
    def setDefinition(self, newDefinition: org.openhab.core.model.persistence.persistence.FilterDetails) -> None: ...
    def setName(self, newName: java.lang.String) -> None: ...
    def toString(self) -> java.lang.String: ...

class GroupConfigImpl(org.eclipse.emf.ecore.impl.MinimalEObjectImpl.Container, org.openhab.core.model.persistence.persistence.GroupConfig):
    """
    Java class 'org.openhab.core.model.persistence.persistence.impl.GroupConfigImpl'
    
        Extends:
            org.eclipse.emf.ecore.impl.MinimalEObjectImpl$Container
    
        Interfaces:
            org.openhab.core.model.persistence.persistence.GroupConfig
    
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
    def getGroup(self) -> java.lang.String: ...
    def setGroup(self, newGroup: java.lang.String) -> None: ...
    def toString(self) -> java.lang.String: ...

class ItemConfigImpl(org.eclipse.emf.ecore.impl.MinimalEObjectImpl.Container, org.openhab.core.model.persistence.persistence.ItemConfig):
    """
    Java class 'org.openhab.core.model.persistence.persistence.impl.ItemConfigImpl'
    
        Extends:
            org.eclipse.emf.ecore.impl.MinimalEObjectImpl$Container
    
        Interfaces:
            org.openhab.core.model.persistence.persistence.ItemConfig
    
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
    def getItem(self) -> java.lang.String: ...
    def setItem(self, newItem: java.lang.String) -> None: ...
    def toString(self) -> java.lang.String: ...

class PersistenceConfigurationImpl(org.eclipse.emf.ecore.impl.MinimalEObjectImpl.Container, org.openhab.core.model.persistence.persistence.PersistenceConfiguration):
    """
    Java class 'org.openhab.core.model.persistence.persistence.impl.PersistenceConfigurationImpl'
    
        Extends:
            org.eclipse.emf.ecore.impl.MinimalEObjectImpl$Container
    
        Interfaces:
            org.openhab.core.model.persistence.persistence.PersistenceConf
            iguration
    
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
    def getAlias(self) -> java.lang.String: ...
    def getFilters(self) -> org.eclipse.emf.common.util.EList[org.openhab.core.model.persistence.persistence.Filter]: ...
    def getItems(self) -> org.eclipse.emf.common.util.EList[org.eclipse.emf.ecore.EObject]: ...
    def getStrategies(self) -> org.eclipse.emf.common.util.EList[org.openhab.core.model.persistence.persistence.Strategy]: ...
    def setAlias(self, newAlias: java.lang.String) -> None: ...
    def toString(self) -> java.lang.String: ...

class PersistenceFactoryImpl(org.eclipse.emf.ecore.impl.EFactoryImpl, org.openhab.core.model.persistence.persistence.PersistenceFactory):
    """
    Java class 'org.openhab.core.model.persistence.persistence.impl.PersistenceFactoryImpl'
    
        Extends:
            org.eclipse.emf.ecore.impl.EFactoryImpl
    
        Interfaces:
            org.openhab.core.model.persistence.persistence.PersistenceFact
            ory
    
      Constructors:
        * PersistenceFactoryImpl()
    
    """
    def __init__(self): ...
    @typing.overload
    def create(self, eClass: org.eclipse.emf.ecore.EClass) -> org.eclipse.emf.ecore.EObject: ...
    @typing.overload
    def create(self, eDataType: org.eclipse.emf.ecore.EDataType) -> org.eclipse.emf.ecore.resource.impl.BinaryResourceImpl.DataConverter[typing.Any]: ...
    def createAllConfig(self) -> org.openhab.core.model.persistence.persistence.AllConfig: ...
    def createCronStrategy(self) -> org.openhab.core.model.persistence.persistence.CronStrategy: ...
    def createFilter(self) -> org.openhab.core.model.persistence.persistence.Filter: ...
    def createFilterDetails(self) -> org.openhab.core.model.persistence.persistence.FilterDetails: ...
    def createGroupConfig(self) -> org.openhab.core.model.persistence.persistence.GroupConfig: ...
    def createItemConfig(self) -> org.openhab.core.model.persistence.persistence.ItemConfig: ...
    def createPersistenceConfiguration(self) -> org.openhab.core.model.persistence.persistence.PersistenceConfiguration: ...
    def createPersistenceModel(self) -> org.openhab.core.model.persistence.persistence.PersistenceModel: ...
    def createStrategy(self) -> org.openhab.core.model.persistence.persistence.Strategy: ...
    def createThresholdFilter(self) -> org.openhab.core.model.persistence.persistence.ThresholdFilter: ...
    def createTimeFilter(self) -> org.openhab.core.model.persistence.persistence.TimeFilter: ...
    @classmethod
    def getPackage(cls) -> org.openhab.core.model.persistence.persistence.PersistencePackage: ...
    def getPersistencePackage(self) -> org.openhab.core.model.persistence.persistence.PersistencePackage: ...
    @classmethod
    def init(cls) -> org.openhab.core.model.persistence.persistence.PersistenceFactory: ...

class PersistenceModelImpl(org.eclipse.emf.ecore.impl.MinimalEObjectImpl.Container, org.openhab.core.model.persistence.persistence.PersistenceModel):
    """
    Java class 'org.openhab.core.model.persistence.persistence.impl.PersistenceModelImpl'
    
        Extends:
            org.eclipse.emf.ecore.impl.MinimalEObjectImpl$Container
    
        Interfaces:
            org.openhab.core.model.persistence.persistence.PersistenceMode
            l
    
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
    def getConfigs(self) -> org.eclipse.emf.common.util.EList[org.openhab.core.model.persistence.persistence.PersistenceConfiguration]: ...
    def getDefaults(self) -> org.eclipse.emf.common.util.EList[org.openhab.core.model.persistence.persistence.Strategy]: ...
    def getFilters(self) -> org.eclipse.emf.common.util.EList[org.openhab.core.model.persistence.persistence.Filter]: ...
    def getStrategies(self) -> org.eclipse.emf.common.util.EList[org.openhab.core.model.persistence.persistence.Strategy]: ...

class PersistencePackageImpl(org.eclipse.emf.ecore.impl.EPackageImpl, org.openhab.core.model.persistence.persistence.PersistencePackage):
    """
    Java class 'org.openhab.core.model.persistence.persistence.impl.PersistencePackageImpl'
    
        Extends:
            org.eclipse.emf.ecore.impl.EPackageImpl
    
        Interfaces:
            org.openhab.core.model.persistence.persistence.PersistencePack
            age
    
    """
    def createPackageContents(self) -> None: ...
    def getAllConfig(self) -> org.eclipse.emf.ecore.EClass: ...
    def getCronStrategy(self) -> org.eclipse.emf.ecore.EClass: ...
    def getCronStrategy_CronExpression(self) -> org.eclipse.emf.ecore.EAttribute: ...
    def getFilter(self) -> org.eclipse.emf.ecore.EClass: ...
    def getFilterDetails(self) -> org.eclipse.emf.ecore.EClass: ...
    def getFilter_Definition(self) -> org.eclipse.emf.ecore.EReference: ...
    def getFilter_Name(self) -> org.eclipse.emf.ecore.EAttribute: ...
    def getGroupConfig(self) -> org.eclipse.emf.ecore.EClass: ...
    def getGroupConfig_Group(self) -> org.eclipse.emf.ecore.EAttribute: ...
    def getItemConfig(self) -> org.eclipse.emf.ecore.EClass: ...
    def getItemConfig_Item(self) -> org.eclipse.emf.ecore.EAttribute: ...
    def getPersistenceConfiguration(self) -> org.eclipse.emf.ecore.EClass: ...
    def getPersistenceConfiguration_Alias(self) -> org.eclipse.emf.ecore.EAttribute: ...
    def getPersistenceConfiguration_Filters(self) -> org.eclipse.emf.ecore.EReference: ...
    def getPersistenceConfiguration_Items(self) -> org.eclipse.emf.ecore.EReference: ...
    def getPersistenceConfiguration_Strategies(self) -> org.eclipse.emf.ecore.EReference: ...
    def getPersistenceFactory(self) -> org.openhab.core.model.persistence.persistence.PersistenceFactory: ...
    def getPersistenceModel(self) -> org.eclipse.emf.ecore.EClass: ...
    def getPersistenceModel_Configs(self) -> org.eclipse.emf.ecore.EReference: ...
    def getPersistenceModel_Defaults(self) -> org.eclipse.emf.ecore.EReference: ...
    def getPersistenceModel_Filters(self) -> org.eclipse.emf.ecore.EReference: ...
    def getPersistenceModel_Strategies(self) -> org.eclipse.emf.ecore.EReference: ...
    def getStrategy(self) -> org.eclipse.emf.ecore.EClass: ...
    def getStrategy_Name(self) -> org.eclipse.emf.ecore.EAttribute: ...
    def getThresholdFilter(self) -> org.eclipse.emf.ecore.EClass: ...
    def getThresholdFilter_Percent(self) -> org.eclipse.emf.ecore.EAttribute: ...
    def getThresholdFilter_Value(self) -> org.eclipse.emf.ecore.EAttribute: ...
    def getTimeFilter(self) -> org.eclipse.emf.ecore.EClass: ...
    def getTimeFilter_Unit(self) -> org.eclipse.emf.ecore.EAttribute: ...
    def getTimeFilter_Value(self) -> org.eclipse.emf.ecore.EAttribute: ...
    @classmethod
    def init(cls) -> org.openhab.core.model.persistence.persistence.PersistencePackage: ...
    def initializePackageContents(self) -> None: ...

class StrategyImpl(org.eclipse.emf.ecore.impl.MinimalEObjectImpl.Container, org.openhab.core.model.persistence.persistence.Strategy):
    """
    Java class 'org.openhab.core.model.persistence.persistence.impl.StrategyImpl'
    
        Extends:
            org.eclipse.emf.ecore.impl.MinimalEObjectImpl$Container
    
        Interfaces:
            org.openhab.core.model.persistence.persistence.Strategy
    
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
    def getName(self) -> java.lang.String: ...
    def setName(self, newName: java.lang.String) -> None: ...
    def toString(self) -> java.lang.String: ...

class CronStrategyImpl(StrategyImpl, org.openhab.core.model.persistence.persistence.CronStrategy):
    """
    Java class 'org.openhab.core.model.persistence.persistence.impl.CronStrategyImpl'
    
        Extends:
            org.openhab.core.model.persistence.persistence.impl.StrategyImpl
    
        Interfaces:
            org.openhab.core.model.persistence.persistence.CronStrategy
    
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
    def getCronExpression(self) -> java.lang.String: ...
    def setCronExpression(self, newCronExpression: java.lang.String) -> None: ...
    def toString(self) -> java.lang.String: ...

class ThresholdFilterImpl(FilterDetailsImpl, org.openhab.core.model.persistence.persistence.ThresholdFilter):
    """
    Java class 'org.openhab.core.model.persistence.persistence.impl.ThresholdFilterImpl'
    
        Extends:
            org.openhab.core.model.persistence.persistence.impl.FilterDetailsImpl
    
        Interfaces:
            org.openhab.core.model.persistence.persistence.ThresholdFilter
    
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
    def getValue(self) -> java.math.BigDecimal: ...
    def isPercent(self) -> bool: ...
    def setPercent(self, newPercent: bool) -> None: ...
    def setValue(self, newValue: java.math.BigDecimal) -> None: ...
    def toString(self) -> java.lang.String: ...

class TimeFilterImpl(FilterDetailsImpl, org.openhab.core.model.persistence.persistence.TimeFilter):
    """
    Java class 'org.openhab.core.model.persistence.persistence.impl.TimeFilterImpl'
    
        Extends:
            org.openhab.core.model.persistence.persistence.impl.FilterDetailsImpl
    
        Interfaces:
            org.openhab.core.model.persistence.persistence.TimeFilter
    
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
    def getUnit(self) -> java.lang.String: ...
    def getValue(self) -> int: ...
    def setUnit(self, newUnit: java.lang.String) -> None: ...
    def setValue(self, newValue: int) -> None: ...
    def toString(self) -> java.lang.String: ...
