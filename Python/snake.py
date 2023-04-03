# Import and initialize the pygame library
from math import floor
import random as rand
import pygame
import time
pygame.init()
width = 500
height = 500
delay = 0.2
scale = 25
font = pygame.font.Font('freesansbold.ttf', 32)
play = False
dead_ = False
avail = []
for i in range(int(width/scale)-1):
    for j in range(int(height/scale)-1):
        avail.append((i, j))
foods = []
imagesB = [
    pygame.transform.scale(pygame.image.load("Python\\LD_snakeB.png"), (scale, scale)),
    pygame.transform.scale(pygame.image.load("Python\\DU_snakeB.png"), (scale, scale)),
    pygame.transform.scale(pygame.image.load("Python\\LU_snakeB.png"), (scale, scale)),
    pygame.transform.scale(pygame.image.load("Python\\RD_snakeB.png"), (scale, scale)),
    pygame.transform.scale(pygame.image.load("Python\\RL_snakeB.png"), (scale, scale)),
    pygame.transform.scale(pygame.image.load("Python\\RU_snakeB.png"), (scale, scale)),
]
imagesG = [
    pygame.transform.scale(pygame.image.load("Python\\LD_snakeG.png"), (scale, scale)),
    pygame.transform.scale(pygame.image.load("Python\\DU_snakeG.png"), (scale, scale)),
    pygame.transform.scale(pygame.image.load("Python\\LU_snakeG.png"), (scale, scale)),
    pygame.transform.scale(pygame.image.load("Python\\RD_snakeG.png"), (scale, scale)),
    pygame.transform.scale(pygame.image.load("Python\\RL_snakeG.png"), (scale, scale)),
    pygame.transform.scale(pygame.image.load("Python\\RU_snakeG.png"), (scale, scale)),
]
images = [imagesG, imagesB]
# Set up the drawing window
screen = pygame.display.set_mode([width, height])
     
def dead():
    dead_ = True
    play = False
    print(dead_, play)
    print("Ha YoU DiEd")
    quit()
pygame.display.set_caption('Snake Multiplayer 3000')
class snake:
    def __init__(self, speed, id, x, y, dirx, diry, color):
        self._speed = speed
        self._id = id
        self._x = x
        self._y = y
        self._dirx = dirx
        self._diry = diry
        self.length = 1
        self.is_move = False
        self.pre = [(self._x, self._y, (self._dirx, self._diry))]
        self._color = color
        # create a text surface object,
        # on which text is drawn on it.
        self.text = font.render("Score P"+str(self._id)+" : ", True, (0, 0, 0))
    def go_up(self):
        if self._dirx != 0 and not self.is_move:
            self._dirx = 0
            self._diry = -1
            self.is_move = True
    def go_down(self):
        if self._dirx != 0 and not self.is_move:
            self._dirx = 0
            self._diry = 1
            self.is_move = True
    def go_right(self):
        if self._diry != 0 and not self.is_move:
            self._dirx = 1
            self._diry = 0
            self.is_move = True
    def go_left(self):
        if self._diry != 0 and not self.is_move:
            self._dirx = -1
            self._diry = 0
            self.is_move = True
    def move(self):
        self._x += self._dirx
        self._y += self._diry
        temp_list = []
        for i in range(2):
            currSnake = eval("snake"+str(i+1)+".pre")
            for i in range((self._id == i), len(currSnake)):
                temp_list.append((currSnake[i][0], currSnake[i][1]))
            if (self._x, self._y) in temp_list:
                dead()
        if not len(self.pre) < self.length:
            self.pre.pop(len(self.pre)-1)
        self.pre.insert(0, (self._x, self._y, (self._dirx, self._diry)))
    def draw(self):
        for i in range(len(self.pre)):
            if i-1 >= 0:
                if self.pre[i][2][0] == 0 and self.pre[i][0] == self.pre[i-1][0]:
                    screen.blit(images[self._id-1][1], (self.pre[i][0]*scale, self.pre[i][1]*scale))
                elif self.pre[i][2][1] == 0 and self.pre[i][1] == self.pre[i-1][1]:
                    screen.blit(images[self._id-1][4], (self.pre[i][0]*scale, self.pre[i][1]*scale))
                #up right
                elif (self.pre[i][2][1] == -1 and self.pre[i-1][2][0] == 1) or (self.pre[i][2][0] == -1 and self.pre[i-1][2][1] == 1):
                    screen.blit(images[self._id-1][3], (self.pre[i][0]*scale, self.pre[i][1]*scale))
                #down left
                elif (self.pre[i][2][1] == 1 and self.pre[i-1][2][0] == -1) or (self.pre[i][2][0] == 1 and self.pre[i-1][2][1] == -1):
                    screen.blit(images[self._id-1][2], (self.pre[i][0]*scale, self.pre[i][1]*scale))
                #up left
                elif (self.pre[i][2][1] == -1 and self.pre[i-1][2][0] == -1) or (self.pre[i][2][0] == 1 and self.pre[i-1][2][1] == 1):
                    screen.blit(images[self._id-1][0], (self.pre[i][0]*scale, self.pre[i][1]*scale))
                #down right
                elif (self.pre[i][2][1] == 1 and self.pre[i-1][2][0] == 1) or (self.pre[i][2][0] == -1 and self.pre[i-1][2][1] == -1):
                    screen.blit(images[self._id-1][5], (self.pre[i][0]*scale, self.pre[i][1]*scale))
            elif i == 0:
                if self.pre[0][2][0] == 1 or self.pre[0][2][0] == -1:
                    screen.blit(images[self._id-1][4], (self.pre[i][0]*scale, self.pre[i][1]*scale))
                elif self.pre[0][2][1] == 1 or self.pre[0][2][1] == -1:
                    screen.blit(images[self._id-1][1], (self.pre[i][0]*scale, self.pre[i][1]*scale))
                        
    def grow(self):
        self.text = font.render("Score P"+str(self._id)+" : " +str(len(self.pre)), True, self._color)
        for i in foods:
            if self._x == i.x and self._y == i.y:    
                self.length+=1
                i.redo()
           
    
