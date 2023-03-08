import pygame
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

clock = pygame.time.Clock()

pygame.init()
pygame.display.init()

screen_width= 1000
screen_height= 700
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill((89, 5, 128))


class player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(player, self).__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("ship.gif").convert_alpha()
        self.rect = self.image.get_rect()

def update(self):
    self.rect = self.image.get_rect()

run = True
while run:
    #player animation
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_SPACE]:
        pass
    
    clock.tick(240)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
