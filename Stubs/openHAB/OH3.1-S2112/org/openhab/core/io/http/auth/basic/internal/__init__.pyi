import java.util
import javax.servlet.http
import org.openhab.core.auth
import org.openhab.core.io.http
import org.openhab.core.io.http.auth
import typing


class BasicChallengeHandler(org.openhab.core.io.http.Handler):
    """
    Java class 'org.openhab.core.io.http.auth.basic.internal.BasicChallengeHandler'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.http.Handler
    
      Constructors:
        * BasicChallengeHandler()
    
    """
    def __init__(self): ...
    def getPriority(self) -> int: ...
    def handle(self, request: javax.servlet.http.HttpServletRequest, response: javax.servlet.http.HttpServletResponse, context: org.openhab.core.io.http.HandlerContext) -> None: ...
    def handleError(self, request: javax.servlet.http.HttpServletRequest, response: javax.servlet.http.HttpServletResponse, context: org.openhab.core.io.http.HandlerContext) -> None: ...

class BasicCredentialsExtractor(org.openhab.core.io.http.auth.CredentialsExtractor[javax.servlet.http.HttpServletRequest]):
    """
    Java class 'org.openhab.core.io.http.auth.basic.internal.BasicCredentialsExtractor'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.http.auth.CredentialsExtractor
    
      Constructors:
        * BasicCredentialsExtractor()
    
    """
    def __init__(self): ...
    @typing.overload
    def retrieveCredentials(self, object: typing.Any) -> java.util.Optional: ...
    @typing.overload
    def retrieveCredentials(self, request: javax.servlet.http.HttpServletRequest) -> java.util.Optional[org.openhab.core.auth.Credentials]: ...