class Food():
    def __init__(self):
        self.x = rand.randint(0, width/scale-1)
        self.y = rand.randint(0, height/scale-1)
    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (self.x*scale+floor(scale/2), self.y*scale+floor(scale/2)), scale/2)
    def redo(self):
        if (width/scale)*(height/scale)-( len(snake1.pre) + len(snake2.pre)):
            # thinking of making a difference of lists on pre and all slots to check for free places rather than doing random
            taken = []
            for i in snake1.pre:
                taken.append((i[0], i[1]))
            for i in snake2.pre:
                taken.append((i[0], i[1]))
            new_avail = set(avail)-set(taken)
            new_choice = rand.choice(list(new_avail))
            self.x = new_choice[0]
            self.y = new_choice[1]

snake2 = snake(1, 1, floor((width/4)*3/scale), floor(height/2/scale), 1, 0, (0, 255, 0))
snake1 = snake(2, 2, floor((width/4)*2/scale), floor(height/2/scale), -1, 0, (0, 0, 255))

 
 

for i in range(2):
    foods.append(Food())
snake1.grow()
snake2.grow()

# create a rectangular object for the
# text surface object
textRect1 = snake1.text.get_rect()
textRect2 = snake2.text.get_rect()
textRect1.topleft = (10, 10)
textRect2.topright = (width-10, 10)
# Run until the user asks to quit
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not play:
                play = True
            if event.key == pygame.K_w:
                snake1.go_up()
            if event.key == pygame.K_s:
                snake1.go_down()
            if event.key == pygame.K_a:
                snake1.go_left()
            if event.key == pygame.K_d:
                snake1.go_right()
            if event.key == pygame.K_UP:
                snake2.go_up()
            if event.key == pygame.K_DOWN:
               snake2.go_down()
            if event.key == pygame.K_LEFT:
                snake2.go_left()
            if event.key == pygame.K_RIGHT:
             snake2.go_right()
    # Fill the background with white
    screen.fill((255, 255, 255))
    
    if play:
        snake1.grow()
        snake2.grow()
        snake1.move()
        snake2.move()
        snake1.is_move = False
        snake2.is_move = False
        

        for i in foods:
            i.draw()
        snake1.draw()
        snake2.draw()
        if play:
            screen.blit(snake1.text, textRect1)
            screen.blit(snake2.text, textRect2)
        else:
            snake1.text = font.render("Score P"+str(snake1._id)+" : "+str(len(snake1.pre)), True, (0, 255, 0))
            snake2.text = font.render("Score P"+str(snake2._id)+" : "+str(len(snake2.pre)), True, (0, 0, 255))
        # Flip the display
    pygame.display.flip()
    time.sleep(delay)

# Done! Time to quit.
pygame.quit()
input("Press anything to quit")
