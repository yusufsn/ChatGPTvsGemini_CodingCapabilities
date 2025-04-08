class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, seating_capacity=50):
        super().__init__(name, max_speed, mileage)  # Call parent constructor
        self.seating_capacity = seating_capacity  # Define specific attribute

# Create a Bus object with default seating capacity
school_bus = Bus("School Volvo", 180, 12)

# Print the seating capacity using the inherited method
print(school_bus.seating_capacity())  # Output: The seating capacity of a bus is 50 passengers

# Create a Bus object with a custom seating capacity
city_bus = Bus("City Metro", 100, 15, 70)

# Print the seating capacity using the inherited method
print(city_bus.seating_capacity())  # Output: The seating capacity of a city metro is 70 passengers
