# Parent class Vehicle
class Vehicle:
    # Define a class attribute color with a default value 'White'
    color = "White"
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Child class Bus inheriting from Vehicle
class Bus(Vehicle):
    pass

# Child class Car inheriting from Vehicle
class Car(Vehicle):
    pass

# Creating objects of Bus and Car classes
school_bus = Bus("School Volvo", 180, 12)
audi_q5 = Car("Audi Q5", 240, 18)

# Displaying the attributes of the Bus object
print(f"Color: {school_bus.color}, Vehicle name: {school_bus.name}, Speed: {school_bus.max_speed}, Mileage: {school_bus.mileage}")

# Displaying the attributes of the Car object
print(f"Color: {audi_q5.color}, Vehicle name: {audi_q5.name}, Speed: {audi_q5.max_speed}, Mileage: {audi_q5.mileage}")
