import pygame


BACKGROUND_FOLDER = "assets/images/background/"


class Background:
    def __init__(self):
        self.bg_images = []
        for i in range(1, 6):
            bg_image = pygame.image.load(f"{BACKGROUND_FOLDER}/parallax_0/{i}.png").convert_alpha()
            bg_image = pygame.transform.scale(bg_image, (720, 480))
            self.bg_images.append(bg_image)
        self.width = self.bg_images[0].get_width()
        self.scroll = 0

    def update(self):
        self.scroll += 2

    def draw(self, screen):
        for n in range(5):
            for i, image in enumerate(self.bg_images):
                if i == 4:
                    continue
                screen.blit(image, (n * self.width - self.scroll, 0))
