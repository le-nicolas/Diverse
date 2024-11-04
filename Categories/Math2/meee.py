import matplotlib.pyplot as plt

# Data for the chart
benefits = [
    "Increased Efficiency and Productivity",
    "Cost Savings",
    "Improved Safety",
    "Scalability and Flexibility",
    "Quality Control",
    "Competitive Advantage",
    "Enhanced Data Collection and Analysis"
]

values = [95, 90, 85, 88, 92, 87, 89]  # Hypothetical values representing the importance/impact of each benefit

# Creating the bar chart
plt.figure(figsize=(12, 8))
plt.barh(benefits, values, color='skyblue')
plt.xlabel('Impact/Importance (%)')
plt.title('Benefits of Robotics Automation')
plt.xlim(0, 100)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.gca().invert_yaxis()  # Highest values at the top

# Display the chart
plt.show()
