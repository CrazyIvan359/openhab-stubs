import java.lang
import org.osgi.dto
import org.osgi.framework.dto
import typing


class BaseDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.service.jaxrs.runtime.dto.BaseDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * BaseDTO()
    
      Attributes:
        name (java.lang.String): field
        serviceId (long): field
    
    """
    name: java.lang.String = ...
    serviceId: int = ...
    def __init__(self): ...

class DTOConstants(java.lang.Object):
    """
    Java class 'org.osgi.service.jaxrs.runtime.dto.DTOConstants'
    
        Extends:
            java.lang.Object
    
      Attributes:
        FAILURE_REASON_UNKNOWN (int): final static field
        FAILURE_REASON_SHADOWED_BY_OTHER_SERVICE (int): final static field
        FAILURE_REASON_SERVICE_NOT_GETTABLE (int): final static field
        FAILURE_REASON_VALIDATION_FAILED (int): final static field
        FAILURE_REASON_NOT_AN_EXTENSION_TYPE (int): final static field
        FAILURE_REASON_REQUIRED_EXTENSIONS_UNAVAILABLE (int): final static field
        FAILURE_REASON_DUPLICATE_NAME (int): final static field
        FAILURE_REASON_REQUIRED_APPLICATION_UNAVAILABLE (int): final static field
    
    """
    FAILURE_REASON_UNKNOWN: typing.ClassVar[int] = ...
    FAILURE_REASON_SHADOWED_BY_OTHER_SERVICE: typing.ClassVar[int] = ...
    FAILURE_REASON_SERVICE_NOT_GETTABLE: typing.ClassVar[int] = ...
    FAILURE_REASON_VALIDATION_FAILED: typing.ClassVar[int] = ...
    FAILURE_REASON_NOT_AN_EXTENSION_TYPE: typing.ClassVar[int] = ...
    FAILURE_REASON_REQUIRED_EXTENSIONS_UNAVAILABLE: typing.ClassVar[int] = ...
    FAILURE_REASON_DUPLICATE_NAME: typing.ClassVar[int] = ...
    FAILURE_REASON_REQUIRED_APPLICATION_UNAVAILABLE: typing.ClassVar[int] = ...

class ResourceMethodInfoDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.service.jaxrs.runtime.dto.ResourceMethodInfoDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * ResourceMethodInfoDTO()
    
      Attributes:
        method (java.lang.String): field
        consumingMimeType ([Ljava.lang.String;): field
        producingMimeType ([Ljava.lang.String;): field
        nameBindings ([Ljava.lang.String;): field
        path (java.lang.String): field
    
    """
    method: java.lang.String = ...
    consumingMimeType: typing.List[java.lang.String] = ...
    producingMimeType: typing.List[java.lang.String] = ...
    nameBindings: typing.List[java.lang.String] = ...
    path: java.lang.String = ...
    def __init__(self): ...

class RuntimeDTO(org.osgi.dto.DTO):
    """
    Java class 'org.osgi.service.jaxrs.runtime.dto.RuntimeDTO'
    
        Extends:
            org.osgi.dto.DTO
    
      Constructors:
        * RuntimeDTO()
    
      Attributes:
        serviceDTO (org.osgi.framework.dto.ServiceReferenceDTO): field
        defaultApplication (org.osgi.service.jaxrs.runtime.dto.ApplicationDTO): field
        applicationDTOs ([Lorg.osgi.service.jaxrs.runtime.dto.ApplicationDTO;): field
        failedResourceDTOs ([Lorg.osgi.service.jaxrs.runtime.dto.FailedResourceDTO;): field
        failedExtensionDTOs ([Lorg.osgi.service.jaxrs.runtime.dto.FailedExtensionDTO;): field
        failedApplicationDTOs ([Lorg.osgi.service.jaxrs.runtime.dto.FailedApplicationDTO;): field
    
    """
    serviceDTO: org.osgi.framework.dto.ServiceReferenceDTO = ...
    defaultApplication: 'ApplicationDTO' = ...
    applicationDTOs: typing.List['ApplicationDTO'] = ...
    failedResourceDTOs: typing.List['FailedResourceDTO'] = ...
    failedExtensionDTOs: typing.List['FailedExtensionDTO'] = ...
    failedApplicationDTOs: typing.List['FailedApplicationDTO'] = ...
    def __init__(self): ...

