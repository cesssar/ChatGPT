from pygame import mixer
from time import sleep

class PlaySound():

    def __init__(self, texto):
        self.texto = texto

    def play(self):
        mixer.init()
        mixer.music.load('audio.mp3')
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            sleep(1)