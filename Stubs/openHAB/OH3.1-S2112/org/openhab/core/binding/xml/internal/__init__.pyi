import com.thoughtworks.xstream.converters
import com.thoughtworks.xstream.io
import java.lang
import java.util
import org
import org.openhab.core.binding
import org.openhab.core.binding.i18n
import org.openhab.core.config.core
import org.openhab.core.config.core.i18n
import org.openhab.core.config.xml
import org.openhab.core.config.xml.osgi
import org.openhab.core.config.xml.util
import org.openhab.core.service
import org.osgi.framework
import org.osgi.service.component
import typing


class BindingInfoConverter(org.openhab.core.config.xml.util.GenericUnmarshaller[org.openhab.core.binding.xml.internal.BindingInfoXmlResult]):
    """
    Java class 'org.openhab.core.binding.xml.internal.BindingInfoConverter'
    
        Extends:
            org.openhab.core.config.xml.util.GenericUnmarshaller
    
      Constructors:
        * BindingInfoConverter()
    
    """
    def __init__(self): ...
    def unmarshal(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, context: com.thoughtworks.xstream.converters.UnmarshallingContext) -> typing.Any: ...

class BindingInfoReader(org.openhab.core.config.xml.util.XmlDocumentReader[org.openhab.core.binding.xml.internal.BindingInfoXmlResult]):
    """
    Java class 'org.openhab.core.binding.xml.internal.BindingInfoReader'
    
        Extends:
            org.openhab.core.config.xml.util.XmlDocumentReader
    
      Constructors:
        * BindingInfoReader()
    
    """
    def __init__(self): ...

class BindingInfoXmlProvider(org.openhab.core.config.xml.osgi.XmlDocumentProvider[org.openhab.core.binding.xml.internal.BindingInfoXmlResult]):
    """
    Java class 'org.openhab.core.binding.xml.internal.BindingInfoXmlProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.xml.osgi.XmlDocumentProvider
    
      Constructors:
        * BindingInfoXmlProvider(org.osgi.framework.Bundle, org.openhab.core.binding.xml.internal.XmlBindingInfoProvider, org.openhab.core.config.xml.AbstractXmlConfigDescriptionProvider)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
    """
    def __init__(self, bundle: org.osgi.framework.Bundle, bindingInfoProvider: 'XmlBindingInfoProvider', configDescriptionProvider: org.openhab.core.config.xml.AbstractXmlConfigDescriptionProvider): ...
    def addingFinished(self) -> None: ...
    @typing.overload
    def addingObject(self, bindingInfoXmlResult: 'BindingInfoXmlResult') -> None: ...
    @typing.overload
    def addingObject(self, object: typing.Any) -> None: ...
    def release(self) -> None: ...

class BindingInfoXmlResult(java.lang.Object):
    """
    Java class 'org.openhab.core.binding.xml.internal.BindingInfoXmlResult'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * BindingInfoXmlResult(org.openhab.core.binding.BindingInfo, org.openhab.core.config.core.ConfigDescription)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
    """
    def __init__(self, bindingInfo: org.openhab.core.binding.BindingInfo, configDescription: org.openhab.core.config.core.ConfigDescription): ...
    def getBindingInfo(self) -> org.openhab.core.binding.BindingInfo: ...
    def getConfigDescription(self) -> org.openhab.core.config.core.ConfigDescription: ...
    def toString(self) -> java.lang.String: ...

class BindingXmlConfigDescriptionProvider(org.openhab.core.config.xml.AbstractXmlConfigDescriptionProvider):
    """
    Java class 'org.openhab.core.binding.xml.internal.BindingXmlConfigDescriptionProvider'
    
        Extends:
            org.openhab.core.config.xml.AbstractXmlConfigDescriptionProvider
    
      Constructors:
        * BindingXmlConfigDescriptionProvider(org.openhab.core.config.core.i18n.ConfigI18nLocalizationService)
    
    """
    def __init__(self, configI18nService: org.openhab.core.config.core.i18n.ConfigI18nLocalizationService): ...

class XmlBindingInfoProvider(org.openhab.core.config.xml.AbstractXmlBasedProvider[java.lang.String, org.openhab.core.binding.BindingInfo], org.openhab.core.binding.BindingInfoProvider, org.openhab.core.config.xml.osgi.XmlDocumentProviderFactory[BindingInfoXmlResult]):
    """
    Java class 'org.openhab.core.binding.xml.internal.XmlBindingInfoProvider'
    
        Extends:
            org.openhab.core.config.xml.AbstractXmlBasedProvider
    
        Interfaces:
            org.openhab.core.binding.BindingInfoProvider,
            org.openhab.core.config.xml.osgi.XmlDocumentProviderFactory
    
      Constructors:
        * XmlBindingInfoProvider(org.openhab.core.binding.i18n.BindingI18nLocalizationService, org.openhab.core.config.core.ConfigDescriptionProvider, org.openhab.core.service.ReadyService)
    
      Attributes:
        READY_MARKER (java.lang.String): final static field
    
    """
    READY_MARKER: typing.ClassVar[java.lang.String] = ...
    def __init__(self, bindingI18nService: org.openhab.core.binding.i18n.BindingI18nLocalizationService, configDescriptionProvider: org.openhab.core.config.core.ConfigDescriptionProvider, readyService: org.openhab.core.service.ReadyService): ...
    def activate(self, componentContext: org.osgi.service.component.ComponentContext) -> None: ...
    def createDocumentProvider(self, bundle: org.osgi.framework.Bundle) -> org.openhab.core.config.xml.osgi.XmlDocumentProvider[BindingInfoXmlResult]: ...
    def deactivate(self, componentContext: org.osgi.service.component.ComponentContext) -> None: ...
    def getBindingInfo(self, id: java.lang.String, locale: java.util.Locale) -> org.openhab.core.binding.BindingInfo: ...
    def getBindingInfos(self, locale: java.util.Locale) -> java.util.Set[org.openhab.core.binding.BindingInfo]: ...
