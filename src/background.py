import pygame

from .constants import *


class Background:
    def __init__(self):
        self.bg_images = []
        for i in range(6):
            bg_image = pygame.image.load(f"{ASSETS_BG_FOLDER}parallax_1/{i+1}.png").convert_alpha()
            bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.bg_images.append(bg_image)
        self.width = self.bg_images[0].get_width()
        self.scroll = 0
        self.n_layers = [0, 0, 0, 0, 0, 0]
        self.pos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.speeds = [0.4, 0.6, 0.8, 1.0, 1.2, 1.6]

    def update(self):
        self.scroll += SCROLL_INCREMENT
        for i, image in enumerate(self.bg_images):
            pos = self.n_layers[i] * self.width - self.scroll * self.speeds[i]
            if -SCREEN_WIDTH < pos < SCREEN_WIDTH:
                self.pos[i] = pos
            else:
                self.n_layers[i] += 1
                self.pos[i] = self.n_layers[i] * self.width - self.scroll * self.speeds[i]

    def draw(self, screen):
        for i, image in enumerate(self.bg_images):
            screen.blit(image, (self.pos[i], 0))
            screen.blit(image, (self.pos[i] + SCREEN_WIDTH, 0))
