import org.eclipse.emf.ecore.resource
import org.eclipse.xtext.generator


class ItemsGenerator(org.eclipse.xtext.generator.AbstractGenerator):
    """
    Java class 'org.openhab.core.model.generator.ItemsGenerator'
    
        Extends:
            org.eclipse.xtext.generator.AbstractGenerator
    
      Constructors:
        * ItemsGenerator()
    
    """
    def __init__(self): ...
    def doGenerate(self, resource: org.eclipse.emf.ecore.resource.Resource, fsa: org.eclipse.xtext.generator.IFileSystemAccess2, context: org.eclipse.xtext.generator.IGeneratorContext) -> None: ...
