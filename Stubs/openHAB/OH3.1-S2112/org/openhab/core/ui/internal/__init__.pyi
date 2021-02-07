import org.osgi.framework


class UIActivator(org.osgi.framework.BundleActivator):
    """
    Java class 'org.openhab.core.ui.internal.UIActivator'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.osgi.framework.BundleActivator
    
      Constructors:
        * UIActivator()
    
    """
    def __init__(self): ...
    @classmethod
    def getContext(cls) -> org.osgi.framework.BundleContext: ...
    def start(self, bc: org.osgi.framework.BundleContext) -> None: ...
    def stop(self, bc: org.osgi.framework.BundleContext) -> None: ...
