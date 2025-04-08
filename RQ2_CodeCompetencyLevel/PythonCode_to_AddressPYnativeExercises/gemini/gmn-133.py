class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass  # Inherit from Vehicle

# Create a Bus object
school_bus = Bus("School Volvo", 180, 12)

# Access and display the inherited attributes
print("Vehicle Name:", school_bus.name)
print("Speed:", school_bus.max_speed)
print("Mileage:", school_bus.mileage)
