import pygame
pygame.init()
display_width = 800
display_height = 600
surface = pygame.display.set_mode((display_width, display_height))
running1 = pygame.image.load('Running1.png')
running2 = pygame.image.load('Running2.png')
standing = pygame.image.load('playerstanding.png')
door = pygame.image.load('Door.png')
key = pygame.image.load('key.png')
running_left1 = pygame.transform.flip(running1, True, False)
running_left2 = pygame.transform.flip(running2, True, False)
running_list = [running1, running2]
counter = 0
clock = pygame.time.Clock()
player_x = 100
player_y = 300
player_xvel = 0
player_yvel = 2
run_direction = 'standing'
jumping = False
gravity = 1.2
key_found = False
level =1
first_loop =0
while True:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                run_direction = 'right'
                player_xvel = 5
            if event.key == pygame.K_LEFT:
                run_direction = 'left'
                player_xvel = -5
            if event.key ==pygame.K_SPACE:
                if jumping ==False:
                    jumping = True
                    player_yvel = -15
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                run_direction='standing'
                player_xvel = 0
            if event.key == pygame.K_LEFT:
                run_direction='standing'
                player_xvel = 0
    if jumping ==True:
        if player_yvel < 8:
            player_yvel = player_yvel + gravity
    player_x = player_x + player_xvel
    player_y = player_y + player_yvel
    surface.fill((255, 255, 255))
    if level ==1:
        pygame.draw.rect(surface, (100, 100, 100), (30, 500, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (200, 450, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (380, 400, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (680, 500, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (550, 450, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (200, 350, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (550, 350, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (680, 300, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (550, 250, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (380, 300, 100, 10))
    if level ==2:
        if first_loop == 0:
            player_x = 720
            player_y = 50
            first_loop = first_loop + 1
        pygame.draw.rect(surface, (100, 100, 100), (700, 100, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (100, 280, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (0, 200, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (100, 120, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (300, 100, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (200, 350, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (680, 500, 100, 10))
        pygame.draw.rect(surface, (100, 100, 100), (380, 300, 100, 10))
        
    pygame.draw.rect(surface, (255, 0, 0), (0, display_height-40, display_width, display_height))
    if level == 1:
        door_rect = surface.blit(door, (425, 270))
        if key_found ==False:
            key_rect = surface.blit(key, (720, 475))
    if level == 2:
        door_rect = surface.blit(door, (720, 470))
        if key_found ==False:
            key_rect = surface.blit(key, (320, 75))
    if run_direction== 'right':
        if counter%2==0:
            character = surface.blit(running1, (player_x, player_y))
        else:
            character =surface.blit(running2, (player_x, player_y))
    if run_direction == 'left':
        if counter%2==0:
            character =surface.blit(running_left1, (player_x, player_y))
        else:
            character =surface.blit(running_left2, (player_x, player_y))
    if run_direction=='standing':
        character = surface.blit(standing, (player_x, player_y))

    if character.colliderect(key_rect):
        key_found = True
    if character.colliderect(door_rect):
        if key_found == True:
            level = 2
            key_found = False
    if surface.get_at((character.left, character.bottom))==(100, 100, 100) or surface.get_at((character.right, character.bottom))==(100, 100, 100):
            player_yvel = 0
            jumping = False

    else:
        if jumping == False:
            player_yvel = 2
    if player_y>display_height-40:
        pygame.quit()
    counter = counter + 1
    pygame.display.update() 
