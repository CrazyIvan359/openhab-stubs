import java.lang
import org.openhab.core.auth.client.oauth2
import org.osgi.service.cm
import typing


class SymmetricKeyCipher(org.openhab.core.auth.client.oauth2.StorageCipher):
    """
    Java class 'org.openhab.core.auth.oauth2client.internal.cipher.SymmetricKeyCipher'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.auth.client.oauth2.StorageCipher
    
      Constructors:
        * SymmetricKeyCipher(org.osgi.service.cm.ConfigurationAdmin)
    
      Raises:
        java.io.IOException: from java
        java.security.NoSuchAlgorithmException: from java
    
      Attributes:
        CIPHER_ID (java.lang.String): final static field
        PID (java.lang.String): final static field
    
    """
    CIPHER_ID: typing.ClassVar[java.lang.String] = ...
    PID: typing.ClassVar[java.lang.String] = ...
    def __init__(self, configurationAdmin: org.osgi.service.cm.ConfigurationAdmin): ...
    def decrypt(self, base64CipherText: java.lang.String) -> java.lang.String: ...
    def encrypt(self, plainText: java.lang.String) -> java.lang.String: ...
    def getUniqueCipherId(self) -> java.lang.String: ...
