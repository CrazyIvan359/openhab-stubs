import java.lang
import java.util
import org.openhab.core.i18n
import org.openhab.core.thing
import org.openhab.core.thing.type
import org.openhab.core.types
import org.openhab.core.util
import org.osgi.framework


class ChannelGroupTypeI18nLocalizationService(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.i18n.ChannelGroupTypeI18nLocalizationService'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelGroupTypeI18nLocalizationService(org.openhab.core.i18n.TranslationProvider, org.openhab.core.thing.i18n.ChannelTypeI18nLocalizationService, org.openhab.core.thing.type.ChannelTypeRegistry)
    
    """
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider, channelTypeI18nLocalizationService: 'ChannelTypeI18nLocalizationService', channelTypeRegistry: org.openhab.core.thing.type.ChannelTypeRegistry): ...
    def createLocalizedChannelGroupType(self, bundle: org.osgi.framework.Bundle, channelGroupType: org.openhab.core.thing.type.ChannelGroupType, locale: java.util.Locale) -> org.openhab.core.thing.type.ChannelGroupType: ...

class ChannelTypeI18nLocalizationService(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.i18n.ChannelTypeI18nLocalizationService'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ChannelTypeI18nLocalizationService(org.openhab.core.i18n.TranslationProvider)
    
    """
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    def createLocalizedChannelType(self, bundle: org.osgi.framework.Bundle, channelType: org.openhab.core.thing.type.ChannelType, locale: java.util.Locale) -> org.openhab.core.thing.type.ChannelType: ...
    def createLocalizedCommandDescription(self, bundle: org.osgi.framework.Bundle, command: org.openhab.core.types.CommandDescription, channelTypeUID: org.openhab.core.thing.type.ChannelTypeUID, locale: java.util.Locale) -> org.openhab.core.types.CommandDescription: ...
    def createLocalizedCommandOptions(self, bundle: org.osgi.framework.Bundle, commandOptions: java.util.List[org.openhab.core.types.CommandOption], channelTypeUID: org.openhab.core.thing.type.ChannelTypeUID, locale: java.util.Locale) -> java.util.List[org.openhab.core.types.CommandOption]: ...
    def createLocalizedStateDescriptionFragment(self, bundle: org.osgi.framework.Bundle, state: org.openhab.core.types.StateDescription, channelTypeUID: org.openhab.core.thing.type.ChannelTypeUID, locale: java.util.Locale) -> org.openhab.core.types.StateDescriptionFragment: ...
    def createLocalizedStateOptions(self, bundle: org.osgi.framework.Bundle, stateOptions: java.util.List[org.openhab.core.types.StateOption], channelTypeUID: org.openhab.core.thing.type.ChannelTypeUID, locale: java.util.Locale) -> java.util.List[org.openhab.core.types.StateOption]: ...
    def createLocalizedStatePattern(self, bundle: org.osgi.framework.Bundle, pattern: java.lang.String, channelTypeUID: org.openhab.core.thing.type.ChannelTypeUID, locale: java.util.Locale) -> java.lang.String: ...

class ThingStatusInfoI18nLocalizationService(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.i18n.ThingStatusInfoI18nLocalizationService'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ThingStatusInfoI18nLocalizationService()
    
    """
    def __init__(self): ...
    def getLocalizedThingStatusInfo(self, thing: org.openhab.core.thing.Thing, locale: java.util.Locale) -> org.openhab.core.thing.ThingStatusInfo: ...
    def setBundleResolver(self, bundleResolver: org.openhab.core.util.BundleResolver) -> None: ...

class ThingTypeI18nLocalizationService(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.i18n.ThingTypeI18nLocalizationService'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ThingTypeI18nLocalizationService(org.openhab.core.i18n.TranslationProvider, org.openhab.core.thing.i18n.ChannelGroupTypeI18nLocalizationService, org.openhab.core.thing.type.ChannelGroupTypeRegistry, org.openhab.core.thing.i18n.ChannelTypeI18nLocalizationService, org.openhab.core.thing.type.ChannelTypeRegistry)
    
    """
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider, channelGroupTypeI18nLocalizationService: ChannelGroupTypeI18nLocalizationService, channelGroupTypeRegistry: org.openhab.core.thing.type.ChannelGroupTypeRegistry, channelTypeI18nLocalizationService: ChannelTypeI18nLocalizationService, channelTypeRegistry: org.openhab.core.thing.type.ChannelTypeRegistry): ...
    def createLocalizedThingType(self, bundle: org.osgi.framework.Bundle, thingType: org.openhab.core.thing.type.ThingType, locale: java.util.Locale) -> org.openhab.core.thing.type.ThingType: ...
