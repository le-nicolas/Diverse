import matplotlib.pyplot as plt
import numpy as np

class FuelInjectionSystem:
    def __init__(self, fuel_tank_capacity=50, injection_rate=0.1):
        self.fuel_tank_capacity = fuel_tank_capacity
        self.fuel_level = fuel_tank_capacity
        self.injection_rate = injection_rate

    def inject_fuel(self, duration):
        fuel_consumed = self.injection_rate * duration
        if fuel_consumed <= self.fuel_level:
            self.fuel_level -= fuel_consumed
            return fuel_consumed
        else:
            fuel_consumed = self.fuel_level
            self.fuel_level = 0
            return fuel_consumed

    def refill_fuel(self, amount):
        if self.fuel_level + amount <= self.fuel_tank_capacity:
            self.fuel_level += amount
        else:
            self.fuel_level = self.fuel_tank_capacity

def visualize_fuel_injection(injection_system, duration):
    fuel_consumed = injection_system.inject_fuel(duration)
    remaining_fuel = injection_system.fuel_level

    # Visualization
    labels = ['Fuel Consumed', 'Remaining Fuel']
    sizes = [fuel_consumed, remaining_fuel]
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)
    
    plt.figure(figsize=(7, 5))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Fuel Injection')
    plt.show()

# Example Usage
injection_system = FuelInjectionSystem(fuel_tank_capacity=60, injection_rate=0.2)
visualize_fuel_injection(injection_system, duration=5)
