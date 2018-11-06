import vk_requests
from flask import Flask, request, json
from settings import *
import json

app = Flask(__name__)


#### KEYBOARD ####

def get_button(label, color, payload=""):
    return {
        "action":{
            "type":"text",
            "payload":json.dumps(payload),
            "label":label
        },
        "color":color
    }

keyboard = {
    "one_time":False,
    "buttons":{
        [
        get_button(label="New task", color="positive")
        get_button(label="Help", color="positive")
        ]
    }
}

# Вопрос иерархии открыт

keyboard = json.dumps(keyboard, ensure_ascii=False).encode("utf-8") #?
keyboard = str(keyboard.decode("utf-8")) #?


####

@app.route('/', methods=['POST'])
def processing():
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
        api.messages.send(access_token=token, user_id=str(user_id), message='Привет, я новый бот!')
        api.messages.send(access_token=token, user_id=str(user_id), message='Тык', keyboard=keyboard)
        vk.method
        # Сообщение о том, что обработка прошла успешно
        return 'ok'




    ##здесь могли бы быть ваши кнопки
#app.run() pythonanywhere автоматом дописывает эту строку, если вы разворачиваете на своем сервере
# то расскомитьте эту строку