class BaseApplicationDTO(BaseDTO):
    """
    Java class 'org.osgi.service.jaxrs.runtime.dto.BaseApplicationDTO'
    
        Extends:
            org.osgi.service.jaxrs.runtime.dto.BaseDTO
    
      Constructors:
        * BaseApplicationDTO()
    
      Attributes:
        base (java.lang.String): field
        resourceDTOs ([Lorg.osgi.service.jaxrs.runtime.dto.ResourceDTO;): field
        extensionDTOs ([Lorg.osgi.service.jaxrs.runtime.dto.ExtensionDTO;): field
    
    """
    base: java.lang.String = ...
    resourceDTOs: typing.List['ResourceDTO'] = ...
    extensionDTOs: typing.List['ExtensionDTO'] = ...
    def __init__(self): ...

class BaseExtensionDTO(BaseDTO):
    """
    Java class 'org.osgi.service.jaxrs.runtime.dto.BaseExtensionDTO'
    
        Extends:
            org.osgi.service.jaxrs.runtime.dto.BaseDTO
    
      Constructors:
        * BaseExtensionDTO()
    
      Attributes:
        extensionTypes ([Ljava.lang.String;): field
    
    """
    extensionTypes: typing.List[java.lang.String] = ...
    def __init__(self): ...

class FailedResourceDTO(BaseDTO):
    """
    Java class 'org.osgi.service.jaxrs.runtime.dto.FailedResourceDTO'
    
        Extends:
            org.osgi.service.jaxrs.runtime.dto.BaseDTO
    
      Constructors:
        * FailedResourceDTO()
    
      Attributes:
        failureReason (int): field
    
    """
    failureReason: int = ...
    def __init__(self): ...

class ResourceDTO(BaseDTO):
    """
    Java class 'org.osgi.service.jaxrs.runtime.dto.ResourceDTO'
    
        Extends:
            org.osgi.service.jaxrs.runtime.dto.BaseDTO
    
      Constructors:
        * ResourceDTO()
    
      Attributes:
        resourceMethods ([Lorg.osgi.service.jaxrs.runtime.dto.ResourceMethodInfoDTO;): field
    
    """
    resourceMethods: typing.List[ResourceMethodInfoDTO] = ...
    def __init__(self): ...

class ApplicationDTO(BaseApplicationDTO):
    """
    Java class 'org.osgi.service.jaxrs.runtime.dto.ApplicationDTO'
    
        Extends:
            org.osgi.service.jaxrs.runtime.dto.BaseApplicationDTO
    
      Constructors:
        * ApplicationDTO()
    
      Attributes:
        resourceMethods ([Lorg.osgi.service.jaxrs.runtime.dto.ResourceMethodInfoDTO;): field
    
    """
    resourceMethods: typing.List[ResourceMethodInfoDTO] = ...
    def __init__(self): ...

class ExtensionDTO(BaseExtensionDTO):
    """
    Java class 'org.osgi.service.jaxrs.runtime.dto.ExtensionDTO'
    
        Extends:
            org.osgi.service.jaxrs.runtime.dto.BaseExtensionDTO
    
      Constructors:
        * ExtensionDTO()
    
      Attributes:
        produces ([Ljava.lang.String;): field
        consumes ([Ljava.lang.String;): field
        nameBindings ([Ljava.lang.String;): field
        filteredByName ([Lorg.osgi.service.jaxrs.runtime.dto.ResourceDTO;): field
    
    """
    produces: typing.List[java.lang.String] = ...
    consumes: typing.List[java.lang.String] = ...
    nameBindings: typing.List[java.lang.String] = ...
    filteredByName: typing.List[ResourceDTO] = ...
    def __init__(self): ...

class FailedApplicationDTO(BaseApplicationDTO):
    """
    Java class 'org.osgi.service.jaxrs.runtime.dto.FailedApplicationDTO'
    
        Extends:
            org.osgi.service.jaxrs.runtime.dto.BaseApplicationDTO
    
      Constructors:
        * FailedApplicationDTO()
    
      Attributes:
        failureReason (int): field
    
    """
    failureReason: int = ...
    def __init__(self): ...

class FailedExtensionDTO(BaseExtensionDTO):
    """
    Java class 'org.osgi.service.jaxrs.runtime.dto.FailedExtensionDTO'
    
        Extends:
            org.osgi.service.jaxrs.runtime.dto.BaseExtensionDTO
    
      Constructors:
        * FailedExtensionDTO()
    
      Attributes:
        failureReason (int): field
    
    """
    failureReason: int = ...
    def __init__(self): ...
