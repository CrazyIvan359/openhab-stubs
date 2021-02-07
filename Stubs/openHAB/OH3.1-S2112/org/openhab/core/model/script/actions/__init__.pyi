import java.lang
import java.time
import java.util
import org.eclipse.xtext.xbase.lib
import org.openhab.core.items
import org.openhab.core.library.types
import org.openhab.core.thing
import org.openhab.core.thing.binding
import org.openhab.core.types
import typing


class Audio(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.actions.Audio'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Audio()
    
    """
    def __init__(self): ...
    @classmethod
    def decreaseMasterVolume(cls, percent: float) -> None: ...
    @classmethod
    def getMasterVolume(cls) -> float: ...
    @classmethod
    def increaseMasterVolume(cls, percent: float) -> None: ...
    @classmethod
    @typing.overload
    def playSound(cls, filename: java.lang.String) -> None: ...
    @classmethod
    @typing.overload
    def playSound(cls, sink: java.lang.String, filename: java.lang.String) -> None: ...
    @classmethod
    @typing.overload
    def playSound(cls, sink: java.lang.String, filename: java.lang.String, volume: org.openhab.core.library.types.PercentType) -> None: ...
    @classmethod
    @typing.overload
    def playSound(cls, filename: java.lang.String, volume: org.openhab.core.library.types.PercentType) -> None: ...
    @classmethod
    @typing.overload
    def playStream(cls, url: java.lang.String) -> None: ...
    @classmethod
    @typing.overload
    def playStream(cls, sink: java.lang.String, url: java.lang.String) -> None: ...
    @classmethod
    @typing.overload
    def setMasterVolume(cls, volume: float) -> None: ...
    @classmethod
    @typing.overload
    def setMasterVolume(cls, percent: org.openhab.core.library.types.PercentType) -> None: ...

class BusEvent(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.actions.BusEvent'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * BusEvent()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def postUpdate(cls, itemName: java.lang.String, stateString: java.lang.String) -> typing.Any: ...
    @classmethod
    @typing.overload
    def postUpdate(cls, item: org.openhab.core.items.Item, state: java.lang.Number) -> typing.Any: ...
    @classmethod
    @typing.overload
    def postUpdate(cls, item: org.openhab.core.items.Item, stateAsString: java.lang.String) -> typing.Any: ...
    @classmethod
    @typing.overload
    def postUpdate(cls, item: org.openhab.core.items.Item, state: org.openhab.core.types.State) -> typing.Any: ...
    @classmethod
    def restoreStates(cls, statesMap: typing.Union[java.util.Map[org.openhab.core.items.Item, org.openhab.core.types.State], typing.Mapping[org.openhab.core.items.Item, org.openhab.core.types.State]]) -> typing.Any: ...
    @classmethod
    @typing.overload
    def sendCommand(cls, itemName: java.lang.String, commandString: java.lang.String) -> typing.Any: ...
    @classmethod
    @typing.overload
    def sendCommand(cls, item: org.openhab.core.items.Item, number: java.lang.Number) -> typing.Any: ...
    @classmethod
    @typing.overload
    def sendCommand(cls, item: org.openhab.core.items.Item, commandString: java.lang.String) -> typing.Any: ...
    @classmethod
    @typing.overload
    def sendCommand(cls, item: org.openhab.core.items.Item, command: org.openhab.core.types.Command) -> typing.Any: ...
    @classmethod
    def storeStates(cls, items: typing.List[org.openhab.core.items.Item]) -> java.util.Map[org.openhab.core.items.Item, org.openhab.core.types.State]: ...

class Ephemeris(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.actions.Ephemeris'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Ephemeris()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def getBankHolidayName(cls) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def getBankHolidayName(cls, offset: int) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def getBankHolidayName(cls, offset: int, filename: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def getBankHolidayName(cls, filename: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def getBankHolidayName(cls, day: java.time.ZonedDateTime) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def getBankHolidayName(cls, day: java.time.ZonedDateTime, filename: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def getDaysUntil(cls, searchedHoliday: java.lang.String) -> int: ...
    @classmethod
    @typing.overload
    def getDaysUntil(cls, searchedHoliday: java.lang.String, filename: java.lang.String) -> int: ...
    @classmethod
    @typing.overload
    def getDaysUntil(cls, day: java.time.ZonedDateTime, searchedHoliday: java.lang.String) -> int: ...
    @classmethod
    @typing.overload
    def getDaysUntil(cls, day: java.time.ZonedDateTime, searchedHoliday: java.lang.String, filename: java.lang.String) -> int: ...
    @classmethod
    def getHolidayDescription(cls, holiday: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def getNextBankHoliday(cls) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def getNextBankHoliday(cls, offset: int) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def getNextBankHoliday(cls, offset: int, filename: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def getNextBankHoliday(cls, filename: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def getNextBankHoliday(cls, day: java.time.ZonedDateTime) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def getNextBankHoliday(cls, day: java.time.ZonedDateTime, filename: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def isBankHoliday(cls) -> bool: ...
    @classmethod
    @typing.overload
    def isBankHoliday(cls, offset: int) -> bool: ...
    @classmethod
    @typing.overload
    def isBankHoliday(cls, offset: int, filename: java.lang.String) -> bool: ...
    @classmethod
    @typing.overload
    def isBankHoliday(cls, filename: java.lang.String) -> bool: ...
    @classmethod
    @typing.overload
    def isBankHoliday(cls, day: java.time.ZonedDateTime) -> bool: ...
    @classmethod
    @typing.overload
    def isBankHoliday(cls, day: java.time.ZonedDateTime, filename: java.lang.String) -> bool: ...
    @classmethod
    @typing.overload
    def isInDayset(cls, daysetName: java.lang.String) -> bool: ...
    @classmethod
    @typing.overload
    def isInDayset(cls, daysetName: java.lang.String, offset: int) -> bool: ...
    @classmethod
    @typing.overload
    def isInDayset(cls, daysetName: java.lang.String, day: java.time.ZonedDateTime) -> bool: ...
    @classmethod
    @typing.overload
    def isWeekend(cls) -> bool: ...
    @classmethod
    @typing.overload
    def isWeekend(cls, offset: int) -> bool: ...
    @classmethod
    @typing.overload
    def isWeekend(cls, day: java.time.ZonedDateTime) -> bool: ...

class Exec(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.actions.Exec'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Exec()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def executeCommandLine(cls, timeout: java.time.Duration, commandLine: typing.List[java.lang.String]) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def executeCommandLine(cls, commandLine: typing.List[java.lang.String]) -> None: ...

class HTTP(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.actions.HTTP'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * HTTP()
    
      Attributes:
        CONTENT_TYPE_JSON (java.lang.String): final static field
    
    """
    CONTENT_TYPE_JSON: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    @classmethod
    @typing.overload
    def sendHttpDeleteRequest(cls, url: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def sendHttpDeleteRequest(cls, url: java.lang.String, timeout: int) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def sendHttpDeleteRequest(cls, url: java.lang.String, headers: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]], timeout: int) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def sendHttpGetRequest(cls, url: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def sendHttpGetRequest(cls, url: java.lang.String, timeout: int) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def sendHttpGetRequest(cls, url: java.lang.String, headers: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]], timeout: int) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def sendHttpPostRequest(cls, url: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def sendHttpPostRequest(cls, url: java.lang.String, timeout: int) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def sendHttpPostRequest(cls, url: java.lang.String, contentType: java.lang.String, content: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def sendHttpPostRequest(cls, url: java.lang.String, contentType: java.lang.String, content: java.lang.String, timeout: int) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def sendHttpPostRequest(cls, url: java.lang.String, contentType: java.lang.String, content: java.lang.String, headers: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]], timeout: int) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def sendHttpPutRequest(cls, url: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def sendHttpPutRequest(cls, url: java.lang.String, timeout: int) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def sendHttpPutRequest(cls, url: java.lang.String, contentType: java.lang.String, content: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def sendHttpPutRequest(cls, url: java.lang.String, contentType: java.lang.String, content: java.lang.String, timeout: int) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def sendHttpPutRequest(cls, url: java.lang.String, contentType: java.lang.String, content: java.lang.String, headers: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]], timeout: int) -> java.lang.String: ...

