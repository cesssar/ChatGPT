from pygame import mixer
from time import sleep

class PlaySound():

    def __init__(self, texto):
        self.texto = texto

    def play(self):
        mixer.pre_init(44100, -16, 1, 512)
        mixer.init()
        mixer.music.load('audio.mp3')
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            sleep(1)