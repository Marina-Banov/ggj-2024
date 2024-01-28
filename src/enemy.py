import math
import pygame

from .constants import *

class Enemy:
    cloud = []

    @staticmethod
    def preload():
        # Add your animation frames to the list (assuming you have fireball_1.png, fireball_2.png, etc.)
        for i in range(16):
            c = pygame.image.load(f"{ASSETS_IMAGES_FOLDER}cloud/{i}.png").convert_alpha()
            Enemy.cloud.append(pygame.transform.scale(c, (160, 90)))
        

    def __init__(self):
        self.cloud_anim_index = 0
        self.image_cloud = Enemy.cloud[self.cloud_anim_index]

        self.height = 130
        self.width = 70

        self.x = SCREEN_WIDTH * 0.1
        self.y = GROUND - self.height
        
        self.vel_y = 0

        self.image = pygame.image.load(f"{ASSETS_IMAGES_FOLDER}enemy.png")
        #self.image = pygame.transform.scale(self.image, (130, 130))

        self.rect = pygame.Rect(0, 0, self.width - 5, self.height - 5)
        self.rect.center = (self.x, self.y)

        self.wobble_amplitude = 13
        self.wobble_frequency = 8
        self.wobble_phase = 1
        self.wobble_offset = 1
        self.last_update = pygame.time.get_ticks()


    def update(self, player):
        # Animate cloud
        now = pygame.time.get_ticks()
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
