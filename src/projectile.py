import pygame
import math
from .constants import *


class Projectile(pygame.sprite.Sprite):
    images = []
    cloud = []

    @staticmethod
    def preload():
        # Add your animation frames to the list (assuming you have fireball_1.png, fireball_2.png, etc.)
        for i in range(6):
            image = pygame.image.load(f"{ASSETS_IMAGES_FOLDER}projectile/{i+1}.png").convert_alpha()
            Projectile.images.append(pygame.transform.smoothscale(image, (160, 80)))
        
    def __init__(self, x, y, angle):
        super().__init__()
        self.index = 0  # Current frame index
        self.image = Projectile.images[self.index]
        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        self.rect = pygame.Rect(x - self.height / 2 + 20, y - self.width / 2 + 20, self.width - 40, self.height - 40)#self.image.get_rect()

        self.speed = 10
        self.angle = math.radians(angle)

        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > FPS:
            self.last_update = now
            self.index = (self.index + 1) % len(Projectile.images)
            self.image = Projectile.images[self.index]
            self.image = pygame.transform.rotate(self.image, math.degrees(self.angle))
            
            # self.surf = pygame.Surface((self.rect.width, self.rect.height))
            # self.surf = pygame.transform.rotate(self.surf, math.degrees(self.angle))
            # self.rect = self.surf.get_rect(center=self.rect.center)
            
        #self.rect = self.image.get_rect(center=self.rect.center)

        self.rect.centerx += self.speed * math.cos(self.angle)
        self.rect.centery -= self.speed * math.sin(self.angle)

        # If the projectile goes off the screen, remove it
        if not -self.width < self.rect.x < SCREEN_WIDTH or not -self.height < self.rect.y < SCREEN_HEIGHT:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x - 20, self.rect.y - 20))
        # pygame.draw.rect(screen, WHITE, self.rect, 2)



# Example of how to use the Projectile class:

# In your main game loop or wherever you handle the enemy shooting:
# Assuming enemy_x, enemy_y, and player_x, player_y are the positions of the enemy and player

# Calculate the angle between the enemy and player
#angle = math.atan2(player_y - enemy_y, player_x - enemy_x)

# Create a new projectile and add it to a sprite group (all_projectiles)
#new_projectile = Projectile(enemy_x, enemy_y, math.degrees(angle))
#all_projectiles.add(new_projectile)
