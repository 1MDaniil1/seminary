import pygame
from pygame.draw import*
import numpy as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 402))

back_color = (255, 255, 0)
screen.fill(back_color)

def multicloud (main_cloud_x, main_cloud_y, cloud_radius, ro_cloud, cv):
	circle(screen, (0, 0, 0), (main_cloud_x, main_cloud_y), cloud_radius + 1) #Cloud0
	circle(screen, (cv, cv, cv), (main_cloud_x, main_cloud_y), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x - ro_cloud * 2, main_cloud_y + ro_cloud * 3), cloud_radius + 1) #Cloud1
	circle(screen, (cv, cv, cv), (main_cloud_x - ro_cloud * 2, main_cloud_y + ro_cloud * 3), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x + ro_cloud * 3, main_cloud_y), cloud_radius + 1) #Cloud2
	circle(screen, (cv, cv, cv), (main_cloud_x + ro_cloud * 3, main_cloud_y), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x + ro_cloud * 2, main_cloud_y + ro_cloud * 3), cloud_radius + 1) #Cloud3
	circle(screen, (cv, cv, cv), (main_cloud_x + ro_cloud * 2, main_cloud_y + ro_cloud * 3), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x + ro_cloud * 6, main_cloud_y + ro_cloud * 3), cloud_radius + 1) #Cloud4
	circle(screen, (cv, cv, cv), (main_cloud_x + ro_cloud * 6, main_cloud_y + ro_cloud * 3), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x + ro_cloud * 8, main_cloud_y), cloud_radius + 1) #Cloud5
	circle(screen, (cv, cv, cv), (main_cloud_x + ro_cloud * 8, main_cloud_y), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x + ro_cloud * 10, main_cloud_y + ro_cloud * 3), cloud_radius + 1) #Cloud6
	circle(screen, (cv, cv, cv), (main_cloud_x + ro_cloud * 10, main_cloud_y + ro_cloud * 3), cloud_radius)

def umbrella(left_upper_x, left_upper_y, dx_umb, h_umb, umb_radius, umb_start, deltha):
	rect(screen, (210, 110, 34), (left_upper_x, left_upper_y, dx_umb, h_umb))
	polygon(screen, (249, 96, 75), [(left_upper_x + dx_umb, left_upper_y),
	 (left_upper_x + dx_umb, left_upper_y + umb_start), (left_upper_x + dx_umb + umb_radius, left_upper_y + umb_start)])
	polygon(screen, (249, 96, 75), [(left_upper_x, left_upper_y),
	 (left_upper_x, left_upper_y + umb_start), (left_upper_x - umb_radius, left_upper_y + umb_start)])
	rect(screen, (249, 96, 75), (left_upper_x, left_upper_y, dx_umb, umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (left_upper_x - umb_radius + 1 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (left_upper_x - umb_radius + 2 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (left_upper_x - umb_radius + 3 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb + umb_radius - 3 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb + umb_radius - 2 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb + umb_radius - 1 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (left_upper_x, left_upper_y + umb_start))
	
def draw_deck(boat_0_x, boat_0_y, proportion,deck_color):
	circle(screen, deck_color, (boat_0_x, boat_0_y), proportion * 7)
	rect(screen, (0, 0, 255), (boat_0_x - proportion * 7, boat_0_y - proportion * 7, proportion * 7 * 2, proportion * 7))
	rect(screen, (0, 0, 255), (boat_0_x, boat_0_y, proportion * 7, proportion * 7))
	rect(screen, (0, 0, 0), (boat_0_x, boat_0_y, proportion * 28 + 2, proportion * 7))
	rect(screen, deck_color, (boat_0_x + 1, boat_0_y, proportion * 28, proportion * 7))
	polygon(screen, (0, 0, 0), [(boat_0_x + proportion * 28 + 2, boat_0_y),
	 (boat_0_x + proportion * 28 + 2, boat_0_y + proportion * 7 - 1), (boat_0_x + proportion * 43, boat_0_y)])
	polygon(screen, deck_color, [(boat_0_x + proportion * 28 + 2, boat_0_y),
	 (boat_0_x + proportion * 28 + 2, boat_0_y + proportion * 7 - 1), (boat_0_x + proportion * 43, boat_0_y)])
	circle(screen, (0, 0, 0), (boat_0_x + proportion * 33, boat_0_y + proportion * 3 - 2), proportion * 2)
	circle(screen, (255, 255, 255), (boat_0_x + proportion * 33, boat_0_y + proportion * 3 - 2), proportion * 2 - 3)
	
def draw_sail(sail_x, sail_y, sail_color, proportion):
	rect(screen, (0, 0, 0), (sail_x, sail_y, proportion * 2 - 2,  2 * 10 * proportion))
	polygon(screen, sail_color, [(sail_x + proportion * 2 - 2, sail_y),
	 (sail_x + proportion * 6, sail_y + proportion * 10), (sail_x + proportion * 14, sail_y + proportion * 10)])
	polygon(screen, sail_color, [(sail_x + proportion * 2 - 2, sail_y + proportion * 10 * 2),
	 (sail_x + proportion * 6, sail_y + proportion * 10), (sail_x + proportion * 14, sail_y + proportion * 10)])
	aaline(screen, (0, 0, 0), (sail_x + proportion * 6, sail_y + proportion *10), (sail_x + proportion * 14, sail_y + proportion * 10))
	aaline(screen, (0, 0, 0), (sail_x + proportion * 6, sail_y + proportion *10), (sail_x + proportion * 2 - 2, sail_y))
	aaline(screen, (0, 0, 0), (sail_x + proportion * 14, sail_y + proportion *10), (sail_x + proportion * 2 - 2, sail_y))
	aaline(screen, (0, 0, 0), (sail_x + proportion * 6, sail_y + proportion *10), (sail_x + proportion * 2 - 2, sail_y + 2 * 10 * proportion))
	aaline(screen, (0, 0, 0), (sail_x + proportion * 14, sail_y + proportion *10), (sail_x + proportion * 2 - 2, sail_y + 2 * 10 * proportion))

def sun(R, r, sunlights, x, y):
        circle(screen, (255, 255, 0), (x,y), R)
        for i in range(sunlights):
                polygon(screen, (255, 255, 0), [(x + R * np.sin ( 2 * i * np.pi / sunlights), 
	y - R * np.cos (2 * i * np.pi / sunlights)), (x + R * np.sin ( (2 * i + 1) * np.pi / sunlights),
	 y - R * np.cos ((2 * i + 1) * np.pi / sunlights)), ((x + (R + r) * np.sin ((2 * i + 0.5) * np.pi / sunlights),
	  y - (R + r) * np.cos ((2 * i + 0.5) * np.pi / sunlights)))])

rect(screen, (0, 0, 255), (0, 0, 600, 260))	



draw_deck(360, 190, 5,(255, 0, 255))



rect(screen, (0, 0, 255), (0, 0, 600, 170))
rect(screen, (129, 218, 247), (0, 0, 600, 160))

sun(40, 8, 20, 540, 60)

multicloud(170, 40, 15, 5, 255)


draw_sail(425, 70, (0, 0, 255), 6)



#rain(50, 306, 30, 8)

#raindrop (310,120)


#multicloud(116, 98, 19, 7)




umbrella(110, 220, 8, 140, 54, 25, 15)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()

