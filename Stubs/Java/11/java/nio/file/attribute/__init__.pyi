import java
import java.io
import java.lang
import java.nio
import java.security
import java.time
import java.util
import java.util.concurrent
import typing


class AclEntry(java.lang.Object):
    """
    Java class 'java.nio.file.attribute.AclEntry'
    
        Extends:
            java.lang.Object
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def flags(self) -> java.util.Set['AclEntryFlag']: ...
    def hashCode(self) -> int: ...
    @classmethod
    @typing.overload
    def newBuilder(cls) -> 'AclEntry.Builder': ...
    @classmethod
    @typing.overload
    def newBuilder(cls, aclEntry: 'AclEntry') -> 'AclEntry.Builder': ...
    def permissions(self) -> java.util.Set['AclEntryPermission']: ...
    def principal(self) -> 'UserPrincipal': ...
    def toString(self) -> java.lang.String: ...
    def type(self) -> 'AclEntryType': ...
    class Builder(java.lang.Object):
        """
        Java class 'java.nio.file.attribute.AclEntry$Builder'
        
            Extends:
                java.lang.Object
        
        """
        def build(self) -> 'AclEntry': ...
        @typing.overload
        def setFlags(self, aclEntryFlagArray: typing.List['AclEntryFlag']) -> 'AclEntry.Builder': ...
        @typing.overload
        def setFlags(self, set: java.util.Set['AclEntryFlag']) -> 'AclEntry.Builder': ...
        @typing.overload
        def setPermissions(self, aclEntryPermissionArray: typing.List['AclEntryPermission']) -> 'AclEntry.Builder': ...
        @typing.overload
        def setPermissions(self, set: java.util.Set['AclEntryPermission']) -> 'AclEntry.Builder': ...
        def setPrincipal(self, userPrincipal: 'UserPrincipal') -> 'AclEntry.Builder': ...
        def setType(self, aclEntryType: 'AclEntryType') -> 'AclEntry.Builder': ...

class AclEntryFlag(java.lang.Enum[java.nio.file.attribute.AclEntryFlag]):
    """
    Java class 'java.nio.file.attribute.AclEntryFlag'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        FILE_INHERIT (java.nio.file.attribute.AclEntryFlag): final static enum constant
        DIRECTORY_INHERIT (java.nio.file.attribute.AclEntryFlag): final static enum constant
        NO_PROPAGATE_INHERIT (java.nio.file.attribute.AclEntryFlag): final static enum constant
        INHERIT_ONLY (java.nio.file.attribute.AclEntryFlag): final static enum constant
    
    """
    FILE_INHERIT: typing.ClassVar['AclEntryFlag'] = ...
    DIRECTORY_INHERIT: typing.ClassVar['AclEntryFlag'] = ...
    NO_PROPAGATE_INHERIT: typing.ClassVar['AclEntryFlag'] = ...
    INHERIT_ONLY: typing.ClassVar['AclEntryFlag'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, string: java.lang.String) -> 'AclEntryFlag': ...
    @classmethod
    def values(cls) -> typing.List['AclEntryFlag']: ...

class AclEntryPermission(java.lang.Enum[java.nio.file.attribute.AclEntryPermission]):
    """
    Java class 'java.nio.file.attribute.AclEntryPermission'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        READ_DATA (java.nio.file.attribute.AclEntryPermission): final static enum constant
        WRITE_DATA (java.nio.file.attribute.AclEntryPermission): final static enum constant
        APPEND_DATA (java.nio.file.attribute.AclEntryPermission): final static enum constant
        READ_NAMED_ATTRS (java.nio.file.attribute.AclEntryPermission): final static enum constant
        WRITE_NAMED_ATTRS (java.nio.file.attribute.AclEntryPermission): final static enum constant
        EXECUTE (java.nio.file.attribute.AclEntryPermission): final static enum constant
        DELETE_CHILD (java.nio.file.attribute.AclEntryPermission): final static enum constant
        READ_ATTRIBUTES (java.nio.file.attribute.AclEntryPermission): final static enum constant
        WRITE_ATTRIBUTES (java.nio.file.attribute.AclEntryPermission): final static enum constant
        DELETE (java.nio.file.attribute.AclEntryPermission): final static enum constant
        READ_ACL (java.nio.file.attribute.AclEntryPermission): final static enum constant
        WRITE_ACL (java.nio.file.attribute.AclEntryPermission): final static enum constant
        WRITE_OWNER (java.nio.file.attribute.AclEntryPermission): final static enum constant
        SYNCHRONIZE (java.nio.file.attribute.AclEntryPermission): final static enum constant
        LIST_DIRECTORY (java.nio.file.attribute.AclEntryPermission): final static field
        ADD_FILE (java.nio.file.attribute.AclEntryPermission): final static field
        ADD_SUBDIRECTORY (java.nio.file.attribute.AclEntryPermission): final static field
    
    """
    READ_DATA: typing.ClassVar['AclEntryPermission'] = ...
    WRITE_DATA: typing.ClassVar['AclEntryPermission'] = ...
    APPEND_DATA: typing.ClassVar['AclEntryPermission'] = ...
    READ_NAMED_ATTRS: typing.ClassVar['AclEntryPermission'] = ...
    WRITE_NAMED_ATTRS: typing.ClassVar['AclEntryPermission'] = ...
    EXECUTE: typing.ClassVar['AclEntryPermission'] = ...
    DELETE_CHILD: typing.ClassVar['AclEntryPermission'] = ...
    READ_ATTRIBUTES: typing.ClassVar['AclEntryPermission'] = ...
    WRITE_ATTRIBUTES: typing.ClassVar['AclEntryPermission'] = ...
    DELETE: typing.ClassVar['AclEntryPermission'] = ...
    READ_ACL: typing.ClassVar['AclEntryPermission'] = ...
    WRITE_ACL: typing.ClassVar['AclEntryPermission'] = ...
    WRITE_OWNER: typing.ClassVar['AclEntryPermission'] = ...
    SYNCHRONIZE: typing.ClassVar['AclEntryPermission'] = ...
    LIST_DIRECTORY: typing.ClassVar['AclEntryPermission'] = ...
    ADD_FILE: typing.ClassVar['AclEntryPermission'] = ...
    ADD_SUBDIRECTORY: typing.ClassVar['AclEntryPermission'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, string: java.lang.String) -> 'AclEntryPermission': ...
    @classmethod
    def values(cls) -> typing.List['AclEntryPermission']: ...

class AclEntryType(java.lang.Enum[java.nio.file.attribute.AclEntryType]):
    """
    Java class 'java.nio.file.attribute.AclEntryType'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        ALLOW (java.nio.file.attribute.AclEntryType): final static enum constant
        DENY (java.nio.file.attribute.AclEntryType): final static enum constant
        AUDIT (java.nio.file.attribute.AclEntryType): final static enum constant
        ALARM (java.nio.file.attribute.AclEntryType): final static enum constant
    
    """
    ALLOW: typing.ClassVar['AclEntryType'] = ...
    DENY: typing.ClassVar['AclEntryType'] = ...
    AUDIT: typing.ClassVar['AclEntryType'] = ...
    ALARM: typing.ClassVar['AclEntryType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, string: java.lang.String) -> 'AclEntryType': ...
    @classmethod
    def values(cls) -> typing.List['AclEntryType']: ...

class AttributeView(java.lang.Object):
    """
    public interface AttributeView
    
        An object that provides a read-only or updatable *view* of non-opaque values associated with an object in a filesystem.
        This interface is extended or implemented by specific attribute views that define the attributes supported by the view.
        A specific attribute view will typically define type-safe methods to read or update the attributes that it supports.
    
        Since:
            1.7
    
    
    """
    def name(self) -> java.lang.String: ...

class BasicFileAttributes(java.lang.Object):
    """
    public interface BasicFileAttributes
    
        Basic attributes associated with a file in a file system.
    
        Basic file attributes are attributes that are common to many file systems and consist of mandatory and optional file
        attributes as defined by this interface.
    
        **Usage Example:**
    
        .. code-block: java
        
            Path file = ...
            BasicFileAttributes attrs = Files.readAttributes(file, BasicFileAttributes.class);
         
    
        Since:
            1.7
    
        Also see:
            :class:`~java.nio.file.attribute.BasicFileAttributeView`
    
    
    """
    def creationTime(self) -> 'FileTime': ...
    def fileKey(self) -> typing.Any: ...
    def isDirectory(self) -> bool: ...
    def isOther(self) -> bool: ...
    def isRegularFile(self) -> bool: ...
    def isSymbolicLink(self) -> bool: ...
    def lastAccessTime(self) -> 'FileTime': ...
    def lastModifiedTime(self) -> 'FileTime': ...
    def size(self) -> int: ...

_FileAttribute__T = typing.TypeVar('_FileAttribute__T')  # <T>
class FileAttribute(java.lang.Object, typing.Generic[_FileAttribute__T]):
    """
    public interface FileAttribute<T>
    
        An object that encapsulates the value of a file attribute that can be set atomically when creating a new file or
        directory by invoking the :meth:`~java.nio.file.Files.createFile` or :meth:`~java.nio.file.Files.createDirectory`
        methods.
    
        Since:
            1.7
    
        Also see:
            :meth:`~java.nio.file.attribute.PosixFilePermissions.asFileAttribute`
    
    
    """
    def name(self) -> java.lang.String: ...
    def value(self) -> _FileAttribute__T: ...

class FileTime(java.lang.Comparable[java.nio.file.attribute.FileTime]):
    """
    Java class 'java.nio.file.attribute.FileTime'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.lang.Comparable
    
    """
    @typing.overload
    def compareTo(self, object: typing.Any) -> int: ...
    @typing.overload
    def compareTo(self, fileTime: 'FileTime') -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    @classmethod
    def fromMillis(cls, long: int) -> 'FileTime': ...
    def hashCode(self) -> int: ...
    def to(self, timeUnit: java.util.concurrent.TimeUnit) -> int: ...
    def toInstant(self) -> java.time.Instant: ...
    def toMillis(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class PosixFilePermission(java.lang.Enum[java.nio.file.attribute.PosixFilePermission]):
    """
    Java class 'java.nio.file.attribute.PosixFilePermission'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        OWNER_READ (java.nio.file.attribute.PosixFilePermission): final static enum constant
        OWNER_WRITE (java.nio.file.attribute.PosixFilePermission): final static enum constant
        OWNER_EXECUTE (java.nio.file.attribute.PosixFilePermission): final static enum constant
        GROUP_READ (java.nio.file.attribute.PosixFilePermission): final static enum constant
        GROUP_WRITE (java.nio.file.attribute.PosixFilePermission): final static enum constant
        GROUP_EXECUTE (java.nio.file.attribute.PosixFilePermission): final static enum constant
        OTHERS_READ (java.nio.file.attribute.PosixFilePermission): final static enum constant
        OTHERS_WRITE (java.nio.file.attribute.PosixFilePermission): final static enum constant
        OTHERS_EXECUTE (java.nio.file.attribute.PosixFilePermission): final static enum constant
    
    """
    OWNER_READ: typing.ClassVar['PosixFilePermission'] = ...
    OWNER_WRITE: typing.ClassVar['PosixFilePermission'] = ...
    OWNER_EXECUTE: typing.ClassVar['PosixFilePermission'] = ...
    GROUP_READ: typing.ClassVar['PosixFilePermission'] = ...
    GROUP_WRITE: typing.ClassVar['PosixFilePermission'] = ...
    GROUP_EXECUTE: typing.ClassVar['PosixFilePermission'] = ...
    OTHERS_READ: typing.ClassVar['PosixFilePermission'] = ...
    OTHERS_WRITE: typing.ClassVar['PosixFilePermission'] = ...
    OTHERS_EXECUTE: typing.ClassVar['PosixFilePermission'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, string: java.lang.String) -> 'PosixFilePermission': ...
    @classmethod
    def values(cls) -> typing.List['PosixFilePermission']: ...

class PosixFilePermissions(java.lang.Object):
    """
    Java class 'java.nio.file.attribute.PosixFilePermissions'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def asFileAttribute(cls, set: java.util.Set[PosixFilePermission]) -> FileAttribute[java.util.Set[PosixFilePermission]]: ...
    @classmethod
    def fromString(cls, string: java.lang.String) -> java.util.Set[PosixFilePermission]: ...
    @typing.overload
    def toString(self) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def toString(cls, set: java.util.Set[PosixFilePermission]) -> java.lang.String: ...

