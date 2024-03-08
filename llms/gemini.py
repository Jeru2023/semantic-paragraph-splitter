import random

import google.generativeai as genai
import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Gemini:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(BASE_DIR, '../config/config.ini'), encoding="utf-8")
        self.api_key = self.config.get('gemini', "key").split(',')

        self.generation_config = genai.GenerationConfig(
            temperature=0,
            top_p=0,
            # top_k=1,
            max_output_tokens=2048
        )
        self.safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            }
        ]

    def generate(self, msg):
        cnt = 1
        while True:
            try:
                genai.configure(api_key=random.choice(self.api_key))
                model = genai.GenerativeModel(model_name="gemini-pro",
                                              generation_config=self.generation_config,
                                              safety_settings=self.safety_settings
                                              )
                response = model.generate_content(msg)
                return response.text
            except:
                if cnt > 5:
                    break
                continue
            else:
                break
        return []

    def generate_pre(self, msg):
        genai.configure(api_key=random.choice(self.api_key))
        model = genai.GenerativeModel(model_name="gemini-pro",
                                      generation_config=self.generation_config,
                                      safety_settings=self.safety_settings
                                      )
        response = model.generate_content(msg)
        return response.text


if __name__ == '__main__':
    # os.system("curl ip.sb")

    gemini = Gemini()
    msg = """
    请你判断[商品标题]是否是一个商品,如果是商品，请返回TRUE，不是商品返回FALSE.(tips: 如果只是商品规格,它不属于商品)
    不需要返回其他多余的文字描述。
    [商品标题] = [80g*2长效控油去屑洗发露]
    """
    print(gemini.generate(msg))
