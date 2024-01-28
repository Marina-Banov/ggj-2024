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
        self.player = Player(SCREEN_WIDTH * 0.44, GROUND - 150, 110, 150)
        self.enemy = Enemy()
        Platform.preload()
        self.platforms = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        Projectile.preload()
        self.projectiles = pygame.sprite.Group()
        self.start_time = pygame.time.get_ticks()
        self.is_shooting = False

    def generate_platforms(self):
        while len(self.platforms) < 8:
            p_w = random.randint(80, 200)
            if len(self.platforms) > 0:
                p_x = self.platforms.sprites()[-1].rect.x + random.randint(150, 250)
            else:
                p_x = random.randint(SCREEN_WIDTH, 1.5 * SCREEN_WIDTH - p_w)
            p_y = random.randint(150, GROUND - 180)
            platform = Platform(p_x, p_y, p_w, Platform.PLATFORM)
            self.platforms.add(platform)

    def generate_walls(self):
        while len(self.walls) < 2:
            p_h = random.randint(120, 250)
            if len(self.walls) > 0:
                p_x = self.walls.sprites()[-1].rect.x + random.randint(800, 1200)
            else:
                p_x = random.randint(SCREEN_WIDTH, 1.5 * SCREEN_WIDTH - p_h)
            wall = Platform(p_x, GROUND - p_h, p_h, Platform.WALL)
            self.walls.add(wall)

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
        if self.player.is_dead:
            return
        self.bg.update()
        self.generate_platforms()
        self.platforms.update()
        self.generate_walls()
        self.walls.update()
        self.player.update(self.platforms, self.walls)
        self.enemy.update(self.player)
        self.generate_projectiles()
        self.projectiles.update()

    def draw(self, screen):
        self.bg.draw(screen)
        self.platforms.draw(screen)
        self.walls.draw(screen)
        self.player.draw(screen)
        self.enemy.draw(screen)
        self.projectiles.draw(screen)

    # return the time passed from the start of the game (in seconds)
    def get_elapsed_time(self):
        return round((pygame.time.get_ticks() - self.start_time)/1000)
