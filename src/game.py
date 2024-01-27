import random
import pygame

from .background import Background
from .platform import Platform
from .player import Player
from .constants import *


class Game:
    def __init__(self):
        self.bg = Background()
        self.player = Player()
        self.platforms = pygame.sprite.Group()

    def generate_platforms(self):
        while len(self.platforms) < 10:
            p_w = random.randint(100, 180)
            if len(self.platforms) > 0:
                p_x = self.platforms.sprites()[-1].rect.x + random.randint(150, 250)
            else:
                p_x = random.randint(SCREEN_WIDTH, 1.5 * SCREEN_WIDTH - p_w)
            p_y = random.randint(self.player.height, GROUND - 50)
            platform = Platform(p_x, p_y, p_w)
            self.platforms.add(platform)

    def process_player_input(self, key):
        if key[pygame.K_SPACE]:
            self.player.jump()

    def update(self):
        self.bg.update()
        self.generate_platforms()
        self.platforms.update()
        self.player.update(self.platforms)

    def draw(self, screen):
        self.bg.draw(screen)
        self.platforms.draw(screen)
        self.player.draw(screen)
