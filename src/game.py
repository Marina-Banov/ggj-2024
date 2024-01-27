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
        self.platforms = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.start_time = pygame.time.get_ticks()
        self.is_shooting = False

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
        self.generate_platforms()
        self.platforms.update()
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
