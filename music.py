"""
Program : music.py
Author : Group 10
Analysis:
1. Manages the game's audio, including background music and sound effects.

Design - pseudocode:
1. Define the significant constant
   BGM_PATH, BGM_COLLISION_PATH, BGM_GAMEOVER_PATH: Paths to audio files.
2. The inputs are
   Triggers for playing background music, collision sound, and game over sound.
3. Computations:
   Initialize Pygame mixer for sound handling.
   Load sound files into Pygame mixer as Sound objects.
   Create sound channels for playing different sounds concurrently.
   Play background music in a loop.
   Play collision sound and game over sound while stopping background music when required.
4. The output is
   Playback of background music, collision sound, and game over sound during gameplay.
"""

import pygame

# Paths to the background music and sound effects
BGM_PATH = "assets/cute_song.mp3"
BGM_COLLISION_PATH = "assets/Collision.mp3"
BGM_GAMEOVER_PATH = "assets/Game_Over.mp3"

# Class representing the music player in the game
class Music:
    def __init__(self) -> None:
        # Initialize the Pygame mixer module for handling sound
        pygame.mixer.init()

        # Set the number of sound channels to 3 (background music, collision sound, game over sound)
        pygame.mixer.set_num_channels(3)

        # Load sound files into Pygame mixer as Sound objects
        self.bgm_sound = pygame.mixer.Sound(BGM_PATH)
        self.collision_sound = pygame.mixer.Sound(BGM_COLLISION_PATH)
        self.gameover_sound = pygame.mixer.Sound(BGM_GAMEOVER_PATH)

        # Create sound channels for playing different sounds concurrently
        self.bgm_channel = pygame.mixer.Channel(0)  # Channel for background music
        self.collision_channel = pygame.mixer.Channel(1)  # Channel for collision sound
        self.gameover_channel = pygame.mixer.Channel(2)  # Channel for game over sound

    # Method to play the background music in a loop
    def play_bgm(self):
        # Check if the background music channel is not currently playing
        if not self.bgm_channel.get_busy():
            # Start playing the background music in a loop
            self.bgm_channel.play(self.bgm_sound, loops=-1) # -1 indicates infinite loop

    # Method to play the collision sound and stop the background music
    def play_collision(self):
        # Check if the background music channel is currently playing
        if self.bgm_channel.get_busy():
            # Stop the background music
            self.bgm_channel.stop()

        # Start playing the collision sound
        self.collision_channel.play(self.collision_sound)

    # Method to play the game over sound and stop the background music
    def play_gameover(self):
        # Check if the background music channel is currently playing
        if self.bgm_channel.get_busy():
            # Stop the background music
            self.bgm_channel.stop()

        # Start playing the game over sound
        self.gameover_channel.play(self.gameover_sound)

# End of the Music class
