import math
import pygame

from .constants import *


class Player:
    def __init__(self) -> None:
        self.x = SCREEN_HEIGHT * 0.7
        self.y = SCREEN_WIDTH * 0.5

        self.height = 130
        self.width = 60

        self.image = pygame.image.load(f"{ASSETS_CHARACTERS}mark.png")
        self.image = pygame.transform.scale(self.image, (130, 130))

        self.rect = pygame.Rect(0, 0, self.width - 5, self.height - 5)
        self.rect.center = (self.x, self.y)

        self.wobble_amplitude = 12
        self.wobble_frequency = 2
        self.wobble_phase = 0
        self.wobble_offset = 0

    def update(self, dy):
        if self.rect.y > 0:
            self.y -= dy
            self.rect.centery = self.y
        self.wobble_offset = self.wobble_amplitude * abs(math.sin(self.wobble_phase))
        self.wobble_phase += 0.1 * self.wobble_frequency

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x - 32, self.rect.y - self.wobble_offset))
        # pygame.draw.rect(screen, WHITE, self.rect, 2)
