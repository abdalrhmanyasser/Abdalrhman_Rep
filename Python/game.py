import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window background color
screen.fill((255, 255, 255))
cell_size = 20

# Set the number of cells in the grid
grid_size = (20, 20)

# Set the width and height of the grid in pixels
grid_width = cell_size * grid_size[0]
grid_height = cell_size * grid_size[1]

# Set the color of the grid lines
grid_color = (0, 0, 0)

# Draw the vertical grid lines
for x in range(cell_size, grid_width, cell_size):
    pygame.draw.line(screen, grid_color, (x, 0), (x, grid_height))

# Draw the horizontal grid lines
for y in range(cell_size, grid_height, cell_size):
    pygame.draw.line(screen, grid_color, (0, y), (grid_width, y))

# Create the Snake class
class Snake:
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 0, 0)
        self.size = cell_size
        self.direction = "right"

    def move(self):
        if self.direction == "right":
            self.position = (self.position[0] + 1, self.position[1])
        elif self.direction == "left":
            self.position = (self.position[0] - 1, self.position[1])
        elif self.direction == "up":
            self.position = (self.position[0], self.position[1] - 1)
        elif self.direction == "down":
            self.position = (self.position[0], self.position[1] + 1)

    def draw(self):
        x, y = self.position
        x *= self.size
        y *= self.size
        pygame.draw.rect(screen, self.color, (x, y, self.size, self.size))

# Create an instance of the Snake class
snake = Snake()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake.direction = "up"
            elif event.key == pygame.K_a:
                snake.direction = "left"
            elif event.key == pygame.K_s:
                snake.direction = "down"
            elif event.key == pygame.K_d:
                snake.direction = "right"

    snake.move()
    screen.fill((255, 255, 255))
    snake.draw()
    pygame.display.update()
# Quit pygame
pygame.quit()
