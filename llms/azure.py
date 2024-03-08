import openai
from loguru import logger



class Azure:

    def __init__(self, api_version, api_key, api_base, engine):
        openai.api_version = api_version
        openai.api_type = "azure"
        openai.api_key = api_key
        openai.api_base = api_base
        self.engine = engine

    def azure_ask(self, messages):
        for response in openai.ChatCompletion.create(
                engine=self.engine,
                messages=[{"role": m["role"], "content": m["content"]} for m in messages],
                stream=True,
                temperature=0.0,
                # n=2,
                top_p=0.0,
        ):
            full_response = response.choices[0].delta.get("content", "")
            yield full_response

    def generate(self, messages):
        response = openai.ChatCompletion.create(
            engine=self.engine,
            messages=[{"role": "user", "content": messages}],
            temperature=0.0,
            top_p=0.0,
        )
        if response.choices[0].message.get("content", None) is None:
            logger.error(response)
        return response.choices[0].message.get("content", None)
