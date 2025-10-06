# sound from pixabay sound
import time 
import pygame
def BG_Sound():
    pygame.mixer.init()
    pygame.mixer.music.load("fur-elise-music-box-70375.mp3")
    pygame.mixer.music.play(-1)
def stop_BG_Sound():
    pygame.mixer.music.stop()
BG_Sound()

