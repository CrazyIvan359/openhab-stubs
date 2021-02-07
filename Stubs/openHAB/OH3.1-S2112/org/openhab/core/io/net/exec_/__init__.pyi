import java.lang
import java.time
import typing


class ExecUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.io.net.exec.ExecUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ExecUtil()
    
    """
    def __init__(self): ...
    @classmethod
    def executeCommandLine(cls, commandLine: typing.List[java.lang.String]) -> None: ...
    @classmethod
    def executeCommandLineAndWaitResponse(cls, timeout: java.time.Duration, commandLine: typing.List[java.lang.String]) -> java.lang.String: ...
