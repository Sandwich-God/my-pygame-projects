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
y = (displayH - 155)
width = 125
height = 125
speed = 10
jump = False
jumpCount = 10

OBx = displayW - 70
OBy = displayH - 130
OBw = 80
OBh = 80

OB2x = displayW - 70
OB2y = displayH - 230
OB2w = 80
OB2h = 80

OB3x = displayW - 70
OB3y = displayH - 330
OB3w = 80
OB3h = 80

on = True

points = 0
lives = 3
on = True
testv = random.randrange(1, 9)

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
	if movement[pygame.K_a] or movement[pygame.K_LEFT] and x > speed + 25:
		x -= speed
	elif movement[pygame.K_d]or movement[pygame.K_RIGHT] and x < displayW - 25 - speed - width:
		x += speed
	if not(jump):
		if movement[pygame.K_w]or movement[pygame.K_UP]:
			jump = True;
	else:
		if jumpCount >= -10:
			y -= (jumpCount * abs(jumpCount)) * .4
			jumpCount -= .5
		else:
			jumpCount = 10
			jump = False
def test():
	global testv, OBx, OB2x, OB3x
	if testv >= 1 and testv <= 3:
		OBx -= 20
		Object()
		ObjectCollision()
	if testv >= 4 and testv <= 6:
		OB2x -= 20
		Object2()
		Object2Collision()
	if testv >= 7 and testv <= 9:
		OB3x -= 20
		Object3()
		Object3Collision()

def ObjectCollision():
	global OBx, OBy, DisplayH, DisplayW, x, y, testv
	if OBx < 30:
		OBx = displayW - 70
		OBy = displayH - 130
		testv = random.randrange(1, 9)
		print('1')
	if x + 95 > OBx and x < OBx + 80 and y + 95 > OBy and y < OBy + 80:
		hit()

def Object2Collision():
	global OB2x, OB2y, DisplayH, DisplayW, x, y, testv
	if OB2x < 30:
		OB2x = displayW - 70
		OB2y = displayH - 230
		testv = random.randrange(1, 9)
		print('2')
	if x + 95 > OB2x and x < OB2x + 80 and y + 95 > OB2y and y < OB2y + 80:
		hit()

def Object3Collision():
	global OB3x, OB3y, DisplayH, DisplayW, x, y, testv
	if OB3x < 30:
		OB3x = displayW - 70
		OB3y = displayH - 330
		testv = random.randrange(1, 9)
		print('3')
	if x + 95 > OB3x and x < OB3x + 80 and y < OB3y + 80 and y + 120 > OB3y:
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
	print('lost')

def game():
	global on, points, OBx, OB2x, OB3x
	on = True
	while on:
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

