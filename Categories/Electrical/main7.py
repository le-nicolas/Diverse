import numpy as np
import trimesh
import matplotlib.pyplot as plt

# Create a simple sphere
sphere = trimesh.primitives.Sphere(radius=1.0, subdivisions=4)

# Analytical sphere properties
print("Sphere Properties:")
print(f"Radius: {sphere.radius}")
print(f"Surface Area: {sphere.area}")
print(f"Volume: {sphere.volume}")

# Voxelize the sphere
voxel_size = 0.1  # Define the voxel resolution
voxelized_sphere = sphere.voxelized(pitch=voxel_size)

# Extract voxel points
voxels = voxelized_sphere.points

# Visualize the analytical sphere
fig = plt.figure(figsize=(12, 6))

# Subplot for the smooth sphere
ax1 = fig.add_subplot(121, projection='3d')
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = sphere.radius * np.cos(u) * np.sin(v)
y = sphere.radius * np.sin(u) * np.sin(v)
z = sphere.radius * np.cos(v)
ax1.plot_surface(x, y, z, color='b', alpha=0.6)
ax1.set_title("Analytical Sphere")
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# Subplot for the voxelized sphere
ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(voxels[:, 0], voxels[:, 1], voxels[:, 2], marker='o', color='r', alpha=0.6)
ax2.set_title("Voxelized Sphere")
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

plt.show()

# Compute properties for the voxelized sphere
voxel_volume = voxelized_sphere.volume
print(f"\nVoxelized Sphere Volume: {voxel_volume} cubic units")
print(f"Number of Voxels: {len(voxels)}")
