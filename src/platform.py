import pygame

from .constants import *


class Platform(pygame.sprite.Sprite):
    platform_image = None
    wall_image = None

    PLATFORM = 0
    WALL = 1

    @staticmethod
    def preload():
        Platform.platform_image = pygame.image.load(f"{ASSETS_IMAGES_FOLDER}platform.png")
        Platform.wall_image = pygame.image.load(f"{ASSETS_IMAGES_FOLDER}wall.png")

    def __init__(self, x, y, size, _type=PLATFORM):
        super().__init__()
        if _type == Platform.PLATFORM:
            self.width = size
            self.height = 30
            self.image = pygame.transform.scale(Platform.platform_image, (self.width, self.height))
        else:
            self.width = 180
            self.height = size
            self.image = pygame.transform.scale(Platform.wall_image, (self.width, self.height))
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def update(self):
        self.rect.x -= SCROLL_INCREMENT * 1.6
        if self.rect.x < -self.width:
            self.kill()
