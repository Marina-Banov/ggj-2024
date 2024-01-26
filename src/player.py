import pygame
from . import constants


class Player:
    def __init__(self) -> None:
        self.x = constants.SCREEN_HEIGHT * 0.7
        self.y = constants.SCREEN_WIDTH * 0.5

        self.height = 130
        self.width = 60

        self.image = pygame.image.load(f"{constants.ASSETS_CHARACTERS}mark.png")
        self.image = pygame.transform.scale(self.image, (130, 130))

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.x, self.y)

    def update(self, x, y):
        self.x += (x * 0.1)
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x - 32, self.rect.y))
        # pygame.draw.rect(screen, constants.WHITE, self.rect, 2)
