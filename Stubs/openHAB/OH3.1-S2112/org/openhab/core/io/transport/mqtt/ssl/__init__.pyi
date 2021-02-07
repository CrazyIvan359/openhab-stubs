import io.netty.handler.ssl.util
import javax.net.ssl
import typing


class CustomTrustManagerFactory(io.netty.handler.ssl.util.SimpleTrustManagerFactory):
    """
    Java class 'org.openhab.core.io.transport.mqtt.ssl.CustomTrustManagerFactory'
    
        Extends:
            io.netty.handler.ssl.util.SimpleTrustManagerFactory
    
      Constructors:
        * CustomTrustManagerFactory(javax.net.ssl.TrustManager[])
    
    """
    def __init__(self, trustManagers: typing.List[javax.net.ssl.TrustManager]): ...
