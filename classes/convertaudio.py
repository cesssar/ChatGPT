import speech_recognition as sr

class ConvertAudio():

    def __init__(self) -> None:
        pass

    def converter(self) -> str:
        print("Faça sua pergunta por voz: ")
        try:
            microfone = sr.Recognizer()
            with sr.Microphone() as source:
                microfone.adjust_for_ambient_noise(source)
                audio = microfone.listen(source)
                try:
                    frase = microfone.recognize_google(audio, language='pt-BR')
                    return frase
                except:
                    return None
        except Exception as e:
            return None