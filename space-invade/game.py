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
FPS = 30
bg = (100, 100, 100) 
gray = (100, 100, 100)
font = pygame.font.SysFont
font1 = font("arial", 24)
x, y = 225, 400
mx, my = 225, 400
#player sprite sheet
bulletpicture = pygame.image.load("projectile.png").convert_alpha()

def get_image(sheet, frame, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image = pygame.transform.scale(image, (width *scale, height * scale))
    image.set_colorkey(gray)
    return image
#player frames
player = get_image(sprite_sheet_image, 0, 50, 100, 1, gray)
bullet = get_image(bulletpicture, 0, 5, 5, 1, gray)

clock = pygame.time.Clock()




        



run = True
while run:
    screen.fill(bg)
    #player animation
    screen.blit(player, (x, y))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 2
    if keys[pygame.K_RIGHT]:
        x += 2
    clock.tick(120)
    screen.blit(bulletpicture, (mx, my))
    if keys[pygame.K_SPACE]:
        my -=5
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

