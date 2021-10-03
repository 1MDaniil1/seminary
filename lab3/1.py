import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill ((255,255,255))
circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (255, 0, 0), (150, 150),
       40)
circle(screen, (0, 0, 0), (150, 150), 20)
circle(screen, (255, 0, 0), (275, 150), 30)
circle(screen, (0, 0, 0), (275, 150), 15)
rect(screen, (0, 0, 0), (100, 250, 200, 40))
line(screen, (0, 0, 0), (70,70), (205, 130), 10)
line(screen, (0, 0, 0), (330,70), (250, 130), 10)





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

