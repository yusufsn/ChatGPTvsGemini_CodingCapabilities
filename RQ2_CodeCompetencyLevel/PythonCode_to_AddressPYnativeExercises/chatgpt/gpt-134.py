# Parent class Vehicle
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

# Child class Bus inherits from Vehicle
class Bus(Vehicle):
    # Override seating_capacity method to give a default value of 50
    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a bus is {capacity} passengers"

# Create a Bus object
school_bus = Bus("Bus", 180, 12)

# Call the seating_capacity method (with the default capacity)
print(school_bus.seating_capacity())  # Expected output: The seating capacity of a bus is 50 passengers
