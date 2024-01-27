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
        self.ground = Platform(0, SCREEN_HEIGHT - 20, SCREEN_WIDTH)
        self.platforms = pygame.sprite.Group()
        platform_image = pygame.image.load(f"{ASSETS_IMAGES_FOLDER}platform.png")
        for p in range(10):
            p_w = random.randint(80, 140)
            p_x = random.randint(0, SCREEN_WIDTH - p_w)
            p_y = p * random.randint(80, 120)
            platform = Platform(p_x, p_y, p_w, image=platform_image)
            self.platforms.add(platform)

    def process_player_input(self, key):
        if key[pygame.K_SPACE]:
            self.player.jump()

    def update(self):
        self.bg.update()
        self.player.update(self.platforms)

    def draw(self, screen):
        self.bg.draw(screen)
        self.player.draw(screen)
        self.platforms.draw(screen)
