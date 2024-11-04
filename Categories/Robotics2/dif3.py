import random
import matplotlib.pyplot as plt

# Parameters
road_length = 10
num_chickens = 10
num_cars = 3
time_steps = 20

# Initialize positions
chickens = [0] * num_chickens  # All chickens start at the beginning of the road
cars = [random.randint(1, road_length - 1) for _ in range(num_cars)]  # Cars are randomly placed on the road

# Track positions over time
chicken_positions_over_time = [[] for _ in range(num_chickens)]
car_positions_over_time = [[] for _ in range(time_steps)]

# Simulation
for t in range(time_steps):
    # Move chickens
    for i in range(num_chickens):
        if chickens[i] < road_length:
            chickens[i] += 1

    # Move cars
    for i in range(num_cars):
        cars[i] = random.randint(1, road_length - 1)  # Cars randomly change positions

    # Check for collisions
    collisions = [i for i in range(num_chickens) if chickens[i] in cars]
    
    # Save positions
    for i in range(num_chickens):
        chicken_positions_over_time[i].append(chickens[i])
    car_positions_over_time[t] = cars[:]

    # Display the road
    road_display = ['_' for _ in range(road_length)]
    for i in range(num_chickens):
        if chickens[i] < road_length:
            road_display[chickens[i]] = 'C' if i not in collisions else 'X'
    for car in cars:
        if road_display[car] == '_':
            road_display[car] = 'A'
    
    # Print road state
    print("Time step:", t)
    print("Road:", ''.join(road_display))
    print("Collisions:", collisions)
    print()

    if len(collisions) > 0:
        break  # Stop the simulation if any collisions occur

# Plot the results
for i in range(num_chickens):
    plt.plot(range(time_steps), chicken_positions_over_time[i], label=f'Chicken {i+1}')
for t in range(time_steps):
    plt.scatter([t]*num_cars, car_positions_over_time[t], color='red', label='Cars' if t == 0 else "")
plt.xlabel('Time step')
plt.ylabel('Position on road')
plt.legend()
plt.show()
