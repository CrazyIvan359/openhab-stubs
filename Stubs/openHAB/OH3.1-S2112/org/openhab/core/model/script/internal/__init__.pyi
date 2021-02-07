import java.lang
import java.util
import org.eclipse.emf.common.util
import org.eclipse.xtext.parser
import org.openhab.core.events
import org.openhab.core.voice.text


class RuleHumanLanguageInterpreter(org.openhab.core.voice.text.HumanLanguageInterpreter):
    """
    Java class 'org.openhab.core.model.script.internal.RuleHumanLanguageInterpreter'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.openhab.core.voice.text.HumanLanguageInterpreter
    
      Constructors:
        * RuleHumanLanguageInterpreter(org.openhab.core.events.EventPublisher)
    
    """
    def __init__(self, eventPublisher: org.openhab.core.events.EventPublisher): ...
    def getGrammar(self, locale: java.util.Locale, format: java.lang.String) -> java.lang.String: ...
    def getId(self) -> java.lang.String: ...
    def getLabel(self, locale: java.util.Locale) -> java.lang.String: ...
    def getSupportedGrammarFormats(self) -> java.util.Set[java.lang.String]: ...
    def getSupportedLocales(self) -> java.util.Set[java.util.Locale]: ...
    def interpret(self, locale: java.util.Locale, text: java.lang.String) -> java.lang.String: ...

class ScriptEncodingProvider(org.eclipse.xtext.parser.IEncodingProvider):
    """
    Java class 'org.openhab.core.model.script.internal.ScriptEncodingProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.eclipse.xtext.parser.IEncodingProvider
    
      Constructors:
        * ScriptEncodingProvider()
    
    """
    def __init__(self): ...
    def getEncoding(self, uri: org.eclipse.emf.common.util.URI) -> java.lang.String: ...
