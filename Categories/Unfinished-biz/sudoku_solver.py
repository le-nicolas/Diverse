import pygame
import random

pygame.init()
# Grid size (9x9)
GRID_SIZE = 9

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class SudokuSolver:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in
range(GRID_SIZE)]
        self.empty_cells = []

    def solve(self):
        if not self.find_next_empty():
            return False
        num = random.randint(1, 9)
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] == 0:
                    self.grid[i][j] = num
                    if self.check_grid() and self.solve():
                        return True
                    self.grid[i][j] = 0
        return False

    def find_next_empty(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] == 0:
                    self.empty_cells.append((i, j))
                    return True
        return False

    def check_grid(self):
        for i in range(GRID_SIZE):
            row = [self.grid[i][j] for j in range(GRID_SIZE)]
            col = [self.grid[j][i] for j in range(GRID_SIZE)]
            region_row = (i // 3) * 3
            region_col = (i % 3) * 3
            region = [self.grid[region_row + r][region_col + c]
                      for r in range(3) for c in range(3)]
            if not set(row) == set(range(1, GRID_SIZE + 1)) or \
               not set(col) == set(range(1, GRID_SIZE + 1)) or \
               not set(region) == set(range(1, GRID_SIZE + 1)):
                return False
        return True

    def draw_grid(self):
        window = pygame.display.set_mode((GRID_SIZE * 50, GRID_SIZE *
50))
        pygame.display.set_caption("Sudoku Solver")
        font = pygame.font.Font(None, 36)
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] != 0:
                    text = font.render(str(self.grid[i][j]), True,
BLACK)
                    window.blit(text, (j * 50 + 5, i * 50 + 5))
        pygame.display.flip()

    def main_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw_grid()
        pygame.quit()

if __name__ == "__main__":
    solver = SudokuSolver()
    solver.solve()
    solver.main_loop()

pygame.quit()