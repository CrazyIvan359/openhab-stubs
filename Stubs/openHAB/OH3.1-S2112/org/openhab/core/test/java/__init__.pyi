import java.lang


class JavaTest(java.lang.Object):
    """
    Java class 'org.openhab.core.test.java.JavaTest'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * JavaTest()
    
    """
    def __init__(self): ...

class JavaOSGiTest(JavaTest):
    """
    Java class 'org.openhab.core.test.java.JavaOSGiTest'
    
        Extends:
            org.openhab.core.test.java.JavaTest
    
      Constructors:
        * JavaOSGiTest()
    
    """
    def __init__(self): ...
    def bindBundleContext(self) -> None: ...
    def unregisterMocks(self) -> None: ...
