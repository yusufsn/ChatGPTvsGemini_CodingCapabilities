class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def __init__(self, name, mileage, capacity=50):  # Set default capacity for Bus
        super().__init__(name, mileage, capacity)

    def fare(self):
        # Call parent class fare method to get base fare
        base_fare = super().fare()
        # Add 10% maintenance charge for Bus
        maintenance_charge = base_fare * 0.1
        total_fare = base_fare + maintenance_charge
        return total_fare


School_bus = Bus("School Volvo", 12)
print("Total Bus fare is:", School_bus.fare())  # Output: Total Bus fare is: 5500.0
