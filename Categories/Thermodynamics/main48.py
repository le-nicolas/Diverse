import pybullet as p
import pybullet_data

# Set up the physics simulation
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

# Load the 3D plane and piston models
plane = p.loadURDF("plane.urdf")
piston = p.loadURDF("piston.urdf")

# Simulate the environment
for i in range(10000):
    p.stepSimulation()

p.disconnect()

