import json
import os

import django
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryAPI.settings")
django.setup()

from django.conf import settings


def get_chat_id(bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    json_data = response.text
    dict_data = json.loads(json_data)
    result = dict_data["result"]
    last_update = max(result, key=lambda x: x["update_id"])
    chat = last_update["message"]["chat"]
    chat_id = chat["id"]
    return chat_id


if __name__ == "__main__":
    print(get_chat_id(settings.TELEGRAM_BOT_TOKEN))
