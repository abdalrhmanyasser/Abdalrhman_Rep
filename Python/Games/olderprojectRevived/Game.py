import pygame
import os
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
# initialize pygame
pygame.init()
screen_size = (1920, 1080)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")
 
# clock is used to set a max fps
clock = pygame.time.Clock()
class sprite:
    def __init__(self, _x : int, _y : int, _image : pygame.Surface):
        self.x = _x
        self.y = _y
        self.image = _image
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

player = sprite(500, 500, pygame.image.load(os.path.join("Python", "Games", "olderprojectRevived", "images", "player.png")))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                game_ended  = True
                break        
    
    #clear the screen
    screen.fill(BLACK)
     
    # draw to the screen
    # YOUR CODE HERE
    player.draw()
 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()