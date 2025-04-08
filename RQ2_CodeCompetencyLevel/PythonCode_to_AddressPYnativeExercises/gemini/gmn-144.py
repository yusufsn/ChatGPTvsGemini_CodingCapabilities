import json

class Vehicle:
  def __init__(self, name, engine, price):
    self.name = name
    self.engine = engine
    self.price = price

  # Define a method to convert the object to JSON (optional)
  def to_json(self):
    return json.dumps(self.__dict__)

# Create a Vehicle object
vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

# Option 1: Using the `json.dumps()` function directly with the object's dictionary
json_data = json.dumps(vehicle.__dict__)

# Option 2: Using the custom `to_json()` method (if defined)
# json_data = vehicle.to_json()

# Print the JSON data
print(json_data)