class UserPrincipal(java.security.Principal):
    """
    public interface UserPrincipal extends :class:`~java.security.Principal`
    
        A :code:`Principal` representing an identity used to determine access rights to objects in a file system.
    
        On many platforms and file systems an entity requires appropriate access rights or permissions in order to access
        objects in a file system. The access rights are generally performed by checking the identity of the entity. For example,
        on implementations that use Access Control Lists (ACLs) to enforce privilege separation then a file in the file system
        may have an associated ACL that determines the access rights of identities specified in the ACL.
    
        A :code:`UserPrincipal` object is an abstract representation of an identity. It has a
        :meth:`~java.security.Principal.getName` that is typically the username or account name that it represents. User
        principal objects may be obtained using a :class:`~java.nio.file.attribute.UserPrincipalLookupService`, or returned by
        :class:`~java.nio.file.attribute.FileAttributeView` implementations that provide access to identity related attributes.
        For example, the :class:`~java.nio.file.attribute.AclFileAttributeView` and
        :class:`~java.nio.file.attribute.PosixFileAttributeView` provide access to a file's
        :meth:`~java.nio.file.attribute.PosixFileAttributes.owner`.
    
        Since:
            1.7
    
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class UserPrincipalLookupService(java.lang.Object):
    """
    Java class 'java.nio.file.attribute.UserPrincipalLookupService'
    
        Extends:
            java.lang.Object
    
    """
    def lookupPrincipalByGroupName(self, string: java.lang.String) -> 'GroupPrincipal': ...
    def lookupPrincipalByName(self, string: java.lang.String) -> UserPrincipal: ...

class UserPrincipalNotFoundException(java.io.IOException):
    """
    Java class 'java.nio.file.attribute.UserPrincipalNotFoundException'
    
        Extends:
            java.io.IOException
    
      Constructors:
        * UserPrincipalNotFoundException(java.lang.String)
    
    """
    def __init__(self, string: java.lang.String): ...
    def getName(self) -> java.lang.String: ...

class DosFileAttributes(BasicFileAttributes):
    """
    Java class 'java.nio.file.attribute.DosFileAttributes'
    
        Interfaces:
            java.nio.file.attribute.BasicFileAttributes
    
    """
    def isArchive(self) -> bool: ...
    def isHidden(self) -> bool: ...
    def isReadOnly(self) -> bool: ...
    def isSystem(self) -> bool: ...

class FileAttributeView(AttributeView):
    """
    Java class 'java.nio.file.attribute.FileAttributeView'
    
        Interfaces:
            java.nio.file.attribute.AttributeView
    
    """

class FileStoreAttributeView(AttributeView):
    """
    Java class 'java.nio.file.attribute.FileStoreAttributeView'
    
        Interfaces:
            java.nio.file.attribute.AttributeView
    
    """

class GroupPrincipal(UserPrincipal):
    """
    Java class 'java.nio.file.attribute.GroupPrincipal'
    
        Interfaces:
            java.nio.file.attribute.UserPrincipal
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class PosixFileAttributes(BasicFileAttributes):
    """
    Java class 'java.nio.file.attribute.PosixFileAttributes'
    
        Interfaces:
            java.nio.file.attribute.BasicFileAttributes
    
    """
    def group(self) -> GroupPrincipal: ...
    def owner(self) -> UserPrincipal: ...
    def permissions(self) -> java.util.Set[PosixFilePermission]: ...

