from gtts import gTTS

class ConvertMP3():

    def __init__(self, texto):
        self.texto = texto

    def converter(self) -> str:
        try:
            audio = gTTS(text=self.texto, lang='pt', slow=False)
            audio.save('audio.mp3')
            return 'audio.mp3'
        except Exception as e:
            return None