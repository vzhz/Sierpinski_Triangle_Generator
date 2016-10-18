import pygame
import random
import time
pygame.init()

surface = pygame.display.set_mode((500, 500))

def draw_pixel(x,y):
    surface.fill(pygame.Color(0,255,0), ((x,y), (1,1)))
    pygame.display.flip()

x = 400
y = 400

for i in range(1,10000):    
    choice = random.randint(1,3)
    A_x = 0
    A_y = 0
    B_x = 500
    B_y = 500
    C_x = 500
    C_y = 0
    if choice == 1:
        x = (x+A_x)/2    
        y = (y+A_y)/2
    elif choice == 2:
        x = (x+B_x)/2    
        y = (y+B_y)/2
    elif choice == 3:
        x = (x+C_x)/2    
        y = (y+C_y)/2

    draw_pixel(x,y)

time.sleep(50)
