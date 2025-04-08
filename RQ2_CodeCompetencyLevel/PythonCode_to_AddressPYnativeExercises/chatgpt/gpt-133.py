# Parent class Vehicle
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Child class Bus inheriting from Vehicle
class Bus(Vehicle):
    pass

# Creating a Bus object
school_bus = Bus("School Volvo", 180, 12)

# Displaying the attributes of the Bus object
print(f"Vehicle Name: {school_bus.name}")
print(f"Speed: {school_bus.max_speed}")
print(f"Mileage: {school_bus.mileage}")
