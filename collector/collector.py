import pygame
import random
import time

pygame.init()

displayW = 800
displayH = 800

Display = pygame.display.set_mode((displayW,displayH))

pygame.display.set_caption('game')

clock = pygame.time.Clock()


black = (0, 0, 0)
white = (255,255,255)
red = (255, 1, 1)
blue = (1, 1, 255)

x = (displayH/4)
y = (displayW/4)
width = 55
height = 55
speed = 8

Colx = random.randrange(15, 745)
Coly = random.randrange(15, 745)
ColW = 40
ColH = 40

OBx = random.randrange(15, 745)
OBy = random.randrange(15, 745)
OBw = 40
OBh = 40

points = 0
lives = 3
on = True

def player():
	pygame.draw.rect(Display, red, (x, y, width, height))

def Object():
	pygame.draw.rect(Display, white, (Colx, Coly, ColW, ColH))

def movement():
	global x, y, speed, width
	movement = pygame.key.get_pressed()
	if movement[pygame.K_a] and x > speed + 10:
		x -= speed
		if movement[pygame.K_s] and y < 790 - height - speed:
			y += speed
		elif movement[pygame.K_w] and y > speed + 10:
			y -= speed
	elif movement[pygame.K_d] and x < 790 - speed - width:
		x += speed
		if movement[pygame.K_s] and y < 790 - height - speed:
			y += speed
		elif movement[pygame.K_w] and y > speed + 10:
			y -= speed
	elif movement[pygame.K_w] and y > speed + 10:
		y -= speed
	elif movement[pygame.K_s] and y < 790 - height - speed:
		y += speed

def ObjectCollision():
	global on, points, Colx, Coly, DisplayH, DisplayW
	if x > Colx and x < Colx + 40 and y > Coly and y < Coly + 40:
		points += 1
		time.sleep(.03)
		Colx = random.randrange(15, 745)
		Coly = random.randrange(15, 745)
		print(points)

	elif x > Colx and x < Colx and y + Coly > 400 and y + 55 < Coly + 40:
		points += 1
		time.sleep(.03)
		Colx = random.randrange(15, 745)
		Coly = random.randrange(15, 745)
		print(points)
		
	elif x + 55> Colx and x < Colx + 40 and y > Coly and y < Coly + 40:
		points += 1
		time.sleep(.03)
		Colx = random.randrange(15, 745)
		Coly = random.randrange(15, 745)
		print(points)

	elif x + 55> Colx and x < Colx + 40 and y + 55 > Coly and y < Coly + 40:
		points += 1
		time.sleep(.03)
		Colx = random.randrange(15, 745)
		Coly = random.randrange(15, 745)
		print(points)

def Boundarybox():
	pygame.draw.rect(Display, blue, (0, 0, 15, 800))
	pygame.draw.rect(Display, blue, (800, 0, -15, 800))
	pygame.draw.rect(Display, blue, (800, 800, -800, -15))
	pygame.draw.rect(Display, blue, (0, 0, 800, 15))

def fonttype(point, font):
	fontcolor = font.render(point, True, white)
	return fontcolor, fontcolor.get_rect()


def scorebox():
	pygame.draw.rect(Display, black, (0, 0, 100, 20))

def scoreboxoutline():
	pygame.draw.rect(Display, blue, (0, 0, 105, 25))

def score(point):
	Font = pygame.font.Font('freesansbold.ttf', 20)
	fontcolor, score = fonttype(point, Font)
	score.center = ((50),(10))
	scoreboxoutline()
	scorebox()
	Display.blit(fontcolor, score)
	pygame.display.update()
		
def start():
	start = True
	while start:
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
        
		Display.fill(black)
		largeText = pygame.font.SysFont('arial',115)
		smallText = pygame.font.SysFont('arial',25)
		fontcolor, TextRect = fonttype("The Collector", largeText)
		fontcolor2, TextRect2 = fonttype("Press 'enter' to start the game, or 'escape' to quit...", smallText)
		TextRect.center = ((400),(400))
		TextRect2.center = ((400),(500))
		Display.blit(fontcolor, TextRect)
		Display.blit(fontcolor2, TextRect2)
		Boundarybox()
		pygame.display.update()
		clock.tick(15)

		QorE = pygame.key.get_pressed()
		if QorE[pygame.K_RETURN]:
			start = False
		elif QorE[pygame.K_ESCAPE]:
			quit()


def game():
	global on, points, Colx, Coly
	on = True
	while on:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				on = False
		
		ObjectCollision()
		movement()
		
		Display.fill(black)
		Boundarybox()
		player()
		Object()
		score(str(points) + " points")
		pygame.display.update()
		clock.tick(60)

start()
game()

