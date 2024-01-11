class CAR:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
tesla_model_s = CAR(4,"electric", 5, "250 km/h")

@property
def number_of_wheels(self):
    return self.number_of_wheels

@number_of_wheels.setter
def set_number_of_wheels(self, number):
    self.number_of_wheels = number

print("hi i have a tesla model s car and it has %s ." %tesla_model_s.number_of_wheels," and my car is %s." %tesla_model_s.type_of_tank,"and i have %s seats." %tesla_model_s.seating_capacity,"and it can speed up to %s." %tesla_model_s.maximum_velocity,)
