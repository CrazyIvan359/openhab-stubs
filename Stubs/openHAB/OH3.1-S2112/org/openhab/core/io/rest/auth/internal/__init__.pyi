import java.lang
import java.security
import java.util
import javax.ws.rs.container
import javax.ws.rs.core
import org
import org.openhab.core.auth
import org.openhab.core.io.rest
import typing


class AnonymousUserSecurityContext(javax.ws.rs.core.SecurityContext):
    """
    Java class 'org.openhab.core.io.rest.auth.internal.AnonymousUserSecurityContext'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            javax.ws.rs.core.SecurityContext
    
      Constructors:
        * AnonymousUserSecurityContext()
    
    """
    def __init__(self): ...
    def getAuthenticationScheme(self) -> java.lang.String: ...
    def getUserPrincipal(self) -> java.security.Principal: ...
    def isSecure(self) -> bool: ...
    def isUserInRole(self, role: java.lang.String) -> bool: ...

class AuthFilter(javax.ws.rs.container.ContainerRequestFilter):
    """
    Java class 'org.openhab.core.io.rest.auth.internal.AuthFilter'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            javax.ws.rs.container.ContainerRequestFilter
    
      Constructors:
        * AuthFilter()
    
    """
    def __init__(self): ...
    def filter(self, requestContext: javax.ws.rs.container.ContainerRequestContext) -> None: ...

class AuthenticationSecurityContext(javax.ws.rs.core.SecurityContext):
    """
    Java class 'org.openhab.core.io.rest.auth.internal.AuthenticationSecurityContext'
    
        Interfaces:
            javax.ws.rs.core.SecurityContext
    
    """
    def getAuthentication(self) -> org.openhab.core.auth.Authentication: ...

