import java.lang
import java.net
import java.nio.channels
import java.util.concurrent
import typing


class AbstractInterruptibleChannel(java.nio.channels.InterruptibleChannel):
    """
    Java class 'java.nio.channels.spi.AbstractInterruptibleChannel'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.nio.channels.Channel,
            java.nio.channels.InterruptibleChannel
    
    """
    def close(self) -> None: ...
    def isOpen(self) -> bool: ...

class AbstractSelectableChannel(java.nio.channels.SelectableChannel):
    """
    Java class 'java.nio.channels.spi.AbstractSelectableChannel'
    
        Extends:
            java.nio.channels.SelectableChannel
    
    """
    def blockingLock(self) -> typing.Any: ...
    def configureBlocking(self, boolean: bool) -> java.nio.channels.SelectableChannel: ...
    def isBlocking(self) -> bool: ...
    def isRegistered(self) -> bool: ...
    def keyFor(self, selector: java.nio.channels.Selector) -> java.nio.channels.SelectionKey: ...
    def provider(self) -> 'SelectorProvider': ...
    @typing.overload
    def register(self, selector: java.nio.channels.Selector, int: int) -> java.nio.channels.SelectionKey: ...
    @typing.overload
    def register(self, selector: java.nio.channels.Selector, int: int, object: typing.Any) -> java.nio.channels.SelectionKey: ...

class AbstractSelectionKey(java.nio.channels.SelectionKey):
    """
    Java class 'java.nio.channels.spi.AbstractSelectionKey'
    
        Extends:
            java.nio.channels.SelectionKey
    
    """
    def cancel(self) -> None: ...
    def isValid(self) -> bool: ...

class AbstractSelector(java.nio.channels.Selector):
    """
    Java class 'java.nio.channels.spi.AbstractSelector'
    
        Extends:
            java.nio.channels.Selector
    
    """
    def close(self) -> None: ...
    def isOpen(self) -> bool: ...
    def provider(self) -> 'SelectorProvider': ...

class AsynchronousChannelProvider(java.lang.Object):
    """
    Java class 'java.nio.channels.spi.AsynchronousChannelProvider'
    
        Extends:
            java.lang.Object
    
    """
    @typing.overload
    def openAsynchronousChannelGroup(self, int: int, threadFactory: java.util.concurrent.ThreadFactory) -> java.nio.channels.AsynchronousChannelGroup: ...
    @typing.overload
    def openAsynchronousChannelGroup(self, executorService: java.util.concurrent.ExecutorService, int: int) -> java.nio.channels.AsynchronousChannelGroup: ...
    def openAsynchronousServerSocketChannel(self, asynchronousChannelGroup: java.nio.channels.AsynchronousChannelGroup) -> java.nio.channels.AsynchronousServerSocketChannel: ...
    def openAsynchronousSocketChannel(self, asynchronousChannelGroup: java.nio.channels.AsynchronousChannelGroup) -> java.nio.channels.AsynchronousSocketChannel: ...
    @classmethod
    def provider(cls) -> 'AsynchronousChannelProvider': ...

class SelectorProvider(java.lang.Object):
    """
    Java class 'java.nio.channels.spi.SelectorProvider'
    
        Extends:
            java.lang.Object
    
    """
    def inheritedChannel(self) -> java.nio.channels.Channel: ...
    @typing.overload
    def openDatagramChannel(self) -> java.nio.channels.DatagramChannel: ...
    @typing.overload
    def openDatagramChannel(self, protocolFamily: java.net.ProtocolFamily) -> java.nio.channels.DatagramChannel: ...
    def openPipe(self) -> java.nio.channels.Pipe: ...
    def openSelector(self) -> AbstractSelector: ...
    def openServerSocketChannel(self) -> java.nio.channels.ServerSocketChannel: ...
    def openSocketChannel(self) -> java.nio.channels.SocketChannel: ...
    @classmethod
    def provider(cls) -> 'SelectorProvider': ...
