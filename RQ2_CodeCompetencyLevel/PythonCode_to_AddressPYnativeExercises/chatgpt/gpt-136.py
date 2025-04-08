# Parent class Vehicle
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    
    # Base fare calculation method
    def fare(self):
        return self.capacity * 100

# Child class Bus inheriting from Vehicle
class Bus(Vehicle):
    # Overriding the fare method to include maintenance charge for Bus
    def fare(self):
        total_fare = super().fare()  # Call the parent class fare method
        maintenance_charge = total_fare * 0.10  # 10% of the total fare
        return total_fare + maintenance_charge

# Create a Bus object
school_bus = Bus("School Volvo", 12, 50)

# Print the total fare for the bus
print("Total Bus fare is:", school_bus.fare())  # Expected output: 5500.0
