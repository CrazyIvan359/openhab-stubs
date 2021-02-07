import java.lang
import java.math
import org.openhab.core.library.types
import org.openhab.core.types
import typing


class NumberExtensions(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.lib.NumberExtensions'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * NumberExtensions()
    
      Attributes:
        NULL_DEFINITION (java.math.BigDecimal): final static field
    
    """
    NULL_DEFINITION: typing.ClassVar[java.math.BigDecimal] = ...
    def __init__(self): ...
    @classmethod
    def numberToBigDecimal(cls, number: java.lang.Number) -> java.math.BigDecimal: ...
    @classmethod
    @typing.overload
    def operator_divide(cls, x: java.lang.Number, y: java.lang.Number) -> java.math.BigDecimal: ...
    @classmethod
    @typing.overload
    def operator_divide(cls, x: java.lang.Number, y: org.openhab.core.library.types.QuantityType[typing.Any]) -> org.openhab.core.library.types.QuantityType[typing.Any]: ...
    @classmethod
    @typing.overload
    def operator_divide(cls, x: org.openhab.core.library.types.QuantityType[typing.Any], y: java.lang.Number) -> org.openhab.core.library.types.QuantityType[typing.Any]: ...
    @classmethod
    @typing.overload
    def operator_divide(cls, x: org.openhab.core.library.types.QuantityType[typing.Any], y: org.openhab.core.library.types.QuantityType[typing.Any]) -> org.openhab.core.library.types.QuantityType[typing.Any]: ...
    @classmethod
    @typing.overload
    def operator_equals(cls, left: java.lang.Number, right: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_equals(cls, left: org.openhab.core.library.types.QuantityType[typing.Any], right: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_equals(cls, left: org.openhab.core.library.types.QuantityType[typing.Any], right: org.openhab.core.library.types.QuantityType[typing.Any]) -> bool: ...
    @classmethod
    @typing.overload
    def operator_equals(cls, type: org.openhab.core.types.Type, x: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_greaterEqualsThan(cls, left: java.lang.Number, right: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_greaterEqualsThan(cls, x: org.openhab.core.library.types.QuantityType[typing.Any], y: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_greaterEqualsThan(cls, x: org.openhab.core.library.types.QuantityType[typing.Any], y: org.openhab.core.library.types.QuantityType[typing.Any]) -> bool: ...
    @classmethod
    @typing.overload
    def operator_greaterEqualsThan(cls, type: org.openhab.core.types.Type, x: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_greaterThan(cls, left: java.lang.Number, right: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_greaterThan(cls, x: org.openhab.core.library.types.QuantityType[typing.Any], y: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_greaterThan(cls, x: org.openhab.core.library.types.QuantityType[typing.Any], y: org.openhab.core.library.types.QuantityType[typing.Any]) -> bool: ...
    @classmethod
    @typing.overload
    def operator_greaterThan(cls, type: org.openhab.core.types.Type, x: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_lessEqualsThan(cls, left: java.lang.Number, right: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_lessEqualsThan(cls, x: org.openhab.core.library.types.QuantityType[typing.Any], y: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_lessEqualsThan(cls, x: org.openhab.core.library.types.QuantityType[typing.Any], y: org.openhab.core.library.types.QuantityType[typing.Any]) -> bool: ...
    @classmethod
    @typing.overload
    def operator_lessEqualsThan(cls, type: org.openhab.core.types.Type, x: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_lessThan(cls, left: java.lang.Number, right: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_lessThan(cls, x: org.openhab.core.library.types.QuantityType[typing.Any], y: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_lessThan(cls, x: org.openhab.core.library.types.QuantityType[typing.Any], y: org.openhab.core.library.types.QuantityType[typing.Any]) -> bool: ...
    @classmethod
    @typing.overload
    def operator_lessThan(cls, type: org.openhab.core.types.Type, x: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_minus(cls, x: java.lang.Number) -> java.math.BigDecimal: ...
    @classmethod
    @typing.overload
    def operator_minus(cls, x: java.lang.Number, y: java.lang.Number) -> java.math.BigDecimal: ...
    @classmethod
    @typing.overload
    def operator_minus(cls, x: org.openhab.core.library.types.QuantityType[typing.Any]) -> org.openhab.core.library.types.QuantityType[typing.Any]: ...
    @classmethod
    @typing.overload
    def operator_minus(cls, x: org.openhab.core.library.types.QuantityType[typing.Any], y: org.openhab.core.library.types.QuantityType[typing.Any]) -> org.openhab.core.library.types.QuantityType[typing.Any]: ...
    @classmethod
    @typing.overload
    def operator_multiply(cls, x: java.lang.Number, y: java.lang.Number) -> java.math.BigDecimal: ...
    @classmethod
    @typing.overload
    def operator_multiply(cls, x: java.lang.Number, y: org.openhab.core.library.types.QuantityType[typing.Any]) -> org.openhab.core.library.types.QuantityType[typing.Any]: ...
    @classmethod
    @typing.overload
    def operator_multiply(cls, x: org.openhab.core.library.types.QuantityType[typing.Any], y: java.lang.Number) -> org.openhab.core.library.types.QuantityType[typing.Any]: ...
    @classmethod
    @typing.overload
    def operator_multiply(cls, x: org.openhab.core.library.types.QuantityType[typing.Any], y: org.openhab.core.library.types.QuantityType[typing.Any]) -> org.openhab.core.library.types.QuantityType[typing.Any]: ...
    @classmethod
    @typing.overload
    def operator_notEquals(cls, left: java.lang.Number, right: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_notEquals(cls, left: org.openhab.core.library.types.QuantityType[typing.Any], right: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_notEquals(cls, left: org.openhab.core.library.types.QuantityType[typing.Any], right: org.openhab.core.library.types.QuantityType[typing.Any]) -> bool: ...
    @classmethod
    @typing.overload
    def operator_notEquals(cls, type: org.openhab.core.types.Type, x: java.lang.Number) -> bool: ...
    @classmethod
    @typing.overload
    def operator_plus(cls, x: java.lang.Number, y: java.lang.Number) -> java.math.BigDecimal: ...
    @classmethod
    @typing.overload
    def operator_plus(cls, x: org.openhab.core.library.types.QuantityType[typing.Any], y: org.openhab.core.library.types.QuantityType[typing.Any]) -> org.openhab.core.library.types.QuantityType[typing.Any]: ...
