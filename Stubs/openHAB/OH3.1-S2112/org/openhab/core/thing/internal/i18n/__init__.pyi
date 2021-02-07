import java.lang
import java.util
import java.util.function
import org.openhab.core.i18n
import org.openhab.core.thing
import org.openhab.core.thing.i18n
import org.openhab.core.thing.type
import org.osgi.framework
import typing


class ChannelGroupI18nUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.internal.i18n.ChannelGroupI18nUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelGroupI18nUtil(org.openhab.core.thing.i18n.ChannelGroupTypeI18nLocalizationService, org.openhab.core.thing.type.ChannelGroupTypeRegistry)
    
    """
    def __init__(self, channelGroupTypeI18nLocalizationService: org.openhab.core.thing.i18n.ChannelGroupTypeI18nLocalizationService, channelGroupTypeRegistry: org.openhab.core.thing.type.ChannelGroupTypeRegistry): ...
    def createLocalizedChannelGroupDefinitions(self, bundle: org.osgi.framework.Bundle, channelGroupDefinitions: java.util.List[org.openhab.core.thing.type.ChannelGroupDefinition], channelGroupLabelResolver: typing.Union[java.util.function.Function[org.openhab.core.thing.type.ChannelGroupDefinition, java.lang.String], typing.Callable[[org.openhab.core.thing.type.ChannelGroupDefinition], java.lang.String]], channelGroupDescriptionResolver: typing.Union[java.util.function.Function[org.openhab.core.thing.type.ChannelGroupDefinition, java.lang.String], typing.Callable[[org.openhab.core.thing.type.ChannelGroupDefinition], java.lang.String]], locale: java.util.Locale) -> java.util.List[org.openhab.core.thing.type.ChannelGroupDefinition]: ...

class ChannelI18nUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.internal.i18n.ChannelI18nUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelI18nUtil(org.openhab.core.thing.i18n.ChannelTypeI18nLocalizationService, org.openhab.core.thing.type.ChannelTypeRegistry)
    
    """
    def __init__(self, channelTypeI18nLocalizationService: org.openhab.core.thing.i18n.ChannelTypeI18nLocalizationService, channelTypeRegistry: org.openhab.core.thing.type.ChannelTypeRegistry): ...
    def createLocalizedChannelDefinitions(self, bundle: org.osgi.framework.Bundle, channelDefinitions: java.util.List[org.openhab.core.thing.type.ChannelDefinition], channelLabelResolver: typing.Union[java.util.function.Function[org.openhab.core.thing.type.ChannelDefinition, java.lang.String], typing.Callable[[org.openhab.core.thing.type.ChannelDefinition], java.lang.String]], channelDescriptionResolver: typing.Union[java.util.function.Function[org.openhab.core.thing.type.ChannelDefinition, java.lang.String], typing.Callable[[org.openhab.core.thing.type.ChannelDefinition], java.lang.String]], locale: java.util.Locale) -> java.util.List[org.openhab.core.thing.type.ChannelDefinition]: ...

class ThingTypeI18nUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.internal.i18n.ThingTypeI18nUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ThingTypeI18nUtil(org.openhab.core.i18n.TranslationProvider)
    
    """
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    def getChannelCommandOption(self, bundle: org.osgi.framework.Bundle, channelTypeUID: org.openhab.core.thing.type.ChannelTypeUID, optionValue: java.lang.String, defaultOptionLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    @typing.overload
    def getChannelDescription(self, bundle: org.osgi.framework.Bundle, thingTypeUID: org.openhab.core.thing.ThingTypeUID, channel: org.openhab.core.thing.type.ChannelDefinition, defaultDescription: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    @typing.overload
    def getChannelDescription(self, bundle: org.osgi.framework.Bundle, channelGroupTypeUID: org.openhab.core.thing.type.ChannelGroupTypeUID, channel: org.openhab.core.thing.type.ChannelDefinition, defaultLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    @typing.overload
    def getChannelDescription(self, bundle: org.osgi.framework.Bundle, channelTypeUID: org.openhab.core.thing.type.ChannelTypeUID, defaultDescription: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    @typing.overload
    def getChannelGroupDescription(self, bundle: org.osgi.framework.Bundle, thingTypeUID: org.openhab.core.thing.ThingTypeUID, channelGroup: org.openhab.core.thing.type.ChannelGroupDefinition, defaultDescription: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    @typing.overload
    def getChannelGroupDescription(self, bundle: org.osgi.framework.Bundle, channelGroupTypeUID: org.openhab.core.thing.type.ChannelGroupTypeUID, defaultDescription: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    @typing.overload
    def getChannelGroupLabel(self, bundle: org.osgi.framework.Bundle, thingTypeUID: org.openhab.core.thing.ThingTypeUID, channelGroup: org.openhab.core.thing.type.ChannelGroupDefinition, defaultLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    @typing.overload
    def getChannelGroupLabel(self, bundle: org.osgi.framework.Bundle, channelGroupTypeUID: org.openhab.core.thing.type.ChannelGroupTypeUID, defaultLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    @typing.overload
    def getChannelLabel(self, bundle: org.osgi.framework.Bundle, thingTypeUID: org.openhab.core.thing.ThingTypeUID, channel: org.openhab.core.thing.type.ChannelDefinition, defaultLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    @typing.overload
    def getChannelLabel(self, bundle: org.osgi.framework.Bundle, channelGroupTypeUID: org.openhab.core.thing.type.ChannelGroupTypeUID, channel: org.openhab.core.thing.type.ChannelDefinition, defaultLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    @typing.overload
    def getChannelLabel(self, bundle: org.osgi.framework.Bundle, channelTypeUID: org.openhab.core.thing.type.ChannelTypeUID, defaultLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getChannelStateOption(self, bundle: org.osgi.framework.Bundle, channelTypeUID: org.openhab.core.thing.type.ChannelTypeUID, optionValue: java.lang.String, defaultOptionLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getChannelStatePattern(self, bundle: org.osgi.framework.Bundle, channelTypeUID: org.openhab.core.thing.type.ChannelTypeUID, defaultPattern: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getDescription(self, bundle: org.osgi.framework.Bundle, thingTypeUID: org.openhab.core.thing.ThingTypeUID, defaultDescription: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getLabel(self, bundle: org.osgi.framework.Bundle, thingTypeUID: org.openhab.core.thing.ThingTypeUID, defaultLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
