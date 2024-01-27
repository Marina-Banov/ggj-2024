import pygame
import math
from .constants import *

class Projectile(pygame.sprite.Sprite):
    images = []

    def preload():
        # Add your animation frames to the list (assuming you have fireball_1.png, fireball_2.png, etc.)
        for i in range(6):
            image = pygame.image.load(f"{ASSETS_IMAGES_FOLDER}projectile/{i+1}.png").convert_alpha()
            Projectile.images.append(pygame.transform.scale(image, (180, 180)))

    def __init__(self, x, y, angle):
        super().__init__()
        
        self.index = 0  # Current frame index
        self.image = Projectile.images[self.index]

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = 10  # Adjust the speed of the projectile
        self.angle = math.radians(angle)  # Convert the angle to radians

        self.last_update = pygame.time.get_ticks()

    def update(self):
        # Animate the projectile
        now = pygame.time.get_ticks()
        if now - self.last_update > FPS:
            self.last_update = now
            self.index = (self.index + 1) % len(Projectile.images)
            self.image = Projectile.images[self.index]

        # Rotate the projectile image based on its angle
        self.image = pygame.transform.rotate(Projectile.images[self.index], math.degrees(self.angle))
        self.rect = self.image.get_rect(center=self.rect.center)

        # Move the projectile based on its angle and speed
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y -= self.speed * math.sin(self.angle)

        # If the projectile goes off the screen, remove it
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH or self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# Example of how to use the Projectile class:

# In your main game loop or wherever you handle the enemy shooting:
# Assuming enemy_x, enemy_y, and player_x, player_y are the positions of the enemy and player

# Calculate the angle between the enemy and player
#angle = math.atan2(player_y - enemy_y, player_x - enemy_x)

# Create a new projectile and add it to a sprite group (all_projectiles)
#new_projectile = Projectile(enemy_x, enemy_y, math.degrees(angle))
#all_projectiles.add(new_projectile)