class Log(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.actions.Log'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Log()
    
    """
    def __init__(self): ...
    @classmethod
    def logDebug(cls, loggerName: java.lang.String, format: java.lang.String, args: typing.List[typing.Any]) -> None: ...
    @classmethod
    def logError(cls, loggerName: java.lang.String, format: java.lang.String, args: typing.List[typing.Any]) -> None: ...
    @classmethod
    def logInfo(cls, loggerName: java.lang.String, format: java.lang.String, args: typing.List[typing.Any]) -> None: ...
    @classmethod
    def logWarn(cls, loggerName: java.lang.String, format: java.lang.String, args: typing.List[typing.Any]) -> None: ...

class Ping(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.actions.Ping'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Ping()
    
    """
    def __init__(self): ...
    @classmethod
    def checkVitality(cls, host: java.lang.String, port: int, timeout: int) -> bool: ...

class ScriptExecution(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.actions.ScriptExecution'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ScriptExecution()
    
    """
    def __init__(self): ...
    @classmethod
    def callScript(cls, scriptName: java.lang.String) -> typing.Any: ...
    @classmethod
    def createTimer(cls, instant: java.time.ZonedDateTime, closure: org.eclipse.xtext.xbase.lib.Procedures.Procedure0) -> 'Timer': ...
    @classmethod
    def createTimerWithArgument(cls, instant: java.time.ZonedDateTime, arg1: typing.Any, closure: org.eclipse.xtext.xbase.lib.Procedures.Procedure1[typing.Any]) -> 'Timer': ...

class Things(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.actions.Things'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Things()
    
    """
    def __init__(self): ...
    @classmethod
    def getActions(cls, scope: java.lang.String, thingUid: java.lang.String) -> org.openhab.core.thing.binding.ThingActions: ...
    @classmethod
    def getThingStatusInfo(cls, thingUid: java.lang.String) -> org.openhab.core.thing.ThingStatusInfo: ...

class Timer(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.actions.Timer'
    
    """
    def cancel(self) -> bool: ...
    def hasTerminated(self) -> bool: ...
    def isActive(self) -> bool: ...
    def isRunning(self) -> bool: ...
    def reschedule(self, newTime: java.time.ZonedDateTime) -> bool: ...

class Voice(java.lang.Object):
    """
    Java class 'org.openhab.core.model.script.actions.Voice'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Voice()
    
    """
    def __init__(self): ...
    @classmethod
    @typing.overload
    def interpret(cls, text: typing.Any) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def interpret(cls, text: typing.Any, interpreter: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def interpret(cls, text: typing.Any, interpreter: java.lang.String, sink: java.lang.String) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def say(cls, text: typing.Any) -> None: ...
    @classmethod
    @typing.overload
    def say(cls, text: typing.Any, voice: java.lang.String) -> None: ...
    @classmethod
    @typing.overload
    def say(cls, text: typing.Any, voice: java.lang.String, sink: java.lang.String) -> None: ...
    @classmethod
    @typing.overload
    def say(cls, text: typing.Any, voice: java.lang.String, sink: java.lang.String, volume: org.openhab.core.library.types.PercentType) -> None: ...
    @classmethod
    @typing.overload
    def say(cls, text: typing.Any, voice: java.lang.String, volume: org.openhab.core.library.types.PercentType) -> None: ...
    @classmethod
    @typing.overload
    def say(cls, text: typing.Any, volume: org.openhab.core.library.types.PercentType) -> None: ...
