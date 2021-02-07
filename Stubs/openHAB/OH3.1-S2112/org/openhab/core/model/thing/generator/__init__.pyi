import org.eclipse.emf.ecore.resource
import org.eclipse.xtext.generator


class ThingGenerator(org.eclipse.xtext.generator.AbstractGenerator):
    """
    Java class 'org.openhab.core.model.thing.generator.ThingGenerator'
    
        Extends:
            org.eclipse.xtext.generator.AbstractGenerator
    
      Constructors:
        * ThingGenerator()
    
    """
    def __init__(self): ...
    def doGenerate(self, resource: org.eclipse.emf.ecore.resource.Resource, iFileSystemAccess2: org.eclipse.xtext.generator.IFileSystemAccess2, iGeneratorContext: org.eclipse.xtext.generator.IGeneratorContext) -> None: ...
