from django.conf import settings
import requests
from django.forms import ValidationError


class GptService:

    def __init__(self):
        self.__model = settings.GPT_MODEL
        self.__open_ai_api_key = settings.OPEN_AI_API_KEY
        self.__open_ai_base_url = settings.OPEN_AI_BASE_URL

    def get_chat_completion(self, messages):
        payload = {
            "model": self.__model,
            "messages": [self.__convert_to_chat_message_format(message) for message in messages]
        }
        headers = {
            "Authorization": f"Bearer {self.__open_ai_api_key}"
        }
        response = requests.post(
            f"{self.__open_ai_base_url}/chat/completions",
            json=payload,
            headers=headers,
        )

        # obtendo o corpo da resposta convertendo em dicionário python
        body = response.json()

        try:
            if body["error"]:
                raise ValidationError(body["error"]["message"])
        except:
            pass

        return body["choices"][0]["message"]["content"]

    def __convert_to_chat_message_format(self, message):
        return {
            'role': message.role,
            'message': message.content
        }
