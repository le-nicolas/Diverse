import PyMesh as pymesh

# Create a cube
cube = pymesh.generate_box_mesh([0, 0, 0], [1, 1, 1])

# Print basic information about the cube
print("Vertices:\n", cube.vertices)
print("Faces:\n", cube.faces)
print("Number of vertices:", cube.num_vertices)
print("Number of faces:", cube.num_faces)

# Save the mesh to a file
pymesh.save_mesh("cube.obj", cube)

# Load the mesh from a file
loaded_cube = pymesh.load_mesh("cube.obj")

# Perform some operations on the loaded mesh
# Example: Compute the bounding box
bbox_min, bbox_max = loaded_cube.bbox
print("Bounding box min corner:", bbox_min)
print("Bounding box max corner:", bbox_max)

# Example: Apply a transformation (scaling)
transformation = pymesh.form_matrix(
    scale=[2, 2, 2]
)
scaled_cube = pymesh.transform_mesh(loaded_cube, transformation)

# Save the transformed mesh to a file
pymesh.save_mesh("scaled_cube.obj", scaled_cube)
