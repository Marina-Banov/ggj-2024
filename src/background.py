import pygame

from .constants import *


class Background:
    def __init__(self):
        self.bg_images = []
        for i in range(6):
            bg_image = pygame.image.load(f"{ASSETS_BG_FOLDER}/parallax_0/{i+1}.png").convert_alpha()
            bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.bg_images.append(bg_image)
        self.width = self.bg_images[0].get_width()
        self.scroll = 0

    def update(self):
        self.scroll += 3

    def draw(self, screen):
        for n in range(10):
            speed = 1
            for i, image in enumerate(self.bg_images):
                pos = n * self.width - self.scroll * speed
                speed += 0.2
                speed = round(speed, 2)
                if -SCREEN_WIDTH < pos < SCREEN_WIDTH:
                    screen.blit(image, (pos, 0))
