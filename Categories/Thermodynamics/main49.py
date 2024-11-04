import gym
from gym import spaces
import numpy as np

class SimpleHeatEngineEnv(gym.Env):
    def __init__(self):
        super(SimpleHeatEngineEnv, self).__init__()
        
        # Action space: increase, decrease, maintain pressure (discrete actions)
        self.action_space = spaces.Discrete(3)
        
        # Observation space: temperature, pressure (continuous state variables)
        self.observation_space = spaces.Box(low=np.array([0, 0]), high=np.array([100, 500]), dtype=np.float32)
        
        # Initialize the state: [temperature, pressure]
        self.state = np.array([20.0, 100.0])  # Start at 20°C and 100 kPa
    
    def step(self, action):
        # Apply action to change the system state
        temp, pressure = self.state
        
        # Apply action effects on pressure (0: decrease, 1: maintain, 2: increase)
        if action == 0:
            pressure -= 5
        elif action == 2:
            pressure += 5
        
        # Update temperature based on pressure changes (simplified relation)
        temp = temp + (pressure - 100) * 0.02  # Increase temp by a factor of pressure change
        
        # Clip the values to stay within observation space limits
        temp = np.clip(temp, 0, 100)
        pressure = np.clip(pressure, 0, 500)
        
        # Update state
        self.state = np.array([temp, pressure])
        
        # Calculate reward (closer to 70°C is better)
        reward = -abs(temp - 70)
        
        # Check if done (if temp or pressure goes too extreme)
        done = bool(temp <= 0 or temp >= 100 or pressure <= 0 or pressure >= 500)
        
        return self.state, reward, done, {}
    
    def reset(self):
        # Reset state to initial conditions
        self.state = np.array([20.0, 100.0])
        return self.state

    def render(self, mode='human'):
        print(f"Current state: Temperature = {self.state[0]}°C, Pressure = {self.state[1]} kPa")


# Test the environment
env = SimpleHeatEngineEnv()
state = env.reset()

for _ in range(10):
    action = env.action_space.sample()  # Random action
    state, reward, done, _ = env.step(action)
    env.render()  # Output the current state
    if done:
        break
