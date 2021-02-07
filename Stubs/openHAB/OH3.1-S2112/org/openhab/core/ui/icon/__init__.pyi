import java.io
import java.lang
import java.util
import org
import org.openhab.core.i18n
import typing


class IconProvider(java.lang.Object):
    """
    @NonNullByDefault public interface IconProvider
    
        An icon provider can provide
        :class:`~org.openhab.core.ui.icon.https:.docs.oracle.com.en.java.javase.11.docs.api.java.base.java.io.InputStream?is`s
        for icons. The source of the images can depend on the provider implementation. The byte stream represents a PNG or SVG
        image, depending on the format. The icon category corresponds to the list of available channel categories. In order to
        provide means to user interfaces to know, what kind of icon sets are available in the system (and offered by some icon
        provider), the provider can additionally provide a set of :class:`~org.openhab.core.ui.icon.IconSet`s.
    
    
    """
    def getIcon(self, category: java.lang.String, iconSetId: java.lang.String, state: java.lang.String, format: 'IconSet.Format') -> java.io.InputStream: ...
    @typing.overload
    def getIconSets(self) -> java.util.Set['IconSet']: ...
    @typing.overload
    def getIconSets(self, locale: java.util.Locale) -> java.util.Set['IconSet']: ...
    def hasIcon(self, category: java.lang.String, iconSetId: java.lang.String, format: 'IconSet.Format') -> int: ...

class IconSet(java.lang.Object):
    """
    Java class 'org.openhab.core.ui.icon.IconSet'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * IconSet(java.lang.String, java.lang.String, java.lang.String, java.util.Set)
    
    """
    def __init__(self, id: java.lang.String, label: java.lang.String, description: java.lang.String, formats: java.util.Set['IconSet.Format']): ...
    def getDescription(self) -> java.lang.String: ...
    def getFormats(self) -> java.util.Set['IconSet.Format']: ...
    def getId(self) -> java.lang.String: ...
    def getLabel(self) -> java.lang.String: ...
    class Format(java.lang.Enum[org.openhab.core.ui.icon.IconSet.Format]):
        """
        Java class 'org.openhab.core.ui.icon.IconSet$Format'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            PNG (org.openhab.core.ui.icon.IconSet$Format): final static enum constant
            SVG (org.openhab.core.ui.icon.IconSet$Format): final static enum constant
        
        """
        PNG: typing.ClassVar['IconSet.Format'] = ...
        SVG: typing.ClassVar['IconSet.Format'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @typing.overload
        def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
        @classmethod
        @typing.overload
        def valueOf(cls, name: java.lang.String) -> 'IconSet.Format': ...
        @classmethod
        def values(cls) -> typing.List['IconSet.Format']: ...

class AbstractResourceIconProvider(IconProvider):
    """
    Java class 'org.openhab.core.ui.icon.AbstractResourceIconProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.ui.icon.IconProvider
    
      Constructors:
        * AbstractResourceIconProvider(org.openhab.core.i18n.TranslationProvider)
    
    """
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    def getIcon(self, category: java.lang.String, iconSetId: java.lang.String, state: java.lang.String, format: IconSet.Format) -> java.io.InputStream: ...
    @typing.overload
    def getIconSets(self, locale: java.util.Locale) -> java.util.Set[IconSet]: ...
    @typing.overload
    def getIconSets(self) -> java.util.Set[IconSet]: ...
    def hasIcon(self, category: java.lang.String, iconSetId: java.lang.String, format: IconSet.Format) -> int: ...
