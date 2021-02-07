import java
import java.io
import java.lang
import java.net
import java.nio.channels
import java.nio.charset
import java.nio.file.attribute
import java.nio.file.spi
import java.security
import java.util
import java.util.concurrent
import java.util.function
import java.util.stream
import typing


class AccessMode(java.lang.Enum[java.nio.file.AccessMode]):
    """
    Java class 'java.nio.file.AccessMode'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        READ (java.nio.file.AccessMode): final static enum constant
        WRITE (java.nio.file.AccessMode): final static enum constant
        EXECUTE (java.nio.file.AccessMode): final static enum constant
    
    """
    READ: typing.ClassVar['AccessMode'] = ...
    WRITE: typing.ClassVar['AccessMode'] = ...
    EXECUTE: typing.ClassVar['AccessMode'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, string: java.lang.String) -> 'AccessMode': ...
    @classmethod
    def values(cls) -> typing.List['AccessMode']: ...

class ClosedDirectoryStreamException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.file.ClosedDirectoryStreamException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * ClosedDirectoryStreamException()
    
    """
    def __init__(self): ...

class ClosedFileSystemException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.file.ClosedFileSystemException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * ClosedFileSystemException()
    
    """
    def __init__(self): ...

class ClosedWatchServiceException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.file.ClosedWatchServiceException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * ClosedWatchServiceException()
    
    """
    def __init__(self): ...

class CopyOption(java.lang.Object):
    """
    public interface CopyOption
    
        An object that configures how to copy or move a file.
    
        Objects of this type may be used with the :meth:`~java.nio.file.Files.copy`, :meth:`~java.nio.file.Files.copy` and
        :meth:`~java.nio.file.Files.move` methods to configure how a file is copied or moved.
    
        The :class:`~java.nio.file.StandardCopyOption` enumeration type defines the *standard* options.
    
        Since:
            1.7
    
    
    """

class DirectoryIteratorException(java.util.ConcurrentModificationException):
    """
    Java class 'java.nio.file.DirectoryIteratorException'
    
        Extends:
            java.util.ConcurrentModificationException
    
      Constructors:
        * DirectoryIteratorException(java.io.IOException)
    
    """
    def __init__(self, iOException: java.io.IOException): ...
    @typing.overload
    def getCause(self) -> java.io.IOException: ...
    @typing.overload
    def getCause(self) -> java.lang.Throwable: ...

_DirectoryStream__Filter__T = typing.TypeVar('_DirectoryStream__Filter__T')  # <T>
_DirectoryStream__T = typing.TypeVar('_DirectoryStream__T')  # <T>
class DirectoryStream(java.io.Closeable, java.lang.Iterable[_DirectoryStream__T], typing.Generic[_DirectoryStream__T]):
    """
    Java class 'java.nio.file.DirectoryStream'
    
        Interfaces:
            java.io.Closeable, java.lang.Iterable
    
    """
    def iterator(self) -> java.util.Iterator[_DirectoryStream__T]: ...
    class Filter(java.lang.Object, typing.Generic[_DirectoryStream__Filter__T]):
        """
        Java class 'java.nio.file.DirectoryStream$Filter'
        
        """
        def accept(self, t: _DirectoryStream__Filter__T) -> bool: ...

class FileStore(java.lang.Object):
    """
    Java class 'java.nio.file.FileStore'
    
        Extends:
            java.lang.Object
    
    """
    def getAttribute(self, string: java.lang.String) -> typing.Any: ...
    def getBlockSize(self) -> int: ...
    _getFileStoreAttributeView__V = typing.TypeVar('_getFileStoreAttributeView__V', bound=java.nio.file.attribute.FileStoreAttributeView)  # <V>
    def getFileStoreAttributeView(self, class_: typing.Type[_getFileStoreAttributeView__V]) -> _getFileStoreAttributeView__V: ...
    def getTotalSpace(self) -> int: ...
    def getUnallocatedSpace(self) -> int: ...
    def getUsableSpace(self) -> int: ...
    def isReadOnly(self) -> bool: ...
    def name(self) -> java.lang.String: ...
    @typing.overload
    def supportsFileAttributeView(self, class_: typing.Type[java.nio.file.attribute.FileAttributeView]) -> bool: ...
    @typing.overload
    def supportsFileAttributeView(self, string: java.lang.String) -> bool: ...
    def type(self) -> java.lang.String: ...

class FileSystem(java.io.Closeable):
    """
    Java class 'java.nio.file.FileSystem'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Closeable
    
    """
    def close(self) -> None: ...
    def getFileStores(self) -> java.lang.Iterable[FileStore]: ...
    def getPath(self, string: java.lang.String, stringArray: typing.List[java.lang.String]) -> 'Path': ...
    def getPathMatcher(self, string: java.lang.String) -> 'PathMatcher': ...
    def getRootDirectories(self) -> java.lang.Iterable['Path']: ...
    def getSeparator(self) -> java.lang.String: ...
    def getUserPrincipalLookupService(self) -> java.nio.file.attribute.UserPrincipalLookupService: ...
    def isOpen(self) -> bool: ...
    def isReadOnly(self) -> bool: ...
    def newWatchService(self) -> 'WatchService': ...
    def provider(self) -> java.nio.file.spi.FileSystemProvider: ...
    def supportedFileAttributeViews(self) -> java.util.Set[java.lang.String]: ...

class FileSystemAlreadyExistsException(java.lang.RuntimeException):
    """
    Java class 'java.nio.file.FileSystemAlreadyExistsException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * FileSystemAlreadyExistsException()
        * FileSystemAlreadyExistsException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: java.lang.String): ...

