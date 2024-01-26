import sys

import pygame

import src
# from src import *


class GGJ_2024_Desktop:
    def __init__(self):
        self.init()
        self.blue = 35
        self.clock = pygame.time.Clock()
        self.fps = 60

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def update(self):
        self.blue = (self.blue + 1) % 255

    def draw(self):
        self.screen.fill((40, 41, self.blue))
        pygame.display.flip()
        self.clock.tick(self.fps)

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    return
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()
            self.update()
            self.draw()


def main():
    ggj_2024 = GGJ_2024_Desktop()
    ggj_2024.game_loop()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
