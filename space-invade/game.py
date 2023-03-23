import pygame
import os
import random

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Space Invaders")

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Set up the game sprites
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30, 30])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width/2
        self.rect.bottom = screen_height - 10
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE]:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)

        # Keep the player within the screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30, 30])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randrange(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > screen_height + 10:
            self.kill()

# Create the sprite groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Add the player sprite to the all_sprites group
player = Player()
all_sprites.add(player)

# Set up the game loop
done = False
score = 0
font = pygame.font.Font(None, 36)

# Set up the enemy spawn timer
enemy_spawn_timer = 0
enemy_spawn_delay = 1000  # milliseconds

while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Spawn new enemies
    if len(enemies) < 10 and pygame.time.get_ticks() - enemy_spawn_timer > enemy_spawn_delay:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        enemy_spawn_timer = pygame.time.get_ticks()

    # Update the sprites
    all_sprites.update()

    # Check for collisions between bullets and enemies
    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for hit in hits:
        score += 1

    # Draw the sprites
    screen.fill((0, 0, 0))
    for sprite in all_sprites:
        pygame.draw.rect(screen, (255, 255, 255), sprite.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
