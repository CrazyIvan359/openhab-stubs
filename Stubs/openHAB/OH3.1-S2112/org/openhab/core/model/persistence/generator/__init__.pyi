import org.eclipse.emf.ecore.resource
import org.eclipse.xtext.generator


class PersistenceGenerator(org.eclipse.xtext.generator.AbstractGenerator):
    """
    Java class 'org.openhab.core.model.persistence.generator.PersistenceGenerator'
    
        Extends:
            org.eclipse.xtext.generator.AbstractGenerator
    
      Constructors:
        * PersistenceGenerator()
    
    """
    def __init__(self): ...
    def doGenerate(self, resource: org.eclipse.emf.ecore.resource.Resource, fsa: org.eclipse.xtext.generator.IFileSystemAccess2, context: org.eclipse.xtext.generator.IGeneratorContext) -> None: ...
