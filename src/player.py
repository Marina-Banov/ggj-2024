import math
import pygame

from .constants import *

class Player:
    pygame.mixer.init()

    sound_deathh = pygame.mixer.Sound(f"{ASSETS_SOUNDS}shout.mp3")

    def __init__(self, x, y, width, height):
        self.height = height
        self.width = width

        self.x = x
        self.y = y
        
        self.vel_y = 0

        self.image = pygame.image.load(f"{ASSETS_CHARACTERS}serena.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = pygame.Rect(5, 5, self.width - 10, self.height - 10)
        self.rect.center = (self.x, self.y)

        self.wobble_amplitude = 12
        self.wobble_frequency = 2
        self.wobble_phase = 0
        self.wobble_offset = 0

        self.is_jumping = False
        self.is_standing = True
        self.is_dead = False

    def jump(self):
        self.is_jumping = True

    def update(self, platforms, walls, projectiles):
        dy = 0
        if not self.is_standing:
            self.vel_y += GRAVITY
        dy += self.vel_y

        if self.is_jumping:
            self.vel_y = -20
            self.is_jumping = False

        # check collision with ground
        if self.rect.bottom + dy > GROUND:
            dy = 0
            self.is_standing = True
        else:
            self.is_standing = False

        # Check the list of colliding platforms
        for p in platforms:
            if p.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.rect.bottom < p.rect.centery:
                    if self.vel_y:
                        self.rect.bottom = p.rect.top
                        dy = 0
                        self.is_standing = True

        # Check the list of colliding platforms
        for w in walls:
            if w.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                Player.sound_deathh.play()
                self.is_dead = True
        
        # Check the list of colliding projectiles
        for projectile in projectiles:
            if projectile.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
                Player.sound_deathh.play()
                self.is_dead = True

        self.rect.y += dy

        self.wobble()

    def wobble(self):
        self.wobble_offset = self.wobble_amplitude * abs(math.sin(self.wobble_phase))
        self.wobble_phase += 0.1 * self.wobble_frequency

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x - 5, self.rect.y - self.wobble_offset))
        # pygame.draw.rect(screen, WHITE, self.rect, 2)
