class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# Create an object of the Vehicle class
car = Vehicle(240, 18)

# Access the object's attributes
print("Max Speed:", car.max_speed)
print("Mileage:", car.mileage)
