import java.util
import org.openhab.core.config.core
import org.openhab.core.config.xml
import org.openhab.core.config.xml.osgi
import org.openhab.core.config.xml.util
import org.osgi.framework
import typing


class ConfigDescriptionReader(org.openhab.core.config.xml.util.XmlDocumentReader[java.util.List[org.openhab.core.config.core.ConfigDescription]]):
    """
    Java class 'org.openhab.core.config.xml.internal.ConfigDescriptionReader'
    
        Extends:
            org.openhab.core.config.xml.util.XmlDocumentReader
    
      Constructors:
        * ConfigDescriptionReader()
    
    """
    def __init__(self): ...

class ConfigDescriptionXmlProvider(org.openhab.core.config.xml.osgi.XmlDocumentProvider[java.util.List[org.openhab.core.config.core.ConfigDescription]]):
    """
    Java class 'org.openhab.core.config.xml.internal.ConfigDescriptionXmlProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.xml.osgi.XmlDocumentProvider
    
      Constructors:
        * ConfigDescriptionXmlProvider(org.osgi.framework.Bundle, org.openhab.core.config.xml.AbstractXmlConfigDescriptionProvider)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
    """
    def __init__(self, bundle: org.osgi.framework.Bundle, configDescriptionProvider: org.openhab.core.config.xml.AbstractXmlConfigDescriptionProvider): ...
    def addingFinished(self) -> None: ...
    @typing.overload
    def addingObject(self, configDescriptions: java.util.List[org.openhab.core.config.core.ConfigDescription]) -> None: ...
    @typing.overload
    def addingObject(self, object: typing.Any) -> None: ...
    def release(self) -> None: ...
