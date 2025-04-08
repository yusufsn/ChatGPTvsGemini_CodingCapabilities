import json

class Vehicle:
  def __init__(self, name, engine, price):
    self.name = name
    self.engine = engine
    self.price = price

# Define the JSON data
json_data = """{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }"""

# Parse the JSON string
data = json.loads(json_data)

# Create a Vehicle object from the data
vehicleObj = Vehicle(data["name"], data["engine"], data["price"])

# Access attributes using dot notation
print(f"Vehicle Name: {vehicleObj.name}")
print(f"Engine: {vehicleObj.engine}")
print(f"Price: ${vehicleObj.price}")
