import java.lang
import java.util
import org.openhab.core.automation
import org.openhab.core.automation.module.provider.i18n
import org.openhab.core.automation.type
import org.openhab.core.config.core.i18n
import org.openhab.core.i18n
import org.osgi.framework
import typing


class ModuleI18nUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.internal.provider.i18n.ModuleI18nUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ModuleI18nUtil(org.openhab.core.i18n.TranslationProvider)
    
    """
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    _getLocalizedModules__T = typing.TypeVar('_getLocalizedModules__T', bound=org.openhab.core.automation.Module)  # <T>
    def getLocalizedModules(self, modules: java.util.List[_getLocalizedModules__T], bundle: org.osgi.framework.Bundle, uid: java.lang.String, prefix: java.lang.String, locale: java.util.Locale) -> java.util.List[_getLocalizedModules__T]: ...

class ModuleTypeI18nServiceImpl(org.openhab.core.automation.module.provider.i18n.ModuleTypeI18nService):
    """
    Java class 'org.openhab.core.automation.internal.provider.i18n.ModuleTypeI18nServiceImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.automation.module.provider.i18n.ModuleTypeI18
            nService
    
      Constructors:
        * ModuleTypeI18nServiceImpl(org.openhab.core.config.core.i18n.ConfigI18nLocalizationService, org.openhab.core.i18n.TranslationProvider)
    
    """
    def __init__(self, configI18nService: org.openhab.core.config.core.i18n.ConfigI18nLocalizationService, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    def getModuleTypePerLocale(self, defModuleType: org.openhab.core.automation.type.ModuleType, locale: java.util.Locale, bundle: org.osgi.framework.Bundle) -> org.openhab.core.automation.type.ModuleType: ...

class ModuleTypeI18nUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.internal.provider.i18n.ModuleTypeI18nUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ModuleTypeI18nUtil(org.openhab.core.i18n.TranslationProvider)
    
      Attributes:
        MODULE_TYPE (java.lang.String): final static field
    
    """
    MODULE_TYPE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    def getLocalizedInputs(self, inputs: java.util.List[org.openhab.core.automation.type.Input], bundle: org.osgi.framework.Bundle, uid: java.lang.String, locale: java.util.Locale) -> java.util.List[org.openhab.core.automation.type.Input]: ...
    def getLocalizedModuleTypeDescription(self, bundle: org.osgi.framework.Bundle, moduleTypeUID: java.lang.String, defaultDescription: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getLocalizedModuleTypeLabel(self, bundle: org.osgi.framework.Bundle, moduleTypeUID: java.lang.String, defaultLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getLocalizedOutputs(self, outputs: java.util.List[org.openhab.core.automation.type.Output], bundle: org.osgi.framework.Bundle, uid: java.lang.String, locale: java.util.Locale) -> java.util.List[org.openhab.core.automation.type.Output]: ...

class RuleTemplateI18nUtil(java.lang.Object):
    """
    Java class 'org.openhab.core.automation.internal.provider.i18n.RuleTemplateI18nUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RuleTemplateI18nUtil(org.openhab.core.i18n.TranslationProvider)
    
      Attributes:
        RULE_TEMPLATE (java.lang.String): final static field
    
    """
    RULE_TEMPLATE: typing.ClassVar[java.lang.String] = ...
    def __init__(self, i18nProvider: org.openhab.core.i18n.TranslationProvider): ...
    def getLocalizedRuleTemplateDescription(self, bundle: org.osgi.framework.Bundle, ruleTemplateUID: java.lang.String, defaultDescription: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getLocalizedRuleTemplateLabel(self, bundle: org.osgi.framework.Bundle, ruleTemplateUID: java.lang.String, defaultLabel: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
