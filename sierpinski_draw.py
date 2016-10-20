import pygame, random, time
from sys import version_info

### window parameters for initial triangle visualization ###
width = 1000
height = 1000
color = pygame.Color(0, 255, 0)

### additional parameters for slower, more informative visualization ###
highlight_P_1 = pygame.Color(255, 50, 50)
previous_P_0 = pygame.Color(50, 255, 50)
ABCD_color = pygame.Color(50, 50, 255)

### create the window ###
pygame.init()
surface = pygame.display.set_mode((width, height))


def draw_pixel(x, y, count):
    """Draws each pixel in the full-speed case"""
    surface.fill(color, ((x, y), (1, 1)))
    if count%100==0:
        pygame.display.flip()

def draw_pixel_recursive(x1, y1, count): #add count if you want to flip only occasionally
    """Draws each pixel in the slower case"""
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

### alternative settings for slower version of visualization ###
# P_0 = (random_row(), random_col())
# varibles = [random_point() for i in range(4)]
# i = random.randint(0,2)

# count = 0
# while count <= 100000:
#   i = (i + random.randint(0,3))%4 #placeholder change 3 if you don't want to repeat a letter
#   chosen_one = varibles[i]
#   P_1 = (midpoint(P_0[0], P_0[1], chosen_one[0], chosen_one[1]))
#   draw_pixel(P_0[0], P_0[1], chosen_one[0], chosen_one[1], P_1[0], P_1[1]) #why is this throwing an error?
#   P_0 = P_1
#   i = (i + random.randint(0,3))%4 #placeholder change 3 if you don't want to repeat a letter
#   chosen_one = varibles[i]
#   draw_pixel_ABCD_1(P_0[0], P_0[1], chosen_one[0], chosen_one[1])
#   count += 1

### call this if user asks for slower version ###
#draw_pixel_recursive(P_0[0], P_0[1], 10000)

def random_row():
    return random.randint(0, height)

def random_col():
    return random.randint(0, width)

def midpoint(row1, row2, col1, col2):
    rowm = (row1+row2)/2
    colm = (col1+col2)/2
    return (rowm, colm)

def random_point():
    return random_row(), random_col()

P = (random_row(), random_col())
varibles = [random_point() for i in range(4)]
i = random.randint(0,2)

def draw_either(chosen_one, P, draw_pixel)
    count = 0
    while count <= 100000:
        i = (i + random.randint(0,3))%4
        chosen_one = varibles[i]
        a_row = chosen_one[0]
        a_col = chosen_one[1]
        b_row = P[0]
        b_col = P[1]
        draw_pixel(b_row, b_col, count)
        P = (midpoint(a_row, b_row, a_col, b_col))
        count += 1


pygame.event.wait()
pygame.event.wait()






