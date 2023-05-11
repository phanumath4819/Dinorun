import pygame
pygame.init()
#setting
Width = 800
Height = 600
bg_x = 0
gameDisplay = pygame.display.set_mode((Width,Height))
pygame.display.set_caption('DINORUN')
icon = pygame.image.load('icon1.png')
pygame.display.set_icon(icon)
animate_player = True
player_x = 100
player_y = 400
player_img_count = 0
bg = pygame.transform.scale(pygame.image.load('background.jpg'),(Width,Height)) 
playerimg = [pygame.image.load('dn1.png'),pygame.image.load('dn2.png'),pygame.image.load('dn3.png'),pygame.image.load('dn4.png'),
		  pygame.image.load('dn6.png'),pygame.image.load('dn6.png'),pygame.image.load('dn7.png'),pygame.image.load('dn8.png'),
		  pygame.image.load('dn9.png')]
#rotate_background
def scrolling_background():
	global bg_x
	relative_x = bg_x % bg.get_rect().width
	gameDisplay.blit(bg,(relative_x - bg.get_rect().width,0))
	if relative_x < Width:
		gameDisplay.blit(bg,(relative_x,0))
	bg_x -= 10
clock = pygame.time.Clock()
run = True
while run:
	clock.tick(18)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	scrolling_background()
	gameDisplay.blit(playerimg[player_img_count],(player_x,player_y))
	player_img_count += 1
	if player_img_count +1 > 8:
		player_img_count = 0
	pygame.display.update()
pygame.quit()
quit()
