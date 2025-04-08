class Vehicle:
    color = "white"  # Class attribute for default color

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    # Property to enforce the color attribute
    @property
    def color(self):
        return self.__color  # Access private attribute

    @color.setter
    def color(self, value):
        raise AttributeError("Color cannot be changed. All vehicles are white.")


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


# Create Vehicle objects (color remains white)
school_bus = Bus("School Volvo", 180, 12)
audi_q5 = Car("Audi Q5", 240, 18)

# Access attributes
print(f"Color: {school_bus.color}, Vehicle name: {school_bus.name}, Speed: {school_bus.max_speed}, Mileage: {school_bus.mileage}")
print(f"Color: 1  {audi_q5.color}, Vehicle name: {audi_q5.name}, Speed: {audi_q5.max_speed}, Mileage: {audi_q5.mileage}")
