import org.eclipse.emf.ecore.resource
import org.eclipse.xtext.generator


class SitemapGenerator(org.eclipse.xtext.generator.AbstractGenerator):
    """
    Java class 'org.openhab.core.model.sitemap.generator.SitemapGenerator'
    
        Extends:
            org.eclipse.xtext.generator.AbstractGenerator
    
      Constructors:
        * SitemapGenerator()
    
    """
    def __init__(self): ...
    def doGenerate(self, resource: org.eclipse.emf.ecore.resource.Resource, fsa: org.eclipse.xtext.generator.IFileSystemAccess2, context: org.eclipse.xtext.generator.IGeneratorContext) -> None: ...
