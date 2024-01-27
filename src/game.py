import random
import pygame
import math

from .background import Background
from .enemy import Enemy
from .platform import Platform
from .player import Player
from .projectile import Projectile
from .constants import *


class Game:
    def __init__(self):
        self.bg = Background()
        self.player = Player()
        self.enemy = Enemy()
        self.ground = Platform(0, GROUND, SCREEN_WIDTH)
        self.platforms = pygame.sprite.Group()
        platform_image = pygame.image.load(f"{ASSETS_IMAGES_FOLDER}platform.png")
        for p in range(10):
            p_w = random.randint(80, 140)
            p_x = random.randint(0, SCREEN_WIDTH - p_w)
            p_y = p * random.randint(80, 120)
            platform = Platform(p_x, p_y, p_w, image=platform_image)
            self.platforms.add(platform)
        self.projectiles = pygame.sprite.Group()
        self.start_time = pygame.time.get_ticks()
        self.is_shooting = False

    def generate_projectiles(self):
        if self.get_elapsed_time() > 0 and self.get_elapsed_time() % 2 == 0 and not self.is_shooting:
            self.is_shooting = True
            angle = math.atan2(self.player.rect.y - self.enemy.rect.y, self.player.rect.x - self.enemy.rect.x)
            new_projectile = Projectile(self.enemy.rect.x, self.enemy.rect.y, math.degrees(angle))
            self.projectiles.add(new_projectile)
        if len(self.projectiles) == 0:
            self.is_shooting = False

    def process_player_input(self, key):
        if key[pygame.K_SPACE]:
            self.player.jump()

    def update(self):
        self.bg.update()
        self.player.update(self.platforms)
        self.enemy.update(self.player)
        self.generate_projectiles()
        self.projectiles.update()

    def draw(self, screen):
        self.bg.draw(screen)
        self.player.draw(screen)
        self.enemy.draw(screen)
        self.platforms.draw(screen)
        self.projectiles.draw(screen)

    # return the time passed from the start of the game (in seconds)
    def get_elapsed_time(self):
        return round((pygame.time.get_ticks() - self.start_time)/1000)