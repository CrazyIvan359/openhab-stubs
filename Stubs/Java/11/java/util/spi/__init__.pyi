import java.io
import java.lang
import java.util
import typing


class LocaleServiceProvider(java.lang.Object):
    """
    Java class 'java.util.spi.LocaleServiceProvider'
    
        Extends:
            java.lang.Object
    
    """
    def getAvailableLocales(self) -> typing.List[java.util.Locale]: ...
    def isSupportedLocale(self, locale: java.util.Locale) -> bool: ...

class ResourceBundleControlProvider(java.lang.Object):
    """
    public interface ResourceBundleControlProvider
    
        An interface for service providers that provide implementations of :class:`~java.util.ResourceBundle.Control`. The
        :meth:`~java.util.ResourceBundle.default_behavior` of the :code:`ResourceBundle.getBundle` factory methods that take no
        :class:`~java.util.ResourceBundle.Control` instance can be modified with :code:`ResourceBundleControlProvider`
        implementations.
    
        Provider implementations are loaded from the application's class path using :class:`~java.util.ServiceLoader` at the
        first invocation of the :code:`ResourceBundle.getBundle` factory method that takes no
        :class:`~java.util.ResourceBundle.Control` instance.
    
        All :code:`ResourceBundleControlProvider`s are ignored in named modules.
    
        Since:
            1.8
    
        Also see:
            :meth:`~java.util.ResourceBundle.getBundle`, :meth:`~java.util.ServiceLoader.load`
    
    
    """
    def getControl(self, string: java.lang.String) -> java.util.ResourceBundle.Control: ...

class ResourceBundleProvider(java.lang.Object):
    """
    public interface ResourceBundleProvider
    
        :code:`ResourceBundleProvider` is a service provider interface for resource bundles. It is used by
        :meth:`~java.util.ResourceBundle.getBundle` factory methods to locate and load the service providers that are deployed
        as modules via :class:`~java.util.ServiceLoader`.
    
        Developing resource bundle services
    -----------------------------------
    
        A service for a resource bundle of a given *:code:`baseName`* must have a fully-qualified class name of the form:
    
        .. code-block: java
        
         <package of baseName> + ".spi." + <simple name of baseName> + "Provider"
         
        The service type is in a :code:`spi` subpackage as it may be packaged in a module separate from the resource bundle
        providers. For example, the service for a resource bundle named :code:`com.example.app.MyResources` must be
        :code:`com.example.app.spi.MyResourcesProvider`:
    
            .. code-block: java
            
             package com.example.app.spi;
             public interface MyResourcesProvider extends ResourceBundleProvider {
             }
             
    
        Deploying resource bundle service providers
    -------------------------------------------
    
        Resource bundles can be deployed in one or more service providers in modules. For example, a provider for a service
        named ":code:`com.example.app.spi.MyResourcesProvider`" has the following implementation class:
    
            .. code-block: java
            
             import com.example.app.spi.MyResourcesProvider;
             class MyResourcesProviderImpl extends AbstractResourceBundleProvider
                 implements MyResourcesProvider
             {
                 public MyResourcesProviderImpl() {
                     super("java.properties");
                 }
                 // this provider maps the resource bundle to per-language package
                 protected String toBundleName(String baseName, Locale locale) {
                     return "p." + locale.getLanguage() + "." + baseName;
                 }
            
                 public ResourceBundle getBundle(String baseName, Locale locale) {
                     // this module only provides bundles in French
                     if (locale.equals(Locale.FRENCH)) {
                          return super.getBundle(baseName, locale);
                     }
                     // otherwise return null
                     return null;
                 }
             }
        This example provides ":code:`com.example.app.MyResources`" resource bundle of the French locale. Traditionally resource
        bundles of all locales are packaged in the same package as the resource bundle base name. When deploying resource
        bundles in more than one modules and two modules containing a package of the same name, *split package*, is not
        supported, resource bundles in each module can be packaged in a different package as shown in this example where this
        provider packages the resource bundles in per-language package, i.e. :code:`com.example.app.fr` for French locale.
    
        A provider can provide more than one services, each of which is a service for a resource bundle of a different base
        name.
    
        :class:`~java.util.spi.AbstractResourceBundleProvider` provides the basic implementation for
        :code:`ResourceBundleProvider` and a subclass can override the
        :meth:`~java.util.spi.AbstractResourceBundleProvider.toBundleName` method to return a provider-specific location of the
        resource to be loaded, for example, per-language package. A provider can override
        :meth:`~java.util.spi.ResourceBundleProvider.getBundle` method for example to only search the known supported locales or
        return resource bundles in other formats such as XML.
    
        The module declaration of this provider module specifies the following directive:
    
        .. code-block: java
        
             provides com.example.app.spi.MyResourcesProvider with com.example.impl.MyResourcesProviderImpl;
         
    
        :class:`~java.util.spi`
    -----------------------
    
        The module declaration of the *consumer module* that calls one of the :code:`ResourceBundle.getBundle` factory methods
        to obtain a resource bundle from service providers must specify the following directive:
    
        .. code-block: java
        
             uses com.example.app.spi.MyResourcesProvider;
         
        :meth:`~java.util.ResourceBundle.getBundle` locates and loads the providers for
        :code:`com.example.app.spi.MyResourcesProvider` service and then invokes
        :meth:`~java.util.spi.ResourceBundleProvider.getBundle` to find the resource bundle of the given base name and locale.
        If the consumer module is a resource bundle service provider for :code:`com.example.app.spi.MyResourcesProvider`,
        :code:`ResourceBundle.getBundle` will locate resource bundles only from service providers. Otherwise,
        :code:`ResourceBundle.getBundle` may continue the search of the resource bundle in other modules and class path per the
        specification of the :code:`ResourceBundle.getBundle` method being called.
    
        Since:
            9
    
        Also see:
            :class:`~java.util.spi.AbstractResourceBundleProvider`, :meth:`~java.util.ResourceBundle.resource`,
            :class:`~java.util.ServiceLoader`
    
    
    """
    def getBundle(self, string: java.lang.String, locale: java.util.Locale) -> java.util.ResourceBundle: ...

