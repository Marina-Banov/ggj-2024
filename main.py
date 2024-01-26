import sys

import pygame

import src
# from src import *


pygame.init()


def main():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
        screen.fill((40, 41, 35))
        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
