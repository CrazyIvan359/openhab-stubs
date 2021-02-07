import java.lang
import java.net
import java.security.cert
import javax.net.ssl
import org.eclipse.jetty.client
import org.eclipse.jetty.websocket.client
import org.openhab.core.io.net.http
import typing


class ExtensibleTrustManagerImpl(javax.net.ssl.X509ExtendedTrustManager, org.openhab.core.io.net.http.ExtensibleTrustManager):
    """
    Java class 'org.openhab.core.io.net.http.internal.ExtensibleTrustManagerImpl'
    
        Extends:
            javax.net.ssl.X509ExtendedTrustManager
    
        Interfaces:
            org.openhab.core.io.net.http.ExtensibleTrustManager
    
      Constructors:
        * ExtensibleTrustManagerImpl()
    
    """
    def __init__(self): ...
    def addTlsCertificateProvider(self, tlsCertificateProvider: org.openhab.core.io.net.http.TlsCertificateProvider) -> None: ...
    def addTlsTrustManagerProvider(self, tlsTrustManagerProvider: org.openhab.core.io.net.http.TlsTrustManagerProvider) -> None: ...
    @typing.overload
    def checkClientTrusted(self, chain: typing.List[java.security.cert.X509Certificate], authType: java.lang.String) -> None: ...
    @typing.overload
    def checkClientTrusted(self, chain: typing.List[java.security.cert.X509Certificate], authType: java.lang.String, socket: java.net.Socket) -> None: ...
    @typing.overload
    def checkClientTrusted(self, chain: typing.List[java.security.cert.X509Certificate], authType: java.lang.String, sslEngine: javax.net.ssl.SSLEngine) -> None: ...
    @typing.overload
    def checkServerTrusted(self, chain: typing.List[java.security.cert.X509Certificate], authType: java.lang.String) -> None: ...
    @typing.overload
    def checkServerTrusted(self, chain: typing.List[java.security.cert.X509Certificate], authType: java.lang.String, socket: java.net.Socket) -> None: ...
    @typing.overload
    def checkServerTrusted(self, chain: typing.List[java.security.cert.X509Certificate], authType: java.lang.String, sslEngine: javax.net.ssl.SSLEngine) -> None: ...
    def getAcceptedIssuers(self) -> typing.List[java.security.cert.X509Certificate]: ...
    def removeTlsCertificateProvider(self, tlsCertificateProvider: org.openhab.core.io.net.http.TlsCertificateProvider) -> None: ...
    def removeTlsTrustManagerProvider(self, tlsTrustManagerProvider: org.openhab.core.io.net.http.TlsTrustManagerProvider) -> None: ...

class WebClientFactoryImpl(org.openhab.core.io.net.http.HttpClientFactory, org.openhab.core.io.net.http.WebSocketFactory):
    """
    Java class 'org.openhab.core.io.net.http.internal.WebClientFactoryImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.net.http.HttpClientFactory,
            org.openhab.core.io.net.http.WebSocketFactory
    
      Constructors:
        * WebClientFactoryImpl(org.openhab.core.io.net.http.ExtensibleTrustManager)
    
    """
    def __init__(self, extensibleTrustManager: org.openhab.core.io.net.http.ExtensibleTrustManager): ...
    def createHttpClient(self, consumerName: java.lang.String) -> org.eclipse.jetty.client.HttpClient: ...
    def createWebSocketClient(self, consumerName: java.lang.String) -> org.eclipse.jetty.websocket.client.WebSocketClient: ...
    def getCommonHttpClient(self) -> org.eclipse.jetty.client.HttpClient: ...
    def getCommonWebSocketClient(self) -> org.eclipse.jetty.websocket.client.WebSocketClient: ...
