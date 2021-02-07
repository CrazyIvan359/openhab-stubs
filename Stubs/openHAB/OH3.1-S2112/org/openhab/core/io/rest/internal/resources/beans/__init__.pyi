import java.lang
import java.util
import org.openhab.core.i18n


class RootBean(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.internal.resources.beans.RootBean'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RootBean(org.openhab.core.i18n.LocaleProvider, org.openhab.core.i18n.UnitProvider)
    
      Attributes:
        version (java.lang.String): final field
        locale (java.lang.String): final field
        measurementSystem (java.lang.String): final field
        runtimeInfo (org.openhab.core.io.rest.internal.resources.beans.RootBean$RuntimeInfo): final field
        links (java.util.List): final field
    
    """
    version: java.lang.String = ...
    locale: java.lang.String = ...
    measurementSystem: java.lang.String = ...
    runtimeInfo: 'RootBean.RuntimeInfo' = ...
    links: java.util.List = ...
    def __init__(self, localeProvider: org.openhab.core.i18n.LocaleProvider, unitProvider: org.openhab.core.i18n.UnitProvider): ...
    class Links(java.lang.Object):
        """
        Java class 'org.openhab.core.io.rest.internal.resources.beans.RootBean$Links'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * Links(java.lang.String, java.lang.String)
        
          Attributes:
            type (java.lang.String): field
            url (java.lang.String): field
        
        """
        type: java.lang.String = ...
        url: java.lang.String = ...
        def __init__(self, type: java.lang.String, url: java.lang.String): ...
    class RuntimeInfo(java.lang.Object):
        """
        Java class 'org.openhab.core.io.rest.internal.resources.beans.RootBean$RuntimeInfo'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * RuntimeInfo()
        
          Attributes:
            version (java.lang.String): final field
            buildString (java.lang.String): final field
        
        """
        version: java.lang.String = ...
        buildString: java.lang.String = ...
        def __init__(self): ...

class SystemInfoBean(java.lang.Object):
    """
    Java class 'org.openhab.core.io.rest.internal.resources.beans.SystemInfoBean'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SystemInfoBean()
    
      Attributes:
        systemInfo (org.openhab.core.io.rest.internal.resources.beans.SystemInfoBean$SystemInfo): final field
    
    """
    systemInfo: 'SystemInfoBean.SystemInfo' = ...
    def __init__(self): ...
    class SystemInfo(java.lang.Object):
        """
        Java class 'org.openhab.core.io.rest.internal.resources.beans.SystemInfoBean$SystemInfo'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * SystemInfo()
        
          Attributes:
            configFolder (java.lang.String): final field
            userdataFolder (java.lang.String): final field
            logFolder (java.lang.String): final field
            javaVersion (java.lang.String): final field
            javaVendor (java.lang.String): final field
            javaVendorVersion (java.lang.String): final field
            osName (java.lang.String): final field
            osVersion (java.lang.String): final field
            osArchitecture (java.lang.String): final field
            availableProcessors (int): final field
            freeMemory (long): final field
            totalMemory (long): final field
        
        """
        configFolder: java.lang.String = ...
        userdataFolder: java.lang.String = ...
        logFolder: java.lang.String = ...
        javaVersion: java.lang.String = ...
        javaVendor: java.lang.String = ...
        javaVendorVersion: java.lang.String = ...
        osName: java.lang.String = ...
        osVersion: java.lang.String = ...
        osArchitecture: java.lang.String = ...
        availableProcessors: int = ...
        freeMemory: int = ...
        totalMemory: int = ...
        def __init__(self): ...
