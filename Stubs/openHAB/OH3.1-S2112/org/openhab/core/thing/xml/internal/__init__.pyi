import com.thoughtworks.xstream
import com.thoughtworks.xstream.converters
import com.thoughtworks.xstream.io
import java.lang
import java.util
import org
import org.openhab.core.config.core
import org.openhab.core.config.core.i18n
import org.openhab.core.config.xml
import org.openhab.core.config.xml.osgi
import org.openhab.core.config.xml.util
import org.openhab.core.service
import org.openhab.core.thing
import org.openhab.core.thing.binding
import org.openhab.core.thing.i18n
import org.openhab.core.thing.type
import org.openhab.core.types
import org.osgi.framework
import typing


_AbstractDescriptionTypeConverter__T = typing.TypeVar('_AbstractDescriptionTypeConverter__T')  # <T>
class AbstractDescriptionTypeConverter(org.openhab.core.config.xml.util.GenericUnmarshaller[_AbstractDescriptionTypeConverter__T], typing.Generic[_AbstractDescriptionTypeConverter__T]):
    """
    Java class 'org.openhab.core.thing.xml.internal.AbstractDescriptionTypeConverter'
    
        Extends:
            org.openhab.core.config.xml.util.GenericUnmarshaller
    
      Constructors:
        * AbstractDescriptionTypeConverter(java.lang.Class, java.lang.String)
    
    """
    def __init__(self, clazz: typing.Type[_AbstractDescriptionTypeConverter__T], type: java.lang.String): ...
    def unmarshal(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, context: com.thoughtworks.xstream.converters.UnmarshallingContext) -> typing.Any: ...

class ChannelConverter(org.openhab.core.config.xml.util.GenericUnmarshaller[org.openhab.core.thing.xml.internal.ChannelXmlResult]):
    """
    Java class 'org.openhab.core.thing.xml.internal.ChannelConverter'
    
        Extends:
            org.openhab.core.config.xml.util.GenericUnmarshaller
    
      Constructors:
        * ChannelConverter()
    
    """
    def __init__(self): ...
    def unmarshal(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, context: com.thoughtworks.xstream.converters.UnmarshallingContext) -> typing.Any: ...

