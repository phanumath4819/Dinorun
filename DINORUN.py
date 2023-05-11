import pygame
import time
import random
import sys
import os

pygame.init()
width = 800
height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (51,204,102)
 
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('DINORUN')
icon = pygame.image.load('icon1.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
player_x = 100
player_y = 390
player_img_count = 0

dinoImg = [pygame.image.load('walk1.png')
dino_width = 30
background = pygame.image.load('background.jpg')
treeImg = pygame.image.load('tree.png')


def thing_score(count):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score : "+str(count), True, black)
    screen.blit(text, (650,20))
    
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(screen, color, [thingx, thingy, thingw, thingh])
    
def walk(x,y):
    screen.blit(dinoImg,(x,y))
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (width*0.5 ,height*0.5)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
    
def crash():
    message_display('YOU  LOSER')
    
def game_loop():
    gameExit = False
    jumping = False
    x = int(width*0.12)
    y = int(height*0.71)
    thing_startx = 800
    thing_starty = y + 30
    thing_speed = 5
    thing_width = 50
    thing_height = 50
    score = 0
    
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if jumping == False:
                        jumping = True
                        y -= 120
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if jumping == True:
                        jumping = False
                        y += 120
            gameExit = False
        

        screen.blit(dinoImg[player_img_count],(player_x,player_y))
        
        things(thing_startx, thing_starty, thing_width, thing_height, green)
        thing_startx -= thing_speed
        thing_score(score)
        
        if thing_startx < 0 :
            thing_startx = 800
            thing_starty = y + 30
            score += 1
            thing_speed += 0.2
            
        if y > thing_starty - thing_height:
            print('y crossover')
            if x > thing_startx and x < thing_startx + thing_width or x + dino_width > thing_startx and x + dino_width < thing_startx + thing_width:
                print('x crossover')
                crash()
    
                
        pygame.display.update()
        clock.tick(60)
        
game_loop()
pygame.quit()
quit()
