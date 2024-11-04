# Define the Engine class
class Engine:
    def __init__(self, max_power):
        self.max_power = max_power  # max torque/power the engine can produce
        self.current_power = 0

    def provide_power(self, throttle):
        # Simulate engine power based on throttle input (0-100%)
        self.current_power = throttle * self.max_power / 100
        return self.current_power

# Define the Transmission class
class Transmission:
    def __init__(self, gear_ratios):
        self.gear_ratios = gear_ratios  # List of gear ratios for each gear
        self.current_gear = 0  # Start in neutral

    def shift_gear(self, gear):
        if 0 <= gear < len(self.gear_ratios):
            self.current_gear = gear
        else:
            print("Invalid gear")

    def transmit_power(self, engine_power):
        if self.current_gear == 0:
            return 0  # Neutral, no power transmitted
        return engine_power * self.gear_ratios[self.current_gear - 1]

# Define the Differential class
class Differential:
    def __init__(self, ratio):
        self.ratio = ratio  # Ratio for the differential

    def split_power(self, power):
        # Split power to two wheels considering the differential ratio
        wheel_power = power * self.ratio
        return wheel_power, wheel_power  # Power to left and right wheels

# Define the Drivetrain class
class Drivetrain:
    def __init__(self, transmission, differential):
        self.transmission = transmission
        self.differential = differential

    def deliver_power_to_wheels(self, engine_power):
        # Transmit power through the transmission and then split through the differential
        trans_power = self.transmission.transmit_power(engine_power)
        left_wheel_power, right_wheel_power = self.differential.split_power(trans_power)
        return left_wheel_power, right_wheel_power

# Define the Clutch class
class Clutch:
    def __init__(self):
        self.engaged = False

    def engage(self):
        self.engaged = True

    def disengage(self):
        self.engaged = False

    def transmit_power(self, engine_power):
        if self.engaged:
            return engine_power
        else:
            return 0  # No power if clutch is disengaged

# Main car system
class Car:
    def __init__(self, max_engine_power, gear_ratios, differential_ratio):
        self.engine = Engine(max_engine_power)
        self.transmission = Transmission(gear_ratios)
        self.differential = Differential(differential_ratio)
        self.clutch = Clutch()
        self.drivetrain = Drivetrain(self.transmission, self.differential)

    def drive(self, throttle, gear):
        self.clutch.engage()
        engine_power = self.engine.provide_power(throttle)
        self.transmission.shift_gear(gear)
        transmitted_power = self.clutch.transmit_power(engine_power)
        left_wheel_power, right_wheel_power = self.drivetrain.deliver_power_to_wheels(transmitted_power)
        print(f"Left wheel power: {left_wheel_power} | Right wheel power: {right_wheel_power}")

# Example usage:
car = Car(max_engine_power=200, gear_ratios=[3.5, 2.0, 1.5, 1.0, 0.7], differential_ratio=0.9)
car.drive(throttle=60, gear=3)  # Drive the car with 60% throttle in 3rd gear
