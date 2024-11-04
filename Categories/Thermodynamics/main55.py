import gym
from gym import spaces
import numpy as np

# Define a custom environment for a 1-joint robotic arm
class RoboticArmEnv(gym.Env):
    def __init__(self):
        super(RoboticArmEnv, self).__init__()
        # The joint angle of the arm ranges from -180 to 180 degrees
        self.action_space = spaces.Box(low=-180, high=180, shape=(1,), dtype=np.float32)
        # Observation space is the distance to the target (a single value)
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(1,), dtype=np.float32)
        
        # Target position (fixed for simplicity)
        self.target_position = 90  # Target at 90 degrees
        self.state = None

    def reset(self):
        # Start with a random joint angle
        self.state = np.random.uniform(-180, 180)
        return np.array([self.state])

    def step(self, action):
        # Apply action to the joint angle
        self.state = action[0]
        
        # Calculate the distance to the target
        distance_to_target = abs(self.state - self.target_position)
        
        # Reward: The closer to the target, the higher the reward (negative distance)
        reward = -distance_to_target
        
        # If the distance is small enough, the task is considered "solved"
        done = distance_to_target < 1.0
        
        return np.array([self.state]), reward, done, {}

    def render(self, mode='human'):
        print(f"Joint angle: {self.state} | Target: {self.target_position}")

    def close(self):
        pass

# Define a custom wrapper to scale actions
class ScaleActionWrapper(gym.ActionWrapper):
    def action(self, action):
        # Scale the action from [-1, 1] to [-180, 180]
        scaled_action = action * 180
        return scaled_action

# Initialize the custom environment and wrapper
env = RoboticArmEnv()
env = ScaleActionWrapper(env)

# Run the environment (without RL agent, for optimization purposes)
state = env.reset()
done = False

while not done:
    # Simple "optimization" - randomly try different joint angles until success
    action = np.random.uniform(-1, 1, size=(1,))
    state, reward, done, _ = env.step(action)
    env.render()

env.close()
