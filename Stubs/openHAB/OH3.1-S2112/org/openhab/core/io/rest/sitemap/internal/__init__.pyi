import java.lang
import java.math
import java.net
import java.util
import javax.servlet.http
import javax.ws.rs.core
import javax.ws.rs.sse
import org
import org.eclipse.emf.common.util
import org.openhab.core.io.rest
import org.openhab.core.io.rest.core.item
import org.openhab.core.io.rest.sitemap
import org.openhab.core.items
import org.openhab.core.model.sitemap
import org.openhab.core.model.sitemap.sitemap
import org.openhab.core.types
import org.openhab.core.ui.items
import org.osgi.dto
import typing


class JerseyResponseBuilderUtils(org.osgi.dto.DTO):
    """
    Java class 'org.openhab.core.io.rest.sitemap.internal.JerseyResponseBuilderUtils'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * JerseyResponseBuilderUtils()
    
    """
    def __init__(self): ...
    @classmethod
    def created(cls, location: java.lang.String) -> org.osgi.dto.DTO: ...
    class JerseyResponseBuilderDTO(org.osgi.dto.DTO):
        """
        Java class 'org.openhab.core.io.rest.sitemap.internal.JerseyResponseBuilderUtils$JerseyResponseBuilderDTO'
        
            Extends:
                org.osgi.dto.DTO
        
          Constructors:
            * JerseyResponseBuilderDTO()
        
          Attributes:
            status (java.lang.String): field
            context (org.openhab.core.io.rest.sitemap.internal.JerseyResponseBuilderUtils$JerseyResponseBuilderDTO$ContextDTO): field
        
        """
        status: java.lang.String = ...
        context: 'JerseyResponseBuilderUtils.JerseyResponseBuilderDTO.ContextDTO' = ...
        def __init__(self): ...
        class ContextDTO(org.osgi.dto.DTO):
            """
            Java class 'org.openhab.core.io.rest.sitemap.internal.JerseyResponseBuilderUtils$JerseyResponseBuilderDTO$ContextDTO'
            
                Extends:
                    org.osgi.dto.DTO
            
              Constructors:
                * ContextDTO()
            
              Attributes:
                headers (java.util.Map): field
                committingOutputStream (org.openhab.core.io.rest.sitemap.internal.JerseyResponseBuilderUtils$JerseyResponseBuilderDTO$ContextDTO$StreamInfoDTO): field
                entityAnnotations (java.util.List): field
                entityStream (org.openhab.core.io.rest.sitemap.internal.JerseyResponseBuilderUtils$JerseyResponseBuilderDTO$ContextDTO$StreamInfoDTO): field
            
            """
            headers: java.util.Map = ...
            committingOutputStream: 'JerseyResponseBuilderUtils.JerseyResponseBuilderDTO.ContextDTO.StreamInfoDTO' = ...
            entityAnnotations: java.util.List = ...
            entityStream: 'JerseyResponseBuilderUtils.JerseyResponseBuilderDTO.ContextDTO.StreamInfoDTO' = ...
            def __init__(self): ...
            class StreamInfoDTO(org.osgi.dto.DTO):
                """
                Java class 'org.openhab.core.io.rest.sitemap.internal.JerseyResponseBuilderUtils$JerseyResponseBuilderDTO$ContextDTO$StreamInfoDTO'
                
                    Extends:
                        org.osgi.dto.DTO
                
                  Constructors:
                    * StreamInfoDTO()
                
                """
                def __init__(self): ...

class MappingDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.sitemap.internal.MappingDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MappingDTO()
    
      Attributes:
        command (java.lang.String): field
        label (java.lang.String): field
    
    """
    command: java.lang.String = ...
    label: java.lang.String = ...
    def __init__(self): ...

class PageChangeListener(org.openhab.core.items.StateChangeListener):
    """
    Java class 'org.openhab.core.io.rest.sitemap.internal.PageChangeListener'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.items.StateChangeListener
    
      Constructors:
        * PageChangeListener(java.lang.String, java.lang.String, org.openhab.core.ui.items.ItemUIRegistry, org.eclipse.emf.common.util.EList)
    
    """
    def __init__(self, sitemapName: java.lang.String, pageId: java.lang.String, itemUIRegistry: org.openhab.core.ui.items.ItemUIRegistry, widgets: org.eclipse.emf.common.util.EList[org.openhab.core.model.sitemap.sitemap.Widget]): ...
    def addCallback(self, callback: org.openhab.core.io.rest.sitemap.SitemapSubscriptionService.SitemapSubscriptionCallback) -> None: ...
    def changeStateTo(self, item: org.openhab.core.items.Item, state: org.openhab.core.types.State) -> None: ...
    def dispose(self) -> None: ...
    def getPageId(self) -> java.lang.String: ...
    def getSitemapName(self) -> java.lang.String: ...
    def keepCurrentState(self, item: org.openhab.core.items.Item) -> None: ...
    def removeCallback(self, callback: org.openhab.core.io.rest.sitemap.SitemapSubscriptionService.SitemapSubscriptionCallback) -> None: ...
    def sendAliveEvent(self) -> None: ...
    def sitemapContentChanged(self, widgets: org.eclipse.emf.common.util.EList[org.openhab.core.model.sitemap.sitemap.Widget]) -> None: ...
    def stateChanged(self, item: org.openhab.core.items.Item, oldState: org.openhab.core.types.State, newState: org.openhab.core.types.State) -> None: ...
    def stateUpdated(self, item: org.openhab.core.items.Item, state: org.openhab.core.types.State) -> None: ...

class PageDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.sitemap.internal.PageDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PageDTO()
    
      Attributes:
        id (java.lang.String): field
        title (java.lang.String): field
        icon (java.lang.String): field
        link (java.lang.String): field
        parent (org.openhab.core.io.rest.sitemap.internal.PageDTO): field
        leaf (boolean): field
        timeout (boolean): field
        widgets (java.util.List): field
    
    """
    id: java.lang.String = ...
    title: java.lang.String = ...
    icon: java.lang.String = ...
    link: java.lang.String = ...
    parent: 'PageDTO' = ...
    leaf: bool = ...
    timeout: bool = ...
    widgets: java.util.List = ...
    def __init__(self): ...

class SitemapDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.sitemap.internal.SitemapDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SitemapDTO()
    
      Attributes:
        name (java.lang.String): field
        icon (java.lang.String): field
        label (java.lang.String): field
        link (java.lang.String): field
        homepage (org.openhab.core.io.rest.sitemap.internal.PageDTO): field
    
    """
    name: java.lang.String = ...
    icon: java.lang.String = ...
    label: java.lang.String = ...
    link: java.lang.String = ...
    homepage: PageDTO = ...
    def __init__(self): ...

class SitemapEvent(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.sitemap.internal.SitemapEvent'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SitemapEvent()
    
      Attributes:
        sitemapName (java.lang.String): field
        pageId (java.lang.String): field
    
    """
    sitemapName: java.lang.String = ...
    pageId: java.lang.String = ...
    def __init__(self): ...

class SitemapResource(org.openhab.core.io.rest.RESTResource, org.openhab.core.io.rest.sitemap.SitemapSubscriptionService.SitemapSubscriptionCallback, org.openhab.core.io.rest.SseBroadcaster.Listener[org.openhab.core.io.rest.sitemap.internal.SseSinkInfo]):
    """
    Java class 'org.openhab.core.io.rest.sitemap.internal.SitemapResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource, org.openhab.core.io.res
            t.sitemap.SitemapSubscriptionService.SitemapSubscriptionCallba
            ck, org.openhab.core.io.rest.SseBroadcaster.Listener
    
      Constructors:
        * SitemapResource(org.openhab.core.ui.items.ItemUIRegistry, org.openhab.core.io.rest.LocaleService, org.openhab.core.io.rest.sitemap.SitemapSubscriptionService)
    
      Attributes:
        PATH_SITEMAPS (java.lang.String): final static field
    
    """
    PATH_SITEMAPS: typing.ClassVar[java.lang.String] = ...
    def __init__(self, itemUIRegistry: org.openhab.core.ui.items.ItemUIRegistry, localeService: org.openhab.core.io.rest.LocaleService, subscriptions: org.openhab.core.io.rest.sitemap.SitemapSubscriptionService): ...
    def addSitemapProvider(self, provider: org.openhab.core.model.sitemap.SitemapProvider) -> None: ...
    def createEventSubscription(self) -> typing.Any: ...
    def getPageData(self, headers: javax.ws.rs.core.HttpHeaders, language: java.lang.String, sitemapname: java.lang.String, pageId: java.lang.String, subscriptionId: java.lang.String, includeHiddenWidgets: bool) -> javax.ws.rs.core.Response: ...
    def getSitemapBeans(self, uri: java.net.URI) -> java.util.Collection[SitemapDTO]: ...
    def getSitemapData(self, headers: javax.ws.rs.core.HttpHeaders, language: java.lang.String, sitemapname: java.lang.String, type: java.lang.String, callback: java.lang.String, includeHiddenWidgets: bool) -> javax.ws.rs.core.Response: ...
    def getSitemapEvents(self, sseEventSink: javax.ws.rs.sse.SseEventSink, response: javax.servlet.http.HttpServletResponse, subscriptionId: java.lang.String, sitemapname: java.lang.String, pageId: java.lang.String) -> None: ...
    def getSitemaps(self) -> javax.ws.rs.core.Response: ...
    def onEvent(self, event: SitemapEvent) -> None: ...
    def onRelease(self, subscriptionId: java.lang.String) -> None: ...
    def removeSitemapProvider(self, provider: org.openhab.core.model.sitemap.SitemapProvider) -> None: ...
    @typing.overload
    def sseEventSinkRemoved(self, sseEventSink: javax.ws.rs.sse.SseEventSink, object: typing.Any) -> None: ...
    @typing.overload
    def sseEventSinkRemoved(self, sink: javax.ws.rs.sse.SseEventSink, info: 'SseSinkInfo') -> None: ...

