import time
import random

class TrafficLight:
    def __init__(self):
        self.state = "RED"  # Initial state
        self.states = ["GREEN", "YELLOW", "RED"]
        self.state_durations = {"GREEN": 10, "YELLOW": 2, "RED": 8}  # Duration of each state in seconds

    def next_state(self):
        current_index = self.states.index(self.state)
        self.state = self.states[(current_index + 1) % len(self.states)]
        
    def get_state(self):
        return self.state

    def get_state_duration(self):
        return self.state_durations[self.state]


class Car:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time

def simulate_traffic(cars_per_minute, simulation_time_minutes):
    traffic_light = TrafficLight()
    cars = []
    car_id = 0

    for minute in range(simulation_time_minutes):
        # Cars arrive
        for _ in range(cars_per_minute):
            cars.append(Car(arrival_time=minute))
        
        # Traffic light cycles
        for _ in range(60):  # Each minute has 60 seconds
            traffic_light.next_state()
            state = traffic_light.get_state()
            state_duration = traffic_light.get_state_duration()
            
            # Process cars based on traffic light state
            if state == "GREEN":
                cars_processed = min(len(cars), state_duration)
                cars = cars[cars_processed:]  # Remove processed cars
            
            #time.sleep(1)  # Simulate real-time (remove for faster simulation)

    return cars  # Remaining cars that didn't get through

# Parameters
cars_per_minute = 10
simulation_time_minutes = 5

# Run Simulation
remaining_cars = simulate_traffic(cars_per_minute, simulation_time_minutes)
print(f"Remaining cars after {simulation_time_minutes} minutes: {len(remaining_cars)}")
