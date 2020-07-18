# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    #the base class
    pass

class FlighVehicle(Vehicle):
    #inherits the class Vehicle
    pass

class Starship(FlighVehicle):
    #inherits the class FlightVehicle
    pass

class GroundVehicle(Vehicle):
    #inherits the class Vehicle
    pass

class Airplane(FlighVehicle):
    #inherits the class FLightVehicle
    pass

class Car(GroundVehicle):
    #inherits the calss GroundVechile
    pass

class Motorcycyle(GroundVehicle):
    # inherits the class GroundVehicle
    pass