class BasicFileAttributeView(FileAttributeView):
    """
    Java class 'java.nio.file.attribute.BasicFileAttributeView'
    
        Interfaces:
            java.nio.file.attribute.FileAttributeView
    
    """
    def name(self) -> java.lang.String: ...
    def readAttributes(self) -> BasicFileAttributes: ...
    def setTimes(self, fileTime: FileTime, fileTime2: FileTime, fileTime3: FileTime) -> None: ...

class FileOwnerAttributeView(FileAttributeView):
    """
    Java class 'java.nio.file.attribute.FileOwnerAttributeView'
    
        Interfaces:
            java.nio.file.attribute.FileAttributeView
    
    """
    def getOwner(self) -> UserPrincipal: ...
    def name(self) -> java.lang.String: ...
    def setOwner(self, userPrincipal: UserPrincipal) -> None: ...

class UserDefinedFileAttributeView(FileAttributeView):
    """
    Java class 'java.nio.file.attribute.UserDefinedFileAttributeView'
    
        Interfaces:
            java.nio.file.attribute.FileAttributeView
    
    """
    def delete(self, string: java.lang.String) -> None: ...
    def list(self) -> java.util.List[java.lang.String]: ...
    def name(self) -> java.lang.String: ...
    def read(self, string: java.lang.String, byteBuffer: java.nio.ByteBuffer) -> int: ...
    def size(self, string: java.lang.String) -> int: ...
    def write(self, string: java.lang.String, byteBuffer: java.nio.ByteBuffer) -> int: ...

