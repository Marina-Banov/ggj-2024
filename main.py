import asyncio

import pygame

from src import *


class GGJ_2024:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("GGJ 2024")
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.game = Game()

    async def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    return
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()
                else:
                    key = pygame.key.get_pressed()
                    self.game.process_player_input(key)
            self.game.update()
            self.game.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.fps)
            await asyncio.sleep(0)
 

async def main():
    ggj_2024 = GGJ_2024()
    await ggj_2024.game_loop()


if __name__ == "__main__":
    asyncio.run(main())
