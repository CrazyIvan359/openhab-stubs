import java.lang
import java.util
import org.openhab.core.io.transport.modbus
import typing


class WriteRequestJsonUtilities(java.lang.Object):
    """
    Java class 'org.openhab.core.io.transport.modbus.json.WriteRequestJsonUtilities'
    
        Extends:
            java.lang.Object
    
      Attributes:
        JSON_FUNCTION_CODE (java.lang.String): final static field
        JSON_ADDRESS (java.lang.String): final static field
        JSON_VALUE (java.lang.String): final static field
        JSON_MAX_TRIES (java.lang.String): final static field
        DEFAULT_MAX_TRIES (int): final static field
    
    """
    JSON_FUNCTION_CODE: typing.ClassVar[java.lang.String] = ...
    JSON_ADDRESS: typing.ClassVar[java.lang.String] = ...
    JSON_VALUE: typing.ClassVar[java.lang.String] = ...
    JSON_MAX_TRIES: typing.ClassVar[java.lang.String] = ...
    DEFAULT_MAX_TRIES: typing.ClassVar[int] = ...
    @classmethod
    def fromJson(cls, unitId: int, jsonString: java.lang.String) -> java.util.Collection[org.openhab.core.io.transport.modbus.ModbusWriteRequestBlueprint]: ...
