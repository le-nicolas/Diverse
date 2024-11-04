import trimesh
import numpy as np
import matplotlib.pyplot as plt

# Load the 3D model of the cow (update this path with your actual model's path)
mesh = trimesh.load(r'C:\Users\User\Altium\cow.obj')

# Set the voxel resolution (number of voxels along one dimension)
voxel_size = 0.1  # Adjust for more precision or performance

# Voxelize the mesh (convert the cow mesh into voxels)
voxelized = mesh.voxelized(pitch=voxel_size)

# Extract the voxel grid
voxels = voxelized.points

# Compute some properties (e.g., volume)
voxel_volume = voxelized.volume
cow_volume = voxel_volume * len(voxels)
print(f"Voxel Volume: {voxel_volume} cubic units")
print(f"Total Cow Volume (approx): {cow_volume} cubic units")

# Visualize the voxelized cow
def plot_voxels(voxels):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(voxels[:, 0], voxels[:, 1], voxels[:, 2], marker='o', alpha=0.6)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()

# Plot the voxelized cow
plot_voxels(voxels)