class SseSinkInfo(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.sitemap.internal.SseSinkInfo'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SseSinkInfo(java.lang.String, org.openhab.core.io.rest.sitemap.SitemapSubscriptionService)
    
      Attributes:
        subscriptionId (java.lang.String): final field
        subscriptions (org.openhab.core.io.rest.sitemap.SitemapSubscriptionService): final field
    
    """
    subscriptionId: java.lang.String = ...
    subscriptions: org.openhab.core.io.rest.sitemap.SitemapSubscriptionService = ...
    def __init__(self, subscriptionId: java.lang.String, subscriptions: org.openhab.core.io.rest.sitemap.SitemapSubscriptionService): ...

class WidgetDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.sitemap.internal.WidgetDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * WidgetDTO()
    
      Attributes:
        widgetId (java.lang.String): field
        type (java.lang.String): field
        name (java.lang.String): field
        visibility (boolean): field
        label (java.lang.String): field
        icon (java.lang.String): field
        labelcolor (java.lang.String): field
        valuecolor (java.lang.String): field
        mappings (java.util.List): final field
        switchSupport (java.lang.Boolean): field
        sendFrequency (java.lang.Integer): field
        separator (java.lang.String): field
        refresh (java.lang.Integer): field
        height (java.lang.Integer): field
        minValue (java.math.BigDecimal): field
        maxValue (java.math.BigDecimal): field
        step (java.math.BigDecimal): field
        url (java.lang.String): field
        encoding (java.lang.String): field
        service (java.lang.String): field
        period (java.lang.String): field
        legend (java.lang.Boolean): field
        state (java.lang.String): field
        item (org.openhab.core.io.rest.core.item.EnrichedItemDTO): field
        linkedPage (org.openhab.core.io.rest.sitemap.internal.PageDTO): field
        widgets (java.util.List): final field
    
    """
    widgetId: java.lang.String = ...
    type: java.lang.String = ...
    name: java.lang.String = ...
    visibility: bool = ...
    label: java.lang.String = ...
    icon: java.lang.String = ...
    labelcolor: java.lang.String = ...
    valuecolor: java.lang.String = ...
    mappings: java.util.List = ...
    switchSupport: bool = ...
    sendFrequency: int = ...
    separator: java.lang.String = ...
    refresh: int = ...
    height: int = ...
    minValue: java.math.BigDecimal = ...
    maxValue: java.math.BigDecimal = ...
    step: java.math.BigDecimal = ...
    url: java.lang.String = ...
    encoding: java.lang.String = ...
    service: java.lang.String = ...
    period: java.lang.String = ...
    legend: bool = ...
    state: java.lang.String = ...
    item: org.openhab.core.io.rest.core.item.EnrichedItemDTO = ...
    linkedPage: PageDTO = ...
    widgets: java.util.List = ...
    def __init__(self): ...

class ServerAliveEvent(SitemapEvent):
    """
    Java class 'org.openhab.core.io.rest.sitemap.internal.ServerAliveEvent'
    
        Extends:
            org.openhab.core.io.rest.sitemap.internal.SitemapEvent
    
      Constructors:
        * ServerAliveEvent()
    
      Attributes:
        TYPE (java.lang.String): final field
    
    """
    TYPE: java.lang.String = ...
    def __init__(self): ...

class SitemapChangedEvent(SitemapEvent):
    """
    Java class 'org.openhab.core.io.rest.sitemap.internal.SitemapChangedEvent'
    
        Extends:
            org.openhab.core.io.rest.sitemap.internal.SitemapEvent
    
      Constructors:
        * SitemapChangedEvent()
    
      Attributes:
        TYPE (java.lang.String): final field
    
    """
    TYPE: java.lang.String = ...
    def __init__(self): ...

class SitemapWidgetEvent(SitemapEvent):
    """
    Java class 'org.openhab.core.io.rest.sitemap.internal.SitemapWidgetEvent'
    
        Extends:
            org.openhab.core.io.rest.sitemap.internal.SitemapEvent
    
      Constructors:
        * SitemapWidgetEvent()
    
      Attributes:
        widgetId (java.lang.String): field
        label (java.lang.String): field
        icon (java.lang.String): field
        labelcolor (java.lang.String): field
        valuecolor (java.lang.String): field
        visibility (boolean): field
        state (java.lang.String): field
        item (org.openhab.core.io.rest.core.item.EnrichedItemDTO): field
    
    """
    widgetId: java.lang.String = ...
    label: java.lang.String = ...
    icon: java.lang.String = ...
    labelcolor: java.lang.String = ...
    valuecolor: java.lang.String = ...
    visibility: bool = ...
    state: java.lang.String = ...
    item: org.openhab.core.io.rest.core.item.EnrichedItemDTO = ...
    def __init__(self): ...
