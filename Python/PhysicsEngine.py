import colorsys
import numpy
import pygame as pg
import time
import random
delay = 1/60
timeStoped = False
gravity = 0.381
dragCoifecient = 0.2
pg.init()
clock = pg.time.Clock()

objects = {"points" :[], "springs" :[], "circleSolids" : [], "SquareSolids" : []}

class Spring():
    def __init__(self, _point1 : int, _point2 : int, _distance, _strength : int):
        self.point1 = _point1
        self.point2 = _point2
        self.distance = _distance
        self.strength = _strength
        self.point1Slider = objects["points"][self.point1].IsSlider
        self.point2Slider = objects["points"][self.point2].IsSlider
        objects["points"][self.point1].relations.append(self)
        objects["points"][self.point2].relations.append(self)
    
    def draw(self):
        pg.draw.line(canvas, (0, 0, 0), (objects["points"][self.point1].x, objects["points"][self.point1].y), (objects["points"][self.point2].x, objects["points"][self.point2].y), 1)
      
    def calculateForce(self):
        Force = -self.strength*(self.distance - dist(objects["points"][self.point1].x, objects["points"][self.point1].y, objects["points"][self.point2].x, objects["points"][self.point2].y))
        return Force
    def applyForce(self):
        Force = self.calculateForce()
        diffX = objects["points"][self.point2].x-objects["points"][self.point1].x
        diffY = objects["points"][self.point2].y-objects["points"][self.point1].y
        if self.point1Slider:
            objects["points"][self.point1].applyForceX((diffX/abs(diffX))*Force*(numpy.cos(numpy.arctan(abs(diffY)/abs(diffX)))))
            objects["points"][self.point1].applyForceY((diffY/abs(diffY))*Force*(numpy.sin(numpy.arctan(abs(diffY)/abs(diffX)))))
        if self.point2Slider:
            objects["points"][self.point2].applyForceX((diffX/abs(diffX))*Force*(numpy.cos(numpy.arctan(abs(diffY)/abs(diffX)))))
            objects["points"][self.point2].applyForceY((diffY/abs(diffY))*Force*(numpy.sin(numpy.arctan(abs(diffY)/abs(diffX)))))

class Point():
    def __init__(self, _x, _y, _color, _IsSlider, _mass : int):
        self.x = _x
        self.y = _y
        self.color = _color
        self.IsSlider = _IsSlider
        self.Mass = _mass
        self.ax = 0
        self.ay = 0
        self.vx = 0
        self.vy = 0
        self.relations = []
    def applyForceX(self, Force):
        self.ax += Force/self.Mass
    def applyForceY(self, Force):
        self.ay += Force/self.Mass
    def draw(self):
        pg.draw.circle(canvas, self.color, (self.x, self.y), 8)
    def move(self):
        self.vx+=self.ax
        self.vy+=self.ay
        self.x+=self.vx
        self.y+=self.vy
        self.ax = 0
        self.ay = 0
    def drag(self):
        print(self.vx, self.vy)
        if self.vx != 0:
            self.applyForceX(-1*(self.vx/abs(self.vx))*dragCoifecient*((self.vx**2)/2))
        if self.vy != 0:
            self.applyForceY(-1*(self.vy/abs(self.vy))*dragCoifecient*((self.vy**2)/2))
    
# CREATING CANVAS
canvas = pg.display.set_mode((0, 0), pg.FULLSCREEN)

# TITLE OF CANVAS
pg.display.set_caption("Physcis Engine 1.0")
exit = False

font = pg.font.Font('freesansbold.ttf', 32)
def createRandomColor(rand : bool, inputC : tuple = ()) -> tuple[int, int, int]:
    #input
    if rand:
        (h, s, v) = (random.randrange(0, 360), random.randrange(0, 100), random.randrange(0, 100))
    else:
        (h, s, v) = inputC
    #normalize
    (h, s, v) = (h / 360, s / 100, v / 100)
    #convert to RGB
    (r, g, b) = colorsys.hsv_to_rgb(h, s, v)
    #expand RGB range
    (r, g, b) = (int(r * 255), int(g * 255), int(b * 255))
    return((r, g, b))

def placePoint(IsSlider : bool) -> None:
    if IsSlider: mass = int(getInput(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]))
    else: mass = 0
    objects["points"].append(Point(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1], (createRandomColor(True)), IsSlider, mass))

