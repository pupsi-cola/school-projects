import pygame
import time
import random
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

pygame.init()
bullets = []
screen = pygame.display.set_mode([500, 500])
sprite_sheet_image = pygame.image.load("spritesheet3.png").convert_alpha()
enemy = pygame.image.load("enemyy.png").convert_alpha()
width = 500
height = 500
vel = 10
FPS = 30
bg = (45, 3, 63)
gray = (100, 100, 100)
font = pygame.font.SysFont
font1 = font("arial", 24)
x, y = 225, 400
mx, my = 245, 400
#player sprite sheet
bulletpicture = pygame.image.load("projectile.png").convert_alpha()
player_image = pygame.image.load("ship.gif").convert_alpha()


def get_image(sheet, frame, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image = pygame.transform.scale(image, (width *scale, height * scale))
    image.set_colorkey(gray)
    return image
#player frames
player_image = get_image(sprite_sheet_image, 0, 50, 100, 1, gray)
bullet = get_image(bulletpicture, 0, 5, 5, 1, gray)
enemy = get_image(enemy, 1, 88, 96, 1, gray)
clock = pygame.time.Clock()

player = player_image.get_rect()
pygame.Rect(player)


run = True
while run:
    screen.fill(bg)
    #player animation
    screen.blit(player_image, (x, y))
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 440:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 400:
        y += vel
    clock.tick(120)
    screen.blit(bulletpicture, (mx, my))
    if keys[pygame.K_SPACE]:
        pygame.key.set_repeat(5, 1)
        my -=vel
    if keys[pygame.K_LEFT] and x > vel:
        mx -= vel
    if keys[pygame.K_RIGHT] and x < 440:
        mx += vel
    if keys[pygame.K_UP] and y > vel:
        my -= vel
    if keys[pygame.K_DOWN] and y < 400:
        my += vel
    clock.tick(240)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            run = False
            
        
            #set score to 0




            #splash screen, "insert coin/press any button" prompt
            #screen switches when button pressed

            #spawn barriers
                #2 barriers, one on each side of the screen
                #barriers block all bullets
                #barriers never disappear

            #player spawn

            #set player hp
                

            #player control functions






        #if player hp hits 0

                #show explosion

                #wait 1 second

                #go to game start screen
    pygame.display.flip()

 