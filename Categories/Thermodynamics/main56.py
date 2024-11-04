import pybullet as p
import pybullet_data
import time
import numpy as np

# Initialize simulation
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Load PyBullet data (e.g., URDFs)

# Load environment and gravity setup
p.setGravity(0, 0, -9.81)
planeId = p.loadURDF("plane.urdf")
p.setRealTimeSimulation(1)

# Load a simple robot arm (KUKA robot) and objects
robotId = p.loadURDF("kuka_iiwa/model.urdf", [0, 0, 0], useFixedBase=True)
cubeId = p.loadURDF("cube.urdf", [0.5, 0, 0.5])

# Camera view and lighting setup
width, height, fov = 640, 480, 60
near, far = 0.1, 100
camera_position = [1, 1, 1]
target_position = [0, 0, 0.5]
camera_up = [0, 0, 1]

# Configure PID control for one joint
jointIndex = 2
targetPosition = np.pi / 4
maxForce = 500
p.setJointMotorControl2(robotId, jointIndex, controlMode=p.POSITION_CONTROL, 
                        targetPosition=targetPosition, force=maxForce)

# Set up physics simulation
p.setTimeStep(1 / 240)
p.setRealTimeSimulation(0)

# Simulate and control the robot
for step in range(10000):
    # Step the simulation forward
    p.stepSimulation()
    
    # Get camera images and display them
    view_matrix = p.computeViewMatrix(camera_position, target_position, camera_up)
    proj_matrix = p.computeProjectionMatrixFOV(fov, width / height, near, far)
    images = p.getCameraImage(width, height, view_matrix, proj_matrix)
    
    # For fun, move cube with a small velocity after some time
    if step > 500 and step < 1500:
        p.resetBaseVelocity(cubeId, linearVelocity=[0, 0, -0.1])
    
    # Artificial delay to simulate real-time movement
    time.sleep(1/240)
    
    # Get robot's joint states for analysis or further control
    joint_states = p.getJointStates(robotId, range(p.getNumJoints(robotId)))
    joint_positions = [state[0] for state in joint_states]  # Extract joint angles
    
    # Optional: Add any condition to stop or adjust the simulation
    if step == 5000:
        p.setJointMotorControl2(robotId, jointIndex, controlMode=p.POSITION_CONTROL, 
                                targetPosition=-np.pi / 4, force=maxForce)

# Disconnect simulation
p.disconnect()
