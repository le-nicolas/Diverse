import pygame
import numpy as np
import math

# Initialize Pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Leader-Follower with Trajectory Prediction")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Drone class
class Drone:
    def __init__(self, x, y, color, is_leader=False):
        self.x = x
        self.y = y
        self.radius = 10
        self.color = color
        self.speed = 2
        self.is_leader = is_leader
        self.vx = 0  # Leader's velocity in x
        self.vy = 0  # Leader's velocity in y
    
    def move_leader(self, dx, dy):
        self.x += dx
        self.y += dy
        self.vx = dx  # Update velocity in x direction
        self.vy = dy  # Update velocity in y direction
    
    def follow(self, predicted_x, predicted_y, distance_offset):
        # Calculate the direction vector from the follower to the predicted position of the leader
        dx = predicted_x - self.x
        dy = predicted_y - self.y
        dist = math.hypot(dx, dy)
        
        # Normalize the direction and maintain distance
        if dist > distance_offset:
            dx, dy = dx / dist, dy / dist
            self.x += dx * self.speed
            self.y += dy * self.speed
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Function to predict the future position of the leader
def predict_trajectory(leader, time_step):
    # Simple constant velocity prediction for the leader
    predicted_x = leader.x + leader.vx * time_step
    predicted_y = leader.y + leader.vy * time_step
    return predicted_x, predicted_y

# Initialize leader and followers
leader = Drone(x=WIDTH//2, y=HEIGHT//2, color=RED, is_leader=True)
followers = [
    Drone(x=WIDTH//2 - 50, y=HEIGHT//2 - 50, color=BLUE),
    Drone(x=WIDTH//2 - 100, y=HEIGHT//2, color=BLUE)
]

# Simulation parameters
running = True
clock = pygame.time.Clock()
distance_offset = 50  # Distance followers should maintain
time_step = 1         # Prediction time step (1 second into the future)

# Main loop
while running:
    screen.fill(WHITE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Leader movement (controlled by arrow keys)
    dx, dy = 0, 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dx = -leader.speed
    if keys[pygame.K_RIGHT]:
        dx = leader.speed
    if keys[pygame.K_UP]:
        dy = -leader.speed
    if keys[pygame.K_DOWN]:
        dy = leader.speed

    # Move leader
    leader.move_leader(dx, dy)

    # Predict the future position of the leader
    predicted_x, predicted_y = predict_trajectory(leader, time_step)

    # Move followers based on the predicted future position of the leader
    for follower in followers:
        follower.follow(predicted_x, predicted_y, distance_offset)

    # Draw leader and followers
    leader.draw(screen)
    for follower in followers:
        follower.draw(screen)
    
    # Visualize the predicted position (optional)
    pygame.draw.circle(screen, (0, 255, 0), (int(predicted_x), int(predicted_y)), leader.radius, 1)

    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
