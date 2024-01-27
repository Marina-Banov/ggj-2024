import math
import pygame

from .constants import *


class Enemy:
    def __init__(self) -> None:

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

        # self.jumping = False
        # self.standing = True

    # def jump(self):
    #     self.jumping = True

    def update(self, player):
        vel_y = (player.rect.y - self.rect.y) / 30
        self.rect.y += vel_y
        
        self.wobble_offset = self.wobble_amplitude * abs(math.sin(self.wobble_phase))
        self.wobble_phase += 0.1 * self.wobble_frequency

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x - 32, self.rect.y - self.wobble_offset))
        # pygame.draw.rect(screen, WHITE, self.rect, 2)
