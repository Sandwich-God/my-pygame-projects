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
OBy = displayH - 80
OBw = 40
OBh = 40

OB2x = displayW - 70
OB2y = displayH - 150
OB2w = 40
OB2h = 40

OB3x = displayW - 70
OB3y = displayH - 220
OB3w = 40
OB3h = 40

on = True

points = 0
lives = 3
on = True

def player():
	pygame.draw.rect(Display, red, (x, y, width, height))

def Object():
	pygame.draw.rect(Display, white, (OBx, OBy, OBw, OBh))

def Object2():
	pygame.draw.rect(Display, white, (OB2x, OB2y, OB2w, OB2h))

def Object3():
	pygame.draw.rect(Display, white, (OB3x, OB3y, OB3w, OB3h))

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
def test():
	testv = random.randrange(1, 3)
	if testv == 1:
		Object()
		ObjectCollision()
	if testv == 2:
		Object2()
		Object2Collision()
	if testv == 3:
		Object3()
		Object3Collision()

def ObjectCollision():
	global OBx, OBy, DisplayH, DisplayW, x, y
	if OBx < 30:
		OBx = displayW - 70
		OBy = displayH - 80
		
	if x > OBx and x < OBx + 40 and y > OBy and y < OBy + 40:
		hit()

	elif x > OBx and x < OBx and y + OBy > displayH/2 and y + 55 < OBy + 40:
		hit()
		
	elif x + 55> OBx and x < OBx + 40 and y > OBy and y < OBy + 40:
		hit()

	elif x + 55> OBx and x < OBx + 40 and y + 55 > OBy and y < OBy + 40:
		hit()

def Object2Collision():
	global OB2x, OB2y, DisplayH, DisplayW, x, y
	if OB2x < 30:
		OB2x = displayW - 70
		OB2y = displayH - 150
		
	if x > OB2x and x < OB2x + 40 and y > OB2y and y < OB2y + 40:
		hit()

	elif x > OB2x and x < OB2x and y + OB2y > displayH/2 and y + 55 < OB2y + 40:
		hit()
		
	elif x + 55> OB2x and x < OB2x + 40 and y > OB2y and y < OB2y + 40:
		hit()

	elif x + 55> OB2x and x < OB2x + 40 and y + 55 > OB2y and y < OB2y + 40:
		hit()

def Object3Collision():
	global OB3x, OB3y, DisplayH, DisplayW, x, y
	if OB3x < 30:
		OB3x = displayW - 70
		OB3y = displayH - 220
		
	if x > OB3x and x < OB3x + 40 and y > OB3y and y < OB3y + 40:
		hit()

	elif x > OB3x and x < OB3x and y + OB3y > displayH/2 and y + 55 < OB3y + 40:
		hit()
		
	elif x + 55> OB3x and x < OB3x + 40 and y > OB3y and y < OB3y + 40:
		hit()

	elif x + 55> OB3x and x < OB3x + 40 and y + 55 > OB3y and y < OB3y + 40:
		hit()

def Boundarybox():
	pygame.draw.rect(Display, blue, (0, 0, 30, displayH)) #left
	pygame.draw.rect(Display, blue, (displayW, 0, -30, displayH)) #right
	pygame.draw.rect(Display, blue, (displayW, displayH, -displayW, -30)) #bottom
	pygame.draw.rect(Display, blue, (0, 0, displayW, 30)) #top

def fonttype(point, font):
	fontOBor = font.render(point, True, white)
	return fontOBor, fontOBor.get_rect()

def hit():
	global on, displayW, displayH
	Display.fill(black)
	largeText = pygame.font.SysFont('arial',115)
	fontOBor, TextRect = fonttype("Lost", largeText)
	TextRect.center = ((displayW/2),(displayH/2))
	Display.blit(fontOBor, TextRect)
	pygame.display.update()
	clock.tick(15)
	time.sleep(2)
	on = False

def game():
	global on, points, OBx, OB2x, OB3x
	on = True
	while on:
		OBx -= 10
		OB2x -= 10
		OB3x -= 10
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				on = False
		
		movement()
		Display.fill(black)
		Boundarybox()
		test()
		player()
		pygame.display.update()
		clock.tick(75)
		QorE = pygame.key.get_pressed()
		if QorE[pygame.K_ESCAPE]:
			on = False
game()

