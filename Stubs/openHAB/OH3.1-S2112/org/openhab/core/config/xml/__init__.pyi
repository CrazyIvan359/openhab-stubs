import com.thoughtworks.xstream.converters
import com.thoughtworks.xstream.io
import java.lang
import java.net
import java.util
import org.openhab.core.common.registry
import org.openhab.core.config.core
import org.openhab.core.config.core.i18n
import org.openhab.core.config.xml.osgi
import org.openhab.core.config.xml.util
import org.openhab.core.service
import org.osgi.framework
import org.osgi.service.component
import typing


_AbstractXmlBasedProvider__T_ID = typing.TypeVar('_AbstractXmlBasedProvider__T_ID')  # <T_ID>
_AbstractXmlBasedProvider__T_OBJECT = typing.TypeVar('_AbstractXmlBasedProvider__T_OBJECT', bound=org.openhab.core.common.registry.Identifiable)  # <T_OBJECT>
class AbstractXmlBasedProvider(java.lang.Object, typing.Generic[_AbstractXmlBasedProvider__T_ID, _AbstractXmlBasedProvider__T_OBJECT]):
    """
    Java class 'org.openhab.core.config.xml.AbstractXmlBasedProvider'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * AbstractXmlBasedProvider()
    
    """
    def __init__(self): ...
    def add(self, bundle: org.osgi.framework.Bundle, object: _AbstractXmlBasedProvider__T_OBJECT) -> None: ...
    def addAll(self, bundle: org.osgi.framework.Bundle, objectList: typing.Union[java.util.Collection[_AbstractXmlBasedProvider__T_OBJECT], typing.Sequence[_AbstractXmlBasedProvider__T_OBJECT]]) -> None: ...
    def removeAll(self, bundle: org.osgi.framework.Bundle) -> None: ...

class ConfigDescriptionConverter(org.openhab.core.config.xml.util.GenericUnmarshaller[org.openhab.core.config.core.ConfigDescription]):
    """
    Java class 'org.openhab.core.config.xml.ConfigDescriptionConverter'
    
        Extends:
            org.openhab.core.config.xml.util.GenericUnmarshaller
    
      Constructors:
        * ConfigDescriptionConverter()
    
    """
    def __init__(self): ...
    def unmarshal(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, context: com.thoughtworks.xstream.converters.UnmarshallingContext) -> typing.Any: ...

class ConfigDescriptionParameterConverter(org.openhab.core.config.xml.util.GenericUnmarshaller[org.openhab.core.config.core.ConfigDescriptionParameter]):
    """
    Java class 'org.openhab.core.config.xml.ConfigDescriptionParameterConverter'
    
        Extends:
            org.openhab.core.config.xml.util.GenericUnmarshaller
    
      Constructors:
        * ConfigDescriptionParameterConverter()
    
    """
    def __init__(self): ...
    def unmarshal(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, context: com.thoughtworks.xstream.converters.UnmarshallingContext) -> typing.Any: ...

class ConfigDescriptionParameterGroupConverter(org.openhab.core.config.xml.util.GenericUnmarshaller[org.openhab.core.config.core.ConfigDescriptionParameterGroup]):
    """
    Java class 'org.openhab.core.config.xml.ConfigDescriptionParameterGroupConverter'
    
        Extends:
            org.openhab.core.config.xml.util.GenericUnmarshaller
    
      Constructors:
        * ConfigDescriptionParameterGroupConverter()
    
    """
    def __init__(self): ...
    def unmarshal(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, marshallingContext: com.thoughtworks.xstream.converters.UnmarshallingContext) -> typing.Any: ...

class FilterCriteriaConverter(org.openhab.core.config.xml.util.GenericUnmarshaller[org.openhab.core.config.core.FilterCriteria]):
    """
    Java class 'org.openhab.core.config.xml.FilterCriteriaConverter'
    
        Extends:
            org.openhab.core.config.xml.util.GenericUnmarshaller
    
      Constructors:
        * FilterCriteriaConverter()
    
    """
    def __init__(self): ...
    def unmarshal(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, context: com.thoughtworks.xstream.converters.UnmarshallingContext) -> typing.Any: ...

class AbstractXmlConfigDescriptionProvider(AbstractXmlBasedProvider[java.net.URI, org.openhab.core.config.core.ConfigDescription], org.openhab.core.config.core.ConfigDescriptionProvider):
    """
    Java class 'org.openhab.core.config.xml.AbstractXmlConfigDescriptionProvider'
    
        Extends:
            org.openhab.core.config.xml.AbstractXmlBasedProvider
    
        Interfaces:
            org.openhab.core.config.core.ConfigDescriptionProvider
    
      Constructors:
        * AbstractXmlConfigDescriptionProvider()
    
    """
    def __init__(self): ...
    def getConfigDescription(self, uri: java.net.URI, locale: java.util.Locale) -> org.openhab.core.config.core.ConfigDescription: ...
    def getConfigDescriptions(self, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.config.core.ConfigDescription]: ...

class ConfigXmlConfigDescriptionProvider(AbstractXmlConfigDescriptionProvider, org.openhab.core.config.xml.osgi.XmlDocumentProviderFactory[java.util.List[org.openhab.core.config.core.ConfigDescription]]):
    """
    Java class 'org.openhab.core.config.xml.ConfigXmlConfigDescriptionProvider'
    
        Extends:
            org.openhab.core.config.xml.AbstractXmlConfigDescriptionProvider
    
        Interfaces:
            org.openhab.core.config.xml.osgi.XmlDocumentProviderFactory
    
      Constructors:
        * ConfigXmlConfigDescriptionProvider(org.openhab.core.config.core.i18n.ConfigI18nLocalizationService, org.openhab.core.service.ReadyService)
    
      Attributes:
        READY_MARKER (java.lang.String): final static field
    
    """
    READY_MARKER: typing.ClassVar[java.lang.String] = ...
    def __init__(self, configI18nService: org.openhab.core.config.core.i18n.ConfigI18nLocalizationService, readyService: org.openhab.core.service.ReadyService): ...
    def activate(self, componentContext: org.osgi.service.component.ComponentContext) -> None: ...
    def createDocumentProvider(self, bundle: org.osgi.framework.Bundle) -> org.openhab.core.config.xml.osgi.XmlDocumentProvider[java.util.List[org.openhab.core.config.core.ConfigDescription]]: ...
    def deactivate(self) -> None: ...
