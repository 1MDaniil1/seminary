import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    global x, y, r, color
    x = randint(100,1100)
    y = randint(100,600)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    ballsc.append(tuple((x,y)))
    ballsr.append(r)
    c()

ballsv=[]
ballsc=[]
ballsr=[]
    
def click(event):
    for i in range(len(ballsc)):
        l=ballsc[i]
        if (l[0]-event.pos[0])**2+(l[1]-event.pos[1])**2<=(ballsr[i])**2:
            circle(screen, (0, 0, 0), (l[0],l[1]), r)
            new_ball()
   
    

pygame.display.update()
clock = pygame.time.Clock()
finished = False

def c():
    global dx, dy
    dx=randint(-10,10)
    dy=randint(-10,10)
    ballsv.append(tuple((dx,dy)))
    
def move(screen):
    global x, y, dx, dy
    x+=dx
    y+=dy
    if x+r>=1200 or x-r<=0:
        dx=-dx
    if y+r>=700 or y-r<=0:
        dy=-dy
    circle(screen, color, (x, y), r)
 

new_ball()

while not finished:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    move(screen)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
