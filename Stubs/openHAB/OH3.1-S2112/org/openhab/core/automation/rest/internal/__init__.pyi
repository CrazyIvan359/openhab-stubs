import java.lang
import java.util
import javax.ws.rs.core
import org.openhab.core.automation
import org.openhab.core.automation.dto
import org.openhab.core.automation.template
import org.openhab.core.automation.type
import org.openhab.core.io.rest
import typing


class ModuleTypeResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.automation.rest.internal.ModuleTypeResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * ModuleTypeResource(org.openhab.core.io.rest.LocaleService, org.openhab.core.automation.type.ModuleTypeRegistry)
    
      Attributes:
        PATH_MODULE_TYPES (java.lang.String): final static field
    
    """
    PATH_MODULE_TYPES: typing.ClassVar[java.lang.String] = ...
    def __init__(self, localeService: org.openhab.core.io.rest.LocaleService, moduleTypeRegistry: org.openhab.core.automation.type.ModuleTypeRegistry): ...
    def getAll(self, language: java.lang.String, tagList: java.lang.String, type: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getByUID(self, language: java.lang.String, moduleTypeUID: java.lang.String) -> javax.ws.rs.core.Response: ...

class RuleResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.automation.rest.internal.RuleResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * RuleResource(org.openhab.core.io.rest.DTOMapper, org.openhab.core.automation.RuleManager, org.openhab.core.automation.RuleRegistry, org.openhab.core.automation.ManagedRuleProvider)
    
      Attributes:
        PATH_RULES (java.lang.String): final static field
    
    """
    PATH_RULES: typing.ClassVar[java.lang.String] = ...
    def __init__(self, dtoMapper: org.openhab.core.io.rest.DTOMapper, ruleManager: org.openhab.core.automation.RuleManager, ruleRegistry: org.openhab.core.automation.RuleRegistry, managedRuleProvider: org.openhab.core.automation.ManagedRuleProvider): ...
    def create(self, rule: org.openhab.core.automation.dto.RuleDTO) -> javax.ws.rs.core.Response: ...
    def enableRule(self, ruleUID: java.lang.String, enabled: java.lang.String) -> javax.ws.rs.core.Response: ...
    def get(self, prefix: java.lang.String, tags: java.util.List[java.lang.String], summary: bool) -> javax.ws.rs.core.Response: ...
    def getActions(self, ruleUID: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getByUID(self, ruleUID: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getConditions(self, ruleUID: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getConfiguration(self, ruleUID: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getModuleById(self, ruleUID: java.lang.String, moduleCategory: java.lang.String, id: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getModuleConfig(self, ruleUID: java.lang.String, moduleCategory: java.lang.String, id: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getModuleConfigParam(self, ruleUID: java.lang.String, moduleCategory: java.lang.String, id: java.lang.String, param: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getTriggers(self, ruleUID: java.lang.String) -> javax.ws.rs.core.Response: ...
    def remove(self, ruleUID: java.lang.String) -> javax.ws.rs.core.Response: ...
    def runNow(self, ruleUID: java.lang.String) -> javax.ws.rs.core.Response: ...
    def setModuleConfigParam(self, ruleUID: java.lang.String, moduleCategory: java.lang.String, id: java.lang.String, param: java.lang.String, value: java.lang.String) -> javax.ws.rs.core.Response: ...
    def update(self, ruleUID: java.lang.String, rule: org.openhab.core.automation.dto.RuleDTO) -> javax.ws.rs.core.Response: ...
    def updateConfiguration(self, ruleUID: java.lang.String, configurationParameters: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> javax.ws.rs.core.Response: ...

class TemplateResource(org.openhab.core.io.rest.RESTResource):
    """
    Java class 'org.openhab.core.automation.rest.internal.TemplateResource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.io.rest.RESTResource
    
      Constructors:
        * TemplateResource(org.openhab.core.io.rest.LocaleService, org.openhab.core.automation.template.TemplateRegistry)
    
      Attributes:
        PATH_TEMPLATES (java.lang.String): final static field
    
    """
    PATH_TEMPLATES: typing.ClassVar[java.lang.String] = ...
    def __init__(self, localeService: org.openhab.core.io.rest.LocaleService, templateRegistry: org.openhab.core.automation.template.TemplateRegistry[org.openhab.core.automation.template.RuleTemplate]): ...
    def getAll(self, language: java.lang.String) -> javax.ws.rs.core.Response: ...
    def getByUID(self, language: java.lang.String, templateUID: java.lang.String) -> javax.ws.rs.core.Response: ...