class ToolProvider(java.lang.Object):
    """
    public interface ToolProvider
    
        An interface for command-line tools to provide a way to be invoked without necessarily starting a new VM.
    
        Tool providers are normally located using the service-provider loading facility defined by
        :class:`~java.util.ServiceLoader`. Each provider must provide a name, and a method to run an instance of the
        corresponding tool. When a tool is run, it will be provided with an array of string arguments, and a pair of streams:
        one for normal (or expected) output and the other for reporting any errors that may occur. The interpretation of the
        string arguments will normally be defined by each individual tool provider, but will generally correspond to the
        arguments that could be provided to the tool when invoking the tool from the command line.
    
        Since:
            9
    
    
    """
    @classmethod
    def findFirst(cls, string: java.lang.String) -> java.util.Optional['ToolProvider']: ...
    def name(self) -> java.lang.String: ...
    @typing.overload
    def run(self, printWriter: java.io.PrintWriter, printWriter2: java.io.PrintWriter, stringArray: typing.List[java.lang.String]) -> int: ...
    @typing.overload
    def run(self, printStream: java.io.PrintStream, printStream2: java.io.PrintStream, stringArray: typing.List[java.lang.String]) -> int: ...

class AbstractResourceBundleProvider(ResourceBundleProvider):
    """
    Java class 'java.util.spi.AbstractResourceBundleProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.util.spi.ResourceBundleProvider
    
    """
    def getBundle(self, string: java.lang.String, locale: java.util.Locale) -> java.util.ResourceBundle: ...

class CalendarDataProvider(LocaleServiceProvider):
    """
    Java class 'java.util.spi.CalendarDataProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getFirstDayOfWeek(self, locale: java.util.Locale) -> int: ...
    def getMinimalDaysInFirstWeek(self, locale: java.util.Locale) -> int: ...

class CalendarNameProvider(LocaleServiceProvider):
    """
    Java class 'java.util.spi.CalendarNameProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getDisplayName(self, string: java.lang.String, int: int, int2: int, int3: int, locale: java.util.Locale) -> java.lang.String: ...
    def getDisplayNames(self, string: java.lang.String, int: int, int2: int, locale: java.util.Locale) -> java.util.Map[java.lang.String, int]: ...

class CurrencyNameProvider(LocaleServiceProvider):
    """
    Java class 'java.util.spi.CurrencyNameProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getDisplayName(self, string: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getSymbol(self, string: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...

class LocaleNameProvider(LocaleServiceProvider):
    """
    Java class 'java.util.spi.LocaleNameProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getDisplayCountry(self, string: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getDisplayLanguage(self, string: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getDisplayScript(self, string: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getDisplayUnicodeExtensionKey(self, string: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getDisplayUnicodeExtensionType(self, string: java.lang.String, string2: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...
    def getDisplayVariant(self, string: java.lang.String, locale: java.util.Locale) -> java.lang.String: ...

class TimeZoneNameProvider(LocaleServiceProvider):
    """
    Java class 'java.util.spi.TimeZoneNameProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getDisplayName(self, string: java.lang.String, boolean: bool, int: int, locale: java.util.Locale) -> java.lang.String: ...
    def getGenericDisplayName(self, string: java.lang.String, int: int, locale: java.util.Locale) -> java.lang.String: ...
