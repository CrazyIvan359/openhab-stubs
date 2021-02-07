import java.lang


class FirmwareDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.firmware.dto.FirmwareDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * FirmwareDTO(java.lang.String, java.lang.String, java.lang.String, boolean, java.lang.String, java.lang.String, java.lang.String, java.lang.String)
    
      Attributes:
        thingTypeUID (java.lang.String): final field
        vendor (java.lang.String): final field
        model (java.lang.String): final field
        modelRestricted (boolean): final field
        description (java.lang.String): final field
        version (java.lang.String): final field
        changelog (java.lang.String): final field
        prerequisiteVersion (java.lang.String): final field
    
    """
    thingTypeUID: java.lang.String = ...
    vendor: java.lang.String = ...
    model: java.lang.String = ...
    modelRestricted: bool = ...
    description: java.lang.String = ...
    version: java.lang.String = ...
    changelog: java.lang.String = ...
    prerequisiteVersion: java.lang.String = ...
    def __init__(self, thingTypeUID: java.lang.String, vendor: java.lang.String, model: java.lang.String, modelRestricted: bool, description: java.lang.String, version: java.lang.String, prerequisiteVersion: java.lang.String, changelog: java.lang.String): ...

class FirmwareStatusDTO(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.firmware.dto.FirmwareStatusDTO'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * FirmwareStatusDTO(java.lang.String, java.lang.String)
    
      Attributes:
        status (java.lang.String): final field
        updatableVersion (java.lang.String): final field
    
    """
    status: java.lang.String = ...
    updatableVersion: java.lang.String = ...
    def __init__(self, status: java.lang.String, updatableVersion: java.lang.String): ...
