import java.lang
import java.util
import javax.measure
import javax.measure.format
import typing


_QuantityFactory__Q = typing.TypeVar('_QuantityFactory__Q', bound=javax.measure.Quantity)  # <Q>
class QuantityFactory(java.lang.Object, typing.Generic[_QuantityFactory__Q]):
    """
    Java class 'javax.measure.spi.QuantityFactory'
    
    """
    def create(self, number: java.lang.Number, unit: javax.measure.Unit[_QuantityFactory__Q]) -> javax.measure.Quantity[_QuantityFactory__Q]: ...
    def getSystemUnit(self) -> javax.measure.Unit[_QuantityFactory__Q]: ...

class ServiceProvider(java.lang.Object):
    """
    Java class 'javax.measure.spi.ServiceProvider'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def available(cls) -> java.util.List['ServiceProvider']: ...
    @classmethod
    def current(cls) -> 'ServiceProvider': ...
    def getPriority(self) -> int: ...
    _getQuantityFactory__Q = typing.TypeVar('_getQuantityFactory__Q', bound=javax.measure.Quantity)  # <Q>
    def getQuantityFactory(self, class_: typing.Type[_getQuantityFactory__Q]) -> QuantityFactory[_getQuantityFactory__Q]: ...
    def getSystemOfUnitsService(self) -> 'SystemOfUnitsService': ...
    def getUnitFormatService(self) -> 'UnitFormatService': ...
    @classmethod
    def setCurrent(cls, serviceProvider: 'ServiceProvider') -> 'ServiceProvider': ...

class SystemOfUnits(java.lang.Object):
    """
    Java class 'javax.measure.spi.SystemOfUnits'
    
    """
    def getName(self) -> java.lang.String: ...
    _getUnit__Q = typing.TypeVar('_getUnit__Q', bound=javax.measure.Quantity)  # <Q>
    def getUnit(self, class_: typing.Type[_getUnit__Q]) -> javax.measure.Unit[_getUnit__Q]: ...
    @typing.overload
    def getUnits(self) -> java.util.Set[javax.measure.Unit[typing.Any]]: ...
    @typing.overload
    def getUnits(self, dimension: javax.measure.Dimension) -> java.util.Set[javax.measure.Unit[typing.Any]]: ...

class SystemOfUnitsService(java.lang.Object):
    """
    Java class 'javax.measure.spi.SystemOfUnitsService'
    
    """
    def getAvailableSystemsOfUnits(self) -> java.util.Collection[SystemOfUnits]: ...
    @typing.overload
    def getSystemOfUnits(self) -> SystemOfUnits: ...
    @typing.overload
    def getSystemOfUnits(self, string: java.lang.String) -> SystemOfUnits: ...

class UnitFormatService(java.lang.Object):
    """
    Java class 'javax.measure.spi.UnitFormatService'
    
    """
    def getAvailableFormatNames(self) -> java.util.Set[java.lang.String]: ...
    @typing.overload
    def getUnitFormat(self) -> javax.measure.format.UnitFormat: ...
    @typing.overload
    def getUnitFormat(self, string: java.lang.String) -> javax.measure.format.UnitFormat: ...