def getInput(x : int, y : int) -> int:
    user_text = ''
    
    # create rectangle
    input_rect = pg.Rect(x, y, 140, 32)

    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color = (133, 133, 133)

    stop = True
    while stop:
        for event in pg.event.get():

        # if user types QUIT then the screen will close
            if event.type == pg.QUIT:
                stop = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return 100
                # Check for backspace
                if event.key == pg.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                if event.key == pg.K_RETURN:
                    return user_text
                # Unicode standard is used for string
                # formation
                else:
                    if event.unicode.isnumeric():
                        user_text += event.unicode
        
        # it will set background color of screen
        canvas.fill((255, 255, 255))
        simulateEverything()
        drawEverything()
            
        # draw rectangle and argument passed which should
        # be on screen
        pg.draw.rect(canvas, color, input_rect)

        text_surface = font.render(user_text, True, (255, 255, 255))
        
        # render at position stated in arguments
        canvas.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width()+10)
        
        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pg.display.flip()  

def dist(x1 : int, y1 : int, x2 : int, y2 : int) -> float:
    return numpy.sqrt((x2 - x1)**2 + (y2 - y1)**2)
def applyGravity():
    for point in objects["points"]:
        if point.IsSlider:
            point.applyForceY(point.Mass * gravity)
gravityEnable = False
def simulateEverything():
    if not timeStoped:
        canvas.blit(stopImg, (width-100,10))
        for spring in objects["springs"]:
            spring.applyForce()
        for point in objects["points"]:
            if point.IsSlider:
                point.move()
            if gravityEnable:
                applyGravity()
                point.drag()
    else:
        canvas.blit(startImg, (width-100,10))

def drawEverything():
    for spring in objects["springs"]:
        spring.draw()
    for point in objects["points"]:
        point.draw()

def selectPoint(text : str):
    stop = True
    while stop:
        minDist = 99999999
        closestPoint = 0
        for point in range(len(objects["points"])):
            distance = (dist(objects["points"][point].x, objects["points"][point].y, pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]))
            if distance < minDist:
                minDist = distance
                closestPoint = point
        for event in pg.event.get():
            if event.type == pg.QUIT:
                stop = False
                exit = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return -1
                if event.key == pg.K_RETURN:
                    return closestPoint
        canvas.fill((255, 255, 255))
        simulateEverything()
        drawEverything()
        pg.draw.circle(canvas, (255, 0, 0), (objects["points"][closestPoint].x, objects["points"][closestPoint].y), 10, 2)
        textSurface = font.render(text, True, (0, 0, 0))
        canvas.blit(textSurface, (objects["points"][closestPoint].x, objects["points"][closestPoint].y))
        pg.display.flip()
        clock.tick(60)
        
width, height = pg.display.get_window_size()

stopImg = pg.image.load('Python\\icons8-pause-button-64.png')
startImg = pg.image.load('Python\\icons8-circled-play-64.png')
while not exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                exit = True
            if event.key == pg.K_p:
                placePoint(False)
            if event.key == pg.K_o:
                placePoint(True)
            if event.key == pg.K_d:
                point = selectPoint("Delete This Point")
                if point != -1:
                    for i in objects["points"][point].relations:
                        objects["springs"].remove(i)
                    del objects["points"][point]
            if event.key == pg.K_SPACE:
                timeStoped = not timeStoped
            if event.key == pg.K_g:
                gravityEnable = not gravityEnable
            if event.key == pg.K_s:
                pointChosen1 = selectPoint("p1")
                if pointChosen1 != -1:
                    pointChosen2 = None
                    stop = True
                    while stop:
                        pointChosen2 = selectPoint("p2")
                        if pointChosen2 != pointChosen1:
                            stop = False
                    Strength = int(getInput(10, 10))
                    objects["springs"].append(Spring(pointChosen1, pointChosen2, dist(objects["points"][pointChosen1].x, objects["points"][pointChosen1].y, objects["points"][pointChosen2].x, objects["points"][pointChosen2].y), Strength))
    canvas.fill((255, 255, 255))
    simulateEverything()
    canvas.blit(font.render(str(clock.get_fps()), True, (0, 0, 0)), (0, height-100))
    drawEverything()
    pg.display.flip()
    clock.tick(60)
    

