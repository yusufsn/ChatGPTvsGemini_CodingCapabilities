import json

# Define the Vehicle class
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price
    
    # Method to convert object to dictionary
    def to_dict(self):
        return {
            "name": self.name,
            "engine": self.engine,
            "price": self.price
        }

# Create a Vehicle object
vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

# Convert the Vehicle object to JSON format using to_dict()
vehicle_json = json.dumps(vehicle.to_dict(), indent=2)

# Print the JSON formatted string
print(vehicle_json)
