import pygame
import random
import time

pygame.init()

displayW = 1920
displayH = 1080

Display = pygame.display.set_mode((displayW,displayH), pygame.FULLSCREEN)

pygame.display.set_caption('game')

clock = pygame.time.Clock()


black = (0, 0, 0)
white = (255,255,255)
red = (255, 1, 1)
blue = (1, 1, 255)

x = (displayW/2)
y = (displayH - 80)
width = 50
height = 50
speed = 10

OBx = (displayW/2)
OBy = (displayH/2)
OBw = 40
OBh = 40


on = True

def movement():
	global x, y, speed, width
	movement = pygame.key.get_pressed()
	if movement[pygame.K_a] and x > speed:
		x -= speed
		if movement[pygame.K_s] and y < displayH - height - speed:
			y += speed
		elif movement[pygame.K_w] and y > speed:
			y -= speed
	elif movement[pygame.K_d] and x < displayW - speed - width:
		x += speed
		if movement[pygame.K_s] and y < displayH - height - speed:
			y += speed
		elif movement[pygame.K_w] and y > speed:
			y -= speed
	elif movement[pygame.K_w] and y > speed:
		y -= speed
	elif movement[pygame.K_s] and y < displayH - height - speed:
		y += speed

def ObjectMainFollow():
	global OBx, OBy, x, y
	if OBx > x:
		OBx -= 3
		if OBy > y:
			OBy -= 3
		elif OBy < y:
			OBy += 3
	elif OBx < x:
		OBx += 3
		if OBy > y:
			OBy -= 3
		elif OBy < y:
			OBy += 3
	elif OBy > y:
		OBy -= 3
	elif OBy < y:
		OBy += 3

def player():
	pygame.draw.rect(Display, red, (x, y, width, height))

def Object():
	pygame.draw.rect(Display, white, (OBx, OBy, OBw, OBh))

def game():
	global on, points, Colx, Coly
	on = True
	while on:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				on = False
		movement()
		ObjectMainFollow()
		Display.fill(black)
		player()
		Object()
		pygame.display.update()
		clock.tick(80)
		QorE = pygame.key.get_pressed()
		if QorE[pygame.K_ESCAPE]:
			on = False
game()

