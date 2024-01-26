import asyncio

import pygame

from main_desktop import GGJ_2024_Desktop


class GGJ_2024(GGJ_2024_Desktop):
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))

    async def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    return
            self.update()
            self.draw()
            await asyncio.sleep(0)


async def main():
    ggj_2024 = GGJ_2024()
    await ggj_2024.game_loop()


asyncio.run(main())
