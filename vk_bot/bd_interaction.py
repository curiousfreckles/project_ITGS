import os
import datetime
import json
import year_info

def change_result(id,mounth,type_task,name):
    root_directory = os.getcwd()
    os.chdir(str(id))
    os.chdir(str(mounth))



def write_templates():
    for num,mounth in enumerate(year_info.info):
        num=str(num+1)
        os.mkdir(num)
        os.chdir(num)

        weeks_db = open('weeks.json', 'w')
        json_db = []
        for i in range(mounth[num]['weeks']):
            json_db.append({str(i+1):[]})
        weeks_db.write(json.dumps(json_db))
        weeks_db.close()

        days_db = open('days.json', 'w')
        json_db = []
        for i in range(mounth[num]['days']):
            json_db.append({str(i+1):[]})
        days_db.write(json.dumps(json_db))
        days_db.close()

        mounth_db = open('mounth.json', 'w').write(json.dumps([]))
        os.chdir("..")

def generate_person_bd(id):
    id = str(id)
    now = datetime.datetime.now()
    root_directory = os.getcwd()  # запомним корень всей БД чтобы вернуться в нее
    os.mkdir(id)
    os.chdir(id)
    write_templates()
    os.chdir(root_directory)


def write_task(id, name, type_task):
    id = str(id)
    root_directory = os.getcwd()
    now = datetime.datetime.now()
    os.chdir(id)
    os.chdir(str(now.month))
    now = datetime.datetime.now()
    task = {"name": name, "result": 0}

    if type_task == "day":
        days_db = open('days.json', 'r').read()
        json_pars = json.loads(days_db)
        json_pars[now.day-1][str(now.day)].append(task)
        days_db = open('days.json', 'w').write(json.dumps(json_pars))
        os.chdir(root_directory)

    elif type_task == "week":
        weeks_db = open('weeks.json', 'r').read()
        json_pars = json.loads(weeks_db)
        json_pars[now.day // 7-1][str(now.day // 7)].append(task)
        days_db = open('weeks.json', 'w').write(json.dumps(json_pars))
        os.chdir(root_directory)

    else:
        mounth_db = open('mounth.json', 'r').read()
        json_pars = json.loads(mounth_db)
        json_pars.append(task)
        mounth_db = open('mounth.json', 'w').write(json.dumps(json_pars))
        os.chdir(root_directory)


def get_tasks(id, type_task):
    tasks = ""
    id = str(id)
    now = datetime.datetime.now()
    root_directory = os.getcwd()
    os.chdir(id)
    os.chdir(str(now.month))

    if type_task == "day":
        days_db = open('days.json', 'r').read()
        json_pars = json.loads(days_db)[now.day-1][str(now.day)]
        os.chdir(root_directory)
        return json_pars

    elif type_task == "week":
        weeks_db = open('weeks.json', 'r').read()
        json_pars = json.loads(weeks_db)[now.day // 7-1][str(now.day //7)]
        os.chdir(root_directory)
        return json_pars

    else:
        mounth_db = open('mounth.json', 'r').read()
        json_pars = json.loads(mounth_db)
        os.chdir(root_directory)
        return json_pars
