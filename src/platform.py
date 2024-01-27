import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height=30, image=None):
        super().__init__()
        if image:
            self.image = pygame.transform.scale(image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)
