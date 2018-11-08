import os
import datetime
import json

def generate_person_bd(id):
    id = str(id)
    now = datetime.datetime.now()
    root_directory = os.getcwd() #запомним корень всей БД чтобы вернуться в нее
    os.mkdir(id)
    os.chdir(id)
    os.mkdir(str(now.month))
    os.chdir(str(now.month))
    weeks_db = open('weeks.json','a')
    #weeks_write() #штука которая запишет каркас файла
    weeks_db.close()
    days_db = open('days.json','a')
    #days_write() #штука которая запишет каркас файла
    days_db.close()
    mounth_db = open('mounth.json','a')
    #mounth_write() #штука которая запишет каркас файла
    mounth_db.close()
    os.chdir(root_directory)

def write_task(id,name,type_task):
    id = str(id)
    os.chdir(id)
    os.chdir(str(now.month))
    now = datetime.datetime.now()
    root_directory = os.getcwd()
    task = {"name":name,"result":0}

    if type_task == "day":
        days_db = open('days.json','r').read()
        json_pars = json.loads(days_db)
        json_pars[str(now.day)].append(task)
        days_db = open('days.json','w').write(json.dumps(json_pars))
        os.chdir(root_directory)

    elif type_task == "week":
        weeks_db = open('weeks.json','r').read()
        json_pars = json.loads(weeks_db)
        json_pars[str(now.isoweekday)].append(task)
        days_db = open('weeks.json','w').write(json.dumps(json_pars))
        os.chdir(root_directory)

    else:
        mounth_db = open('mounth.json','r').read()
        json_pars = json.loads(mounth_db)
        json_pars[0].append(task)
        mounth_db = open('mounth.json','w').write(json.dumps(json_pars))
        os.chdir(root_directory)

def get_tasks(id,type_task):
        tasks = ""
        id = str(id)
        now = datetime.datetime.now()
        root_directory = os.getcwd()
        os.chdir(id)
        os.chdir(str(now.month))

        if type_task == "day":
            days_db = open('days.json','r').read()
            json_pars = json.loads(days_db)[str(now.day)]
            os.chdir(root_directory)
            return json_pars

        elif type_task == "week":
            weeks_db = open('weeks.json','r').read()
            json_pars = json.loads(weeks_db)[str(now.isoweekday)]
            os.chdir(root_directory)
            return json_pars

        else:
            mounth_db = open('mounth.json','r').read()
            json_pars = json.loads(mounth_db)
            os.chdir(root_directory)
            return json_pars