class JwtHelper(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.auth.internal.JwtHelper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * JwtHelper()
    
    """
    def __init__(self): ...
    def getJwtAccessToken(self, user: org.openhab.core.auth.User, clientId: java.lang.String, scope: java.lang.String, tokenLifetime: int) -> java.lang.String: ...
    def verifyAndParseJwtAccessToken(self, jwt: java.lang.String) -> org.openhab.core.auth.Authentication: ...

class RolesAllowedDynamicFeatureImpl(javax.ws.rs.container.DynamicFeature):
    """
    Java class 'org.openhab.core.io.rest.auth.internal.RolesAllowedDynamicFeatureImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            javax.ws.rs.container.DynamicFeature
    
      Constructors:
        * RolesAllowedDynamicFeatureImpl()
    
    """
    def __init__(self): ...
    def configure(self, resourceInfo: javax.ws.rs.container.ResourceInfo, configuration: javax.ws.rs.core.FeatureContext) -> None: ...

class TokenEndpointException(org.openhab.core.auth.AuthenticationException):
    """
    Java class 'org.openhab.core.io.rest.auth.internal.TokenEndpointException'
    
        Extends:
            org.openhab.core.auth.AuthenticationException
    
      Constructors:
        * TokenEndpointException(org.openhab.core.io.rest.auth.internal.TokenEndpointException.ErrorType)
    
    """
    def __init__(self, errorType: 'TokenEndpointException.ErrorType'): ...
    def getErrorDTO(self) -> 'TokenResponseErrorDTO': ...
    class ErrorType(java.lang.Enum[org.openhab.core.io.rest.auth.internal.TokenEndpointException.ErrorType]):
        """
        Java class 'org.openhab.core.io.rest.auth.internal.TokenEndpointException$ErrorType'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            INVALID_REQUEST (org.openhab.core.io.rest.auth.internal.TokenEndpointException$ErrorType): final static enum constant
            INVALID_GRANT (org.openhab.core.io.rest.auth.internal.TokenEndpointException$ErrorType): final static enum constant
            INVALID_CLIENT (org.openhab.core.io.rest.auth.internal.TokenEndpointException$ErrorType): final static enum constant
            INVALID_SCOPE (org.openhab.core.io.rest.auth.internal.TokenEndpointException$ErrorType): final static enum constant
            UNAUTHORIZED_CLIENT (org.openhab.core.io.rest.auth.internal.TokenEndpointException$ErrorType): final static enum constant
            UNSUPPORTED_GRANT_TYPE (org.openhab.core.io.rest.auth.internal.TokenEndpointException$ErrorType): final static enum constant
        
        """
        INVALID_REQUEST: typing.ClassVar['TokenEndpointException.ErrorType'] = ...
        INVALID_GRANT: typing.ClassVar['TokenEndpointException.ErrorType'] = ...
        INVALID_CLIENT: typing.ClassVar['TokenEndpointException.ErrorType'] = ...
        INVALID_SCOPE: typing.ClassVar['TokenEndpointException.ErrorType'] = ...
        UNAUTHORIZED_CLIENT: typing.ClassVar['TokenEndpointException.ErrorType'] = ...
        UNSUPPORTED_GRANT_TYPE: typing.ClassVar['TokenEndpointException.ErrorType'] = ...
        def getError(self) -> java.lang.String: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @typing.overload
        def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
        @classmethod
        @typing.overload
        def valueOf(cls, name: java.lang.String) -> 'TokenEndpointException.ErrorType': ...
        @classmethod
        def values(cls) -> typing.List['TokenEndpointException.ErrorType']: ...

class TokenResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.io.rest.auth.internal.TokenResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * TokenResource(org.openhab.core.auth.UserRegistry, org.openhab.core.io.rest.auth.internal.JwtHelper)
    
      Attributes:
        PATH_AUTH (java.lang.String): final static field
        SESSIONID_COOKIE_NAME (java.lang.String): final static field
        TOKEN_LIFETIME (int): final static field
    
    """
    PATH_AUTH: typing.ClassVar[java.lang.String] = ...
    SESSIONID_COOKIE_NAME: typing.ClassVar[java.lang.String] = ...
    TOKEN_LIFETIME: typing.ClassVar[int] = ...
    def __init__(self, userRegistry: org.openhab.core.auth.UserRegistry, jwtHelper: JwtHelper): ...
    def deleteSession(self, refreshToken: java.lang.String, id: java.lang.String, sessionCookie: javax.ws.rs.core.Cookie, securityContext: javax.ws.rs.core.SecurityContext) -> javax.ws.rs.core.Response: ...
    def getApiTokens(self, securityContext: javax.ws.rs.core.SecurityContext) -> javax.ws.rs.core.Response: ...
    def getSessions(self, securityContext: javax.ws.rs.core.SecurityContext) -> javax.ws.rs.core.Response: ...
    def getToken(self, grantType: java.lang.String, code: java.lang.String, redirectUri: java.lang.String, clientId: java.lang.String, refreshToken: java.lang.String, codeVerifier: java.lang.String, useCookie: bool, sessionCookie: javax.ws.rs.core.Cookie) -> javax.ws.rs.core.Response: ...
    def removeApiToken(self, securityContext: javax.ws.rs.core.SecurityContext, name: java.lang.String) -> javax.ws.rs.core.Response: ...

class TokenResponseDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.auth.internal.TokenResponseDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * TokenResponseDTO(java.lang.String, java.lang.String, java.lang.Integer, java.lang.String, java.lang.String, org.openhab.core.auth.User)
    
      Attributes:
        access_token (java.lang.String): field
        token_type (java.lang.String): field
        expires_in (java.lang.Integer): field
        refresh_token (java.lang.String): field
        scope (java.lang.String): field
        user (org.openhab.core.io.rest.auth.internal.UserDTO): field
    
    """
    access_token: java.lang.String = ...
    token_type: java.lang.String = ...
    expires_in: int = ...
    refresh_token: java.lang.String = ...
    scope: java.lang.String = ...
    user: 'UserDTO' = ...
    def __init__(self, access_token: java.lang.String, token_type: java.lang.String, expires_in: int, refresh_token: java.lang.String, scope: java.lang.String, user: org.openhab.core.auth.User): ...

class TokenResponseErrorDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.auth.internal.TokenResponseErrorDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * TokenResponseErrorDTO(java.lang.String)
    
      Attributes:
        error (java.lang.String): field
        error_description (java.lang.String): field
        error_uri (java.lang.String): field
    
    """
    error: java.lang.String = ...
    error_description: java.lang.String = ...
    error_uri: java.lang.String = ...
    def __init__(self, error: java.lang.String): ...

class UserApiTokenDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.auth.internal.UserApiTokenDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * UserApiTokenDTO(java.lang.String, java.util.Date, java.lang.String)
    
    """
    def __init__(self, name: java.lang.String, createdTime: java.util.Date, scope: java.lang.String): ...

class UserDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.auth.internal.UserDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * UserDTO(org.openhab.core.auth.User)
    
    """
    def __init__(self, user: org.openhab.core.auth.User): ...

class UserSessionDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.auth.internal.UserSessionDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * UserSessionDTO(java.lang.String, java.util.Date, java.util.Date, java.lang.String, java.lang.String)
    
    """
    def __init__(self, sessionId: java.lang.String, createdTime: java.util.Date, lastRefreshTime: java.util.Date, clientId: java.lang.String, scope: java.lang.String): ...

class JwtSecurityContext(AuthenticationSecurityContext):
    """
    Java class 'org.openhab.core.io.rest.auth.internal.JwtSecurityContext'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.auth.internal.AuthenticationSecurityC
            ontext
    
      Constructors:
        * JwtSecurityContext(org.openhab.core.auth.Authentication)
    
    """
    def __init__(self, authentication: org.openhab.core.auth.Authentication): ...
    def getAuthentication(self) -> org.openhab.core.auth.Authentication: ...
    def getAuthenticationScheme(self) -> java.lang.String: ...
    def getUserPrincipal(self) -> java.security.Principal: ...
    def isSecure(self) -> bool: ...
    def isUserInRole(self, role: java.lang.String) -> bool: ...

class UserSecurityContext(AuthenticationSecurityContext):
    """
    Java class 'org.openhab.core.io.rest.auth.internal.UserSecurityContext'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.auth.internal.AuthenticationSecurityC
            ontext
    
      Constructors:
        * UserSecurityContext(org.openhab.core.auth.User, org.openhab.core.auth.Authentication, java.lang.String)
    
    """
    def __init__(self, user: org.openhab.core.auth.User, authentication: org.openhab.core.auth.Authentication, authenticationScheme: java.lang.String): ...
    def getAuthentication(self) -> org.openhab.core.auth.Authentication: ...
    def getAuthenticationScheme(self) -> java.lang.String: ...
    def getUserPrincipal(self) -> java.security.Principal: ...
    def isSecure(self) -> bool: ...
    def isUserInRole(self, role: java.lang.String) -> bool: ...
