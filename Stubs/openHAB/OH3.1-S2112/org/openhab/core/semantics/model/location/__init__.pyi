import java.lang
import java.util.stream
import org.openhab.core.semantics.model
import typing


class Indoor(org.openhab.core.semantics.model.Location):
    """
    Java class 'org.openhab.core.semantics.model.location.Indoor'
    
        Interfaces:
            org.openhab.core.semantics.model.Location
    
    """

class Locations(java.lang.Object):
    """
    Java class 'org.openhab.core.semantics.model.location.Locations'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Locations()
    
    """
    def __init__(self): ...
    @classmethod
    def stream(cls) -> java.util.stream.Stream[typing.Type[org.openhab.core.semantics.model.Location]]: ...

class Outdoor(org.openhab.core.semantics.model.Location):
    """
    Java class 'org.openhab.core.semantics.model.location.Outdoor'
    
        Interfaces:
            org.openhab.core.semantics.model.Location
    
    """

class Apartment(Indoor):
    """
    Java class 'org.openhab.core.semantics.model.location.Apartment'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Indoor
    
    """

class Building(Indoor):
    """
    Java class 'org.openhab.core.semantics.model.location.Building'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Indoor
    
    """

class Carport(Outdoor):
    """
    Java class 'org.openhab.core.semantics.model.location.Carport'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Outdoor
    
    """

class Corridor(Indoor):
    """
    Java class 'org.openhab.core.semantics.model.location.Corridor'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Indoor
    
    """

class Driveway(Outdoor):
    """
    Java class 'org.openhab.core.semantics.model.location.Driveway'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Outdoor
    
    """

class Floor(Indoor):
    """
    Java class 'org.openhab.core.semantics.model.location.Floor'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Indoor
    
    """

class Garden(Outdoor):
    """
    Java class 'org.openhab.core.semantics.model.location.Garden'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Outdoor
    
    """

class Patio(Outdoor):
    """
    Java class 'org.openhab.core.semantics.model.location.Patio'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Outdoor
    
    """

class Porch(Outdoor):
    """
    Java class 'org.openhab.core.semantics.model.location.Porch'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Outdoor
    
    """

class Room(Indoor):
    """
    Java class 'org.openhab.core.semantics.model.location.Room'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Indoor
    
    """

class Terrace(Outdoor):
    """
    Java class 'org.openhab.core.semantics.model.location.Terrace'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Outdoor
    
    """

class Attic(Floor):
    """
    Java class 'org.openhab.core.semantics.model.location.Attic'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Floor
    
    """

class Basement(Floor):
    """
    Java class 'org.openhab.core.semantics.model.location.Basement'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Floor
    
    """

class Bathroom(Room):
    """
    Java class 'org.openhab.core.semantics.model.location.Bathroom'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Room
    
    """

class Bedroom(Room):
    """
    Java class 'org.openhab.core.semantics.model.location.Bedroom'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Room
    
    """

class BoilerRoom(Room):
    """
    Java class 'org.openhab.core.semantics.model.location.BoilerRoom'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Room
    
    """

class Cellar(Room):
    """
    Java class 'org.openhab.core.semantics.model.location.Cellar'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Room
    
    """

class DiningRoom(Room):
    """
    Java class 'org.openhab.core.semantics.model.location.DiningRoom'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Room
    
    """

class Entry(Room):
    """
    Java class 'org.openhab.core.semantics.model.location.Entry'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Room
    
    """

class FamilyRoom(Room):
    """
    Java class 'org.openhab.core.semantics.model.location.FamilyRoom'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Room
    
    """

class FirstFloor(Floor):
    """
    Java class 'org.openhab.core.semantics.model.location.FirstFloor'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Floor
    
    """

class Garage(Building):
    """
    Java class 'org.openhab.core.semantics.model.location.Garage'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Building
    
    """

class GroundFloor(Floor):
    """
    Java class 'org.openhab.core.semantics.model.location.GroundFloor'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Floor
    
    """

class GuestRoom(Room):
    """
    Java class 'org.openhab.core.semantics.model.location.GuestRoom'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Room
    
    """

class House(Building):
    """
    Java class 'org.openhab.core.semantics.model.location.House'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Building
    
    """

class Kitchen(Room):
    """
    Java class 'org.openhab.core.semantics.model.location.Kitchen'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Room
    
    """

class LaundryRoom(Room):
    """
    Java class 'org.openhab.core.semantics.model.location.LaundryRoom'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Room
    
    """

class LivingRoom(Room):
    """
    Java class 'org.openhab.core.semantics.model.location.LivingRoom'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Room
    
    """

class Office(Room):
    """
    Java class 'org.openhab.core.semantics.model.location.Office'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Room
    
    """

class SecondFloor(Floor):
    """
    Java class 'org.openhab.core.semantics.model.location.SecondFloor'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Floor
    
    """

class Shed(Building):
    """
    Java class 'org.openhab.core.semantics.model.location.Shed'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Building
    
    """

class SummerHouse(Building):
    """
    Java class 'org.openhab.core.semantics.model.location.SummerHouse'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Building
    
    """

class ThirdFloor(Floor):
    """
    Java class 'org.openhab.core.semantics.model.location.ThirdFloor'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Floor
    
    """

class Veranda(Room):
    """
    Java class 'org.openhab.core.semantics.model.location.Veranda'
    
        Interfaces:
            org.openhab.core.semantics.model.location.Room
    
    """
