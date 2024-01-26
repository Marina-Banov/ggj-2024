import pygame

from .constants import *


class Background:
    def __init__(self):
        self.bg_images = []
        for i in range(1, 6):
            if i == 5:
                continue
            bg_image = pygame.image.load(f"{ASSETS_BG_FOLDER}/parallax_0/{i}.png").convert_alpha()
            bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.bg_images.append(bg_image)
        self.width = self.bg_images[0].get_width()
        self.scroll = 0

    def update(self):
        if self.scroll < self.width * len(self.bg_images) / 2:
            self.scroll += 3

    def draw(self, screen):
        for n in range(5):
            speed = 1
            for i, image in enumerate(self.bg_images):
                screen.blit(image, (n * self.width - self.scroll * speed, 0))
                speed += 0.2
