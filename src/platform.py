import pygame

from .constants import *


class Platform(pygame.sprite.Sprite):
    platform_image = None
    wall_image = None
    font = None

    PLATFORM = 0
    WALL = 1

    wall_messages = [
        ["Hit space", "to jump"],
        ["Avoid walls"],
        ["Walls will", "kill you"],
        ["Einstein WILL", "kill you"],
    ]

    @staticmethod
    def preload():
        Platform.platform_image = pygame.image.load(f"{ASSETS_IMAGES_FOLDER}platform.png")
        Platform.wall_image = pygame.image.load(f"{ASSETS_IMAGES_FOLDER}wall.png")
        Platform.font = pygame.font.Font(f"{ASSETS_FONT_FOLDER}FuturaHandwritten.ttf", 32)

    def __init__(self, x, y, size, _type=PLATFORM, m=0):
        super().__init__()
        if _type == Platform.PLATFORM:
            self.width = size
            self.height = 30
            self.image = pygame.transform.scale(Platform.platform_image, (self.width, self.height))
        else:
            self.width = 180
            self.height = size
            self.image = pygame.transform.scale(Platform.wall_image, (self.width, self.height))
        self._type = _type
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.labels = [Platform.font.render(mess, True, WHITE) for mess in Platform.wall_messages[m]]

    def update(self):
        self.rect.x -= SCROLL_INCREMENT * 1.6
        if self.rect.x < -self.width:
            self.kill()

    def draw(self, screen):
        if self._type == Platform.WALL:
            screen.blit(self.image, (self.rect.x, self.rect.y))
            for line, label in enumerate(self.labels):
                screen.blit(
                    label,
                    (
                        self.rect.x + self.rect.width // 2 - label.get_width() // 2,
                        self.rect.y + 10 + line * 32 + 15 * line
                    )
                )
