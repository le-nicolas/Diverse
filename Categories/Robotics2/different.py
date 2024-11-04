import matplotlib.pyplot as plt

# Define the fibers and their tensile strengths
fibers = ["Jute", "Hemp", "Flax", "Cotton", "Silk", "Wool", "Bamboo"]
tensile_strengths = [300, 550, 800, 400, 600, 200, 500]  # Tensile strengths in MPa

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(fibers, tensile_strengths, color=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f'])

# Add title and labels
plt.title('Tensile Strength of Different Natural Fibers')
plt.xlabel('Fiber Type')
plt.ylabel('Tensile Strength (MPa)')

# Display the chart
plt.show()