class ChannelGroupTypeXmlResult(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.xml.internal.ChannelGroupTypeXmlResult'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelGroupTypeXmlResult(org.openhab.core.thing.type.ChannelGroupTypeUID, java.lang.String, java.lang.String, java.lang.String, java.util.List)
    
    """
    def __init__(self, channelGroupTypeUID: org.openhab.core.thing.type.ChannelGroupTypeUID, label: java.lang.String, description: java.lang.String, category: java.lang.String, channelTypeReferences: java.util.List['ChannelXmlResult']): ...
    def getUID(self) -> org.openhab.core.thing.type.ChannelGroupTypeUID: ...
    def toChannelGroupType(self) -> org.openhab.core.thing.type.ChannelGroupType: ...
    def toString(self) -> java.lang.String: ...

class ChannelTypeXmlResult(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.xml.internal.ChannelTypeXmlResult'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelTypeXmlResult(org.openhab.core.thing.type.ChannelType, org.openhab.core.config.core.ConfigDescription)
        * ChannelTypeXmlResult(org.openhab.core.thing.type.ChannelType, org.openhab.core.config.core.ConfigDescription, boolean)
    
    """
    @typing.overload
    def __init__(self, channelType: org.openhab.core.thing.type.ChannelType, configDescription: org.openhab.core.config.core.ConfigDescription): ...
    @typing.overload
    def __init__(self, channelType: org.openhab.core.thing.type.ChannelType, configDescription: org.openhab.core.config.core.ConfigDescription, system: bool): ...
    def getConfigDescription(self) -> org.openhab.core.config.core.ConfigDescription: ...
    def isSystem(self) -> bool: ...
    def toChannelType(self) -> org.openhab.core.thing.type.ChannelType: ...
    def toString(self) -> java.lang.String: ...

class ChannelXmlResult(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.xml.internal.ChannelXmlResult'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelXmlResult(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.util.List, org.openhab.core.thing.type.AutoUpdatePolicy)
    
    """
    def __init__(self, id: java.lang.String, typeId: java.lang.String, label: java.lang.String, description: java.lang.String, properties: java.util.List[org.openhab.core.config.xml.util.NodeValue], autoUpdatePolicy: org.openhab.core.thing.type.AutoUpdatePolicy): ...
    def getAutoUpdatePolicy(self) -> org.openhab.core.thing.type.AutoUpdatePolicy: ...
    def getDescription(self) -> java.lang.String: ...
    def getId(self) -> java.lang.String: ...
    def getLabel(self) -> java.lang.String: ...
    def getProperties(self) -> java.util.List[org.openhab.core.config.xml.util.NodeValue]: ...
    def getTypeId(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class CommandDescriptionConverter(org.openhab.core.config.xml.util.GenericUnmarshaller[org.openhab.core.types.CommandDescription]):
    """
    Java class 'org.openhab.core.thing.xml.internal.CommandDescriptionConverter'
    
        Extends:
            org.openhab.core.config.xml.util.GenericUnmarshaller
    
      Constructors:
        * CommandDescriptionConverter()
    
    """
    def __init__(self): ...
    @typing.overload
    def unmarshal(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, context: com.thoughtworks.xstream.converters.UnmarshallingContext) -> org.openhab.core.types.CommandDescription: ...
    @typing.overload
    def unmarshal(self, hierarchicalStreamReader: com.thoughtworks.xstream.io.HierarchicalStreamReader, unmarshallingContext: com.thoughtworks.xstream.converters.UnmarshallingContext) -> typing.Any: ...

class EventDescriptionConverter(org.openhab.core.config.xml.util.GenericUnmarshaller[org.openhab.core.types.EventDescription]):
    """
    Java class 'org.openhab.core.thing.xml.internal.EventDescriptionConverter'
    
        Extends:
            org.openhab.core.config.xml.util.GenericUnmarshaller
    
      Constructors:
        * EventDescriptionConverter()
    
    """
    def __init__(self): ...
    def unmarshal(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, context: com.thoughtworks.xstream.converters.UnmarshallingContext) -> typing.Any: ...

class StateDescriptionConverter(org.openhab.core.config.xml.util.GenericUnmarshaller[org.openhab.core.types.StateDescription]):
    """
    Java class 'org.openhab.core.thing.xml.internal.StateDescriptionConverter'
    
        Extends:
            org.openhab.core.config.xml.util.GenericUnmarshaller
    
      Constructors:
        * StateDescriptionConverter()
    
    """
    def __init__(self): ...
    def unmarshal(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, context: com.thoughtworks.xstream.converters.UnmarshallingContext) -> typing.Any: ...

class ThingDescriptionConverter(org.openhab.core.config.xml.util.GenericUnmarshaller[org.openhab.core.thing.xml.internal.ThingDescriptionList]):
    """
    Java class 'org.openhab.core.thing.xml.internal.ThingDescriptionConverter'
    
        Extends:
            org.openhab.core.config.xml.util.GenericUnmarshaller
    
      Constructors:
        * ThingDescriptionConverter()
    
    """
    def __init__(self): ...
    def unmarshal(self, reader: com.thoughtworks.xstream.io.HierarchicalStreamReader, context: com.thoughtworks.xstream.converters.UnmarshallingContext) -> typing.Any: ...

class ThingDescriptionList(java.util.ArrayList):
    """
    Java class 'org.openhab.core.thing.xml.internal.ThingDescriptionList'
    
        Extends:
            java.util.ArrayList
    
      Constructors:
        * ThingDescriptionList(java.util.Collection)
    
    """
    def __init__(self, list: java.util.Collection): ...

class ThingDescriptionReader(org.openhab.core.config.xml.util.XmlDocumentReader[java.util.List[typing.Any]]):
    """
    Java class 'org.openhab.core.thing.xml.internal.ThingDescriptionReader'
    
        Extends:
            org.openhab.core.config.xml.util.XmlDocumentReader
    
      Constructors:
        * ThingDescriptionReader()
    
    """
    def __init__(self): ...
    def registerAliases(self, xstream: com.thoughtworks.xstream.XStream) -> None: ...
    def registerConverters(self, xstream: com.thoughtworks.xstream.XStream) -> None: ...

class ThingTypeXmlProvider(org.openhab.core.config.xml.osgi.XmlDocumentProvider[java.util.List[typing.Any]]):
    """
    Java class 'org.openhab.core.thing.xml.internal.ThingTypeXmlProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.config.xml.osgi.XmlDocumentProvider
    
      Constructors:
        * ThingTypeXmlProvider(org.osgi.framework.Bundle, org.openhab.core.config.xml.AbstractXmlConfigDescriptionProvider, org.openhab.core.thing.xml.internal.XmlThingTypeProvider, org.openhab.core.thing.xml.internal.XmlChannelTypeProvider, org.openhab.core.thing.xml.internal.XmlChannelGroupTypeProvider)
    
      Raises:
        java.lang.IllegalArgumentException: from java
    
    """
    def __init__(self, bundle: org.osgi.framework.Bundle, configDescriptionProvider: org.openhab.core.config.xml.AbstractXmlConfigDescriptionProvider, thingTypeProvider: 'XmlThingTypeProvider', channelTypeProvider: 'XmlChannelTypeProvider', channelGroupTypeProvider: 'XmlChannelGroupTypeProvider'): ...
    def addingFinished(self) -> None: ...
    @typing.overload
    def addingObject(self, types: java.util.List[typing.Any]) -> None: ...
    @typing.overload
    def addingObject(self, object: typing.Any) -> None: ...
    def release(self) -> None: ...

class ThingTypeXmlResult(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.xml.internal.ThingTypeXmlResult'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ThingTypeXmlResult(org.openhab.core.thing.ThingTypeUID, java.util.List, java.lang.String, java.lang.String, java.lang.String, boolean, java.util.List, java.util.List[], java.util.List, java.lang.String, java.lang.Object[])
    
    """
    def __init__(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID, supportedBridgeTypeUIDs: java.util.List[java.lang.String], label: java.lang.String, description: java.lang.String, category: java.lang.String, listed: bool, extensibleChannelTypeIds: java.util.List[java.lang.String], channelTypeReferenceObjects: typing.List[java.util.List[ChannelXmlResult]], properties: java.util.List[org.openhab.core.config.xml.util.NodeValue], representationProperty: java.lang.String, configDescriptionObjects: typing.List[typing.Any]): ...
    def getConfigDescription(self) -> org.openhab.core.config.core.ConfigDescription: ...
    def getUID(self) -> org.openhab.core.thing.ThingTypeUID: ...
    def toString(self) -> java.lang.String: ...
    def toThingType(self) -> org.openhab.core.thing.type.ThingType: ...

class ThingXmlConfigDescriptionProvider(org.openhab.core.config.xml.AbstractXmlConfigDescriptionProvider):
    """
    Java class 'org.openhab.core.thing.xml.internal.ThingXmlConfigDescriptionProvider'
    
        Extends:
            org.openhab.core.config.xml.AbstractXmlConfigDescriptionProvider
    
      Constructors:
        * ThingXmlConfigDescriptionProvider(org.openhab.core.config.core.i18n.ConfigI18nLocalizationService)
    
    """
    def __init__(self, configI18nService: org.openhab.core.config.core.i18n.ConfigI18nLocalizationService): ...

class XmlChannelGroupTypeProvider(org.openhab.core.config.xml.AbstractXmlBasedProvider[org.openhab.core.thing.UID, org.openhab.core.thing.type.ChannelGroupType], org.openhab.core.thing.type.ChannelGroupTypeProvider):
    """
    Java class 'org.openhab.core.thing.xml.internal.XmlChannelGroupTypeProvider'
    
        Extends:
            org.openhab.core.config.xml.AbstractXmlBasedProvider
    
        Interfaces:
            org.openhab.core.thing.type.ChannelGroupTypeProvider
    
      Constructors:
        * XmlChannelGroupTypeProvider(org.openhab.core.thing.i18n.ChannelGroupTypeI18nLocalizationService)
    
    """
    def __init__(self, channelGroupTypeI18nLocalizationService: org.openhab.core.thing.i18n.ChannelGroupTypeI18nLocalizationService): ...
    def getChannelGroupType(self, channelGroupTypeUID: org.openhab.core.thing.type.ChannelGroupTypeUID, locale: java.util.Locale) -> org.openhab.core.thing.type.ChannelGroupType: ...
    def getChannelGroupTypes(self, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.thing.type.ChannelGroupType]: ...

class XmlChannelTypeProvider(org.openhab.core.config.xml.AbstractXmlBasedProvider[org.openhab.core.thing.UID, org.openhab.core.thing.type.ChannelType], org.openhab.core.thing.type.ChannelTypeProvider):
    """
    Java class 'org.openhab.core.thing.xml.internal.XmlChannelTypeProvider'
    
        Extends:
            org.openhab.core.config.xml.AbstractXmlBasedProvider
    
        Interfaces:
            org.openhab.core.thing.type.ChannelTypeProvider
    
      Constructors:
        * XmlChannelTypeProvider(org.openhab.core.thing.i18n.ChannelTypeI18nLocalizationService)
    
    """
    def __init__(self, channelTypeI18nLocalizationService: org.openhab.core.thing.i18n.ChannelTypeI18nLocalizationService): ...
    def getChannelType(self, channelTypeUID: org.openhab.core.thing.type.ChannelTypeUID, locale: java.util.Locale) -> org.openhab.core.thing.type.ChannelType: ...
    def getChannelTypes(self, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.thing.type.ChannelType]: ...

class XmlHelper(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.xml.internal.XmlHelper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * XmlHelper()
    
      Attributes:
        SYSTEM_NAMESPACE_PREFIX (java.lang.String): final static field
    
    """
    SYSTEM_NAMESPACE_PREFIX: typing.ClassVar[java.lang.String] = ...
    def __init__(self): ...
    @classmethod
    def getSystemUID(cls, typeId: java.lang.String) -> java.lang.String: ...

class XmlThingTypeProvider(org.openhab.core.config.xml.AbstractXmlBasedProvider[org.openhab.core.thing.UID, org.openhab.core.thing.type.ThingType], org.openhab.core.thing.binding.ThingTypeProvider, org.openhab.core.config.xml.osgi.XmlDocumentProviderFactory[java.util.List[typing.Any]]):
    """
    Java class 'org.openhab.core.thing.xml.internal.XmlThingTypeProvider'
    
        Extends:
            org.openhab.core.config.xml.AbstractXmlBasedProvider
    
        Interfaces:
            org.openhab.core.thing.binding.ThingTypeProvider,
            org.openhab.core.config.xml.osgi.XmlDocumentProviderFactory
    
      Constructors:
        * XmlThingTypeProvider(org.openhab.core.thing.type.ChannelGroupTypeProvider, org.openhab.core.thing.type.ChannelTypeProvider, org.openhab.core.config.core.ConfigDescriptionProvider, org.openhab.core.service.ReadyService, org.openhab.core.thing.i18n.ThingTypeI18nLocalizationService)
    
      Attributes:
        READY_MARKER (java.lang.String): final static field
    
    """
    READY_MARKER: typing.ClassVar[java.lang.String] = ...
    def __init__(self, channelGroupTypeProvider: org.openhab.core.thing.type.ChannelGroupTypeProvider, channelTypeProvider: org.openhab.core.thing.type.ChannelTypeProvider, configDescriptionProvider: org.openhab.core.config.core.ConfigDescriptionProvider, readyService: org.openhab.core.service.ReadyService, thingTypeI18nLocalizationService: org.openhab.core.thing.i18n.ThingTypeI18nLocalizationService): ...
    def createDocumentProvider(self, bundle: org.osgi.framework.Bundle) -> org.openhab.core.config.xml.osgi.XmlDocumentProvider[java.util.List[typing.Any]]: ...
    def getThingType(self, thingTypeUID: org.openhab.core.thing.ThingTypeUID, locale: java.util.Locale) -> org.openhab.core.thing.type.ThingType: ...
    def getThingTypes(self, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.thing.type.ThingType]: ...

class BridgeTypeXmlResult(ThingTypeXmlResult):
    """
    Java class 'org.openhab.core.thing.xml.internal.BridgeTypeXmlResult'
    
        Extends:
            org.openhab.core.thing.xml.internal.ThingTypeXmlResult
    
      Constructors:
        * BridgeTypeXmlResult(org.openhab.core.thing.ThingTypeUID, java.util.List, java.lang.String, java.lang.String, java.lang.String, boolean, java.util.List, java.util.List[], java.util.List, java.lang.String, java.lang.Object[])
    
    """
    def __init__(self, bridgeTypeUID: org.openhab.core.thing.ThingTypeUID, supportedBridgeTypeUIDs: java.util.List[java.lang.String], label: java.lang.String, description: java.lang.String, category: java.lang.String, listed: bool, extensibleChannelTypeIds: java.util.List[java.lang.String], channelTypeReferenceObjects: typing.List[java.util.List[ChannelXmlResult]], properties: java.util.List[org.openhab.core.config.xml.util.NodeValue], representationProperty: java.lang.String, configDescriptionObjects: typing.List[typing.Any]): ...
    def toString(self) -> java.lang.String: ...
    @typing.overload
    def toThingType(self) -> org.openhab.core.thing.type.BridgeType: ...
    @typing.overload
    def toThingType(self) -> org.openhab.core.thing.type.ThingType: ...

class ChannelGroupTypeConverter(AbstractDescriptionTypeConverter[ChannelGroupTypeXmlResult]):
    """
    Java class 'org.openhab.core.thing.xml.internal.ChannelGroupTypeConverter'
    
        Extends:
            org.openhab.core.thing.xml.internal.AbstractDescriptionTypeConverter
    
      Constructors:
        * ChannelGroupTypeConverter()
    
    """
    def __init__(self): ...

class ChannelTypeConverter(AbstractDescriptionTypeConverter[ChannelTypeXmlResult]):
    """
    Java class 'org.openhab.core.thing.xml.internal.ChannelTypeConverter'
    
        Extends:
            org.openhab.core.thing.xml.internal.AbstractDescriptionTypeConverter
    
      Constructors:
        * ChannelTypeConverter()
    
    """
    def __init__(self): ...

class ThingTypeConverter(AbstractDescriptionTypeConverter[ThingTypeXmlResult]):
    """
    Java class 'org.openhab.core.thing.xml.internal.ThingTypeConverter'
    
        Extends:
            org.openhab.core.thing.xml.internal.AbstractDescriptionTypeConverter
    
      Constructors:
        * ThingTypeConverter()
    
    """
    def __init__(self): ...

class BridgeTypeConverter(ThingTypeConverter):
    """
    Java class 'org.openhab.core.thing.xml.internal.BridgeTypeConverter'
    
        Extends:
            org.openhab.core.thing.xml.internal.ThingTypeConverter
    
      Constructors:
        * BridgeTypeConverter()
    
    """
    def __init__(self): ...
