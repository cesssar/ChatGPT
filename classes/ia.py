import os
import json
from openai import OpenAI
import warnings

warnings.simplefilter("ignore", DeprecationWarning)

class IA():

    def __init__(self, questao):
        self.questao = questao
        self.api_key = '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'

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