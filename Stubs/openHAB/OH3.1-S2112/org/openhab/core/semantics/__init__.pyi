import java.lang
import java.util
import java.util.function
import org.openhab.core.items
import org.openhab.core.semantics.model
import typing


class SemanticTags(java.lang.Object):
    """
    Java class 'org.openhab.core.semantics.SemanticTags'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SemanticTags()
    
    """
    def __init__(self): ...
    @classmethod
    def getById(cls, tagId: java.lang.String) -> typing.Type[org.openhab.core.semantics.model.Tag]: ...
    @classmethod
    def getByLabel(cls, tagLabel: java.lang.String, locale: java.util.Locale) -> typing.Type[org.openhab.core.semantics.model.Tag]: ...
    @classmethod
    def getByLabelOrSynonym(cls, tagLabelOrSynonym: java.lang.String, locale: java.util.Locale) -> java.util.List[typing.Type[org.openhab.core.semantics.model.Tag]]: ...
    @classmethod
    def getLabel(cls, tag: typing.Type[org.openhab.core.semantics.model.Tag], locale: java.util.Locale) -> java.lang.String: ...
    @classmethod
    def getLabelAndSynonyms(cls, tag: typing.Type[org.openhab.core.semantics.model.Tag], locale: java.util.Locale) -> java.util.List[java.lang.String]: ...
    @classmethod
    def getProperty(cls, item: org.openhab.core.items.Item) -> typing.Type[org.openhab.core.semantics.model.Property]: ...
    @classmethod
    def getSemanticType(cls, item: org.openhab.core.items.Item) -> typing.Type[org.openhab.core.semantics.model.Tag]: ...

class SemanticsPredicates(java.lang.Object):
    """
    Java class 'org.openhab.core.semantics.SemanticsPredicates'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SemanticsPredicates()
    
    """
    def __init__(self): ...
    @classmethod
    def isA(cls, type: typing.Type[org.openhab.core.semantics.model.Tag]) -> java.util.function.Predicate[org.openhab.core.items.Item]: ...
    @classmethod
    def isEquipment(cls) -> java.util.function.Predicate[org.openhab.core.items.Item]: ...
    @classmethod
    def isLocation(cls) -> java.util.function.Predicate[org.openhab.core.items.Item]: ...
    @classmethod
    def isPoint(cls) -> java.util.function.Predicate[org.openhab.core.items.Item]: ...
    @classmethod
    def relatesTo(cls, property: typing.Type[org.openhab.core.semantics.model.Property]) -> java.util.function.Predicate[org.openhab.core.items.Item]: ...

class SemanticsService(java.lang.Object):
    """
    @NonNullByDefault public interface SemanticsService
    
        This interface defines a service, which offers functionality regarding semantic tags.
    
    
    """
    @typing.overload
    def getItemsInLocation(self, locationType: typing.Type[org.openhab.core.semantics.model.Location]) -> java.util.Set[org.openhab.core.items.Item]: ...
    @typing.overload
    def getItemsInLocation(self, labelOrSynonym: java.lang.String, locale: java.util.Locale) -> java.util.Set[org.openhab.core.items.Item]: ...
