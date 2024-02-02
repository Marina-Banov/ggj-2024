import pygame

from .constants import *


class SoundManager:
    ENEMY_WARNING = "ENEMY_WARNING"
    ENEMY_SHOOT = "ENEMY_SHOOT"
    MUSIC_INTRO = "MUSIC_INTRO"
    MUSIC_GAME = "MUSIC_GAME"
    PLAYER_JUMP = "PLAYER_JUMP"
    PLAYER_DEATH = "PLAYER_DEATH"
    sounds = {}

    @staticmethod
    def preload():
        SoundManager.sounds = {
            SoundManager.ENEMY_WARNING: pygame.mixer.Sound(f"{ASSETS_SOUNDS}gasp.mp3"),
            SoundManager.ENEMY_SHOOT: pygame.mixer.Sound(f"{ASSETS_SOUNDS}scream.mp3"),
            SoundManager.MUSIC_INTRO: pygame.mixer.Sound(f"{ASSETS_SOUNDS}intro_music.mp3"),
            SoundManager.MUSIC_GAME: pygame.mixer.Sound(f"{ASSETS_SOUNDS}game_music.wav"),
            SoundManager.PLAYER_JUMP: pygame.mixer.Sound(f"{ASSETS_SOUNDS}jump.mp3"),
            SoundManager.PLAYER_DEATH: pygame.mixer.Sound(f"{ASSETS_SOUNDS}shout.mp3"),
        }

    def __init__(self):
        self.sounds = SoundManager.sounds

    def play(self, sound):
        self.sounds[sound].play()

    def stop(self, sound):
        self.sounds[sound].stop()
