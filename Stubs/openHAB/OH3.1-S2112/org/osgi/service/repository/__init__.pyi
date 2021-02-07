import java.io
import java.lang
import java.util
import org.osgi.resource
import org.osgi.util.promise
import typing


class ContentNamespace(org.osgi.resource.Namespace):
    """
    Java class 'org.osgi.service.repository.ContentNamespace'
    
        Extends:
            org.osgi.resource.Namespace
    
      Attributes:
        CONTENT_NAMESPACE (java.lang.String): final static field
        CAPABILITY_URL_ATTRIBUTE (java.lang.String): final static field
        CAPABILITY_SIZE_ATTRIBUTE (java.lang.String): final static field
        CAPABILITY_MIME_ATTRIBUTE (java.lang.String): final static field
    
    """
    CONTENT_NAMESPACE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_URL_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_SIZE_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_MIME_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...

class ExpressionCombiner(java.lang.Object):
    """
    Java class 'org.osgi.service.repository.ExpressionCombiner'
    
    """
    def identity(self, requirement: org.osgi.resource.Requirement) -> 'IdentityExpression': ...

class Repository(java.lang.Object):
    """
    Java class 'org.osgi.service.repository.Repository'
    
      Attributes:
        URL (java.lang.String): final static field
    
    """
    URL: typing.ClassVar[java.lang.String] = ...
    @typing.overload
    def findProviders(self, collection: typing.Union[java.util.Collection[org.osgi.resource.Requirement], typing.Sequence[org.osgi.resource.Requirement]]) -> java.util.Map[org.osgi.resource.Requirement, java.util.Collection[org.osgi.resource.Capability]]: ...
    @typing.overload
    def findProviders(self, requirementExpression: 'RequirementExpression') -> org.osgi.util.promise.Promise[java.util.Collection[org.osgi.resource.Resource]]: ...
    def getExpressionCombiner(self) -> ExpressionCombiner: ...
    def newRequirementBuilder(self, string: java.lang.String) -> 'RequirementBuilder': ...

class RepositoryContent(java.lang.Object):
    """
    Java class 'org.osgi.service.repository.RepositoryContent'
    
    """
    def getContent(self) -> java.io.InputStream: ...

class RequirementBuilder(java.lang.Object):
    """
    Java class 'org.osgi.service.repository.RequirementBuilder'
    
    """
    def addAttribute(self, string: java.lang.String, object: typing.Any) -> 'RequirementBuilder': ...
    def addDirective(self, string: java.lang.String, string2: java.lang.String) -> 'RequirementBuilder': ...
    def build(self) -> org.osgi.resource.Requirement: ...
    def buildExpression(self) -> 'IdentityExpression': ...
    def setAttributes(self, map: typing.Union[java.util.Map[java.lang.String, typing.Any], typing.Mapping[java.lang.String, typing.Any]]) -> 'RequirementBuilder': ...
    def setDirectives(self, map: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> 'RequirementBuilder': ...
    def setResource(self, resource: org.osgi.resource.Resource) -> 'RequirementBuilder': ...

class RequirementExpression(java.lang.Object):
    """
    Java class 'org.osgi.service.repository.RequirementExpression'
    
    """

class AndExpression(RequirementExpression):
    """
    Java class 'org.osgi.service.repository.AndExpression'
    
        Interfaces:
            org.osgi.service.repository.RequirementExpression
    
    """
    def getRequirementExpressions(self) -> java.util.List[RequirementExpression]: ...

class IdentityExpression(RequirementExpression):
    """
    Java class 'org.osgi.service.repository.IdentityExpression'
    
        Interfaces:
            org.osgi.service.repository.RequirementExpression
    
    """
    def getRequirement(self) -> org.osgi.resource.Requirement: ...

class NotExpression(RequirementExpression):
    """
    Java class 'org.osgi.service.repository.NotExpression'
    
        Interfaces:
            org.osgi.service.repository.RequirementExpression
    
    """
    def getRequirementExpression(self) -> RequirementExpression: ...

class OrExpression(RequirementExpression):
    """
    Java class 'org.osgi.service.repository.OrExpression'
    
        Interfaces:
            org.osgi.service.repository.RequirementExpression
    
    """
    def getRequirementExpressions(self) -> java.util.List[RequirementExpression]: ...
