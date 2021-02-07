import java.io
import java.lang
import java.net
import org.osgi.framework


class ResourceBundleClassLoader(java.lang.ClassLoader):
    """
    Java class 'org.openhab.core.common.osgi.ResourceBundleClassLoader'
    
        Extends:
            java.lang.ClassLoader
    
      Constructors:
        * ResourceBundleClassLoader(org.osgi.framework.Bundle, java.lang.String, java.lang.String)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
    """
    def __init__(self, bundle: org.osgi.framework.Bundle, path: java.lang.String, filePattern: java.lang.String): ...
    def getResource(self, name: java.lang.String) -> java.net.URL: ...
    def getResourceAsStream(self, name: java.lang.String) -> java.io.InputStream: ...
