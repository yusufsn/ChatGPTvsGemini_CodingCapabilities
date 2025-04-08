import json

# Define the Vehicle class
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price
    
    # String representation of the Vehicle object for easy printout
    def __repr__(self):
        return f"Vehicle(name={self.name}, engine={self.engine}, price={self.price})"

# JSON data
json_data = '''{
    "name": "Toyota Rav4",
    "engine": "2.5L",
    "price": 32000
}'''

# Convert JSON to dictionary
data = json.loads(json_data)

# Create Vehicle object from the dictionary
vehicleObj = Vehicle(**data)

# Access attributes using dot operator
print(vehicleObj.name)    # Toyota Rav4
print(vehicleObj.engine)  # 2.5L
print(vehicleObj.price)   # 32000
