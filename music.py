import pygame

BGM_PATH = "assets/cute_song.mp3"
BGM_COLLISION_PATH = "assets/Collision.mp3"
BGM_GAMEOVER_PATH = "assets/Game_Over.mp3"


class Music:
    def __init__(self) -> None:
        pygame.mixer.init()
        pygame.mixer.set_num_channels(3)

        self.bgm_sound = pygame.mixer.Sound(BGM_PATH)
        self.collision_sound = pygame.mixer.Sound(BGM_COLLISION_PATH)
        self.gameover_sound = pygame.mixer.Sound(BGM_GAMEOVER_PATH)

        self.bgm_channel = pygame.mixer.Channel(0)
        self.collision_channel = pygame.mixer.Channel(1)
        self.gameover_channel = pygame.mixer.Channel(2)

    def play_bgm(self):
        if not self.bgm_channel.get_busy():
            self.bgm_channel.play(self.bgm_sound, loops=-1)

    def play_collision(self):
        if self.bgm_channel.get_busy():
            self.bgm_channel.stop()
        self.collision_channel.play(self.collision_sound)

    def play_gameover(self):
        if self.bgm_channel.get_busy():
            self.bgm_channel.stop()
        self.gameover_channel.play(self.gameover_sound)
