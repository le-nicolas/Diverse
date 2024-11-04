#Game Development with Pygame:
#Creating a full-fledged 2D game using the Pygame library.

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple 2D Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player class
class Player:
    def __init__(self):
        self.size = 50
        self.pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (*self.pos, self.size, self.size))

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.pos[0] -= self.speed
        if keys[pygame.K_RIGHT]:
            self.pos[0] += self.speed
        if keys[pygame.K_UP]:
            self.pos[1] -= self.speed
        if keys[pygame.K_DOWN]:
            self.pos[1] += self.speed

# Enemy class
class Enemy:
    def __init__(self):
        self.size = 50
        self.pos = [random.randint(0, SCREEN_WIDTH - self.size), 0]
        self.speed = random.randint(1, 5)

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (*self.pos, self.size, self.size))

    def move(self):
        self.pos[1] += self.speed
        if self.pos[1] > SCREEN_HEIGHT:
            self.pos = [random.randint(0, SCREEN_WIDTH - self.size), 0]

# Collision detection
def detect_collision(player, enemy):
    p_x, p_y = player.pos
    e_x, e_y = enemy.pos
    return (p_x < e_x < p_x + player.size or p_x < e_x + enemy.size < p_x + player.size) and \
           (p_y < e_y < p_y + player.size or p_y < e_y + enemy.size < p_y + player.size)

# Main game loop
def game_loop():
    player = Player()
    enemies = [Enemy() for _ in range(5)]
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        for enemy in enemies:
            enemy.move()
            if detect_collision(player, enemy):
                running = False

        screen.fill(WHITE)
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()
