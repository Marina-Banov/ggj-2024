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

        self.bg = Background()
        self.player = Player()

    def update(self):
        self.bg.update()
        self.player.update(2)

    def draw(self):
        self.bg.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(self.fps)

    async def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    return
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()
            self.update()
            self.draw()
            await asyncio.sleep(0)


async def main():
    ggj_2024 = GGJ_2024()
    await ggj_2024.game_loop()


if __name__ == "__main__":
    asyncio.run(main())
