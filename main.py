import pygame
from main_menu import Menu

BGM_PATH = "assets/cute_song.mp3"

pygame.mixer.init()
pygame.mixer.music.load(BGM_PATH)
pygame.mixer.music.play(-1)

main_app = Menu()
main_app.mainloop()

pygame.mixer.music.stop()
