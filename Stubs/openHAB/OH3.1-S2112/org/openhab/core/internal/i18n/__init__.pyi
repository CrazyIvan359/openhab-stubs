import java.lang
import java.time
import java.util
import javax.measure
import javax.measure.spi
import org.openhab.core.i18n
import org.openhab.core.library.types
import org.osgi.framework
import org.osgi.service.component
import org.osgi.util.tracker
import typing


class I18nProviderImpl(org.openhab.core.i18n.TranslationProvider, org.openhab.core.i18n.LocaleProvider, org.openhab.core.i18n.LocationProvider, org.openhab.core.i18n.TimeZoneProvider, org.openhab.core.i18n.UnitProvider):
    """
    Java class 'org.openhab.core.internal.i18n.I18nProviderImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.i18n.TranslationProvider,
            org.openhab.core.i18n.LocaleProvider,
            org.openhab.core.i18n.LocationProvider,
            org.openhab.core.i18n.TimeZoneProvider,
            org.openhab.core.i18n.UnitProvider
    
      Constructors:
        * I18nProviderImpl(org.osgi.service.component.ComponentContext)
    
      Attributes:
        CONFIGURATION_PID (java.lang.String): final static field
        LANGUAGE (java.lang.String): final static field
        SCRIPT (java.lang.String): final static field
        REGION (java.lang.String): final static field
        VARIANT (java.lang.String): final static field
    
    """
    CONFIGURATION_PID: typing.ClassVar[java.lang.String] = ...
    LANGUAGE: typing.ClassVar[java.lang.String] = ...
    SCRIPT: typing.ClassVar[java.lang.String] = ...
    REGION: typing.ClassVar[java.lang.String] = ...
    VARIANT: typing.ClassVar[java.lang.String] = ...
    def __init__(self, componentContext: org.osgi.service.component.ComponentContext): ...
    def getLocale(self) -> java.util.Locale: ...
    def getLocation(self) -> org.openhab.core.library.types.PointType: ...
    def getMeasurementSystem(self) -> javax.measure.spi.SystemOfUnits: ...
    @typing.overload
    def getText(self, bundle: org.osgi.framework.Bundle, key: java.lang.String, defaultText: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    @typing.overload
    def getText(self, bundle: org.osgi.framework.Bundle, key: java.lang.String, defaultText: java.lang.String, locale: java.util.Locale, arguments: typing.List[typing.Any]) -> java.lang.String: ...
    def getTimeZone(self) -> java.time.ZoneId: ...
    _getUnit__T = typing.TypeVar('_getUnit__T', bound=javax.measure.Quantity)  # <T>
    def getUnit(self, dimension: typing.Type[_getUnit__T]) -> javax.measure.Unit[_getUnit__T]: ...

class LanguageResourceBundleManager(java.lang.Object):
    """
    Java class 'org.openhab.core.internal.i18n.LanguageResourceBundleManager'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * LanguageResourceBundleManager(org.openhab.core.i18n.LocaleProvider, org.osgi.framework.Bundle)
    
    """
    def __init__(self, localeProvider: org.openhab.core.i18n.LocaleProvider, bundle: org.osgi.framework.Bundle): ...
    def clearCache(self) -> None: ...
    def containsResource(self, resource: java.lang.String) -> bool: ...
    def containsResources(self) -> bool: ...
    def getBundle(self) -> org.osgi.framework.Bundle: ...
    @typing.overload
    def getText(self, resource: java.lang.String, key: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    @typing.overload
    def getText(self, key: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...

class ResourceBundleTracker(org.osgi.util.tracker.BundleTracker):
    """
    Java class 'org.openhab.core.internal.i18n.ResourceBundleTracker'
    
        Extends:
            org.osgi.util.tracker.BundleTracker
    
      Constructors:
        * ResourceBundleTracker(org.osgi.framework.BundleContext, org.openhab.core.i18n.LocaleProvider)
    
    """
    def __init__(self, bundleContext: org.osgi.framework.BundleContext, localeProvider: org.openhab.core.i18n.LocaleProvider): ...
    def addingBundle(self, bundle: org.osgi.framework.Bundle, event: org.osgi.framework.BundleEvent) -> typing.Any: ...
    def close(self) -> None: ...
    def getAllLanguageResources(self) -> java.util.Collection[LanguageResourceBundleManager]: ...
    def getLanguageResource(self, bundle: org.osgi.framework.Bundle) -> LanguageResourceBundleManager: ...
    def open(self) -> None: ...
    def removedBundle(self, bundle: org.osgi.framework.Bundle, event: org.osgi.framework.BundleEvent, object: typing.Any) -> None: ...
