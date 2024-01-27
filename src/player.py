import math
import pygame

from .constants import *


class Player:
    def __init__(self) -> None:

        self.height = 130
        self.width = 60

        self.x = SCREEN_WIDTH * 0.44
        self.y = GROUND - self.height
        
        self.vel_y = 0

        self.image = pygame.image.load(f"{ASSETS_CHARACTERS}mark.png")
        self.image = pygame.transform.scale(self.image, (130, 130))

        self.rect = pygame.Rect(0, 0, self.width - 5, self.height - 5)
        self.rect.center = (self.x, self.y)

        self.wobble_amplitude = 12
        self.wobble_frequency = 2
        self.wobble_phase = 0
        self.wobble_offset = 0

        self.jumping = False
        self.standing = True

    def jump(self):
        self.jumping = True

    def update(self, platforms):
        dy = 0
        if not self.standing:
            self.vel_y += GRAVITY
        dy += self.vel_y

        if self.jumping:
            self.vel_y = -20
            self.jumping = False

        # check collision with ground
        if self.rect.bottom + dy > GROUND:
            dy = 0
            self.standing = True
        else:
            self.standing = False

        # Check the list of colliding platforms
        for p in platforms:
            if p.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.rect.bottom < p.rect.centery:
                    if self.vel_y:
                        self.rect.bottom = p.rect.top
                        dy = 0
                        self.standing = True

        self.rect.y += dy

        self.wobble_offset = self.wobble_amplitude * abs(math.sin(self.wobble_phase))
        self.wobble_phase += 0.1 * self.wobble_frequency

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x - 32, self.rect.y - self.wobble_offset))
        # pygame.draw.rect(screen, WHITE, self.rect, 2)
