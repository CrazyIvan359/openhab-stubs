import java.io
import java.lang
import java.net
import java.security.cert
import java.time
import java.util
import javax.net.ssl
import org.eclipse.jetty.client
import org.eclipse.jetty.http
import org.eclipse.jetty.websocket.client
import org.openhab.core.library.types
import typing


class ExtensibleTrustManager(javax.net.ssl.TrustManager):
    """
    public interface ExtensibleTrustManager extends :class:`~org.openhab.core.io.net.http.https:.docs.oracle.com.en.java.javase.11.docs.api.java.base.javax.net.ssl.TrustManager?is`
    
        Provides an extensible composite TrustManager The trust manager can be extended with implementations of the following
        interfaces: - :code:`TlsTrustManagerProvider` - :code:`TlsCertificateProvider`
    
    
    """
    def addTlsCertificateProvider(self, tlsCertificateProvider: 'TlsCertificateProvider') -> None: ...
    def addTlsTrustManagerProvider(self, tlsTrustManagerProvider: 'TlsTrustManagerProvider') -> None: ...
    def removeTlsCertificateProvider(self, tlsCertificateProvider: 'TlsCertificateProvider') -> None: ...
    def removeTlsTrustManagerProvider(self, tlsTrustManagerProvider: 'TlsTrustManagerProvider') -> None: ...

class HttpClientFactory(java.lang.Object):
    """
    @NonNullByDefault public interface HttpClientFactory
    
        Factory class to create Jetty http clients
    
    
    """
    def createHttpClient(self, consumerName: java.lang.String) -> org.eclipse.jetty.client.HttpClient: ...
    def getCommonHttpClient(self) -> org.eclipse.jetty.client.HttpClient: ...

class HttpClientInitializationException(java.lang.RuntimeException):
    """
    Java class 'org.openhab.core.io.net.http.HttpClientInitializationException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * HttpClientInitializationException(java.lang.String, java.lang.Throwable)
    
    """
    def __init__(self, message: java.lang.String, cause: java.lang.Throwable): ...

class HttpRequestBuilder(java.lang.Object):
    """
    Java class 'org.openhab.core.io.net.http.HttpRequestBuilder'
    
        Extends:
            java.lang.Object
    
    """
    def getContentAsString(self) -> java.lang.String: ...
    @classmethod
    def getFrom(cls, url: java.lang.String) -> 'HttpRequestBuilder': ...
    @classmethod
    def postTo(cls, url: java.lang.String) -> 'HttpRequestBuilder': ...
    @typing.overload
    def withContent(self, content: java.lang.String) -> 'HttpRequestBuilder': ...
    @typing.overload
    def withContent(self, content: java.lang.String, contentType: java.lang.String) -> 'HttpRequestBuilder': ...
    def withHeader(self, header: java.lang.String, value: java.lang.String) -> 'HttpRequestBuilder': ...
    def withTimeout(self, timeout: java.time.Duration) -> 'HttpRequestBuilder': ...

class HttpUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.io.net.http.HttpUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * HttpUtil()
    
    """
    def __init__(self): ...
    @classmethod
    def createHttpMethod(cls, httpMethodString: java.lang.String) -> org.eclipse.jetty.http.HttpMethod: ...
    @classmethod
    @typing.overload
    def downloadData(cls, url: java.lang.String, contentTypeRegex: java.lang.String, scanTypeInContent: bool, maxContentLength: int) -> org.openhab.core.library.types.RawType: ...
    @classmethod
    @typing.overload
    def downloadData(cls, url: java.lang.String, contentTypeRegex: java.lang.String, scanTypeInContent: bool, maxContentLength: int, timeout: int) -> org.openhab.core.library.types.RawType: ...
    @classmethod
    @typing.overload
    def downloadImage(cls, url: java.lang.String) -> org.openhab.core.library.types.RawType: ...
    @classmethod
    @typing.overload
    def downloadImage(cls, url: java.lang.String, scanTypeInContent: bool, maxContentLength: int) -> org.openhab.core.library.types.RawType: ...
    @classmethod
    @typing.overload
    def downloadImage(cls, url: java.lang.String, scanTypeInContent: bool, maxContentLength: int, timeout: int) -> org.openhab.core.library.types.RawType: ...
    @classmethod
    @typing.overload
    def downloadImage(cls, url: java.lang.String, timeout: int) -> org.openhab.core.library.types.RawType: ...
    @classmethod
    @typing.overload
    def executeUrl(cls, httpMethod: java.lang.String, url: java.lang.String, timeout: int) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def executeUrl(cls, httpMethod: java.lang.String, url: java.lang.String, content: java.io.InputStream, contentType: java.lang.String, timeout: int) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def executeUrl(cls, httpMethod: java.lang.String, url: java.lang.String, httpHeaders: java.util.Properties, content: java.io.InputStream, contentType: java.lang.String, timeout: int) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def executeUrl(cls, httpMethod: java.lang.String, url: java.lang.String, httpHeaders: java.util.Properties, content: java.io.InputStream, contentType: java.lang.String, timeout: int, proxyHost: java.lang.String, proxyPort: int, proxyUser: java.lang.String, proxyPassword: java.lang.String, nonProxyHosts: java.lang.String) -> java.lang.String: ...
    @classmethod
    def guessContentTypeFromData(cls, data: typing.List[int]) -> java.lang.String: ...

class TlsProvider(java.lang.Object):
    """
    @NonNullByDefault public interface TlsProvider
    
        Provides some TLS validation implementation for the given host name You should implement one of children of this
        interface, in order to request the framework to use a specific implementation for the given host. NOTE: implementations
        of this interface should be immutable, to guarantee efficient and correct functionality
    
    
    """
    def getHostName(self) -> java.lang.String: ...

class TrustAllTrustManager(javax.net.ssl.X509ExtendedTrustManager):
    """
    Java class 'org.openhab.core.io.net.http.TrustAllTrustManager'
    
        Extends:
            javax.net.ssl.X509ExtendedTrustManager
    
    """
    @typing.overload
    def checkClientTrusted(self, chain: typing.List[java.security.cert.X509Certificate], authType: java.lang.String) -> None: ...
    @typing.overload
    def checkClientTrusted(self, chain: typing.List[java.security.cert.X509Certificate], authType: java.lang.String, socket: java.net.Socket) -> None: ...
    @typing.overload
    def checkClientTrusted(self, chain: typing.List[java.security.cert.X509Certificate], authType: java.lang.String, engine: javax.net.ssl.SSLEngine) -> None: ...
    @typing.overload
    def checkServerTrusted(self, chain: typing.List[java.security.cert.X509Certificate], authType: java.lang.String) -> None: ...
    @typing.overload
    def checkServerTrusted(self, chain: typing.List[java.security.cert.X509Certificate], authType: java.lang.String, socket: java.net.Socket) -> None: ...
    @typing.overload
    def checkServerTrusted(self, chain: typing.List[java.security.cert.X509Certificate], authType: java.lang.String, engine: javax.net.ssl.SSLEngine) -> None: ...
    def getAcceptedIssuers(self) -> typing.List[java.security.cert.X509Certificate]: ...
    @classmethod
    def getInstance(cls) -> 'TrustAllTrustManager': ...

class WebSocketFactory(java.lang.Object):
    """
    @NonNullByDefault public interface WebSocketFactory
    
        Factory class to create Jetty web socket clients
    
    
    """
    def createWebSocketClient(self, consumerName: java.lang.String) -> org.eclipse.jetty.websocket.client.WebSocketClient: ...
    def getCommonWebSocketClient(self) -> org.eclipse.jetty.websocket.client.WebSocketClient: ...

class TlsCertificateProvider(TlsProvider):
    """
    Java class 'org.openhab.core.io.net.http.TlsCertificateProvider'
    
        Interfaces:
            org.openhab.core.io.net.http.TlsProvider
    
    """
    def getCertificate(self) -> java.net.URL: ...

class TlsTrustManagerProvider(TlsProvider):
    """
    Java class 'org.openhab.core.io.net.http.TlsTrustManagerProvider'
    
        Interfaces:
            org.openhab.core.io.net.http.TlsProvider
    
    """
    def getTrustManager(self) -> javax.net.ssl.X509ExtendedTrustManager: ...
