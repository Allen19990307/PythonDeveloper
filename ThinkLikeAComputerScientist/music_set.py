import os
import time
import pygame
file = r'/Users/allen/Desktop/Adele-Make You Feel My Love.mp3'
def worker(file):
    if not os.path.exists(file):
        print("File does not exist")
    pygame.mixer.init()
    track = pygame.mixer_music.load(file)
    while pygame.mixer.music.get_busy()==0:
          pygame.mixer_music.play(loops=4)
    time.sleep(30)
    pygame.sleep(30)

if __name__ == '__main__':
   worker(file)