class AclFileAttributeView(FileOwnerAttributeView):
    """
    Java class 'java.nio.file.attribute.AclFileAttributeView'
    
        Interfaces:
            java.nio.file.attribute.FileOwnerAttributeView
    
    """
    def getAcl(self) -> java.util.List[AclEntry]: ...
    def name(self) -> java.lang.String: ...
    def setAcl(self, list: java.util.List[AclEntry]) -> None: ...

class DosFileAttributeView(BasicFileAttributeView):
    """
    Java class 'java.nio.file.attribute.DosFileAttributeView'
    
        Interfaces:
            java.nio.file.attribute.BasicFileAttributeView
    
    """
    def name(self) -> java.lang.String: ...
    @typing.overload
    def readAttributes(self) -> DosFileAttributes: ...
    @typing.overload
    def readAttributes(self) -> BasicFileAttributes: ...
    def setArchive(self, boolean: bool) -> None: ...
    def setHidden(self, boolean: bool) -> None: ...
    def setReadOnly(self, boolean: bool) -> None: ...
    def setSystem(self, boolean: bool) -> None: ...

class PosixFileAttributeView(BasicFileAttributeView, FileOwnerAttributeView):
    """
    Java class 'java.nio.file.attribute.PosixFileAttributeView'
    
        Interfaces:
            java.nio.file.attribute.BasicFileAttributeView,
            java.nio.file.attribute.FileOwnerAttributeView
    
    """
    def name(self) -> java.lang.String: ...
    @typing.overload
    def readAttributes(self) -> PosixFileAttributes: ...
    @typing.overload
    def readAttributes(self) -> BasicFileAttributes: ...
    def setGroup(self, groupPrincipal: GroupPrincipal) -> None: ...
    def setPermissions(self, set: java.util.Set[PosixFilePermission]) -> None: ...
