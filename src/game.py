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
    # Initialize the mixer module
    # pygame.mixer.init()
    # Load a sound effect
    sound_warning = pygame.mixer.Sound(f"{ASSETS_SOUNDS}gasp.mp3")
    sound_shoot = pygame.mixer.Sound(f"{ASSETS_SOUNDS}scream.mp3")
    sound_death = pygame.mixer.Sound(f"{ASSETS_SOUNDS}shout.mp3")
    bg_music_game = pygame.mixer.Sound(f"{ASSETS_SOUNDS}combat_music.wav")

    def __init__(self, clock):
        Platform.preload()
        Projectile.preload()
        Enemy.preload()

        self.clock = clock
        self.bg = Background()
        self.player = Player(SCREEN_WIDTH * 0.44, GROUND - 150, 110, 150)
        self.enemy = Enemy()
        self.platforms = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.start_time = pygame.time.get_ticks()
        self.is_shooting = False
        font = pygame.font.Font(f"{ASSETS_FONT_FOLDER}FuturaHandwritten.ttf", 32)
        self.restart_text = font.render("You died. Press space to restart.", True, WHITE)
        self.restart_bubble = pygame.Rect(SCREEN_WIDTH // 2 - 245, SCREEN_HEIGHT // 2 - 30, 520, 55)
        self.warned = False

        Game.bg_music_game.play()

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
                m = random.randint(0, len(Platform.wall_messages)-1)
            else:
                p_x = random.randint(SCREEN_WIDTH, 1.5 * SCREEN_WIDTH - p_h)
                m = 0
            wall = Platform(p_x, GROUND - p_h, p_h, Platform.WALL, m)
            self.walls.add(wall)

    def generate_projectiles(self):
        if self.get_elapsed_time() > 0 and (self.get_elapsed_time() + 1) % 3 == 0 and not self.is_shooting:
            if not self.warned:
                Game.sound_warning.play()
                self.enemy.warning()
                self.warned = True

        if self.get_elapsed_time() > 0 and self.get_elapsed_time() % 3 == 0 and not self.is_shooting:
            self.warned = False
            Game.sound_shoot.play()
            self.enemy.shoot()
            self.is_shooting = True
            angle = math.atan2(self.player.rect.y - self.enemy.rect.y, self.player.rect.x - self.enemy.rect.x)
            new_projectile = Projectile(self.enemy.rect.x + self.enemy.width, self.enemy.rect.y + 80, math.degrees(angle))
            self.projectiles.add(new_projectile)

        if len(self.projectiles) == 0:
            self.is_shooting = False

    def process_player_input(self, _):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            if self.player.is_dead:
                self.bg = Background()
                self.player = Player(SCREEN_WIDTH * 0.44, GROUND - 150, 110, 150)
                self.enemy = Enemy()
                self.platforms = pygame.sprite.Group()
                self.walls = pygame.sprite.Group()
                self.projectiles = pygame.sprite.Group()
                self.start_time = pygame.time.get_ticks()
                self.is_shooting = False
            else:
                self.player.jump()

    def update(self):
        if self.player.is_dead:
            return
        self.bg.update()
        self.generate_platforms()
        self.platforms.update()
        self.generate_walls()
        self.walls.update()
        self.player.update(self.platforms, self.walls, self.projectiles)
        self.enemy.update(self.player)
        self.generate_projectiles()
        self.projectiles.update()

    def draw(self, screen):
        self.bg.draw(screen)
        self.platforms.draw(screen)
        for w in self.walls.sprites():
            w.draw(screen)
        self.player.draw(screen)
        self.enemy.draw(screen)
        self.projectiles.draw(screen)
        for p in self.projectiles.sprites():
            p.draw(screen)
        if self.player.is_dead:
            pygame.draw.rect(screen, BLACK, self.restart_bubble, border_radius=30)
            screen.blit(self.restart_text, (SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 - 25))

    # return the time passed from the start of the game (in seconds)
    def get_elapsed_time(self):
        return round((pygame.time.get_ticks() - self.start_time)/1000)
