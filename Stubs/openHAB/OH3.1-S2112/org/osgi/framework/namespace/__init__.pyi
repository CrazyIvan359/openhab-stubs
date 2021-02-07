import java.lang
import org.osgi.resource
import typing


class AbstractWiringNamespace(org.osgi.resource.Namespace):
    """
    Java class 'org.osgi.framework.namespace.AbstractWiringNamespace'
    
        Extends:
            org.osgi.resource.Namespace
    
      Attributes:
        CAPABILITY_MANDATORY_DIRECTIVE (java.lang.String): final static field
        CAPABILITY_BUNDLE_VERSION_ATTRIBUTE (java.lang.String): final static field
    
    """
    CAPABILITY_MANDATORY_DIRECTIVE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_BUNDLE_VERSION_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...

class ExecutionEnvironmentNamespace(org.osgi.resource.Namespace):
    """
    Java class 'org.osgi.framework.namespace.ExecutionEnvironmentNamespace'
    
        Extends:
            org.osgi.resource.Namespace
    
      Attributes:
        EXECUTION_ENVIRONMENT_NAMESPACE (java.lang.String): final static field
        CAPABILITY_VERSION_ATTRIBUTE (java.lang.String): final static field
    
    """
    EXECUTION_ENVIRONMENT_NAMESPACE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_VERSION_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...

class IdentityNamespace(org.osgi.resource.Namespace):
    """
    Java class 'org.osgi.framework.namespace.IdentityNamespace'
    
        Extends:
            org.osgi.resource.Namespace
    
      Attributes:
        IDENTITY_NAMESPACE (java.lang.String): final static field
        CAPABILITY_SINGLETON_DIRECTIVE (java.lang.String): final static field
        CAPABILITY_VERSION_ATTRIBUTE (java.lang.String): final static field
        CAPABILITY_TYPE_ATTRIBUTE (java.lang.String): final static field
        TYPE_BUNDLE (java.lang.String): final static field
        TYPE_FRAGMENT (java.lang.String): final static field
        TYPE_UNKNOWN (java.lang.String): final static field
        CAPABILITY_COPYRIGHT_ATTRIBUTE (java.lang.String): final static field
        CAPABILITY_DESCRIPTION_ATTRIBUTE (java.lang.String): final static field
        CAPABILITY_DOCUMENTATION_ATTRIBUTE (java.lang.String): final static field
        CAPABILITY_LICENSE_ATTRIBUTE (java.lang.String): final static field
        REQUIREMENT_CLASSIFIER_DIRECTIVE (java.lang.String): final static field
        CLASSIFIER_SOURCES (java.lang.String): final static field
        CLASSIFIER_JAVADOC (java.lang.String): final static field
    
    """
    IDENTITY_NAMESPACE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_SINGLETON_DIRECTIVE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_VERSION_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_TYPE_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    TYPE_BUNDLE: typing.ClassVar[java.lang.String] = ...
    TYPE_FRAGMENT: typing.ClassVar[java.lang.String] = ...
    TYPE_UNKNOWN: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_COPYRIGHT_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_DESCRIPTION_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_DOCUMENTATION_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_LICENSE_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    REQUIREMENT_CLASSIFIER_DIRECTIVE: typing.ClassVar[java.lang.String] = ...
    CLASSIFIER_SOURCES: typing.ClassVar[java.lang.String] = ...
    CLASSIFIER_JAVADOC: typing.ClassVar[java.lang.String] = ...

class NativeNamespace(org.osgi.resource.Namespace):
    """
    Java class 'org.osgi.framework.namespace.NativeNamespace'
    
        Extends:
            org.osgi.resource.Namespace
    
      Attributes:
        NATIVE_NAMESPACE (java.lang.String): final static field
        CAPABILITY_OSNAME_ATTRIBUTE (java.lang.String): final static field
        CAPABILITY_OSVERSION_ATTRIBUTE (java.lang.String): final static field
        CAPABILITY_PROCESSOR_ATTRIBUTE (java.lang.String): final static field
        CAPABILITY_LANGUAGE_ATTRIBUTE (java.lang.String): final static field
    
    """
    NATIVE_NAMESPACE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_OSNAME_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_OSVERSION_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_PROCESSOR_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_LANGUAGE_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...

