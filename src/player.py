import math
import pygame

from .constants import *


class Player:
    pygame.mixer.init()

    sound_death = pygame.mixer.Sound(f"{ASSETS_SOUNDS}shout.mp3")
    sound_jump = pygame.mixer.Sound(f"{ASSETS_SOUNDS}jump.mp3")

    def __init__(self, rect_x, rect_y, image_width, image_height):
        self.is_jumping = False
        self.is_standing = True
        self.is_dead = False

        self.image = pygame.image.load(f"{ASSETS_CHARACTERS}serena.png")
        self.image = pygame.transform.scale(self.image, (image_width, image_height))
        self.image_width = image_width
        self.image_height = image_height

        self.rect = pygame.Rect(rect_x, rect_y, self.image_width * 0.5, self.image_height * 0.7)
        self.vel_y = 0

        self.wobble_amplitude = 12
        self.wobble_frequency = 2
        self.wobble_phase = 0
        self.wobble_offset = 0

    def jump(self):
        if self.is_standing:
            Player.sound_jump.play()
        self.is_jumping = True

    def update(self, platforms, walls, projectiles):
        self.wobble()

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
            if p.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.rect.bottom < p.rect.centery:
                    if self.vel_y:
                        self.rect.bottom = p.rect.top
                        dy = 0
                        self.is_standing = True

        # Check the list of colliding platforms
        for w in walls:
            if w.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                Player.sound_death.play()
                self.is_dead = True
        
        # Check the list of colliding projectiles
        for projectile in projectiles:
            if projectile.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                Player.sound_death.play()
                self.is_dead = True

        self.rect.y += dy

    def wobble(self):
        self.rect.y -= self.wobble_offset
        self.wobble_offset = self.wobble_amplitude * abs(math.sin(self.wobble_phase))
        self.wobble_phase += 0.1 * self.wobble_frequency
        self.rect.y += self.wobble_offset

    def draw(self, screen):
        screen.blit(
            self.image,
            (
                self.rect.x - self.image_width * 0.35,
                self.rect.y - self.image_height * 0.3
            )
        )
        # pygame.draw.rect(screen, WHITE, self.rect, 2)