class FileSystemException(java.io.IOException):
    """
    Java class 'java.nio.file.FileSystemException'
    
        Extends:
            java.io.IOException
    
      Constructors:
        * FileSystemException(java.lang.String)
        * FileSystemException(java.lang.String, java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, string: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, string2: java.lang.String, string3: java.lang.String): ...
    def getFile(self) -> java.lang.String: ...
    def getMessage(self) -> java.lang.String: ...
    def getOtherFile(self) -> java.lang.String: ...
    def getReason(self) -> java.lang.String: ...

class FileSystemNotFoundException(java.lang.RuntimeException):
    """
    Java class 'java.nio.file.FileSystemNotFoundException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * FileSystemNotFoundException()
        * FileSystemNotFoundException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: java.lang.String): ...

class FileSystems(java.lang.Object):
    """
    Java class 'java.nio.file.FileSystems'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def getDefault(cls) -> FileSystem: ...
    @classmethod
    def getFileSystem(cls, uRI: java.net.URI) -> FileSystem: ...
    @classmethod
    @typing.overload
    def newFileSystem(cls, uRI: java.net.URI, map: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> FileSystem: ...
    @classmethod
    @typing.overload
    def newFileSystem(cls, uRI: java.net.URI, map: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]], classLoader: java.lang.ClassLoader) -> FileSystem: ...
    @classmethod
    @typing.overload
    def newFileSystem(cls, path: 'Path', classLoader: java.lang.ClassLoader) -> FileSystem: ...

class FileVisitOption(java.lang.Enum[java.nio.file.FileVisitOption]):
    """
    Java class 'java.nio.file.FileVisitOption'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        FOLLOW_LINKS (java.nio.file.FileVisitOption): final static enum constant
    
    """
    FOLLOW_LINKS: typing.ClassVar['FileVisitOption'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, string: java.lang.String) -> 'FileVisitOption': ...
    @classmethod
    def values(cls) -> typing.List['FileVisitOption']: ...

class FileVisitResult(java.lang.Enum[java.nio.file.FileVisitResult]):
    """
    Java class 'java.nio.file.FileVisitResult'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        CONTINUE (java.nio.file.FileVisitResult): final static enum constant
        TERMINATE (java.nio.file.FileVisitResult): final static enum constant
        SKIP_SUBTREE (java.nio.file.FileVisitResult): final static enum constant
        SKIP_SIBLINGS (java.nio.file.FileVisitResult): final static enum constant
    
    """
    CONTINUE: typing.ClassVar['FileVisitResult'] = ...
    TERMINATE: typing.ClassVar['FileVisitResult'] = ...
    SKIP_SUBTREE: typing.ClassVar['FileVisitResult'] = ...
    SKIP_SIBLINGS: typing.ClassVar['FileVisitResult'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, string: java.lang.String) -> 'FileVisitResult': ...
    @classmethod
    def values(cls) -> typing.List['FileVisitResult']: ...

_FileVisitor__T = typing.TypeVar('_FileVisitor__T')  # <T>
class FileVisitor(java.lang.Object, typing.Generic[_FileVisitor__T]):
    """
    public interface FileVisitor<T>
    
        A visitor of files. An implementation of this interface is provided to the :meth:`~java.nio.file.Files.walkFileTree`
        methods to visit each file in a file tree.
    
        **Usage Examples:** Suppose we want to delete a file tree. In that case, each directory should be deleted after the
        entries in the directory are deleted.
    
        .. code-block: java
        
             Path start = ...
             Files.walkFileTree(start, new SimpleFileVisitor<Path>() {
                 @Override
                 public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
                     throws IOException
                 {
                     Files.delete(file);
                     return FileVisitResult.CONTINUE;
                 }
                 @Override
                 public FileVisitResult postVisitDirectory(Path dir, IOException e)
                     throws IOException
                 {
                     if (e == null) {
                         Files.delete(dir);
                         return FileVisitResult.CONTINUE;
                     } else {
                         // directory iteration failed
                         throw e;
                     }
                 }
             });
         
    
        Furthermore, suppose we want to copy a file tree to a target location. In that case, symbolic links should be followed
        and the target directory should be created before the entries in the directory are copied.
    
        .. code-block: java
        
             final Path source = ...
             final Path target = ...
        
             Files.walkFileTree(source, EnumSet.of(FileVisitOption.FOLLOW_LINKS), Integer.MAX_VALUE,
                 new SimpleFileVisitor<Path>() {
                     @Override
                     public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs)
                         throws IOException
                     {
                         Path targetdir = target.resolve(source.relativize(dir));
                         try {
                             Files.copy(dir, targetdir);
                         } catch (FileAlreadyExistsException e) {
                              if (!Files.isDirectory(targetdir))
                                  throw e;
                         }
                         return CONTINUE;
                     }
                     @Override
                     public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
                         throws IOException
                     {
                         Files.copy(file, target.resolve(source.relativize(file)));
                         return CONTINUE;
                     }
                 });
         
    
        Since:
            1.7
    
    
    """
    def postVisitDirectory(self, t: _FileVisitor__T, iOException: java.io.IOException) -> FileVisitResult: ...
    def preVisitDirectory(self, t: _FileVisitor__T, basicFileAttributes: java.nio.file.attribute.BasicFileAttributes) -> FileVisitResult: ...
    def visitFile(self, t: _FileVisitor__T, basicFileAttributes: java.nio.file.attribute.BasicFileAttributes) -> FileVisitResult: ...
    def visitFileFailed(self, t: _FileVisitor__T, iOException: java.io.IOException) -> FileVisitResult: ...

class Files(java.lang.Object):
    """
    Java class 'java.nio.file.Files'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    @typing.overload
    def copy(cls, path: 'Path', path2: 'Path', copyOptionArray: typing.List[CopyOption]) -> 'Path': ...
    @classmethod
    @typing.overload
    def copy(cls, inputStream: java.io.InputStream, path: 'Path', copyOptionArray: typing.List[CopyOption]) -> int: ...
    @classmethod
    @typing.overload
    def copy(cls, path: 'Path', outputStream: java.io.OutputStream) -> int: ...
    @classmethod
    def createDirectories(cls, path: 'Path', fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @classmethod
    def createDirectory(cls, path: 'Path', fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @classmethod
    def createFile(cls, path: 'Path', fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @classmethod
    def createLink(cls, path: 'Path', path2: 'Path') -> 'Path': ...
    @classmethod
    def createSymbolicLink(cls, path: 'Path', path2: 'Path', fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @classmethod
    @typing.overload
    def createTempDirectory(cls, string: java.lang.String, fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @classmethod
    @typing.overload
    def createTempDirectory(cls, path: 'Path', string: java.lang.String, fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @classmethod
    @typing.overload
    def createTempFile(cls, string: java.lang.String, string2: java.lang.String, fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @classmethod
    @typing.overload
    def createTempFile(cls, path: 'Path', string: java.lang.String, string2: java.lang.String, fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @classmethod
    def delete(cls, path: 'Path') -> None: ...
    @classmethod
    def deleteIfExists(cls, path: 'Path') -> bool: ...
    @classmethod
    def exists(cls, path: 'Path', linkOptionArray: typing.List['LinkOption']) -> bool: ...
    @classmethod
    def find(cls, path: 'Path', int: int, biPredicate: typing.Union[java.util.function.BiPredicate['Path', java.nio.file.attribute.BasicFileAttributes], typing.Callable[['Path'], java.nio.file.attribute.BasicFileAttributes]], fileVisitOptionArray: typing.List[FileVisitOption]) -> java.util.stream.Stream['Path']: ...
    @classmethod
    def getAttribute(cls, path: 'Path', string: java.lang.String, linkOptionArray: typing.List['LinkOption']) -> typing.Any: ...
    _getFileAttributeView__V = typing.TypeVar('_getFileAttributeView__V', bound=java.nio.file.attribute.FileAttributeView)  # <V>
    @classmethod
    def getFileAttributeView(cls, path: 'Path', class_: typing.Type[_getFileAttributeView__V], linkOptionArray: typing.List['LinkOption']) -> _getFileAttributeView__V: ...
    @classmethod
    def getFileStore(cls, path: 'Path') -> FileStore: ...
    @classmethod
    def getLastModifiedTime(cls, path: 'Path', linkOptionArray: typing.List['LinkOption']) -> java.nio.file.attribute.FileTime: ...
    @classmethod
    def getOwner(cls, path: 'Path', linkOptionArray: typing.List['LinkOption']) -> java.nio.file.attribute.UserPrincipal: ...
    @classmethod
    def getPosixFilePermissions(cls, path: 'Path', linkOptionArray: typing.List['LinkOption']) -> java.util.Set[java.nio.file.attribute.PosixFilePermission]: ...
    @classmethod
    def isDirectory(cls, path: 'Path', linkOptionArray: typing.List['LinkOption']) -> bool: ...
    @classmethod
    def isExecutable(cls, path: 'Path') -> bool: ...
    @classmethod
    def isHidden(cls, path: 'Path') -> bool: ...
    @classmethod
    def isReadable(cls, path: 'Path') -> bool: ...
    @classmethod
    def isRegularFile(cls, path: 'Path', linkOptionArray: typing.List['LinkOption']) -> bool: ...
    @classmethod
    def isSameFile(cls, path: 'Path', path2: 'Path') -> bool: ...
    @classmethod
    def isSymbolicLink(cls, path: 'Path') -> bool: ...
    @classmethod
    def isWritable(cls, path: 'Path') -> bool: ...
    @classmethod
    @typing.overload
    def lines(cls, path: 'Path') -> java.util.stream.Stream[java.lang.String]: ...
    @classmethod
    @typing.overload
    def lines(cls, path: 'Path', charset: java.nio.charset.Charset) -> java.util.stream.Stream[java.lang.String]: ...
    @classmethod
    def list(cls, path: 'Path') -> java.util.stream.Stream['Path']: ...
    @classmethod
    def move(cls, path: 'Path', path2: 'Path', copyOptionArray: typing.List[CopyOption]) -> 'Path': ...
    @classmethod
    @typing.overload
    def newBufferedReader(cls, path: 'Path') -> java.io.BufferedReader: ...
    @classmethod
    @typing.overload
    def newBufferedReader(cls, path: 'Path', charset: java.nio.charset.Charset) -> java.io.BufferedReader: ...
    @classmethod
    @typing.overload
    def newBufferedWriter(cls, path: 'Path', charset: java.nio.charset.Charset, openOptionArray: typing.List['OpenOption']) -> java.io.BufferedWriter: ...
    @classmethod
    @typing.overload
    def newBufferedWriter(cls, path: 'Path', openOptionArray: typing.List['OpenOption']) -> java.io.BufferedWriter: ...
    @classmethod
    @typing.overload
    def newByteChannel(cls, path: 'Path', openOptionArray: typing.List['OpenOption']) -> java.nio.channels.SeekableByteChannel: ...
    @classmethod
    @typing.overload
    def newByteChannel(cls, path: 'Path', set: java.util.Set['OpenOption'], fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> java.nio.channels.SeekableByteChannel: ...
    @classmethod
    @typing.overload
    def newDirectoryStream(cls, path: 'Path') -> DirectoryStream['Path']: ...
    @classmethod
    @typing.overload
    def newDirectoryStream(cls, path: 'Path', string: java.lang.String) -> DirectoryStream['Path']: ...
    @classmethod
    @typing.overload
    def newDirectoryStream(cls, path: 'Path', filter: typing.Union[DirectoryStream.Filter['Path'], typing.Callable[[], 'Path']]) -> DirectoryStream['Path']: ...
    @classmethod
    def newInputStream(cls, path: 'Path', openOptionArray: typing.List['OpenOption']) -> java.io.InputStream: ...
    @classmethod
    def newOutputStream(cls, path: 'Path', openOptionArray: typing.List['OpenOption']) -> java.io.OutputStream: ...
    @classmethod
    def notExists(cls, path: 'Path', linkOptionArray: typing.List['LinkOption']) -> bool: ...
    @classmethod
    def probeContentType(cls, path: 'Path') -> java.lang.String: ...
    @classmethod
    def readAllBytes(cls, path: 'Path') -> typing.List[int]: ...
    @classmethod
    @typing.overload
    def readAllLines(cls, path: 'Path') -> java.util.List[java.lang.String]: ...
    @classmethod
    @typing.overload
    def readAllLines(cls, path: 'Path', charset: java.nio.charset.Charset) -> java.util.List[java.lang.String]: ...
    _readAttributes_0__A = typing.TypeVar('_readAttributes_0__A', bound=java.nio.file.attribute.BasicFileAttributes)  # <A>
    @classmethod
    @typing.overload
    def readAttributes(cls, path: 'Path', class_: typing.Type[_readAttributes_0__A], linkOptionArray: typing.List['LinkOption']) -> _readAttributes_0__A: ...
    @classmethod
    @typing.overload
    def readAttributes(cls, path: 'Path', string: java.lang.String, linkOptionArray: typing.List['LinkOption']) -> java.util.Map[java.lang.String, typing.Any]: ...
    @classmethod
    @typing.overload
    def readString(cls, path: 'Path') -> java.lang.String: ...
    @classmethod
    @typing.overload
    def readString(cls, path: 'Path', charset: java.nio.charset.Charset) -> java.lang.String: ...
    @classmethod
    def readSymbolicLink(cls, path: 'Path') -> 'Path': ...
    @classmethod
    def setAttribute(cls, path: 'Path', string: java.lang.String, object: typing.Any, linkOptionArray: typing.List['LinkOption']) -> 'Path': ...
    @classmethod
    def setLastModifiedTime(cls, path: 'Path', fileTime: java.nio.file.attribute.FileTime) -> 'Path': ...
    @classmethod
    def setOwner(cls, path: 'Path', userPrincipal: java.nio.file.attribute.UserPrincipal) -> 'Path': ...
    @classmethod
    def setPosixFilePermissions(cls, path: 'Path', set: java.util.Set[java.nio.file.attribute.PosixFilePermission]) -> 'Path': ...
    @classmethod
    def size(cls, path: 'Path') -> int: ...
    @classmethod
    @typing.overload
    def walk(cls, path: 'Path', int: int, fileVisitOptionArray: typing.List[FileVisitOption]) -> java.util.stream.Stream['Path']: ...
    @classmethod
    @typing.overload
    def walk(cls, path: 'Path', fileVisitOptionArray: typing.List[FileVisitOption]) -> java.util.stream.Stream['Path']: ...
    @classmethod
    @typing.overload
    def walkFileTree(cls, path: 'Path', fileVisitor: FileVisitor['Path']) -> 'Path': ...
    @classmethod
    @typing.overload
    def walkFileTree(cls, path: 'Path', set: java.util.Set[FileVisitOption], int: int, fileVisitor: FileVisitor['Path']) -> 'Path': ...
    @classmethod
    @typing.overload
    def write(cls, path: 'Path', byteArray: typing.List[int], openOptionArray: typing.List['OpenOption']) -> 'Path': ...
    @classmethod
    @typing.overload
    def write(cls, path: 'Path', iterable: java.lang.Iterable[java.lang.CharSequence], charset: java.nio.charset.Charset, openOptionArray: typing.List['OpenOption']) -> 'Path': ...
    @classmethod
    @typing.overload
    def write(cls, path: 'Path', iterable: java.lang.Iterable[java.lang.CharSequence], openOptionArray: typing.List['OpenOption']) -> 'Path': ...
    @classmethod
    @typing.overload
    def writeString(cls, path: 'Path', charSequence: java.lang.CharSequence, charset: java.nio.charset.Charset, openOptionArray: typing.List['OpenOption']) -> 'Path': ...
    @classmethod
    @typing.overload
    def writeString(cls, path: 'Path', charSequence: java.lang.CharSequence, openOptionArray: typing.List['OpenOption']) -> 'Path': ...

class InvalidPathException(java.lang.IllegalArgumentException):
    """
    Java class 'java.nio.file.InvalidPathException'
    
        Extends:
            java.lang.IllegalArgumentException
    
      Constructors:
        * InvalidPathException(java.lang.String, java.lang.String, int)
        * InvalidPathException(java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, string: java.lang.String, string2: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, string2: java.lang.String, int: int): ...
    def getIndex(self) -> int: ...
    def getInput(self) -> java.lang.String: ...
    def getMessage(self) -> java.lang.String: ...
    def getReason(self) -> java.lang.String: ...

class LinkPermission(java.security.BasicPermission):
    """
    Java class 'java.nio.file.LinkPermission'
    
        Extends:
            java.security.BasicPermission
    
      Constructors:
        * LinkPermission(java.lang.String)
        * LinkPermission(java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, string: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, string2: java.lang.String): ...

class OpenOption(java.lang.Object):
    """
    public interface OpenOption
    
        An object that configures how to open or create a file.
    
        Objects of this type are used by methods such as :meth:`~java.nio.file.Files.newOutputStream`,
        :meth:`~java.nio.file.Files.newByteChannel`, :meth:`~java.nio.channels.FileChannel.open`, and
        :meth:`~java.nio.channels.AsynchronousFileChannel.open` when opening or creating a file.
    
        The :class:`~java.nio.file.StandardOpenOption` enumeration type defines the *standard* options.
    
        Since:
            1.7
    
    
    """

class PathMatcher(java.lang.Object):
    """
    :class:`~java.lang.FunctionalInterface` public interface PathMatcher
    
        An interface that is implemented by objects that perform match operations on paths.
    
        Since:
            1.7
    
        Also see:
            :meth:`~java.nio.file.FileSystem.getPathMatcher`, :meth:`~java.nio.file.Files.newDirectoryStream`
    
    
    """
    def matches(self, path: 'Path') -> bool: ...

class Paths(java.lang.Object):
    """
    Java class 'java.nio.file.Paths'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    @typing.overload
    def get(cls, string: java.lang.String, stringArray: typing.List[java.lang.String]) -> 'Path': ...
    @classmethod
    @typing.overload
    def get(cls, uRI: java.net.URI) -> 'Path': ...

class ProviderMismatchException(java.lang.IllegalArgumentException):
    """
    Java class 'java.nio.file.ProviderMismatchException'
    
        Extends:
            java.lang.IllegalArgumentException
    
      Constructors:
        * ProviderMismatchException()
        * ProviderMismatchException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: java.lang.String): ...

class ProviderNotFoundException(java.lang.RuntimeException):
    """
    Java class 'java.nio.file.ProviderNotFoundException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * ProviderNotFoundException()
        * ProviderNotFoundException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: java.lang.String): ...

class ReadOnlyFileSystemException(java.lang.UnsupportedOperationException):
    """
    Java class 'java.nio.file.ReadOnlyFileSystemException'
    
        Extends:
            java.lang.UnsupportedOperationException
    
      Constructors:
        * ReadOnlyFileSystemException()
    
    """
    def __init__(self): ...

class StandardWatchEventKinds(java.lang.Object):
    """
    Java class 'java.nio.file.StandardWatchEventKinds'
    
        Extends:
            java.lang.Object
    
      Attributes:
        OVERFLOW (java.nio.file.WatchEvent$Kind): final static field
        ENTRY_CREATE (java.nio.file.WatchEvent$Kind): final static field
        ENTRY_DELETE (java.nio.file.WatchEvent$Kind): final static field
        ENTRY_MODIFY (java.nio.file.WatchEvent$Kind): final static field
    
    """
    OVERFLOW: typing.ClassVar['WatchEvent.Kind'] = ...
    ENTRY_CREATE: typing.ClassVar['WatchEvent.Kind'] = ...
    ENTRY_DELETE: typing.ClassVar['WatchEvent.Kind'] = ...
    ENTRY_MODIFY: typing.ClassVar['WatchEvent.Kind'] = ...

_WatchEvent__Kind__T = typing.TypeVar('_WatchEvent__Kind__T')  # <T>
_WatchEvent__T = typing.TypeVar('_WatchEvent__T')  # <T>
class WatchEvent(java.lang.Object, typing.Generic[_WatchEvent__T]):
    """
    public interface WatchEvent<T>
    
        An event or a repeated event for an object that is registered with a :class:`~java.nio.file.WatchService`.
    
        An event is classified by its :meth:`~java.nio.file.WatchEvent.kind` and has a :meth:`~java.nio.file.WatchEvent.count`
        to indicate the number of times that the event has been observed. This allows for efficient representation of repeated
        events. The :meth:`~java.nio.file.WatchEvent.context` method returns any context associated with the event. In the case
        of a repeated event then the context is the same for all events.
    
        Watch events are immutable and safe for use by multiple concurrent threads.
    
        Since:
            1.7
    
    
    """
    def context(self) -> _WatchEvent__T: ...
    def count(self) -> int: ...
    def kind(self) -> 'WatchEvent.Kind'[_WatchEvent__T]: ...
    class Kind(java.lang.Object, typing.Generic[_WatchEvent__Kind__T]):
        """
        Java class 'java.nio.file.WatchEvent$Kind'
        
        """
        def name(self) -> java.lang.String: ...
        def type(self) -> typing.Type[_WatchEvent__Kind__T]: ...
    class Modifier(java.lang.Object):
        """
        Java class 'java.nio.file.WatchEvent$Modifier'
        
        """
        def name(self) -> java.lang.String: ...

class WatchKey(java.lang.Object):
    """
    public interface WatchKey
    
        A token representing the registration of a :class:`~java.nio.file.Watchable` object with a
        :class:`~java.nio.file.WatchService`.
    
        A watch key is created when a watchable object is registered with a watch service. The key remains
        :meth:`~java.nio.file.WatchKey.isValid` until:
    
          1.  It is cancelled, explicitly, by invoking its :meth:`~java.nio.file.WatchKey.cancel` method, or
          2.  Cancelled implicitly, because the object is no longer accessible, or
          3.  By :meth:`~java.nio.file.WatchService.close` the watch service.
    
    
        A watch key has a state. When initially created the key is said to be *ready*. When an event is detected then the key is
        *signalled* and queued so that it can be retrieved by invoking the watch service's
        :meth:`~java.nio.file.WatchService.poll` or :meth:`~java.nio.file.WatchService.take` methods. Once signalled, a key
        remains in this state until its :meth:`~java.nio.file.WatchKey.reset` method is invoked to return the key to the ready
        state. Events detected while the key is in the signalled state are queued but do not cause the key to be re-queued for
        retrieval from the watch service. Events are retrieved by invoking the key's :meth:`~java.nio.file.WatchKey.pollEvents`
        method. This method retrieves and removes all events accumulated for the object. When initially created, a watch key has
        no pending events. Typically events are retrieved when the key is in the signalled state leading to the following idiom:
    
        .. code-block: java
        
             for (;;) {
                 // retrieve key
                 WatchKey key = watcher.take();
        
                 // process events
                 for (WatchEvent<?> event: key.pollEvents()) {
                     :
                 }
        
                 // reset the key
                 boolean valid = key.reset();
                 if (!valid) {
                     // object no longer registered
                 }
             }
         
    
        Watch keys are safe for use by multiple concurrent threads. Where there are several threads retrieving signalled keys
        from a watch service then care should be taken to ensure that the :code:`reset` method is only invoked after the events
        for the object have been processed. This ensures that one thread is processing the events for an object at any time.
    
        Since:
            1.7
    
    
    """
    def cancel(self) -> None: ...
    def isValid(self) -> bool: ...
    def pollEvents(self) -> java.util.List[WatchEvent[typing.Any]]: ...
    def reset(self) -> bool: ...
    def watchable(self) -> 'Watchable': ...

class WatchService(java.io.Closeable):
    """
    Java class 'java.nio.file.WatchService'
    
        Interfaces:
            java.io.Closeable
    
    """
    def close(self) -> None: ...
    @typing.overload
    def poll(self) -> WatchKey: ...
    @typing.overload
    def poll(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> WatchKey: ...
    def take(self) -> WatchKey: ...

class Watchable(java.lang.Object):
    """
    public interface Watchable
    
        An object that may be registered with a watch service so that it can be *watched* for changes and events.
    
        This interface defines the :meth:`~java.nio.file.Watchable.register` method to register the object with a
        :class:`~java.nio.file.WatchService` returning a :class:`~java.nio.file.WatchKey` to represent the registration. An
        object may be registered with more than one watch service. Registration with a watch service is cancelled by invoking
        the key's :meth:`~java.nio.file.WatchKey.cancel` method.
    
        Since:
            1.7
    
        Also see:
            :meth:`~java.nio.file.Path.register`
    
    
    """
    @typing.overload
    def register(self, watchService: WatchService, kindArray: typing.List[WatchEvent.Kind[typing.Any]]) -> WatchKey: ...
    @typing.overload
    def register(self, watchService: WatchService, kindArray: typing.List[WatchEvent.Kind[typing.Any]], modifierArray: typing.List[WatchEvent.Modifier]) -> WatchKey: ...

class AccessDeniedException(FileSystemException):
    """
    Java class 'java.nio.file.AccessDeniedException'
    
        Extends:
            java.nio.file.FileSystemException
    
      Constructors:
        * AccessDeniedException(java.lang.String)
        * AccessDeniedException(java.lang.String, java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, string: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, string2: java.lang.String, string3: java.lang.String): ...

class AtomicMoveNotSupportedException(FileSystemException):
    """
    Java class 'java.nio.file.AtomicMoveNotSupportedException'
    
        Extends:
            java.nio.file.FileSystemException
    
      Constructors:
        * AtomicMoveNotSupportedException(java.lang.String, java.lang.String, java.lang.String)
    
    """
    def __init__(self, string: java.lang.String, string2: java.lang.String, string3: java.lang.String): ...

class DirectoryNotEmptyException(FileSystemException):
    """
    Java class 'java.nio.file.DirectoryNotEmptyException'
    
        Extends:
            java.nio.file.FileSystemException
    
      Constructors:
        * DirectoryNotEmptyException(java.lang.String)
    
    """
    def __init__(self, string: java.lang.String): ...

class FileAlreadyExistsException(FileSystemException):
    """
    Java class 'java.nio.file.FileAlreadyExistsException'
    
        Extends:
            java.nio.file.FileSystemException
    
      Constructors:
        * FileAlreadyExistsException(java.lang.String)
        * FileAlreadyExistsException(java.lang.String, java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, string: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, string2: java.lang.String, string3: java.lang.String): ...

class FileSystemLoopException(FileSystemException):
    """
    Java class 'java.nio.file.FileSystemLoopException'
    
        Extends:
            java.nio.file.FileSystemException
    
      Constructors:
        * FileSystemLoopException(java.lang.String)
    
    """
    def __init__(self, string: java.lang.String): ...

class LinkOption(java.lang.Enum[java.nio.file.LinkOption], OpenOption, CopyOption):
    """
    Java class 'java.nio.file.LinkOption'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            java.nio.file.OpenOption, java.nio.file.CopyOption
    
      Attributes:
        NOFOLLOW_LINKS (java.nio.file.LinkOption): final static enum constant
    
    """
    NOFOLLOW_LINKS: typing.ClassVar['LinkOption'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, string: java.lang.String) -> 'LinkOption': ...
    @classmethod
    def values(cls) -> typing.List['LinkOption']: ...

class NoSuchFileException(FileSystemException):
    """
    Java class 'java.nio.file.NoSuchFileException'
    
        Extends:
            java.nio.file.FileSystemException
    
      Constructors:
        * NoSuchFileException(java.lang.String)
        * NoSuchFileException(java.lang.String, java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, string: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, string2: java.lang.String, string3: java.lang.String): ...

class NotDirectoryException(FileSystemException):
    """
    Java class 'java.nio.file.NotDirectoryException'
    
        Extends:
            java.nio.file.FileSystemException
    
      Constructors:
        * NotDirectoryException(java.lang.String)
    
    """
    def __init__(self, string: java.lang.String): ...

class NotLinkException(FileSystemException):
    """
    Java class 'java.nio.file.NotLinkException'
    
        Extends:
            java.nio.file.FileSystemException
    
      Constructors:
        * NotLinkException(java.lang.String)
        * NotLinkException(java.lang.String, java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, string: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, string2: java.lang.String, string3: java.lang.String): ...

class Path(java.lang.Comparable[java.nio.file.Path], java.lang.Iterable[java.nio.file.Path], Watchable):
    """
    Java class 'java.nio.file.Path'
    
        Interfaces:
            java.lang.Comparable, java.lang.Iterable,
            java.nio.file.Watchable
    
    """
    @typing.overload
    def compareTo(self, path: 'Path') -> int: ...
    @typing.overload
    def compareTo(self, object: typing.Any) -> int: ...
    @typing.overload
    def endsWith(self, path: 'Path') -> bool: ...
    @typing.overload
    def endsWith(self, string: java.lang.String) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getFileName(self) -> 'Path': ...
    def getFileSystem(self) -> FileSystem: ...
    def getName(self, int: int) -> 'Path': ...
    def getNameCount(self) -> int: ...
    def getParent(self) -> 'Path': ...
    def getRoot(self) -> 'Path': ...
    def hashCode(self) -> int: ...
    def isAbsolute(self) -> bool: ...
    def iterator(self) -> java.util.Iterator['Path']: ...
    def normalize(self) -> 'Path': ...
    @classmethod
    @typing.overload
    def of(cls, string: java.lang.String, stringArray: typing.List[java.lang.String]) -> 'Path': ...
    @classmethod
    @typing.overload
    def of(cls, uRI: java.net.URI) -> 'Path': ...
    @typing.overload
    def register(self, watchService: WatchService, kindArray: typing.List[WatchEvent.Kind[typing.Any]], modifierArray: typing.List[WatchEvent.Modifier]) -> WatchKey: ...
    @typing.overload
    def register(self, watchService: WatchService, kindArray: typing.List[WatchEvent.Kind[typing.Any]]) -> WatchKey: ...
    def relativize(self, path: 'Path') -> 'Path': ...
    @typing.overload
    def resolve(self, path: 'Path') -> 'Path': ...
    @typing.overload
    def resolve(self, string: java.lang.String) -> 'Path': ...
    @typing.overload
    def resolveSibling(self, string: java.lang.String) -> 'Path': ...
    @typing.overload
    def resolveSibling(self, path: 'Path') -> 'Path': ...
    @typing.overload
    def startsWith(self, path: 'Path') -> bool: ...
    @typing.overload
    def startsWith(self, string: java.lang.String) -> bool: ...
    def subpath(self, int: int, int2: int) -> 'Path': ...
    def toAbsolutePath(self) -> 'Path': ...
    def toFile(self) -> java.io.File: ...
    def toRealPath(self, linkOptionArray: typing.List[LinkOption]) -> 'Path': ...
    def toString(self) -> java.lang.String: ...
    def toUri(self) -> java.net.URI: ...

_SecureDirectoryStream__T = typing.TypeVar('_SecureDirectoryStream__T')  # <T>
class SecureDirectoryStream(DirectoryStream[_SecureDirectoryStream__T], typing.Generic[_SecureDirectoryStream__T]):
    """
    Java class 'java.nio.file.SecureDirectoryStream'
    
        Interfaces:
            java.nio.file.DirectoryStream
    
    """
    def deleteDirectory(self, t: _SecureDirectoryStream__T) -> None: ...
    def deleteFile(self, t: _SecureDirectoryStream__T) -> None: ...
    _getFileAttributeView_0__V = typing.TypeVar('_getFileAttributeView_0__V', bound=java.nio.file.attribute.FileAttributeView)  # <V>
    @typing.overload
    def getFileAttributeView(self, class_: typing.Type[_getFileAttributeView_0__V]) -> _getFileAttributeView_0__V: ...
    _getFileAttributeView_1__V = typing.TypeVar('_getFileAttributeView_1__V', bound=java.nio.file.attribute.FileAttributeView)  # <V>
    @typing.overload
    def getFileAttributeView(self, t: _SecureDirectoryStream__T, class_: typing.Type[_getFileAttributeView_1__V], linkOptionArray: typing.List[LinkOption]) -> _getFileAttributeView_1__V: ...
    def move(self, t: _SecureDirectoryStream__T, secureDirectoryStream: 'SecureDirectoryStream'[_SecureDirectoryStream__T], t2: _SecureDirectoryStream__T) -> None: ...
    def newByteChannel(self, t: _SecureDirectoryStream__T, set: java.util.Set[OpenOption], fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> java.nio.channels.SeekableByteChannel: ...
    def newDirectoryStream(self, t: _SecureDirectoryStream__T, linkOptionArray: typing.List[LinkOption]) -> 'SecureDirectoryStream'[_SecureDirectoryStream__T]: ...

_SimpleFileVisitor__T = typing.TypeVar('_SimpleFileVisitor__T')  # <T>
class SimpleFileVisitor(FileVisitor[_SimpleFileVisitor__T], typing.Generic[_SimpleFileVisitor__T]):
    """
    Java class 'java.nio.file.SimpleFileVisitor'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.nio.file.FileVisitor
    
    """
    def postVisitDirectory(self, t: _SimpleFileVisitor__T, iOException: java.io.IOException) -> FileVisitResult: ...
    def preVisitDirectory(self, t: _SimpleFileVisitor__T, basicFileAttributes: java.nio.file.attribute.BasicFileAttributes) -> FileVisitResult: ...
    def visitFile(self, t: _SimpleFileVisitor__T, basicFileAttributes: java.nio.file.attribute.BasicFileAttributes) -> FileVisitResult: ...
    def visitFileFailed(self, t: _SimpleFileVisitor__T, iOException: java.io.IOException) -> FileVisitResult: ...

class StandardCopyOption(java.lang.Enum[java.nio.file.StandardCopyOption], CopyOption):
    """
    Java class 'java.nio.file.StandardCopyOption'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            java.nio.file.CopyOption
    
      Attributes:
        REPLACE_EXISTING (java.nio.file.StandardCopyOption): final static enum constant
        COPY_ATTRIBUTES (java.nio.file.StandardCopyOption): final static enum constant
        ATOMIC_MOVE (java.nio.file.StandardCopyOption): final static enum constant
    
    """
    REPLACE_EXISTING: typing.ClassVar['StandardCopyOption'] = ...
    COPY_ATTRIBUTES: typing.ClassVar['StandardCopyOption'] = ...
    ATOMIC_MOVE: typing.ClassVar['StandardCopyOption'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, string: java.lang.String) -> 'StandardCopyOption': ...
    @classmethod
    def values(cls) -> typing.List['StandardCopyOption']: ...

class StandardOpenOption(java.lang.Enum[java.nio.file.StandardOpenOption], OpenOption):
    """
    Java class 'java.nio.file.StandardOpenOption'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            java.nio.file.OpenOption
    
      Attributes:
        READ (java.nio.file.StandardOpenOption): final static enum constant
        WRITE (java.nio.file.StandardOpenOption): final static enum constant
        APPEND (java.nio.file.StandardOpenOption): final static enum constant
        TRUNCATE_EXISTING (java.nio.file.StandardOpenOption): final static enum constant
        CREATE (java.nio.file.StandardOpenOption): final static enum constant
        CREATE_NEW (java.nio.file.StandardOpenOption): final static enum constant
        DELETE_ON_CLOSE (java.nio.file.StandardOpenOption): final static enum constant
        SPARSE (java.nio.file.StandardOpenOption): final static enum constant
        SYNC (java.nio.file.StandardOpenOption): final static enum constant
        DSYNC (java.nio.file.StandardOpenOption): final static enum constant
    
    """
    READ: typing.ClassVar['StandardOpenOption'] = ...
    WRITE: typing.ClassVar['StandardOpenOption'] = ...
    APPEND: typing.ClassVar['StandardOpenOption'] = ...
    TRUNCATE_EXISTING: typing.ClassVar['StandardOpenOption'] = ...
    CREATE: typing.ClassVar['StandardOpenOption'] = ...
    CREATE_NEW: typing.ClassVar['StandardOpenOption'] = ...
    DELETE_ON_CLOSE: typing.ClassVar['StandardOpenOption'] = ...
    SPARSE: typing.ClassVar['StandardOpenOption'] = ...
    SYNC: typing.ClassVar['StandardOpenOption'] = ...
    DSYNC: typing.ClassVar['StandardOpenOption'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, string: java.lang.String) -> 'StandardOpenOption': ...
    @classmethod
    def values(cls) -> typing.List['StandardOpenOption']: ...
