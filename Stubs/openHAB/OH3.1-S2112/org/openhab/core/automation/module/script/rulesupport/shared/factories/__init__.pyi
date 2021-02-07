import org.openhab.core.automation
import org.openhab.core.automation.handler
import org.openhab.core.automation.module.script.rulesupport.shared


class ScriptedActionHandlerFactory(org.openhab.core.automation.module.script.rulesupport.shared.ScriptedHandler):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.shared.factories.ScriptedActionHandlerFactory'
    
        Interfaces:
            org.openhab.core.automation.module.script.rulesupport.shared.S
            criptedHandler
    
    """
    def get(self, action: org.openhab.core.automation.Action) -> org.openhab.core.automation.handler.ActionHandler: ...

class ScriptedConditionHandlerFactory(org.openhab.core.automation.module.script.rulesupport.shared.ScriptedHandler):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.shared.factories.ScriptedConditionHandlerFactory'
    
        Interfaces:
            org.openhab.core.automation.module.script.rulesupport.shared.S
            criptedHandler
    
    """
    def get(self, module: org.openhab.core.automation.Condition) -> org.openhab.core.automation.handler.ConditionHandler: ...

class ScriptedTriggerHandlerFactory(org.openhab.core.automation.module.script.rulesupport.shared.ScriptedHandler):
    """
    Java class 'org.openhab.core.automation.module.script.rulesupport.shared.factories.ScriptedTriggerHandlerFactory'
    
        Interfaces:
            org.openhab.core.automation.module.script.rulesupport.shared.S
            criptedHandler
    
    """
    def get(self, module: org.openhab.core.automation.Trigger) -> org.openhab.core.automation.handler.TriggerHandler: ...
