import java.lang
import java.util
import org.openhab.core.automation.template
import org.openhab.core.common.registry
import typing


class RuleTemplateRegistry(org.openhab.core.common.registry.AbstractRegistry[org.openhab.core.automation.template.RuleTemplate, java.lang.String, org.openhab.core.automation.template.RuleTemplateProvider], org.openhab.core.automation.template.TemplateRegistry[org.openhab.core.automation.template.RuleTemplate]):
    """
    Java class 'org.openhab.core.automation.internal.template.RuleTemplateRegistry'
    
        Extends:
            org.openhab.core.common.registry.AbstractRegistry
    
        Interfaces:
            org.openhab.core.automation.template.TemplateRegistry
    
      Constructors:
        * RuleTemplateRegistry()
    
    """
    def __init__(self): ...
    @typing.overload
    def get(self, templateUID: java.lang.String) -> org.openhab.core.automation.template.RuleTemplate: ...
    @typing.overload
    def get(self, templateUID: java.lang.String, locale: java.util.Locale) -> org.openhab.core.automation.template.RuleTemplate: ...
    @typing.overload
    def get(self, string: java.lang.String, locale: java.util.Locale) -> org.openhab.core.automation.template.Template: ...
    @typing.overload
    def get(self, object: typing.Any) -> org.openhab.core.common.registry.Identifiable: ...
    @typing.overload
    def getAll(self, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.automation.template.RuleTemplate]: ...
    @typing.overload
    def getAll(self) -> java.util.Collection[org.openhab.core.common.registry.Identifiable]: ...
    @typing.overload
    def getByTag(self, tag: java.lang.String) -> java.util.Collection[org.openhab.core.automation.template.RuleTemplate]: ...
    @typing.overload
    def getByTag(self, tag: java.lang.String, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.automation.template.RuleTemplate]: ...
    @typing.overload
    def getByTags(self, tags: typing.List[java.lang.String]) -> java.util.Collection[org.openhab.core.automation.template.RuleTemplate]: ...
    @typing.overload
    def getByTags(self, locale: java.util.Locale, tags: typing.List[java.lang.String]) -> java.util.Collection[org.openhab.core.automation.template.RuleTemplate]: ...
