from classes.convertmp3 import *
from classes.ia import *
from classes.playsound import *
from classes.convertaudio import *

import os
from dotenv import load_dotenv

load_dotenv()
key = os.environ.get('KEY')

while True:
  os.system('cls' if os.name == 'nt' else 'clear')

  questao = ConvertAudio().converter()
  print(f'\nSua pergunta é: {questao}')
  print('\nFormulando resposta...')
  resposta = IA(questao, key).resposta()

  if resposta:
      print('\n')
      print(resposta)
      audio = ConvertMP3(resposta).converter()
      if audio:
          PlaySound(audio).play()

  input("\nPressione uma tecla para continuar...")
