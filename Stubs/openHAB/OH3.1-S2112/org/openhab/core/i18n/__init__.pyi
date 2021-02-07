import java.lang
import java.time
import java.util
import java.util.function
import javax.measure
import javax.measure.spi
import org.openhab.core.library.types
import org.osgi.framework
import typing


class I18nUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.i18n.I18nUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * I18nUtil()
    
    """
    def __init__(self): ...
    @classmethod
    def isConstant(cls, key: java.lang.String) -> bool: ...
    @classmethod
    def stripConstant(cls, key: java.lang.String) -> java.lang.String: ...
    @classmethod
    def stripConstantOr(cls, key: java.lang.String, supplier: typing.Union[java.util.function.Supplier[java.lang.String], typing.Callable[[], java.lang.String]]) -> java.lang.String: ...

class LocaleProvider(java.lang.Object):
    """
    @NonNullByDefault public interface LocaleProvider
    
        The interface describe a provider for a locale.
    
    
    """
    def getLocale(self) -> java.util.Locale: ...

class LocalizedKey(java.lang.Object):
    """
    Java class 'org.openhab.core.i18n.LocalizedKey'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * LocalizedKey(java.lang.Object, java.lang.String)
    
    """
    def __init__(self, id: typing.Any, locale: java.lang.String): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getKey(self) -> typing.Any: ...
    def getLocale(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...

class LocationProvider(java.lang.Object):
    """
    @NonNullByDefault public interface LocationProvider
    
        This interface describes a provider for a location.
    
    
    """
    def getLocation(self) -> org.openhab.core.library.types.PointType: ...

class TimeZoneProvider(java.lang.Object):
    """
    @NonNullByDefault public interface TimeZoneProvider
    
        This interface describes a provider for time zone.
    
    
    """
    def getTimeZone(self) -> java.time.ZoneId: ...

class TranslationProvider(java.lang.Object):
    """
    @NonNullByDefault public interface TranslationProvider
    
        The :class:`~org.openhab.core.i18n.TranslationProvider` is a service interface for internationalization support within
        the platform. This service can be used to translate specific keys into its according text by considering the specified
        :class:`~org.openhab.core.i18n.https:.docs.oracle.com.en.java.javase.11.docs.api.java.base.java.util.Locale?is`
        (language). Any module which supports resource files is managed by this provider and used for translation. This service
        uses the i18n mechanism of Java.
    
    
    """
    @typing.overload
    def getText(self, bundle: org.osgi.framework.Bundle, key: java.lang.String, defaultText: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    @typing.overload
    def getText(self, bundle: org.osgi.framework.Bundle, key: java.lang.String, defaultText: java.lang.String, locale: java.util.Locale, arguments: typing.List[typing.Any]) -> java.lang.String: ...

class UnitProvider(java.lang.Object):
    """
    @NonNullByDefault public interface UnitProvider
    
        Provides :code:`Unit`s and the current :code:`SystemOfUnits`.
    
    
    """
    def getMeasurementSystem(self) -> javax.measure.spi.SystemOfUnits: ...
    _getUnit__T = typing.TypeVar('_getUnit__T', bound=javax.measure.Quantity)  # <T>
    def getUnit(self, dimension: typing.Type[_getUnit__T]) -> javax.measure.Unit[_getUnit__T]: ...
