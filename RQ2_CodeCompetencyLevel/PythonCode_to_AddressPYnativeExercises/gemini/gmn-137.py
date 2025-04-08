class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)

# Check object type using the built-in type() function
print(type(School_bus))  # Output: <class '__main__.Bus'>

# Alternatively, use isinstance() for more flexibility
print(isinstance(School_bus, Bus))  # Output: True
