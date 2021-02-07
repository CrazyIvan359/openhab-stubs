import org.osgi.framework


class CertificateGenerator(org.osgi.framework.BundleActivator):
    """
    Java class 'org.openhab.io.jetty.certificate.internal.CertificateGenerator'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.osgi.framework.BundleActivator
    
      Constructors:
        * CertificateGenerator()
    
    """
    def __init__(self): ...
    def start(self, context: org.osgi.framework.BundleContext) -> None: ...
    def stop(self, context: org.osgi.framework.BundleContext) -> None: ...
