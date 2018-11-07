import os
import datetime
import json

def generate_person_bd(id):
    id = str(id)
    now = datetime.datetime.now()
    root_directory = os.getcwd()
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
    now = datetime.datetime.now()
    root_directory = os.getcwd()
    task = {"name":name,"result":0}

    if type_task == "day":
        os.chdir(id)
        os.chdir(str(now.month))
        days_db = open('days.json','r').read()
        json_pars = json.loads(days_db)
        print(json_pars)
        print(now.day)
        json_pars[str(now.day)].append(task)
        days_db = open('days.json','w').write(json.dumps(json_pars))
        os.chdir(root_directory)

    elif type_task == "week":
        os.chdir(id)
        os.chdir(str(now.month))
        weeks_db = open('weeks.json','r').read()
        json_pars = json.loads(weeks_db)
        json_pars[str(now.isoweekday)].append(task)
        days_db = open('weeks.json','w').write(json.dumps(json_pars))
        os.chdir(root_directory)

    else:
        os.chdir(id)
        os.chdir(str(now.month))
        mounth_db = open('mounth.json','r').read()
        json_pars = json.loads(mounth_db)
        json_pars[str(now.isoweekday)].append(task)
        mounth_db = open('mounth.json','w').write(json.dumps(json_pars))
        os.chdir(root_directory)
