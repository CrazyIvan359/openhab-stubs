import java.lang


class Transformation(java.lang.Object):
    """
    Java class 'org.openhab.core.transform.actions.Transformation'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Transformation()
    
    """
    def __init__(self): ...
    @classmethod
    def transform(cls, type: java.lang.String, function: java.lang.String, value: java.lang.String) -> java.lang.String: ...
    @classmethod
    def transformRaw(cls, type: java.lang.String, function: java.lang.String, value: java.lang.String) -> java.lang.String: ...
