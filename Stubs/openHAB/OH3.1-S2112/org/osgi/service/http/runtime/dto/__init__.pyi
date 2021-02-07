import java.lang
import java.util
import org.osgi.dto
import org.osgi.framework.dto
import typing


class BaseServletDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.service.http.runtime.dto.BaseServletDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * BaseServletDTO()
    
      Attributes:
        name (java.lang.String): field
        servletInfo (java.lang.String): field
        asyncSupported (boolean): field
        initParams (java.util.Map): field
        servletContextId (long): field
        serviceId (long): field
    
    """
    name: java.lang.String = ...
    servletInfo: java.lang.String = ...
    asyncSupported: bool = ...
    initParams: java.util.Map = ...
    servletContextId: int = ...
    serviceId: int = ...
    def __init__(self): ...

class DTOConstants(java.lang.Object):
    """
    Java class 'org.osgi.service.http.runtime.dto.DTOConstants'
    
        Extends:
            java.lang.Object
    
      Attributes:
        FAILURE_REASON_UNKNOWN (int): final static field
        FAILURE_REASON_NO_SERVLET_CONTEXT_MATCHING (int): final static field
        FAILURE_REASON_SERVLET_CONTEXT_FAILURE (int): final static field
        FAILURE_REASON_SHADOWED_BY_OTHER_SERVICE (int): final static field
        FAILURE_REASON_EXCEPTION_ON_INIT (int): final static field
        FAILURE_REASON_SERVICE_NOT_GETTABLE (int): final static field
        FAILURE_REASON_VALIDATION_FAILED (int): final static field
        FAILURE_REASON_SERVICE_IN_USE (int): final static field
    
    """
    FAILURE_REASON_UNKNOWN: typing.ClassVar[int] = ...
    FAILURE_REASON_NO_SERVLET_CONTEXT_MATCHING: typing.ClassVar[int] = ...
    FAILURE_REASON_SERVLET_CONTEXT_FAILURE: typing.ClassVar[int] = ...
    FAILURE_REASON_SHADOWED_BY_OTHER_SERVICE: typing.ClassVar[int] = ...
    FAILURE_REASON_EXCEPTION_ON_INIT: typing.ClassVar[int] = ...
    FAILURE_REASON_SERVICE_NOT_GETTABLE: typing.ClassVar[int] = ...
    FAILURE_REASON_VALIDATION_FAILED: typing.ClassVar[int] = ...
    FAILURE_REASON_SERVICE_IN_USE: typing.ClassVar[int] = ...

class FilterDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.service.http.runtime.dto.FilterDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * FilterDTO()
    
      Attributes:
        name (java.lang.String): field
        patterns ([Ljava.lang.String;): field
        servletNames ([Ljava.lang.String;): field
        regexs ([Ljava.lang.String;): field
        asyncSupported (boolean): field
        dispatcher ([Ljava.lang.String;): field
        initParams (java.util.Map): field
        serviceId (long): field
        servletContextId (long): field
    
    """
    name: java.lang.String = ...
    patterns: typing.List[java.lang.String] = ...
    servletNames: typing.List[java.lang.String] = ...
    regexs: typing.List[java.lang.String] = ...
    asyncSupported: bool = ...
    dispatcher: typing.List[java.lang.String] = ...
    initParams: java.util.Map = ...
    serviceId: int = ...
    servletContextId: int = ...
    def __init__(self): ...

class ListenerDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.service.http.runtime.dto.ListenerDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * ListenerDTO()
    
      Attributes:
        types ([Ljava.lang.String;): field
        serviceId (long): field
        servletContextId (long): field
    
    """
    types: typing.List[java.lang.String] = ...
    serviceId: int = ...
    servletContextId: int = ...
    def __init__(self): ...

class RequestInfoDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.service.http.runtime.dto.RequestInfoDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * RequestInfoDTO()
    
      Attributes:
        path (java.lang.String): field
        servletContextId (long): field
        filterDTOs ([Lorg.osgi.service.http.runtime.dto.FilterDTO;): field
        servletDTO (org.osgi.service.http.runtime.dto.ServletDTO): field
        resourceDTO (org.osgi.service.http.runtime.dto.ResourceDTO): field
    
    """
    path: java.lang.String = ...
    servletContextId: int = ...
    filterDTOs: typing.List[FilterDTO] = ...
    servletDTO: 'ServletDTO' = ...
    resourceDTO: 'ResourceDTO' = ...
    def __init__(self): ...

class ResourceDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.service.http.runtime.dto.ResourceDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * ResourceDTO()
    
      Attributes:
        patterns ([Ljava.lang.String;): field
        prefix (java.lang.String): field
        serviceId (long): field
        servletContextId (long): field
    
    """
    patterns: typing.List[java.lang.String] = ...
    prefix: java.lang.String = ...
    serviceId: int = ...
    servletContextId: int = ...
    def __init__(self): ...

class RuntimeDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.service.http.runtime.dto.RuntimeDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * RuntimeDTO()
    
      Attributes:
        serviceDTO (org.osgi.framework.dto.ServiceReferenceDTO): field
        servletContextDTOs ([Lorg.osgi.service.http.runtime.dto.ServletContextDTO;): field
        failedServletContextDTOs ([Lorg.osgi.service.http.runtime.dto.FailedServletContextDTO;): field
        failedServletDTOs ([Lorg.osgi.service.http.runtime.dto.FailedServletDTO;): field
        failedResourceDTOs ([Lorg.osgi.service.http.runtime.dto.FailedResourceDTO;): field
        failedFilterDTOs ([Lorg.osgi.service.http.runtime.dto.FailedFilterDTO;): field
        failedErrorPageDTOs ([Lorg.osgi.service.http.runtime.dto.FailedErrorPageDTO;): field
        failedListenerDTOs ([Lorg.osgi.service.http.runtime.dto.FailedListenerDTO;): field
    
    """
    serviceDTO: org.osgi.framework.dto.ServiceReferenceDTO = ...
    servletContextDTOs: typing.List['ServletContextDTO'] = ...
    failedServletContextDTOs: typing.List['FailedServletContextDTO'] = ...
    failedServletDTOs: typing.List['FailedServletDTO'] = ...
    failedResourceDTOs: typing.List['FailedResourceDTO'] = ...
    failedFilterDTOs: typing.List['FailedFilterDTO'] = ...
    failedErrorPageDTOs: typing.List['FailedErrorPageDTO'] = ...
    failedListenerDTOs: typing.List['FailedListenerDTO'] = ...
    def __init__(self): ...

class ServletContextDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.service.http.runtime.dto.ServletContextDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * ServletContextDTO()
    
      Attributes:
        name (java.lang.String): field
        contextPath (java.lang.String): field
        initParams (java.util.Map): field
        attributes (java.util.Map): field
        serviceId (long): field
        servletDTOs ([Lorg.osgi.service.http.runtime.dto.ServletDTO;): field
        resourceDTOs ([Lorg.osgi.service.http.runtime.dto.ResourceDTO;): field
        filterDTOs ([Lorg.osgi.service.http.runtime.dto.FilterDTO;): field
        errorPageDTOs ([Lorg.osgi.service.http.runtime.dto.ErrorPageDTO;): field
        listenerDTOs ([Lorg.osgi.service.http.runtime.dto.ListenerDTO;): field
    
    """
    name: java.lang.String = ...
    contextPath: java.lang.String = ...
    initParams: java.util.Map = ...
    attributes: java.util.Map = ...
    serviceId: int = ...
    servletDTOs: typing.List['ServletDTO'] = ...
    resourceDTOs: typing.List[ResourceDTO] = ...
    filterDTOs: typing.List[FilterDTO] = ...
    errorPageDTOs: typing.List['ErrorPageDTO'] = ...
    listenerDTOs: typing.List[ListenerDTO] = ...
    def __init__(self): ...

class ErrorPageDTO(BaseServletDTO):
    """
    Java class 'org.osgi.service.http.runtime.dto.ErrorPageDTO'
    
        Extends:
            org.osgi.service.http.runtime.dto.BaseServletDTO
    
      Constructors:
        * ErrorPageDTO()
    
      Attributes:
        exceptions ([Ljava.lang.String;): field
        errorCodes ([J): field
    
    """
    exceptions: typing.List[java.lang.String] = ...
    errorCodes: typing.List[int] = ...
    def __init__(self): ...

class FailedFilterDTO(FilterDTO):
    """
    Java class 'org.osgi.service.http.runtime.dto.FailedFilterDTO'
    
        Extends:
            org.osgi.service.http.runtime.dto.FilterDTO
    
      Constructors:
        * FailedFilterDTO()
    
      Attributes:
        failureReason (int): field
    
    """
    failureReason: int = ...
    def __init__(self): ...

class FailedListenerDTO(ListenerDTO):
    """
    Java class 'org.osgi.service.http.runtime.dto.FailedListenerDTO'
    
        Extends:
            org.osgi.service.http.runtime.dto.ListenerDTO
    
      Constructors:
        * FailedListenerDTO()
    
      Attributes:
        failureReason (int): field
    
    """
    failureReason: int = ...
    def __init__(self): ...

class FailedResourceDTO(ResourceDTO):
    """
    Java class 'org.osgi.service.http.runtime.dto.FailedResourceDTO'
    
        Extends:
            org.osgi.service.http.runtime.dto.ResourceDTO
    
      Constructors:
        * FailedResourceDTO()
    
      Attributes:
        failureReason (int): field
    
    """
    failureReason: int = ...
    def __init__(self): ...

class FailedServletContextDTO(ServletContextDTO):
    """
    Java class 'org.osgi.service.http.runtime.dto.FailedServletContextDTO'
    
        Extends:
            org.osgi.service.http.runtime.dto.ServletContextDTO
    
      Constructors:
        * FailedServletContextDTO()
    
      Attributes:
        failureReason (int): field
    
    """
    failureReason: int = ...
    def __init__(self): ...

class ServletDTO(BaseServletDTO):
    """
    Java class 'org.osgi.service.http.runtime.dto.ServletDTO'
    
        Extends:
            org.osgi.service.http.runtime.dto.BaseServletDTO
    
      Constructors:
        * ServletDTO()
    
      Attributes:
        patterns ([Ljava.lang.String;): field
    
    """
    patterns: typing.List[java.lang.String] = ...
    def __init__(self): ...

class FailedErrorPageDTO(ErrorPageDTO):
    """
    Java class 'org.osgi.service.http.runtime.dto.FailedErrorPageDTO'
    
        Extends:
            org.osgi.service.http.runtime.dto.ErrorPageDTO
    
      Constructors:
        * FailedErrorPageDTO()
    
      Attributes:
        failureReason (int): field
    
    """
    failureReason: int = ...
    def __init__(self): ...

class FailedServletDTO(ServletDTO):
    """
    Java class 'org.osgi.service.http.runtime.dto.FailedServletDTO'
    
        Extends:
            org.osgi.service.http.runtime.dto.ServletDTO
    
      Constructors:
        * FailedServletDTO()
    
      Attributes:
        failureReason (int): field
    
    """
    failureReason: int = ...
    def __init__(self): ...
