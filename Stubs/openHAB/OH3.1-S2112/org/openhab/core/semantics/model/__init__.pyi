import java.lang
import java.lang.annotation
import typing


class Tag(java.lang.Object):
    """
    @NonNullByDefault public interface Tag
    
        This is a marker interface for all semantic tag classes.
    
    
    """

class TagInfo(java.lang.annotation.Annotation):
    """
    Java class 'org.openhab.core.semantics.model.TagInfo'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def description(self) -> java.lang.String: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def id(self) -> java.lang.String: ...
    def label(self) -> java.lang.String: ...
    def synonyms(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...

class Equipment(Tag):
    """
    Java class 'org.openhab.core.semantics.model.Equipment'
    
        Interfaces:
            org.openhab.core.semantics.model.Tag
    
    """
    def hasLocation(self) -> 'Location': ...
    def isPartOf(self) -> 'Equipment': ...

class Location(Tag):
    """
    Java class 'org.openhab.core.semantics.model.Location'
    
        Interfaces:
            org.openhab.core.semantics.model.Tag
    
    """
    def isPartOf(self) -> 'Location': ...
    @classmethod
    def name(cls) -> java.lang.String: ...

class Point(Tag):
    """
    Java class 'org.openhab.core.semantics.model.Point'
    
        Interfaces:
            org.openhab.core.semantics.model.Tag
    
    """
    def hasLocation(self) -> Location: ...
    def relatesTo(self) -> 'Property': ...

class Property(Tag):
    """
    Java class 'org.openhab.core.semantics.model.Property'
    
        Interfaces:
            org.openhab.core.semantics.model.Tag
    
    """
