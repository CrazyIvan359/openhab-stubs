import java.lang
import java.util
import org.openhab.core.io.console
import org.openhab.core.io.console.extensions
import org.openhab.core.io.transport.serial
import org.openhab.core.io.transport.serial.internal
import typing


class SerialCommandExtension(org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension):
    """
    Java class 'org.openhab.core.io.transport.serial.internal.console.SerialCommandExtension'
    
        Extends:
            org.openhab.core.io.console.extensions.AbstractConsoleCommandExtension
    
      Constructors:
        * SerialCommandExtension(org.openhab.core.io.transport.serial.SerialPortManager, org.openhab.core.io.transport.serial.internal.SerialPortRegistry)
    
    """
    def __init__(self, serialPortManager: org.openhab.core.io.transport.serial.SerialPortManager, serialPortRegistry: org.openhab.core.io.transport.serial.internal.SerialPortRegistry): ...
    def execute(self, args: typing.List[java.lang.String], console: org.openhab.core.io.console.Console) -> None: ...
    def getUsages(self) -> java.util.List[java.lang.String]: ...
