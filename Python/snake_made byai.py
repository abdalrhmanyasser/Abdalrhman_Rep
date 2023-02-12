import pygame
import random
import time
# Constants for the grid size and cell size
GRID_SIZE = 20
CELL_SIZE = 20

# Constants for the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# The Snake class
class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 1
        self.dy = 0
        self.body = [(self.x, self.y)]

    def move(self):
        # Calculate the new position of the snake's head
        new_x = self.x + self.dx
        new_y = self.y + self.dy

        # Check if the new position is within the grid bounds
        if new_x < 0 or new_x >= GRID_SIZE or new_y < 0 or new_y >= GRID_SIZE:
            return False

        # Update the position of the snake's head
        self.x = new_x
        self.y = new_y
        self.body.insert(0, (self.x, self.y))

        # Check if the snake has eaten an apple
        if self.x == apple.x and self.y == apple.y:
            # Generate a new apple
            apple.x = random.randint(0, GRID_SIZE-1)
            apple.y = random.randint(0, GRID_SIZE-1)
        else:
            # Remove the tail of the snake if it has not eaten an apple
            self.body.pop()

        return True

# The Apple class
class Apple:
    def __init__(self):
        self.x = 0
        self.y = 0

# Initialize the snake and apple
snake = Snake()
apple = Apple()
apple.x = random.randint(0, GRID_SIZE-1)
apple.y = random.randint(0, GRID_SIZE-1)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((GRID_SIZE*CELL_SIZE, GRID_SIZE*CELL_SIZE))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Change the direction of the snake based on the key pressed
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0

    # Update the snake'
    # Draw the grid and the snake
    screen.fill(BLACK)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, rect, 1)
    for x, y in snake.body:
        rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, rect)

    # Draw the apple
    rect = pygame.Rect(apple.x*CELL_SIZE, apple.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, rect)

    # Update the display
    snake.move()
    pygame.display.flip()
    time.sleep(0.1)
# Quit pygame
pygame.quit()
