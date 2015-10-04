import pygame
import random
import time

width = 1000
height = 1000
highlight_P_1 = pygame.Color(255, 50, 50)
previous_P_0 = pygame.Color(50, 255, 50)
ABCD_color = pygame.Color(50, 50, 255)

pygame.init()
surface = pygame.display.set_mode((width, height)) # creates a window

# def draw_pixel(x1, y1, x2, y2, x3, y3, count): #add count if you want to flip only occasionally
#     surface.fill(previous_P_0, ((x1, y1), (3, 3)))
#     #if count%1==0:
#     surface.fill(chosen_ABCD_0, ((x2, y2), (3, 3)))
#     pygame.draw.line(surface, (255, 50, 50), (x1, y1), (x2, y2), 1)
#     surface.fill(highlight_P_1, ((x3, y3), (3, 3)))
#     pygame.display.flip()
#     time.sleep(0.5)
#     pygame.draw.line(surface, (0, 0, 0), (x1, y1), (x2, y2), 1)
#     pygame.display.flip()
#     time.sleep(0.5)
# def draw_pixel_ABCD_1(x1, y1, x2, y2, count):
# 	surface.fill(previous_P_0, ((x1, y1), (3, 3)))
# 	surface.fill(chosen_ABCD_0, ((x2, y2), (3, 3)))
# 	pygame.draw.line(surface, (255, 50, 50), (x1, y1), (x2, y2), 1)
# 	pygame.display.flip()
# 	time.sleep(0.5)
# 	pygame.draw.line(surface, (0, 0, 0), (x1, y1), (x2, y2), 1)
# 	pygame.display.flip()
# 	time.sleep(0.5)



#how to test if pixel cluster is always offset the same way

def random_row():
	return random.randint(0, height)

def random_col():
	return random.randint(0, width)

def midpoint(x1, y1, x2, y2):
	x_m = (x1+x2)/2
	y_m = (y1+y2)/2
	return (x_m, y_m)

def random_point():
	return random_row(), random_col()

ABCD = [random_point() for i in range(4)]
for x,y in ABCD:
	surface.fill(ABCD_color, ((x, y), (5, 5)))
P_0 = (random_row(), random_col())
	
def draw_pixel_recursive(x1, y1, count): #add count if you want to flip only occasionally
    if count==0:
    	return
    chosen_one = ABCD[random.randint(0,3)]
    P_1 = midpoint(x1, y1, chosen_one[0], chosen_one[1])
    surface.fill(previous_P_0, ((x1, y1), (5, 5)))
    pygame.draw.line(surface, (255, 50, 50), (x1, y1), (chosen_one[0], chosen_one[1]), 1)
    pygame.display.flip()
    time.sleep(0.5)
    pygame.draw.line(surface, (0, 0, 0), (x1, y1), (chosen_one[0], chosen_one[1]), 1)
    pygame.display.flip()
    time.sleep(0.5)
    draw_pixel_recursive(P_1[0],P_1[1], count-1)

# P_0 = (random_row(), random_col())
# varibles = [random_point() for i in range(4)]
# i = random.randint(0,2)

# count = 0
# while count <= 100000:
# 	i = (i + random.randint(0,3))%4 #placeholder change 3 if you don't want to repeat a letter
# 	chosen_one = varibles[i]
# 	P_1 = (midpoint(P_0[0], P_0[1], chosen_one[0], chosen_one[1]))
# 	draw_pixel(P_0[0], P_0[1], chosen_one[0], chosen_one[1], P_1[0], P_1[1]) #why is this throwing an error?
# 	P_0 = P_1
# 	i = (i + random.randint(0,3))%4 #placeholder change 3 if you don't want to repeat a letter
# 	chosen_one = varibles[i]
# 	draw_pixel_ABCD_1(P_0[0], P_0[1], chosen_one[0], chosen_one[1])
# 	count += 1
draw_pixel_recursive(P_0[0], P_0[1], 10000)

pygame.event.wait()
pygame.event.wait()

#what the hell is this shit? http://stackoverflow.com/questions/4276342/python-pygame-how-can-i-delete-a-line
#can I only redraw where the deleted lines where?  Let's just make them a pixel



