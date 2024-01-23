from classes.convertmp3 import *
from classes.ia import *
from classes.playsound import *
import os

while True:
  os.system('cls' if os.name == 'nt' else 'clear')

  questao = input("Faça sua pergunta: ")
  print("Formulando resposta...")
  resposta = IA(questao).resposta()

  if resposta:
      print('\n')
      print(resposta)
      audio = ConvertMP3(resposta).converter()
      if audio:
          PlaySound(audio).play()

  input("\nPressione uma tecla para continuar...")
