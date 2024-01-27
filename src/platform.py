import pygame

from .constants import *


class Platform(pygame.sprite.Sprite):
    platform_image = None

    def preload():
        Platform.platform_image = pygame.image.load(f"{ASSETS_IMAGES_FOLDER}platform.png")

    def __init__(self, x, y, width, height=30):
        super().__init__()
        self.image = pygame.transform.scale(Platform.platform_image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.width = width

    def update(self):
        self.rect.x -= SCROLL_INCREMENT * 1.6
        if self.rect.x < -self.width:
            self.kill()
