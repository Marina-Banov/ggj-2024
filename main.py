import sys

import pygame

from src import *


class RonTontoTon:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("RonTontoTon")
        self.clock = pygame.time.Clock()
        pygame.mixer.init()
        SoundManager.preload()
        self.current_scene = Intro(self.clock)

    def game_loop(self):
        while True:
            if isinstance(self.current_scene, Intro) and self.current_scene.is_finished:
                self.current_scene = Game(self.clock)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    return
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()
                else:
                    self.current_scene.process_player_input(event)
            self.current_scene.update()
            self.current_scene.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(constants.FPS)
 

def main():
    ggj_2024 = RonTontoTon()
    ggj_2024.game_loop()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
