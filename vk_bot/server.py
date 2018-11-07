import vk_requests
from flask import Flask, request, json
from settings import *
import json

app = Flask(__name__)

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

@app.route('/', methods=['POST'])
def main():
    keyboard = {
        'one_time': False,
        'buttons': [[get_button(label="Список задач", color="positive"), get_button(label="Новая задача", color="negative"),
        get_button(label="Приступить сейчас", color="primary"),
        get_button(label="Справка", color="default")
        ]]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    #Распаковываем json из пришедшего POST-запроса
    data = json.loads(request.data)
    #Вконтакте в своих запросах всегда отправляет поле типа
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        api = vk_requests.create_api()
        user_id = data['object']['user_id']
        #api.messages.send(access_token=token, user_id=str(user_id), message='Привет, я новый бот!')
        api.messages.send(access_token=token, user_id=str(user_id), message='Тык', keyboard=keyboard)
        # Сообщение о том, что обработка прошла успешно
        return 'ok'




    ##здесь могли бы быть ваши кнопки
#app.run() pythonanywhere автоматом дописывает эту строку, если вы разворачиваете на своем сервере
# то расскомитьте эту строку
