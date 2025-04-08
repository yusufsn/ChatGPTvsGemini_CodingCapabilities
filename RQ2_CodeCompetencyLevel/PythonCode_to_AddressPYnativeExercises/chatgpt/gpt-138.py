# Parent class Vehicle
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

# Child class Bus inheriting from Vehicle
class Bus(Vehicle):
    pass

# Create a Bus object
school_bus = Bus("School Volvo", 12, 50)

# Check if School_bus is an instance of Vehicle
print(f"Is the object an instance of Vehicle? {isinstance(school_bus, Vehicle)}")
