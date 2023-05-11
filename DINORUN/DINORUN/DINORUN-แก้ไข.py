import pygame
import time

pygame.init()
#setting
Width = 800
Height = 600
bg_x = 0
backvelo = 0
black = (0,0,0)
gameDisplay = pygame.display.set_mode((Width,Height))
pygame.display.set_caption('DINORUN')
icon = pygame.image.load('icon1.png')
pygame.display.set_icon(icon)
animate_player = True
player_x = 100
player_y = 387
player_img_count = 0
FPS = 24
treex = 650
treey = 412
tree_height = 50
tree_width = 40
tree1_height = 48
tree1_width = 50
tree2_height = 50
tree2_width = 64
tree_speed = 25
egg_height = 32
egg_width = 32
score = 0
birdx = 600
birdy = 80 
eggx = 650
eggy = 250
bg = pygame.transform.scale(pygame.image.load('background.jpg'),(Width,Height)) 
tree = pygame.image.load('tree.png')
tree1 = pygame.image.load('tree1.png')
tree2 = pygame.image.load('tree2.png')
egg = pygame.image.load('egg.png')
clock = pygame.time.Clock()
bird = pygame.image.load('bird.png') 
playerimg = [pygame.image.load('dn1.png'),pygame.image.load('dn2.png'),pygame.image.load('dn3.png'), 
            pygame.image.load('dn4.png'),pygame.image.load('dn6.png'),pygame.image.load('dn6.png'),
            pygame.image.load('dn7.png'),pygame.image.load('dn8.png'),pygame.image.load('dn9.png')]

playerimg_width = 30

def thing_score(count):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score : "+str(count), True, black)
    gameDisplay.blit(text, (650,20))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (Width*0.5 ,Height*0.5)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    
    
def crash():
    message_display('YOU  LOSE')

def crash_egg():
    pygame.display.update()
    
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
isJump = False
vel = 2
jumpCount = 10

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    keys = pygame.key.get_pressed()
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True 
    else:
        if jumpCount >= -10:
            player_y -= (jumpCount * abs(jumpCount)) * 0.45
            jumpCount -= 1 
        else:
            jumpCount = 10
            isJump = False
    
    if treex < -800:
        treex = 800
        tree_speed += 0.5
    if eggx < -800:
    	eggx = 800

    if player_x > treex and player_x < treex + tree_width or player_x + playerimg_width > treex and player_x + playerimg_width < treex + tree_width == True:
        score += 1

    if player_x > treex+400 and player_x < treex + 400+ tree1_width or player_x + playerimg_width > treex+400 and player_x + playerimg_width < treex + 400 + tree1_width == True:
        score += 1

    if player_x > treex+800 and player_x < treex + 800+ tree1_width or player_x + playerimg_width > treex+800 and player_x + playerimg_width < treex + 800 + tree2_width == True:
        score += 1
    scrolling_background()
    treex -= 6
    eggx -= 10

            
    if player_y > treey - tree_height:
        print('player_y crossover')
        if player_x > treex and player_x < treex + tree_width or player_x + playerimg_width > treex and player_x + playerimg_width < treex + tree_width:
            print('player_x crossover')
            crash()
    if player_y > treey-8 - tree1_height:
        print('player_y crossover')
        if player_x > treex+400 and player_x < treex + 400+ tree1_width or player_x + playerimg_width > treex+400 and player_x + playerimg_width < treex + 400 + tree1_width:
            print('player_x crossover')
            crash()
    if player_y > treey-11 - tree1_height:
        print('player_y crossover')
        if player_x > treex+800 and player_x < treex + 800+ tree1_width or player_x + playerimg_width > treex+800 and player_x + playerimg_width < treex + 800 + tree2_width:
            print('player_x crossover')
            crash()

    
    if Height - player_y > Height - eggy :
        print('player_y crossover')
        if player_x + playerimg_width  > eggx+800 and player_x + playerimg_width < eggx+800 + egg_width :
            print('player_x crossover')
            crash_egg()
            eggx = 650
            eggy = 250
            score += 1
        
        
    gameDisplay.blit(playerimg[player_img_count],(player_x,player_y))
    thing_score(score)
    gameDisplay.blit(tree,(treex,treey))
    gameDisplay.blit(tree1,(treex+400,treey-8))
    gameDisplay.blit(tree2,(treex+800,treey-11))
    gameDisplay.blit(bird,(birdx,birdy))
    gameDisplay.blit(egg,(eggx+800,eggy))

    
    
    player_img_count += 1
    if player_img_count +1 > 8:
        player_img_count = 0

    
    pygame.display.update()

pygame.quit()
quit()
