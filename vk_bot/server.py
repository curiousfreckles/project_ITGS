import vk_requests
from flask import Flask, request, json
from settings import *
import json
from keyboard import keyboard1
from keyboard import keyboard2
from keyboard import keyboard_newtask
import bd_interaction
from shutil import rmtree
app = Flask(__name__)
@app.route('/', methods=['POST'])
def main():
    #Распаковываем json из пришедшего POST-запроса
    data = json.loads(request.data)
    #Вконтакте в своих запросах всегда отправляет поле типа
    api = vk_requests.create_api()
    user_id = data['object']['user_id']
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data["type"] == "group_join":
        bd_interaction.generate_person_bd(user_id)
        return "ok"
    elif data["type"] == "group_leave":
        rmtree(str(user_id))
        return "ok"
    elif data['type'] == 'message_new':
        if data["object"]["body"][0]=='0':
            name = data["object"]["body"][1:]
            bd_interaction.write_task(user_id,name,"days")
            return "ok"
        if data["object"]["body"][0]=='1':
            name = data["object"]["body"][1:]
            bd_interaction.write_task(user_id,name,"weeks")
            return "ok"
        if data["object"]["body"][0]=='2':
            name = data["object"]["body"][1:]
            bd_interaction.write_task(user_id,name,"mounth")
            return "ok"


        if data["object"]["body"]=="Новая задача":
            api.messages.send(access_token=token, user_id=str(user_id), message="Оп,занятой человек?", keyboard=keyboard_newtask)
        if data["object"]["body"]=="Сегодня":
            api.messages.send(access_token=token, user_id=str(user_id), message="Напиши цель задачи, но поставь для меня вначале сообщения символ '0'", keyboard=keyboard_newtask)
        if data["object"]["body"]=="Неделя":
            api.messages.send(access_token=token, user_id=str(user_id), message="Напиши цель задачи, но поставь для меня вначале сообщения символ '1'", keyboard=keyboard_newtask)
        if data["object"]["body"]=="Месяц":
            api.messages.send(access_token=token, user_id=str(user_id), message="Напиши цель задачи, но поставь для меня вначале сообщения символ '2'", keyboard=keyboard_newtask)
        if data["object"]["body"]=="Назад":
            api.messages.send(access_token=token, user_id=str(user_id), message="Ну и сиди без задач!", keyboard=keyboard1)
        if data["object"]["body"]=="Список задач":
            days = bd_interaction.get_tasks(user_id,"days")
            weeks = bd_interaction.get_tasks(user_id,"weeks")
            mounths= bd_interaction.get_tasks(user_id,"mounth")
            answer = "На день:\n"
            for i in days:
                answer+=i['name']+"\n"
            answer += "\n\nНа Неделю:\n"
            for i in weeks:
                answer+=i['name']+"\n"
            answer += "\n\nНа Месяц:\n"
            for i in mounths:
                answer+=i['name']+"\n"
            api.messages.send(access_token=token, user_id=str(user_id), message=answer, keyboard=keyboard1)


        # Сообщение о том, что обработка прошла успешно
    return 'ok'
    ##здесь могли бы быть ваши кнопки
#app.run() pythonanywhere автоматом дописывает эту строку, если вы разворачиваете на своем сервере
# то расскомитьте эту строку