class BundleNamespace(AbstractWiringNamespace):
    """
    Java class 'org.osgi.framework.namespace.BundleNamespace'
    
        Extends:
            org.osgi.framework.namespace.AbstractWiringNamespace
    
      Attributes:
        BUNDLE_NAMESPACE (java.lang.String): final static field
        CAPABILITY_SINGLETON_DIRECTIVE (java.lang.String): final static field
        CAPABILITY_FRAGMENT_ATTACHMENT_DIRECTIVE (java.lang.String): final static field
        REQUIREMENT_EXTENSION_DIRECTIVE (java.lang.String): final static field
        REQUIREMENT_VISIBILITY_DIRECTIVE (java.lang.String): final static field
        VISIBILITY_PRIVATE (java.lang.String): final static field
        VISIBILITY_REEXPORT (java.lang.String): final static field
    
    """
    BUNDLE_NAMESPACE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_SINGLETON_DIRECTIVE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_FRAGMENT_ATTACHMENT_DIRECTIVE: typing.ClassVar[java.lang.String] = ...
    REQUIREMENT_EXTENSION_DIRECTIVE: typing.ClassVar[java.lang.String] = ...
    REQUIREMENT_VISIBILITY_DIRECTIVE: typing.ClassVar[java.lang.String] = ...
    VISIBILITY_PRIVATE: typing.ClassVar[java.lang.String] = ...
    VISIBILITY_REEXPORT: typing.ClassVar[java.lang.String] = ...

class HostNamespace(AbstractWiringNamespace):
    """
    Java class 'org.osgi.framework.namespace.HostNamespace'
    
        Extends:
            org.osgi.framework.namespace.AbstractWiringNamespace
    
      Attributes:
        HOST_NAMESPACE (java.lang.String): final static field
        CAPABILITY_SINGLETON_DIRECTIVE (java.lang.String): final static field
        CAPABILITY_FRAGMENT_ATTACHMENT_DIRECTIVE (java.lang.String): final static field
        FRAGMENT_ATTACHMENT_ALWAYS (java.lang.String): final static field
        FRAGMENT_ATTACHMENT_RESOLVETIME (java.lang.String): final static field
        FRAGMENT_ATTACHMENT_NEVER (java.lang.String): final static field
        REQUIREMENT_EXTENSION_DIRECTIVE (java.lang.String): final static field
        EXTENSION_FRAMEWORK (java.lang.String): final static field
        EXTENSION_BOOTCLASSPATH (java.lang.String): final static field
        REQUIREMENT_VISIBILITY_DIRECTIVE (java.lang.String): final static field
    
    """
    HOST_NAMESPACE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_SINGLETON_DIRECTIVE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_FRAGMENT_ATTACHMENT_DIRECTIVE: typing.ClassVar[java.lang.String] = ...
    FRAGMENT_ATTACHMENT_ALWAYS: typing.ClassVar[java.lang.String] = ...
    FRAGMENT_ATTACHMENT_RESOLVETIME: typing.ClassVar[java.lang.String] = ...
    FRAGMENT_ATTACHMENT_NEVER: typing.ClassVar[java.lang.String] = ...
    REQUIREMENT_EXTENSION_DIRECTIVE: typing.ClassVar[java.lang.String] = ...
    EXTENSION_FRAMEWORK: typing.ClassVar[java.lang.String] = ...
    EXTENSION_BOOTCLASSPATH: typing.ClassVar[java.lang.String] = ...
    REQUIREMENT_VISIBILITY_DIRECTIVE: typing.ClassVar[java.lang.String] = ...

class PackageNamespace(AbstractWiringNamespace):
    """
    Java class 'org.osgi.framework.namespace.PackageNamespace'
    
        Extends:
            org.osgi.framework.namespace.AbstractWiringNamespace
    
      Attributes:
        PACKAGE_NAMESPACE (java.lang.String): final static field
        CAPABILITY_INCLUDE_DIRECTIVE (java.lang.String): final static field
        CAPABILITY_EXCLUDE_DIRECTIVE (java.lang.String): final static field
        CAPABILITY_VERSION_ATTRIBUTE (java.lang.String): final static field
        CAPABILITY_BUNDLE_SYMBOLICNAME_ATTRIBUTE (java.lang.String): final static field
        RESOLUTION_DYNAMIC (java.lang.String): final static field
    
    """
    PACKAGE_NAMESPACE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_INCLUDE_DIRECTIVE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_EXCLUDE_DIRECTIVE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_VERSION_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    CAPABILITY_BUNDLE_SYMBOLICNAME_ATTRIBUTE: typing.ClassVar[java.lang.String] = ...
    RESOLUTION_DYNAMIC: typing.ClassVar[java.lang.String] = ...
