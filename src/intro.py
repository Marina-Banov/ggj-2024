import random
import pygame

from .player import Player
from .constants import *


class Intro:
    LABORATORY = 0
    COLOR_BURST = 1
    END = 2

    def __init__(self):
        self.scene = 0
        self.is_finished = True
        self.space_clicked = 0

        self.laboratory_image = pygame.image.load(f"{ASSETS_BG_FOLDER}laboratory.png").convert_alpha()
        self.laboratory_image = pygame.transform.scale(self.laboratory_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        # Image by <a href="https://www.freepik.com/free-vector/flat-laboratory-room-illustration_12983121.htm
        # ">Freepik</a>

        self.player = Player(250, 470, 220, 300)
        self.font = pygame.font.Font(f"{ASSETS_FONT_FOLDER}FuturaHandwritten.ttf", 32)
        self.text = [
            "I did it! I achieved my lifelong dream!",
            "I built the perfect time machine!",
            "I can finally meet my idol, Einstein!",
            "It's working!",
            "Hi Einstein! I love you!",
            "Look what I made!",
            "Time travel is now possible thanks to me!",
            "Wait... Something's not right...",
            "My machine is falling apart!",
            "Oh no, Einstein, I'm so sorry!",
            "It seems like we are going to",
            "the dinosaur age!",
            "Please, Einstein, don't be mad!",
        ]
        self.labels = [
            [self.font.render(line, True, BLACK) for line in self.text[:3]],
            [self.font.render(self.text[3], True, BLACK)],
            [self.font.render(line, True, BLACK) for line in self.text[4:7]],
            [self.font.render(line, True, BLACK) for line in self.text[7:9]],
            [self.font.render(self.text[9], True, BLACK)],
            [self.font.render(line, True, BLACK) for line in self.text[10:12]],
            [self.font.render(self.text[12], True, BLACK)],
        ]
        self.monologue_step = 0
        self.bubble = None
        self.update_bubble()

        self.color_burst = []

        self.counter = 0
        self.last_update = pygame.time.get_ticks()

        self.instructions = self.font.render("Press space", True, WHITE)
        self.instructions_bubble = pygame.Rect(SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT - 105, 240, 50)

    def process_player_input(self, key):
        if key[pygame.K_SPACE]:
            if self.space_clicked == 0:
                self.monologue_step += 1
                self.update_bubble()
                if self.monologue_step in [1, 7]:
                    self.scene += 1
                self.space_clicked = self.counter
            self.is_finished = (self.scene == Intro.END)

    def burst(self):
        if self.counter % 10 == 0:
            self.color_burst.append(ColorCircle())
        for i, circle in enumerate(reversed(self.color_burst)):
            circle.r += 2 * (i + 1)
        while len(self.color_burst) > 10:
            del self.color_burst[0]

    def update_bubble(self):
        if self.monologue_step >= len(self.labels):
            return
        w = max([line.get_width() for line in self.labels[self.monologue_step]]) + 40
        h = len(self.labels[self.monologue_step]) * 32 + 15 * (len(self.labels[self.monologue_step])-1) + 40
        x = SCREEN_WIDTH // 2 - 85 - w // 2
        y = SCREEN_HEIGHT // 2 - 165
        self.bubble = pygame.Rect(x, y, w, h)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > FPS:
            self.last_update = now
            self.counter += 1
        if (self.counter - self.space_clicked) == 15:
            self.space_clicked = 0
        if self.scene == Intro.LABORATORY:
            self.player.wobble()
        elif self.scene == Intro.COLOR_BURST:
            self.burst()

    def draw(self, screen):
        if self.scene == Intro.LABORATORY:
            screen.blit(self.laboratory_image, (0, 0))
            self.draw_monologue(screen)
            self.player.draw(screen)
        elif self.scene == Intro.COLOR_BURST:
            for circle in self.color_burst:
                pygame.draw.circle(screen, circle.color, (circle.x, circle.y), circle.r)
            self.draw_monologue(screen)
        pygame.draw.rect(screen, BLACK, self.instructions_bubble, border_radius=20)
        screen.blit(
            self.instructions,
            (SCREEN_WIDTH // 2 - self.instructions.get_width() // 2, SCREEN_HEIGHT - 100)
        )

    def draw_monologue(self, screen):
        if self.monologue_step >= len(self.labels):
            return
        pygame.draw.rect(screen, WHITE, self.bubble, border_radius=30)
        for line, label in enumerate(self.labels[self.monologue_step]):
            screen.blit(
                label,
                (
                    SCREEN_WIDTH // 2 - 85 - label.get_width() // 2,
                    SCREEN_HEIGHT // 2 - 150 + line * 32 + 15 * line
                )
            )


class ColorCircle:
    colors = [(250, 169, 22), (251, 255, 254), (109, 103, 110), (27, 27, 30), (150, 3, 26)]

    def __init__(self):
        self.x = (SCREEN_WIDTH - 2) // 2
        self.y = (SCREEN_HEIGHT - 2) // 2
        self.r = 2
        self.color = ColorCircle.colors[random.randint(0, 4)]
