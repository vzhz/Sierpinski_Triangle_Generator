import pygame
import random

width = 1000
height = 1000
color = pygame.Color(0, 255, 0)

pygame.init()
surface = pygame.display.set_mode((width, height)) # creates a window

def draw_pixel(x, y, count):
    surface.fill(color, ((x, y), (1, 1)))
    if count%100==0:
    	pygame.display.flip()

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






