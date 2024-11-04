import simpy
import matplotlib.pyplot as plt

# Constants
INITIAL_TEMP = 0  # Initial room temperature in degrees Fahrenheit
MELTING_POINT = 32  # Temperature at which the ice cube starts melting (32°F or 0°C)
HEAT_INCREMENT = 1  # Temperature increment per hour
SIM_DURATION = 40  # Total simulation time in hours

class Room:
    def __init__(self, env):
        self.env = env
        self.temperature = INITIAL_TEMP
        self.temperatures = []  # To store temperature at each time step
        self.time_steps = []  # To store corresponding time steps
    
    def heat_room(self):
        """
        This process gradually heats the room, increasing the temperature by 1 degree per hour.
        """
        while True:
            yield self.env.timeout(1)  # Wait for 1 hour
            self.temperature += HEAT_INCREMENT
            self.temperatures.append(self.temperature)  # Log temperature
            self.time_steps.append(self.env.now)  # Log time step
            print(f'Hour {int(self.env.now)}: Room temperature is {self.temperature}°F')

class IceCube:
    def __init__(self, env, room):
        self.env = env
        self.room = room
        self.melted = False

    def monitor_ice(self):
        """
        This process monitors the temperature and determines when the ice cube starts melting.
        """
        while not self.melted:
            if self.room.temperature >= MELTING_POINT:
                self.melted = True
                print(f'Hour {int(self.env.now)}: The ice cube begins to melt.')
            yield self.env.timeout(1)  # Check again in 1 hour

# Plotting function using Matplotlib
def generate_report(room):
    plt.figure(figsize=(10, 6))
    plt.plot(room.time_steps, room.temperatures, label='Room Temperature', color='blue')
    plt.axhline(y=MELTING_POINT, color='red', linestyle='--', label='Melting Point (32°F)')
    plt.xlabel('Time (hours)')
    plt.ylabel('Temperature (°F)')
    plt.title('Room Temperature Over Time and Ice Melting Point')
    plt.legend()
    plt.grid(True)
    plt.show()

# Simulation setup
env = simpy.Environment()

# Create the room and ice cube objects
room = Room(env)
ice_cube = IceCube(env, room)

# Start the processes
env.process(room.heat_room())
env.process(ice_cube.monitor_ice())

# Run the simulation
env.run(until=SIM_DURATION)

# After simulation, generate the report with Matplotlib
generate_report(room)
