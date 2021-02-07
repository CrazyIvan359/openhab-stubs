import com.google.inject
import java.lang
import java.net
import java.util
import org.eclipse.emf.common.util
import org.eclipse.xtext.ide.server
import org.eclipse.xtext.resource
import org.openhab.core.model.script
import org.openhab.core.model.script.engine
import typing


class MappingUriExtensions(org.eclipse.xtext.ide.server.UriExtensions):
    """
    Java class 'org.openhab.core.model.lsp.internal.MappingUriExtensions'
    
        Extends:
            org.eclipse.xtext.ide.server.UriExtensions
    
      Constructors:
        * MappingUriExtensions(java.lang.String)
    
    """
    def __init__(self, configFolder: java.lang.String): ...
    def toUri(self, pathWithScheme: java.lang.String) -> org.eclipse.emf.common.util.URI: ...
    @typing.overload
    def toUriString(self, uri: java.net.URI) -> java.lang.String: ...
    @typing.overload
    def toUriString(self, uri: org.eclipse.emf.common.util.URI) -> java.lang.String: ...

class ModelServer(java.lang.Object):
    """
    Java class 'org.openhab.core.model.lsp.internal.ModelServer'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ModelServer(org.openhab.core.model.script.ScriptServiceUtil, org.openhab.core.model.script.engine.ScriptEngine)
    
      Attributes:
        CONFIGURATION_PID (java.lang.String): final static field
    
    """
    CONFIGURATION_PID: typing.ClassVar[java.lang.String] = ...
    def __init__(self, scriptServiceUtil: org.openhab.core.model.script.ScriptServiceUtil, scriptEngine: org.openhab.core.model.script.engine.ScriptEngine): ...
    def activate(self, config: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> None: ...
    def deactivate(self) -> None: ...

class RegistryProvider(com.google.inject.Provider[org.eclipse.xtext.resource.IResourceServiceProvider.Registry]):
    """
    Java class 'org.openhab.core.model.lsp.internal.RegistryProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            com.google.inject.Provider
    
      Constructors:
        * RegistryProvider(org.openhab.core.model.script.ScriptServiceUtil, org.openhab.core.model.script.engine.ScriptEngine)
    
    """
    def __init__(self, scriptServiceUtil: org.openhab.core.model.script.ScriptServiceUtil, scriptEngine: org.openhab.core.model.script.engine.ScriptEngine): ...
    @typing.overload
    def get(self) -> typing.Any: ...
    @typing.overload
    def get(self) -> org.eclipse.xtext.resource.IResourceServiceProvider.Registry: ...

class RuntimeServerModule(com.google.inject.AbstractModule):
    """
    Java class 'org.openhab.core.model.lsp.internal.RuntimeServerModule'
    
        Extends:
            com.google.inject.AbstractModule
    
      Constructors:
        * RuntimeServerModule(org.openhab.core.model.script.ScriptServiceUtil, org.openhab.core.model.script.engine.ScriptEngine)
    
    """
    def __init__(self, scriptServiceUtil: org.openhab.core.model.script.ScriptServiceUtil, scriptEngine: org.openhab.core.model.script.engine.ScriptEngine): ...
