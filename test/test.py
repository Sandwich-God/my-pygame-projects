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
jump = False
jumpCount = 10

on = True

def player():
	pygame.draw.rect(Display, red, (x, y, width, height))

def movement():
	global x, y, speed, width, jump, jumpCount
	movement = pygame.key.get_pressed()
	if movement[pygame.K_a] and x > speed + 25:
		x -= speed
	elif movement[pygame.K_d] and x < displayW - 25 - speed - width:
		x += speed
	if not(jump):
		if movement[pygame.K_w]:
			jump = True;
	else:
		if jumpCount >= -10:
			y -= (jumpCount * abs(jumpCount)) * .5
			jumpCount -= .5
		else:
			jumpCount = 10
			jump = False


def Boundarybox():
	pygame.draw.rect(Display, blue, (0, 0, 30, displayH)) #left
	pygame.draw.rect(Display, blue, (displayW, 0, -30, displayH)) #right
	pygame.draw.rect(Display, blue, (displayW, displayH, -displayW, -30)) #bottom
	pygame.draw.rect(Display, blue, (0, 0, displayW, 30)) #top

def game():
	global on, points, Colx, Coly
	on = True
	while on:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				on = False
		movement()
		Display.fill(black)
		Boundarybox()
		player()
		pygame.display.update()
		clock.tick(90)
		QorE = pygame.key.get_pressed()
		if QorE[pygame.K_ESCAPE]:
			on = False
game()

