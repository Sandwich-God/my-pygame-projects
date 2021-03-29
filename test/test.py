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

x = (displayW/10)
y = (displayH - 80)
width = 50
height = 50
speed = 10
jump = False
jumpCount = 10

OBx = displayW - 70
OBy = random.randrange(displayH - 150, displayH - 100)
OBw = 40
OBh = 40

Colx = displayW - 70
Coly = random.randrange(displayH - 400, displayH - 270)
ColW = 40
ColH = 40

on = True

points = 0
lives = 3
on = True

def player():
	pygame.draw.rect(Display, red, (x, y, width, height))

def Object():
	pygame.draw.rect(Display, white, (Colx, Coly, ColW, ColH))

def Object2():
	pygame.draw.rect(Display, white, (OBx, OBy, OBw, OBh))

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
			jumpCount -= 1
		else:
			jumpCount = 10
			jump = False


def ObjectCollision():
	global Colx, Coly, DisplayH, DisplayW, x, y
	if Colx < 30:
		Colx = displayW - 70
		Coly = random.randrange(displayH - 400, displayH - 270)
		
	if x > Colx and x < Colx + 40 and y > Coly and y < Coly + 40:
		hit()

	elif x > Colx and x < Colx and y + Coly > displayH/2 and y + 55 < Coly + 40:
		hit()
		
	elif x + 55> Colx and x < Colx + 40 and y > Coly and y < Coly + 40:
		hit()

	elif x + 55> Colx and x < Colx + 40 and y + 55 > Coly and y < Coly + 40:
		hit()

def Object2Collision():
	global OBx, OBy, DisplayH, DisplayW, x, y
	if OBx < 30:
		OBx = displayW - 70
		OBy = random.randrange(displayH - 150, displayH - 100)
		
	if x > OBx and x < OBx + 40 and y > OBy and y < OBy + 40:
		hit()

	elif x > OBx and x < OBx and y + OBy > displayH/2 and y + 55 < OBy + 40:
		hit()
		
	elif x + 55> OBx and x < OBx + 40 and y > OBy and y < OBy + 40:
		hit()

	elif x + 55> OBx and x < OBx + 40 and y + 55 > OBy and y < OBy + 40:
		hit()

def Boundarybox():
	pygame.draw.rect(Display, blue, (0, 0, 30, displayH)) #left
	pygame.draw.rect(Display, blue, (displayW, 0, -30, displayH)) #right
	pygame.draw.rect(Display, blue, (displayW, displayH, -displayW, -30)) #bottom
	pygame.draw.rect(Display, blue, (0, 0, displayW, 30)) #top

def fonttype(point, font):
	fontcolor = font.render(point, True, white)
	return fontcolor, fontcolor.get_rect()

def hit():
	global on, displayW, displayH
	Display.fill(black)
	largeText = pygame.font.SysFont('arial',115)
	fontcolor, TextRect = fonttype("Lost", largeText)
	TextRect.center = ((displayW/2),(displayH/2))
	Display.blit(fontcolor, TextRect)
	pygame.display.update()
	clock.tick(15)
	time.sleep(2)
	on = False

def game():
	global on, points, Colx, Coly, OBx
	on = True
	while on:
		Colx -= 10
		OBx -= 10
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				on = False
		ObjectCollision()
		Object2Collision()
		movement()
		Display.fill(black)
		Boundarybox()
		player()
		Object()
		Object2()
		pygame.display.update()
		clock.tick(75)
		QorE = pygame.key.get_pressed()
		if QorE[pygame.K_ESCAPE]:
			on = False
game()

