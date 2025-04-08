class Vehicle:
    # Constructor to initialize instance attributes
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed  # max speed of the vehicle
        self.mileage = mileage  # mileage of the vehicle

# Creating an instance of the Vehicle class
my_vehicle = Vehicle(150, 50000)

# Accessing the instance attributes
print("Max Speed:", my_vehicle.max_speed)  # 150
print("Mileage:", my_vehicle.mileage)  # 50000
