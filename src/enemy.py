import math
import pygame

from .constants import *


class Enemy:
    cloud = []
    images = []

    @staticmethod
    def preload():
        for i in range(16):
            c = pygame.image.load(f"{ASSETS_IMAGES_FOLDER}cloud/{i}.png").convert_alpha()
            Enemy.cloud.append(pygame.transform.scale(c, (160, 90)))
        for i in range(3):
            img = pygame.image.load(f"{ASSETS_IMAGES_FOLDER}enemy/{i}.png").convert_alpha()
            Enemy.images.append(img)

    def __init__(self):
        self.is_shooting = False
        self.is_warned = False

        self.cloud_anim_index = 0
        self.image_cloud = Enemy.cloud[self.cloud_anim_index]

        self.height = 130
        self.width = 70

        self.x = SCREEN_WIDTH * 0.1
        self.y = GROUND - self.height
        
        self.vel_y = 0

        self.image = Enemy.images[0]

        self.rect = pygame.Rect(0, 0, self.width - 5, self.height - 5)
        self.rect.center = (self.x, self.y)

        self.wobble_amplitude = 5
        self.wobble_frequency = 8
        self.wobble_phase = 1
        self.wobble_offset = 1
        self.last_update = pygame.time.get_ticks()
        self.last_shot = 0

    def warning(self):
        self.is_warned = True
        self.image = Enemy.images[1]
        self.last_shot = pygame.time.get_ticks()

    def shoot(self):
        self.is_warned = False
        self.is_shooting = True
        self.image = Enemy.images[2]
        self.last_shot = pygame.time.get_ticks()

    def update(self, player):
        now = pygame.time.get_ticks()

        if abs(self.last_shot - now) > 1000:
            self.image = Enemy.images[0]

        # Animate cloud
        if now - self.last_update > FPS:
            self.last_update = now
            self.cloud_anim_index = (self.cloud_anim_index + 1) % len(Enemy.cloud)
            self.image_cloud = Enemy.cloud[self.cloud_anim_index]
            
        vel_y = (player.rect.y - self.rect.y) / 30
        self.rect.y += vel_y
        
        self.wobble_offset = self.wobble_amplitude * abs(math.sin(self.wobble_phase))
        self.wobble_phase += 0.1 * self.wobble_frequency

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x - 32, self.rect.y - self.wobble_offset))
        screen.blit(self.image_cloud, (self.rect.x - 70, self.rect.y + 80))
        # pygame.draw.rect(screen, WHITE, self.rect, 2)
