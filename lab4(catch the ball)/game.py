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
j=0
def new_ball():
    global x, y, r, color, j
    x = randint(100,1100)
    y = randint(100,600)
    r = randint(30,50)
    j+=1
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    ballsc.append([x,y])
    ballsr.append(r)
    bcolours.append(color)
    c()

ballsv=[]
ballsc=[]
ballsr=[]
bcolours=[]

def click(event):
    global j, score
    for i in range(j):
        if (ballsc[i][0]-event.pos[0])**2+(ballsc[i][1]-event.pos[1])**2<=(ballsr[i])**2:
            circle(screen, (50, 50, 50), (ballsc[i]), ballsr[i])
            score+=1
            ballsc[i]=[randint(100,1100),randint(100,600)]
            ballsr[i]=randint(30,50)
            ballsv[i]=[randint(-5,5),randint(-5,5)]
            bcolours[i]=COLORS[randint(0, 5)]
            break
   


pygame.display.update()
clock = pygame.time.Clock()
finished = False

def c():
    ballsv.append([randint(-5,5),randint(-5,5)])
    
def move(screen):
    for i in range(j):
        if ballsc[i][0]+ballsr[i]>=1200 or ballsc[i][0]-ballsr[i]<=0:
            ballsv[i][0]=-ballsv[i][0]       
        if ballsc[i][1]+ballsr[i]>=700 or ballsc[i][1]-ballsr[i]<=0:
            ballsv[i][1]=-ballsv[i][1]
        ballsc[i][0]+=ballsv[i][0]
        ballsc[i][1]+=ballsv[i][1]
        circle(screen, (0,0,0), (ballsc[i][0], ballsc[i][1]), ballsr[i])
        circle(screen, bcolours[i], (ballsc[i][0], ballsc[i][1]), ballsr[i])


score=0
for i in range(5):
    new_ball()
    
FONT = pygame.font.Font(None, 50)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    move(screen)
  
 

    score_display = FONT.render(str(score), True, (255, 255, 255))
    screen.blit(score_display, (10, 10))
    pygame.display.update()
    screen.fill(BLACK)
    
pygame.quit()
