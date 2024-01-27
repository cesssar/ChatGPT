import os
import json
from openai import OpenAI
import warnings

warnings.simplefilter("ignore", DeprecationWarning)

class IA():

    def __init__(self, questao, api_key):
        self.questao = questao
        self.api_key = api_key

    def resposta(self) -> str:
        try:
            client = OpenAI(
                api_key=self.api_key
            )
            completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                    {"role": "user", "content": self.questao}
                ]
            )
            resposta = completion.json()
            resposta = json.loads(resposta)
            return resposta['choices'][0]['message']['content']
        except Exception as e:
            print(e)
            return None