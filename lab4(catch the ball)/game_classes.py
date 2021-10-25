import pygame
import math
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


class image():
    def __init__(self, r, x, y, Vx, Vy, score1, score2, score3):
        self.x=x
        self.y=y
        self.Vx=Vx
        self.Vy=Vy
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.r = r


    def move(self):
        if self.Vx==0:
            self.Vx+=2
        if self.Vy==0:
            self.Vy+=2
        if self.x+self.r>=1200 or self.x-self.r<=-50:
            self.Vx=-self.Vx
        if self.y+self.r>=700 or self.y-self.r<=-50:
            self.Vy=-self.Vy
        self.x+=self.Vx
        self.y+=self.Vy
        screen.blit(myimage, (self.x, self.y))
        self.score2 += 1
        self.score3 += 1
        if self.score2>=50:
            self.score2=0
            self.Vx = randint(-10, 10)
        if self.score3>=80:
            self.Vy = randint(-10, 10)
            self.score3=0

    def check(self):
        if (self.x-event.pos[0])**2+(self.y-event.pos[1])**2<=(self.r)**2:
            circle(screen, (0,0,0), (self.x, self.y), self.r)
            self.score1+=1
            self.x = randint(100,1100)
            self.y = randint(100,600)
            self.Vx = randint(-5,5)
            self.Vy = randint(-5,5)


image=image(50, randint(100,1100), randint(100,600), randint(-10,10), randint(-10,10), 0, 0, 0)

class Ball():
    def __init__(self, r, colour, x, y, Vx, Vy, score):
        self.r=r
        self.colour=colour
        self.x=x
        self.y=y
        self.Vx=Vx
        self.Vy=Vy
        self.score=score


    def move(self):
        if self.Vx==0:
            self.Vx+=2
        if self.Vy==0:
            self.Vy+=2
        if self.x+self.r>=1200 or self.x-self.r<=0:
            self.Vx=-self.Vx       
        if self.y+self.r>=700 or self.y-self.r<=0:
            self.Vy=-self.Vy
        circle(screen, (0,0,0), (self.x, self.y), self.r)
        self.x+=self.Vx
        self.y+=self.Vy
        circle(screen, self.colour, (self.x, self.y), self.r)

    def check(self):
        if (self.x-event.pos[0])**2+(self.y-event.pos[1])**2<=(self.r)**2:
            circle(screen, (0,0,0), (self.x, self.y), self.r)
            self.score+=1
            ball = Ball(randint(30, 50), COLORS[randint(0, 5)], randint(100, 1100), randint(100, 600), randint(-5, 5), randint(-5, 5), self.score)
            balls.append(ball)






def click(event):
    count=len(balls)
    for ball in balls:
        ball.check()
        if len(balls)>count:
            balls.remove(ball)
    image.check()



pygame.display.update()
clock = pygame.time.Clock()
finished = False
    


balls=[]

for i in range(5):
    ball=Ball(randint(30, 50), COLORS[randint(0, 5)], randint(100,1100), randint(100,600), randint(-5,5), randint(-5,5), 0)
    balls.append(ball)
    
FONT = pygame.font.Font(None, 50)

myimage=pygame.image.load("смайлик.png").convert()
myimage= pygame.transform.scale(myimage, (50, 50))

time=0


gamers = []
scores = []
gamers_to_delete = []

file = open('leaders.txt', 'r')

for line in file.readlines():
    n = line.find(':') + 2
    gamers += [line[:n-2]]
    scores += [line[n:][:-1]]

file.close()

for i in range(len(gamers)):
    for j in range(i + 1, len(gamers)):
        if i != j and gamers[i] == gamers[j]:
            scores[i] = str(max(int(scores[i]), int(scores[j])))
            gamers_to_delete += [j]

for i in gamers_to_delete:
    gamers.pop(i)
    scores.pop(i)
    for j in range(len(gamers_to_delete)):
        gamers_to_delete[j] -= 1

for i in range(len(gamers)):
    if score >= scores[i]:
        gamers = gamers[:i+1] + [gamer] + gamers[i+1:]
        scores = scores[:i+1] + [score] + scores[i+1:]

file = open('leaders.txt', 'w')

print(gamers, scores)
for i in range(len(gamers)):
    file.write(str(gamers[i]) + ": " + str(scores[i]) + '\n')

file.close()

while not finished:
    clock.tick(FPS)
    time += 1/FPS
    if time>=35:
        finished=True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    sum=0
    for ball in balls:
        ball.move()
        sum+=ball.score
    sum+=image.score1*3
    image.move()

    time_display = FONT.render(str(35-math.floor(time)), True, (255, 255, 255))
    screen.blit(time_display, (500, 10))
    score_display = FONT.render(str(sum), True, (255, 255, 255))
    screen.blit(score_display, (10, 10))
    score_display1 = FONT.render(str(image.score1), True, (255, 0, 0))
    screen.blit(score_display1, (100, 10))
    pygame.display.update()
    screen.fill(BLACK)
    
pygame.quit()
