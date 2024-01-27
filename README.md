# Voz e Audição ao ChatGPT 

> Utiliza bibliotecas Python para transformar voz em texto, perguntar ao ChatGPT e devolver a resposta em texto e voz.

## 💻 Pré-requisitos

Python 3.10 (testado nesta versão)


## 🚀 Preparando ambiente para execução

Preferencialmente criar um ambiente virtual para instalar as bibiliotecas isoladamente do resto do sistema operacional.

''
python -m venv venv

''
Consulte como criar e ativar em: https://docs.python.org/pt-br/3/tutorial/venv.html
Instalar as bibliotecas necessárias para execução do projeto:

''
pip install -r requirements.txt

''

## 🚀 Executar

Para executar o projeto, digitar na linha de comando:

''
python main.py

## Possíveis erros

1. Caso de erro com a biblioteca urllib executar comandos abaixo

''
pip uninstall urllib3
pip install 'urllib3<2.0'
''

2. Captura de audio pelo microfone seguir passos do link abaixo

https://realpython.com/python-speech-recognition/

Para macOS

brew install portaudio
pip install pyaudio