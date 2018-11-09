# -*- coding: utf-8 -*-

import json

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

# | Новая задача | Список задач |
# | Cправка |
keyboard1 = {
    "one_time": False,
    "buttons": [
    [get_button(label="Новая задача", color="primary"), 
    get_button(label="Список задач", color="primary")],
    [get_button(label="Справка", color="default")]
    ]
}

# | Выполнено | Удалить |
# | Назад |
keyboard2 = {
    "one_time": False,
    "buttons": [
    [get_button(label="Выполнено", color="positive"), 
    get_button(label="Удалить", color="negative")],
    [get_button(label="Назад", color="default")]
    ]
}

keyboard1 = json.dumps(keyboard1, ensure_ascii=False)
keyboard2 = json.dumps(keyboard2, ensure_ascii=False)
