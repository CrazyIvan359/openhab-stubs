import java.lang
import java.util
import org.openhab.core.auth
import typing


_CredentialsExtractor__C = typing.TypeVar('_CredentialsExtractor__C')  # <C>
class CredentialsExtractor(java.lang.Object, typing.Generic[_CredentialsExtractor__C]):
    """
    public interface CredentialsExtractor<C>
    
        Provider of credentials which works in given context and can provide credentials out of it.
    
    
    """
    def retrieveCredentials(self, requestContext: _CredentialsExtractor__C) -> java.util.Optional[org.openhab.core.auth.Credentials]: ...
