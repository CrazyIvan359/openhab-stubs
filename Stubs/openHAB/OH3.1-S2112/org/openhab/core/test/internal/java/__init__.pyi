import java.io
import java.lang
import org.osgi.framework
import typing


class MissingServiceAnalyzer(java.lang.Object):
    """
    Java class 'org.openhab.core.test.internal.java.MissingServiceAnalyzer'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MissingServiceAnalyzer(java.io.PrintStream, org.osgi.framework.BundleContext)
    
    """
    def __init__(self, ps: java.io.PrintStream, bundleContext: org.osgi.framework.BundleContext): ...
    _printMissingServiceDetails__T = typing.TypeVar('_printMissingServiceDetails__T')  # <T>
    def printMissingServiceDetails(self, clazz: typing.Type[_printMissingServiceDetails__T]) -> None: ...
