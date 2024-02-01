import random
import pygame

from .player import Player
from .constants import *


class Intro:
    LABORATORY = 0
    COLOR_BURST = 1
    END = 2

    pygame.mixer.init()
    bg_music_intro = pygame.mixer.Sound(f"{ASSETS_SOUNDS}intro_music.mp3")

    def __init__(self):
        self.scene = 0
        self.is_finished = False
        self.counter = 0
        self.last_update = pygame.time.get_ticks()

        self.laboratory_image = pygame.image.load(f"{ASSETS_BG_FOLDER}laboratory.png").convert_alpha()
        self.laboratory_image = pygame.transform.scale(self.laboratory_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        #

        self.player = Player(250, 470, 220, 300)

        Bubble.preload()
        self.text = [
            ["I did it! I achieved my lifelong dream!", "I built the perfect time machine!", "I can finally meet my idol, Einstein!"],
            ["It's working!"],
            ["Hi Einstein! I love you!", "Look what I made!", "Time travel is now possible thanks to me!"],
            ["Wait... Something's not right...", "My machine is falling apart!"],
            ["Oh no, Einstein, I'm so sorry!"],
            ["It seems like we are going to", "the dinosaur age!"],
            ["Please, Einstein, don't be mad!"],
        ]
        self.bubbles = [Bubble(lines, WHITE, BLACK, -85, -165) for lines in self.text]
        self.monologue_step = 0
        self.instructions_bubble = Bubble(["Press space"], BLACK, WHITE, 0, 250, (240, 50))

        self.color_burst = []

        Intro.bg_music_intro.play()

    def process_player_input(self, event):
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            self.monologue_step += 1
            if self.monologue_step in [1, 7]:
                self.scene += 1
            if self.scene == Intro.END:
                self.is_finished = True
                Intro.bg_music_intro.stop()

    def burst(self):
        if self.counter % 10 == 0:
            self.color_burst.append(ColorCircle())
        for i, circle in enumerate(reversed(self.color_burst)):
            circle.r += 2 * (i + 1)
        while len(self.color_burst) > 10:
            del self.color_burst[0]

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > FPS:
            self.last_update = now
            self.counter += 1
        if self.scene == Intro.LABORATORY:
            self.player.wobble()
        elif self.scene == Intro.COLOR_BURST:
            self.burst()

    def draw(self, screen):
        if self.scene == Intro.LABORATORY:
            screen.blit(self.laboratory_image, (0, 0))
            self.bubbles[self.monologue_step].draw(screen)
            self.player.draw(screen)
        elif self.scene == Intro.COLOR_BURST:
            for circle in self.color_burst:
                pygame.draw.circle(screen, circle.color, (circle.x, circle.y), circle.r)
            if self.monologue_step < len(self.text):
                self.bubbles[self.monologue_step].draw(screen)
        self.instructions_bubble.draw(screen)


class ColorCircle:
    colors = [(250, 169, 22), (251, 255, 254), (109, 103, 110), (27, 27, 30), (150, 3, 26)]

    def __init__(self):
        self.x = (SCREEN_WIDTH - 2) // 2
        self.y = (SCREEN_HEIGHT - 2) // 2
        self.r = 2
        self.color = ColorCircle.colors[random.randint(0, 4)]


class Bubble:
    font = None

    @staticmethod
    def preload():
        Bubble.font = pygame.font.Font(f"{ASSETS_FONT_FOLDER}FuturaHandwritten.ttf", 32)

    def __init__(self, lines, bg_color=WHITE, fg_color=BLACK, offsetx=0, offsety=0, size=None):
        self.bg_color = bg_color
        self.lines = [Bubble.font.render(line, True, fg_color) for line in lines]

        if size is None:
            w = max([line.get_width() for line in self.lines]) + 40
            h = len(lines) * 32 + 15 * (len(lines) - 1) + 40
        else:
            w, h = size
        x = SCREEN_WIDTH // 2 + offsetx - w // 2
        y = SCREEN_HEIGHT // 2 + offsety
        self.rect = pygame.Rect(x, y, w, h)
        self.ls = 15 if size is None else h // 2 - 20

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect, border_radius=30)
        for line, label in enumerate(self.lines):
            screen.blit(
                label,
                (
                    self.rect.x + self.rect.width // 2 - label.get_width() // 2,
                    self.rect.y + line * 32 + self.ls * (line + 1)
                )
            )
