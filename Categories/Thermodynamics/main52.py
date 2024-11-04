import simpy
import random
import matplotlib.pyplot as plt

# Constants
INITIAL_TEMP = 300  # Initial steam temperature in K
INITIAL_PRESSURE = 1000  # Initial pressure in kPa
BOILING_POINT = 373  # Boiling point of water in K
RANDOM_FAILURE_PROBABILITY = 0.1  # 10% chance of component failure

SIM_DURATION = 200  # Total simulation time in hours
time_data, temp_data, pressure_data = [], [], []  # Data for visualization

# 1. Object-oriented approach - Class for Power Plant
class PowerPlant:
    def __init__(self, env):
        self.env = env
        self.temperature = INITIAL_TEMP
        self.pressure = INITIAL_PRESSURE
        self.resource = simpy.Resource(env, capacity=1)  # Water/Steam as a resource
    
    def monitor_system(self):
        """Monitor temperature and pressure over time"""
        while True:
            time_data.append(self.env.now)
            temp_data.append(self.temperature)
            pressure_data.append(self.pressure)
            yield self.env.timeout(1)
    
    def adjust_parameters(self):
        """Adjust temperature and pressure based on system behavior"""
        while True:
            self.temperature = max(self.temperature - random.uniform(1, 5), BOILING_POINT)
            self.pressure = max(self.pressure - random.uniform(5, 20), 0)
            yield self.env.timeout(1)

# 2. Boiler Class (Modularity)
class Boiler:
    def __init__(self, env, plant):
        self.env = env
        self.plant = plant
    
    def heat_water(self):
        """Simulate the boiler heating water"""
        while True:
            with self.plant.resource.request() as request:
                yield request
                self.plant.temperature = min(self.plant.temperature + random.uniform(5, 15), 800)
                yield self.env.timeout(1)

# 3. Turbine Class (Resource Handling + Random Failure)
class Turbine:
    def __init__(self, env, plant):
        self.env = env
        self.plant = plant
    
    def generate_power(self):
        """Simulate power generation with a chance of failure"""
        while True:
            with self.plant.resource.request() as request:
                yield request
                if random.random() < RANDOM_FAILURE_PROBABILITY:
                    print(f'Hour {self.env.now}: Turbine failure!')
                    self.plant.temperature -= 50  # Cool down after failure
                    yield self.env.timeout(5)  # Time to repair
                else:
                    self.plant.pressure -= 50  # Pressure drop in the turbine
                yield self.env.timeout(1)

# 4. Condenser Class (Delays)
class Condenser:
    def __init__(self, env, plant):
        self.env = env
        self.plant = plant
    
    def cool_steam(self):
        """Simulate steam cooling in the condenser"""
        while True:
            with self.plant.resource.request() as request:
                yield request
                self.plant.temperature = max(self.plant.temperature - random.uniform(10, 20), BOILING_POINT)
                self.plant.pressure = max(self.plant.pressure - random.uniform(20, 40), 0)
                yield self.env.timeout(1)

# 5. Pump Class (Efficiency + Optimization)
class Pump:
    def __init__(self, env, plant, power):
        self.env = env
        self.plant = plant
        self.power = power
    
    def pump_water(self):
        """Simulate water pumping with optimized power usage"""
        while True:
            with self.plant.resource.request() as request:
                yield request
                self.plant.pressure += random.uniform(10, 30) * (self.power / 1000)
                yield self.env.timeout(1)

# 6. Matplotlib Visualization
def visualize():
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(time_data, temp_data, label="Temperature (K)", color="blue")
    plt.axhline(y=BOILING_POINT, color="red", linestyle="--", label="Boiling Point (373K)")
    plt.xlabel("Time (hours)")
    plt.ylabel("Temperature (K)")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(time_data, pressure_data, label="Pressure (kPa)", color="green")
    plt.xlabel("Time (hours)")
    plt.ylabel("Pressure (kPa)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# 7. Reporting - Generate final report
def generate_report():
    print("\nSimulation Report:")
    print(f"Final Temperature: {temp_data[-1]} K")
    print(f"Final Pressure: {pressure_data[-1]} kPa")

# 8. Real-world Behaviors & Randomness
env = simpy.Environment()
plant = PowerPlant(env)

boiler = Boiler(env, plant)
turbine = Turbine(env, plant)
condenser = Condenser(env, plant)
pump = Pump(env, plant, power=0.5)  # 0.5 kW pump

env.process(plant.monitor_system())
env.process(plant.adjust_parameters())
env.process(boiler.heat_water())
env.process(turbine.generate_power())
env.process(condenser.cool_steam())
env.process(pump.pump_water())

# 9. Run Simulation
env.run(until=SIM_DURATION)

# 10. Visualization and Reporting
visualize()
generate_report()
