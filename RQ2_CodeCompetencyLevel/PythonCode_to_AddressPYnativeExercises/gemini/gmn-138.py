class Vehicle:
  def __init__(self, name, mileage, capacity):
    self.name = name
    self.mileage = mileage
    self.capacity = capacity

class Bus(Vehicle):
  pass

# Create a School Bus object
School_bus = Bus("School Volvo", 12, 50)

# Check if School_bus is an instance of Vehicle
is_vehicle_instance = isinstance(School_bus, Vehicle)

# Print the result
print(f"School_bus is an instance of Vehicle: {is_vehicle_instance}")
