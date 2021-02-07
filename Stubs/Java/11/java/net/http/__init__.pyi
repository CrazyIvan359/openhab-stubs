import java
import java.io
import java.lang
import java.net
import java.nio
import java.nio.charset
import java.nio.file
import java.time
import java.util
import java.util.concurrent
import java.util.function
import java.util.stream
import javax.net.ssl
import typing


class HttpClient(java.lang.Object):
    """
    Java class 'java.net.http.HttpClient'
    
        Extends:
            java.lang.Object
    
    """
    def authenticator(self) -> java.util.Optional[java.net.Authenticator]: ...
    def connectTimeout(self) -> java.util.Optional[java.time.Duration]: ...
    def cookieHandler(self) -> java.util.Optional[java.net.CookieHandler]: ...
    def executor(self) -> java.util.Optional[java.util.concurrent.Executor]: ...
    def followRedirects(self) -> 'HttpClient.Redirect': ...
    @classmethod
    def newBuilder(cls) -> 'HttpClient.Builder': ...
    @classmethod
    def newHttpClient(cls) -> 'HttpClient': ...
    def newWebSocketBuilder(self) -> 'WebSocket.Builder': ...
    def proxy(self) -> java.util.Optional[java.net.ProxySelector]: ...
    _send__T = typing.TypeVar('_send__T')  # <T>
    def send(self, httpRequest: 'HttpRequest', bodyHandler: typing.Union['HttpResponse.BodyHandler'[_send__T], typing.Callable[[], _send__T]]) -> 'HttpResponse'[_send__T]: ...
    _sendAsync_0__T = typing.TypeVar('_sendAsync_0__T')  # <T>
    @typing.overload
    def sendAsync(self, httpRequest: 'HttpRequest', bodyHandler: typing.Union['HttpResponse.BodyHandler'[_sendAsync_0__T], typing.Callable[[], _sendAsync_0__T]]) -> java.util.concurrent.CompletableFuture['HttpResponse'[_sendAsync_0__T]]: ...
    _sendAsync_1__T = typing.TypeVar('_sendAsync_1__T')  # <T>
    @typing.overload
    def sendAsync(self, httpRequest: 'HttpRequest', bodyHandler: typing.Union['HttpResponse.BodyHandler'[_sendAsync_1__T], typing.Callable[[], _sendAsync_1__T]], pushPromiseHandler: 'HttpResponse.PushPromiseHandler'[_sendAsync_1__T]) -> java.util.concurrent.CompletableFuture['HttpResponse'[_sendAsync_1__T]]: ...
    def sslContext(self) -> javax.net.ssl.SSLContext: ...
    def sslParameters(self) -> javax.net.ssl.SSLParameters: ...
    def version(self) -> 'HttpClient.Version': ...
    class Builder(java.lang.Object):
        """
        Java class 'java.net.http.HttpClient$Builder'
        
          Attributes:
            NO_PROXY (java.net.ProxySelector): final static field
        
        """
        NO_PROXY: typing.ClassVar[java.net.ProxySelector] = ...
        def authenticator(self, authenticator: java.net.Authenticator) -> 'HttpClient.Builder': ...
        def build(self) -> 'HttpClient': ...
        def connectTimeout(self, duration: java.time.Duration) -> 'HttpClient.Builder': ...
        def cookieHandler(self, cookieHandler: java.net.CookieHandler) -> 'HttpClient.Builder': ...
        def executor(self, executor: java.util.concurrent.Executor) -> 'HttpClient.Builder': ...
        def followRedirects(self, redirect: 'HttpClient.Redirect') -> 'HttpClient.Builder': ...
        def priority(self, int: int) -> 'HttpClient.Builder': ...
        def proxy(self, proxySelector: java.net.ProxySelector) -> 'HttpClient.Builder': ...
        def sslContext(self, sSLContext: javax.net.ssl.SSLContext) -> 'HttpClient.Builder': ...
        def sslParameters(self, sSLParameters: javax.net.ssl.SSLParameters) -> 'HttpClient.Builder': ...
        def version(self, version: 'HttpClient.Version') -> 'HttpClient.Builder': ...
    class Redirect(java.lang.Enum[java.net.http.HttpClient.Redirect]):
        """
        Java class 'java.net.http.HttpClient$Redirect'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            NEVER (java.net.http.HttpClient$Redirect): final static enum constant
            ALWAYS (java.net.http.HttpClient$Redirect): final static enum constant
            NORMAL (java.net.http.HttpClient$Redirect): final static enum constant
        
        """
        NEVER: typing.ClassVar['HttpClient.Redirect'] = ...
        ALWAYS: typing.ClassVar['HttpClient.Redirect'] = ...
        NORMAL: typing.ClassVar['HttpClient.Redirect'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @typing.overload
        def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
        @classmethod
        @typing.overload
        def valueOf(cls, string: java.lang.String) -> 'HttpClient.Redirect': ...
        @classmethod
        def values(cls) -> typing.List['HttpClient.Redirect']: ...
    class Version(java.lang.Enum[java.net.http.HttpClient.Version]):
        """
        Java class 'java.net.http.HttpClient$Version'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            HTTP_1_1 (java.net.http.HttpClient$Version): final static enum constant
            HTTP_2 (java.net.http.HttpClient$Version): final static enum constant
        
        """
        HTTP_1_1: typing.ClassVar['HttpClient.Version'] = ...
        HTTP_2: typing.ClassVar['HttpClient.Version'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @typing.overload
        def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
        @classmethod
        @typing.overload
        def valueOf(cls, string: java.lang.String) -> 'HttpClient.Version': ...
        @classmethod
        def values(cls) -> typing.List['HttpClient.Version']: ...

class HttpHeaders(java.lang.Object):
    """
    Java class 'java.net.http.HttpHeaders'
    
        Extends:
            java.lang.Object
    
    """
    def allValues(self, string: java.lang.String) -> java.util.List[java.lang.String]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def firstValue(self, string: java.lang.String) -> java.util.Optional[java.lang.String]: ...
    def firstValueAsLong(self, string: java.lang.String) -> java.util.OptionalLong: ...
    def hashCode(self) -> int: ...
    def map(self) -> java.util.Map[java.lang.String, java.util.List[java.lang.String]]: ...
    @classmethod
    def of(cls, map: typing.Union[java.util.Map[java.lang.String, java.util.List[java.lang.String]], typing.Mapping[java.lang.String, java.util.List[java.lang.String]]], biPredicate: typing.Union[java.util.function.BiPredicate[java.lang.String, java.lang.String], typing.Callable[[java.lang.String], java.lang.String]]) -> 'HttpHeaders': ...
    def toString(self) -> java.lang.String: ...

class HttpRequest(java.lang.Object):
    """
    Java class 'java.net.http.HttpRequest'
    
        Extends:
            java.lang.Object
    
    """
    def bodyPublisher(self) -> java.util.Optional['HttpRequest.BodyPublisher']: ...
    def equals(self, object: typing.Any) -> bool: ...
    def expectContinue(self) -> bool: ...
    def hashCode(self) -> int: ...
    def headers(self) -> HttpHeaders: ...
    def method(self) -> java.lang.String: ...
    @classmethod
    @typing.overload
    def newBuilder(cls) -> 'HttpRequest.Builder': ...
    @classmethod
    @typing.overload
    def newBuilder(cls, uRI: java.net.URI) -> 'HttpRequest.Builder': ...
    def timeout(self) -> java.util.Optional[java.time.Duration]: ...
    def uri(self) -> java.net.URI: ...
    def version(self) -> java.util.Optional[HttpClient.Version]: ...
    class BodyPublisher(java.util.concurrent.Flow.Publisher[java.nio.ByteBuffer]):
        """
        Java class 'java.net.http.HttpRequest$BodyPublisher'
        
            Interfaces:
                java.util.concurrent.Flow.Publisher
        
        """
        def contentLength(self) -> int: ...
    class BodyPublishers(java.lang.Object):
        """
        Java class 'java.net.http.HttpRequest$BodyPublishers'
        
            Extends:
                java.lang.Object
        
        """
        @classmethod
        @typing.overload
        def fromPublisher(cls, publisher: typing.Union[java.util.concurrent.Flow.Publisher[java.nio.ByteBuffer], typing.Callable[[], java.nio.ByteBuffer]]) -> 'HttpRequest.BodyPublisher': ...
        @classmethod
        @typing.overload
        def fromPublisher(cls, publisher: typing.Union[java.util.concurrent.Flow.Publisher[java.nio.ByteBuffer], typing.Callable[[], java.nio.ByteBuffer]], long: int) -> 'HttpRequest.BodyPublisher': ...
        @classmethod
        def noBody(cls) -> 'HttpRequest.BodyPublisher': ...
        @classmethod
        @typing.overload
        def ofByteArray(cls, byteArray: typing.List[int]) -> 'HttpRequest.BodyPublisher': ...
        @classmethod
        @typing.overload
        def ofByteArray(cls, byteArray: typing.List[int], int: int, int2: int) -> 'HttpRequest.BodyPublisher': ...
        @classmethod
        def ofByteArrays(cls, iterable: java.lang.Iterable[typing.List[int]]) -> 'HttpRequest.BodyPublisher': ...
        @classmethod
        def ofFile(cls, path: java.nio.file.Path) -> 'HttpRequest.BodyPublisher': ...
        @classmethod
        def ofInputStream(cls, supplier: typing.Union[java.util.function.Supplier[java.io.InputStream], typing.Callable[[], java.io.InputStream]]) -> 'HttpRequest.BodyPublisher': ...
        @classmethod
        @typing.overload
        def ofString(cls, string: java.lang.String) -> 'HttpRequest.BodyPublisher': ...
        @classmethod
        @typing.overload
        def ofString(cls, string: java.lang.String, charset: java.nio.charset.Charset) -> 'HttpRequest.BodyPublisher': ...
    class Builder(java.lang.Object):
        """
        Java class 'java.net.http.HttpRequest$Builder'
        
        """
        def DELETE(self) -> 'HttpRequest.Builder': ...
        def GET(self) -> 'HttpRequest.Builder': ...
        def POST(self, bodyPublisher: 'HttpRequest.BodyPublisher') -> 'HttpRequest.Builder': ...
        def PUT(self, bodyPublisher: 'HttpRequest.BodyPublisher') -> 'HttpRequest.Builder': ...
        def build(self) -> 'HttpRequest': ...
        def copy(self) -> 'HttpRequest.Builder': ...
        def expectContinue(self, boolean: bool) -> 'HttpRequest.Builder': ...
        def header(self, string: java.lang.String, string2: java.lang.String) -> 'HttpRequest.Builder': ...
        def headers(self, stringArray: typing.List[java.lang.String]) -> 'HttpRequest.Builder': ...
        def method(self, string: java.lang.String, bodyPublisher: 'HttpRequest.BodyPublisher') -> 'HttpRequest.Builder': ...
        def setHeader(self, string: java.lang.String, string2: java.lang.String) -> 'HttpRequest.Builder': ...
        def timeout(self, duration: java.time.Duration) -> 'HttpRequest.Builder': ...
        def uri(self, uRI: java.net.URI) -> 'HttpRequest.Builder': ...
        def version(self, version: HttpClient.Version) -> 'HttpRequest.Builder': ...

_HttpResponse__BodyHandler__T = typing.TypeVar('_HttpResponse__BodyHandler__T')  # <T>
_HttpResponse__BodySubscriber__T = typing.TypeVar('_HttpResponse__BodySubscriber__T')  # <T>
_HttpResponse__PushPromiseHandler__T = typing.TypeVar('_HttpResponse__PushPromiseHandler__T')  # <T>
_HttpResponse__T = typing.TypeVar('_HttpResponse__T')  # <T>
class HttpResponse(java.lang.Object, typing.Generic[_HttpResponse__T]):
    """
    public interface HttpResponse<T>
    
        An HTTP response.
    
        An :code:`HttpResponse` is not created directly, but rather returned as a result of sending an
        :class:`~java.net.http.HttpRequest`. An :code:`HttpResponse` is made available when the response status code and headers
        have been received, and typically after the response body has also been completely received. Whether or not the
        :code:`HttpResponse` is made available before the response body has been completely received depends on the
        :class:`~java.net.http.HttpResponse.BodyHandler` provided when sending the :code:`HttpRequest`.
    
        This class provides methods for accessing the response status code, headers, the response body, and the
        :code:`HttpRequest` corresponding to this response.
    
        The following is an example of retrieving a response as a String:
    
        .. code-block: java
        
           HttpResponse<String> response = client
             .send(request, BodyHandlers.ofString()); 
    
        The class :class:`~java.net.http.HttpResponse.BodyHandlers` provides implementations of many common response handlers.
        Alternatively, a custom :code:`BodyHandler` implementation can be used.
    
        Since:
            11
    
    
    """
    def body(self) -> _HttpResponse__T: ...
    def headers(self) -> HttpHeaders: ...
    def previousResponse(self) -> java.util.Optional['HttpResponse'[_HttpResponse__T]]: ...
    def request(self) -> HttpRequest: ...
    def sslSession(self) -> java.util.Optional[javax.net.ssl.SSLSession]: ...
    def statusCode(self) -> int: ...
    def uri(self) -> java.net.URI: ...
    def version(self) -> HttpClient.Version: ...
    class BodyHandler(java.lang.Object, typing.Generic[_HttpResponse__BodyHandler__T]):
        """
        Java class 'java.net.http.HttpResponse$BodyHandler'
        
        """
        def apply(self, responseInfo: 'HttpResponse.ResponseInfo') -> 'HttpResponse.BodySubscriber'[_HttpResponse__BodyHandler__T]: ...
    class BodyHandlers(java.lang.Object):
        """
        Java class 'java.net.http.HttpResponse$BodyHandlers'
        
            Extends:
                java.lang.Object
        
        """
        _buffering__T = typing.TypeVar('_buffering__T')  # <T>
        @classmethod
        def buffering(cls, bodyHandler: typing.Union['HttpResponse.BodyHandler'[_buffering__T], typing.Callable[[], _buffering__T]], int: int) -> 'HttpResponse.BodyHandler'[_buffering__T]: ...
        @classmethod
        def discarding(cls) -> 'HttpResponse.BodyHandler'[None]: ...
        @classmethod
        @typing.overload
        def fromLineSubscriber(cls, subscriber: java.util.concurrent.Flow.Subscriber[java.lang.String]) -> 'HttpResponse.BodyHandler'[None]: ...
        _fromLineSubscriber_1__S = typing.TypeVar('_fromLineSubscriber_1__S', bound=java.util.concurrent.Flow.Subscriber)  # <S>
        _fromLineSubscriber_1__T = typing.TypeVar('_fromLineSubscriber_1__T')  # <T>
        @classmethod
        @typing.overload
        def fromLineSubscriber(cls, s: _fromLineSubscriber_1__S, function: typing.Union[java.util.function.Function[_fromLineSubscriber_1__S, _fromLineSubscriber_1__T], typing.Callable[[_fromLineSubscriber_1__S], _fromLineSubscriber_1__T]], string: java.lang.String) -> 'HttpResponse.BodyHandler'[_fromLineSubscriber_1__T]: ...
        @classmethod
        @typing.overload
        def fromSubscriber(cls, subscriber: java.util.concurrent.Flow.Subscriber[java.util.List[java.nio.ByteBuffer]]) -> 'HttpResponse.BodyHandler'[None]: ...
        _fromSubscriber_1__S = typing.TypeVar('_fromSubscriber_1__S', bound=java.util.concurrent.Flow.Subscriber)  # <S>
        _fromSubscriber_1__T = typing.TypeVar('_fromSubscriber_1__T')  # <T>
        @classmethod
        @typing.overload
        def fromSubscriber(cls, s: _fromSubscriber_1__S, function: typing.Union[java.util.function.Function[_fromSubscriber_1__S, _fromSubscriber_1__T], typing.Callable[[_fromSubscriber_1__S], _fromSubscriber_1__T]]) -> 'HttpResponse.BodyHandler'[_fromSubscriber_1__T]: ...
        @classmethod
        def ofByteArray(cls) -> 'HttpResponse.BodyHandler'[typing.List[int]]: ...
        @classmethod
        def ofByteArrayConsumer(cls, consumer: typing.Union[java.util.function.Consumer[java.util.Optional[typing.List[int]]], typing.Callable[[], java.util.Optional[typing.List[int]]]]) -> 'HttpResponse.BodyHandler'[None]: ...
        @classmethod
        @typing.overload
        def ofFile(cls, path: java.nio.file.Path) -> 'HttpResponse.BodyHandler'[java.nio.file.Path]: ...
        @classmethod
        @typing.overload
        def ofFile(cls, path: java.nio.file.Path, openOptionArray: typing.List[java.nio.file.OpenOption]) -> 'HttpResponse.BodyHandler'[java.nio.file.Path]: ...
        @classmethod
        def ofFileDownload(cls, path: java.nio.file.Path, openOptionArray: typing.List[java.nio.file.OpenOption]) -> 'HttpResponse.BodyHandler'[java.nio.file.Path]: ...
        @classmethod
        def ofInputStream(cls) -> 'HttpResponse.BodyHandler'[java.io.InputStream]: ...
        @classmethod
        def ofLines(cls) -> 'HttpResponse.BodyHandler'[java.util.stream.Stream[java.lang.String]]: ...
        @classmethod
        def ofPublisher(cls) -> 'HttpResponse.BodyHandler'[java.util.concurrent.Flow.Publisher[java.util.List[java.nio.ByteBuffer]]]: ...
        @classmethod
        @typing.overload
        def ofString(cls) -> 'HttpResponse.BodyHandler'[java.lang.String]: ...
        @classmethod
        @typing.overload
        def ofString(cls, charset: java.nio.charset.Charset) -> 'HttpResponse.BodyHandler'[java.lang.String]: ...
        _replacing__U = typing.TypeVar('_replacing__U')  # <U>
        @classmethod
        def replacing(cls, u: _replacing__U) -> 'HttpResponse.BodyHandler'[_replacing__U]: ...
    class BodySubscriber(java.util.concurrent.Flow.Subscriber[java.util.List[java.nio.ByteBuffer]], typing.Generic[_HttpResponse__BodySubscriber__T]):
        """
        Java class 'java.net.http.HttpResponse$BodySubscriber'
        
            Interfaces:
                java.util.concurrent.Flow.Subscriber
        
        """
        def getBody(self) -> java.util.concurrent.CompletionStage[_HttpResponse__BodySubscriber__T]: ...
    class BodySubscribers(java.lang.Object):
        """
        Java class 'java.net.http.HttpResponse$BodySubscribers'
        
            Extends:
                java.lang.Object
        
        """
        _buffering__T = typing.TypeVar('_buffering__T')  # <T>
        @classmethod
        def buffering(cls, bodySubscriber: 'HttpResponse.BodySubscriber'[_buffering__T], int: int) -> 'HttpResponse.BodySubscriber'[_buffering__T]: ...
        @classmethod
        def discarding(cls) -> 'HttpResponse.BodySubscriber'[None]: ...
        @classmethod
        @typing.overload
        def fromLineSubscriber(cls, subscriber: java.util.concurrent.Flow.Subscriber[java.lang.String]) -> 'HttpResponse.BodySubscriber'[None]: ...
        _fromLineSubscriber_1__S = typing.TypeVar('_fromLineSubscriber_1__S', bound=java.util.concurrent.Flow.Subscriber)  # <S>
        _fromLineSubscriber_1__T = typing.TypeVar('_fromLineSubscriber_1__T')  # <T>
        @classmethod
        @typing.overload
        def fromLineSubscriber(cls, s: _fromLineSubscriber_1__S, function: typing.Union[java.util.function.Function[_fromLineSubscriber_1__S, _fromLineSubscriber_1__T], typing.Callable[[_fromLineSubscriber_1__S], _fromLineSubscriber_1__T]], charset: java.nio.charset.Charset, string: java.lang.String) -> 'HttpResponse.BodySubscriber'[_fromLineSubscriber_1__T]: ...
        @classmethod
        @typing.overload
        def fromSubscriber(cls, subscriber: java.util.concurrent.Flow.Subscriber[java.util.List[java.nio.ByteBuffer]]) -> 'HttpResponse.BodySubscriber'[None]: ...
        _fromSubscriber_1__S = typing.TypeVar('_fromSubscriber_1__S', bound=java.util.concurrent.Flow.Subscriber)  # <S>
        _fromSubscriber_1__T = typing.TypeVar('_fromSubscriber_1__T')  # <T>
        @classmethod
        @typing.overload
        def fromSubscriber(cls, s: _fromSubscriber_1__S, function: typing.Union[java.util.function.Function[_fromSubscriber_1__S, _fromSubscriber_1__T], typing.Callable[[_fromSubscriber_1__S], _fromSubscriber_1__T]]) -> 'HttpResponse.BodySubscriber'[_fromSubscriber_1__T]: ...
        _mapping__T = typing.TypeVar('_mapping__T')  # <T>
        _mapping__U = typing.TypeVar('_mapping__U')  # <U>
        @classmethod
        def mapping(cls, bodySubscriber: 'HttpResponse.BodySubscriber'[_mapping__T], function: typing.Union[java.util.function.Function[_mapping__T, _mapping__U], typing.Callable[[_mapping__T], _mapping__U]]) -> 'HttpResponse.BodySubscriber'[_mapping__U]: ...
        @classmethod
        def ofByteArray(cls) -> 'HttpResponse.BodySubscriber'[typing.List[int]]: ...
        @classmethod
        def ofByteArrayConsumer(cls, consumer: typing.Union[java.util.function.Consumer[java.util.Optional[typing.List[int]]], typing.Callable[[], java.util.Optional[typing.List[int]]]]) -> 'HttpResponse.BodySubscriber'[None]: ...
        @classmethod
        @typing.overload
        def ofFile(cls, path: java.nio.file.Path) -> 'HttpResponse.BodySubscriber'[java.nio.file.Path]: ...
        @classmethod
        @typing.overload
        def ofFile(cls, path: java.nio.file.Path, openOptionArray: typing.List[java.nio.file.OpenOption]) -> 'HttpResponse.BodySubscriber'[java.nio.file.Path]: ...
        @classmethod
        def ofInputStream(cls) -> 'HttpResponse.BodySubscriber'[java.io.InputStream]: ...
        @classmethod
        def ofLines(cls, charset: java.nio.charset.Charset) -> 'HttpResponse.BodySubscriber'[java.util.stream.Stream[java.lang.String]]: ...
        @classmethod
        def ofPublisher(cls) -> 'HttpResponse.BodySubscriber'[java.util.concurrent.Flow.Publisher[java.util.List[java.nio.ByteBuffer]]]: ...
        @classmethod
        def ofString(cls, charset: java.nio.charset.Charset) -> 'HttpResponse.BodySubscriber'[java.lang.String]: ...
        _replacing__U = typing.TypeVar('_replacing__U')  # <U>
        @classmethod
        def replacing(cls, u: _replacing__U) -> 'HttpResponse.BodySubscriber'[_replacing__U]: ...
    class PushPromiseHandler(java.lang.Object, typing.Generic[_HttpResponse__PushPromiseHandler__T]):
        """
        Java class 'java.net.http.HttpResponse$PushPromiseHandler'
        
        """
        def applyPushPromise(self, httpRequest: HttpRequest, httpRequest2: HttpRequest, function: typing.Union[java.util.function.Function[typing.Union['HttpResponse.BodyHandler'[_HttpResponse__PushPromiseHandler__T], typing.Callable[[], _HttpResponse__PushPromiseHandler__T]], java.util.concurrent.CompletableFuture['HttpResponse'[_HttpResponse__PushPromiseHandler__T]]], typing.Callable[[typing.Union['HttpResponse.BodyHandler'[_HttpResponse__PushPromiseHandler__T], typing.Callable[[], _HttpResponse__PushPromiseHandler__T]]], java.util.concurrent.CompletableFuture['HttpResponse'[_HttpResponse__PushPromiseHandler__T]]]]) -> None: ...
        _of__T = typing.TypeVar('_of__T')  # <T>
        @classmethod
        def of(cls, function: typing.Union[java.util.function.Function[HttpRequest, typing.Union['HttpResponse.BodyHandler'[_of__T], typing.Callable[[], _of__T]]], typing.Callable[[HttpRequest], typing.Union['HttpResponse.BodyHandler'[_of__T], typing.Callable[[], _of__T]]]], concurrentMap: java.util.concurrent.ConcurrentMap[HttpRequest, java.util.concurrent.CompletableFuture['HttpResponse'[_of__T]]]) -> 'HttpResponse.PushPromiseHandler'[_of__T]: ...
    class ResponseInfo(java.lang.Object):
        """
        Java class 'java.net.http.HttpResponse$ResponseInfo'
        
        """
        def headers(self) -> HttpHeaders: ...
        def statusCode(self) -> int: ...
        def version(self) -> HttpClient.Version: ...

class HttpTimeoutException(java.io.IOException):
    """
    Java class 'java.net.http.HttpTimeoutException'
    
        Extends:
            java.io.IOException
    
      Constructors:
        * HttpTimeoutException(java.lang.String)
    
    """
    def __init__(self, string: java.lang.String): ...

class WebSocket(java.lang.Object):
    """
    public interface WebSocket
    
        A WebSocket Client.
    
        :code:`WebSocket` instances are created through :class:`~java.net.http.WebSocket.Builder`.
    
        WebSocket has an input and an output side. These sides are independent from each other. A side can either be open or
        closed. Once closed, the side remains closed. WebSocket messages are sent through a :code:`WebSocket` and received
        through a :code:`WebSocket.Listener` associated with it. Messages can be sent until the WebSocket's output is closed,
        and received until the WebSocket's input is closed.
    
        A send method is any of the :code:`sendText`, :code:`sendBinary`, :code:`sendPing`, :code:`sendPong` and
        :code:`sendClose` methods of :code:`WebSocket`. A send method initiates a send operation and returns a
        :code:`CompletableFuture` which completes once the operation has completed. If the :code:`CompletableFuture` completes
        normally the operation is considered succeeded. If the :code:`CompletableFuture` completes exceptionally, the operation
        is considered failed. An operation that has been initiated but not yet completed is considered pending.
    
        A receive method is any of the :code:`onText`, :code:`onBinary`, :code:`onPing`, :code:`onPong` and :code:`onClose`
        methods of :code:`Listener`. WebSocket initiates a receive operation by invoking a receive method on the listener. The
        listener then must return a :code:`CompletionStage` which completes once the operation has completed.
    
        To control receiving of messages, a WebSocket maintains an :class:`~java.net.http`. This counter's value is a number of
        times the WebSocket has yet to invoke a receive method. While this counter is zero the WebSocket does not invoke receive
        methods. The counter is incremented by :code:`n` when :code:`request(n)` is called. The counter is decremented by one
        when the WebSocket invokes a receive method. :code:`onOpen` and :code:`onError` are not receive methods. WebSocket
        invokes :code:`onOpen` prior to any other methods on the listener. WebSocket invokes :code:`onOpen` at most once.
        WebSocket may invoke :code:`onError` at any given time. If the WebSocket invokes :code:`onError` or :code:`onClose`,
        then no further listener's methods will be invoked, no matter the value of the counter. For a newly built WebSocket the
        counter is zero.
    
        Unless otherwise stated, :code:`null` arguments will cause methods of :code:`WebSocket` to throw
        :code:`NullPointerException`, similarly, :code:`WebSocket` will not pass :code:`null` arguments to methods of
        :code:`Listener`. The state of a WebSocket is not changed by the invocations that throw or return a
        :code:`CompletableFuture` that completes with one of the :code:`NullPointerException`, :code:`IllegalArgumentException`,
        :code:`IllegalStateException` exceptions.
    
        :code:`WebSocket` handles received Ping and Close messages automatically (as per the WebSocket Protocol) by replying
        with Pong and Close messages. If the listener receives Ping or Close messages, no mandatory actions from the listener
        are required.
    
        API Note:
            The relationship between a WebSocket and the associated Listener is analogous to that of a Subscription and the
            associated Subscriber of type :class:`~java.util.concurrent.Flow`.
    
        Since:
            11
    
    
    """
    NORMAL_CLOSURE: typing.ClassVar[int] = ...
    def abort(self) -> None: ...
    def getSubprotocol(self) -> java.lang.String: ...
    def isInputClosed(self) -> bool: ...
    def isOutputClosed(self) -> bool: ...
    def request(self, long: int) -> None: ...
    def sendBinary(self, byteBuffer: java.nio.ByteBuffer, boolean: bool) -> java.util.concurrent.CompletableFuture['WebSocket']: ...
    def sendClose(self, int: int, string: java.lang.String) -> java.util.concurrent.CompletableFuture['WebSocket']: ...
    def sendPing(self, byteBuffer: java.nio.ByteBuffer) -> java.util.concurrent.CompletableFuture['WebSocket']: ...
    def sendPong(self, byteBuffer: java.nio.ByteBuffer) -> java.util.concurrent.CompletableFuture['WebSocket']: ...
    def sendText(self, charSequence: java.lang.CharSequence, boolean: bool) -> java.util.concurrent.CompletableFuture['WebSocket']: ...
    class Builder(java.lang.Object):
        """
        Java class 'java.net.http.WebSocket$Builder'
        
        """
        def buildAsync(self, uRI: java.net.URI, listener: 'WebSocket.Listener') -> java.util.concurrent.CompletableFuture['WebSocket']: ...
        def connectTimeout(self, duration: java.time.Duration) -> 'WebSocket.Builder': ...
        def header(self, string: java.lang.String, string2: java.lang.String) -> 'WebSocket.Builder': ...
        def subprotocols(self, string: java.lang.String, stringArray: typing.List[java.lang.String]) -> 'WebSocket.Builder': ...
    class Listener(java.lang.Object):
        """
        Java class 'java.net.http.WebSocket$Listener'
        
        """
        def onBinary(self, webSocket: 'WebSocket', byteBuffer: java.nio.ByteBuffer, boolean: bool) -> java.util.concurrent.CompletionStage[typing.Any]: ...
        def onClose(self, webSocket: 'WebSocket', int: int, string: java.lang.String) -> java.util.concurrent.CompletionStage[typing.Any]: ...
        def onError(self, webSocket: 'WebSocket', throwable: java.lang.Throwable) -> None: ...
        def onOpen(self, webSocket: 'WebSocket') -> None: ...
        def onPing(self, webSocket: 'WebSocket', byteBuffer: java.nio.ByteBuffer) -> java.util.concurrent.CompletionStage[typing.Any]: ...
        def onPong(self, webSocket: 'WebSocket', byteBuffer: java.nio.ByteBuffer) -> java.util.concurrent.CompletionStage[typing.Any]: ...
        def onText(self, webSocket: 'WebSocket', charSequence: java.lang.CharSequence, boolean: bool) -> java.util.concurrent.CompletionStage[typing.Any]: ...

class WebSocketHandshakeException(java.io.IOException):
    """
    Java class 'java.net.http.WebSocketHandshakeException'
    
        Extends:
            java.io.IOException
    
      Constructors:
        * WebSocketHandshakeException(java.net.http.HttpResponse)
    
    """
    def __init__(self, httpResponse: HttpResponse[typing.Any]): ...
    def getResponse(self) -> HttpResponse[typing.Any]: ...
    @typing.overload
    def initCause(self, throwable: java.lang.Throwable) -> java.lang.Throwable: ...
    @typing.overload
    def initCause(self, throwable: java.lang.Throwable) -> 'WebSocketHandshakeException': ...

class HttpConnectTimeoutException(HttpTimeoutException):
    """
    Java class 'java.net.http.HttpConnectTimeoutException'
    
        Extends:
            java.net.http.HttpTimeoutException
    
      Constructors:
        * HttpConnectTimeoutException(java.lang.String)
    
    """
    def __init__(self, string: java.lang.String): ...
