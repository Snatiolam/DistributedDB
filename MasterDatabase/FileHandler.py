import json
from sre_constants import FAILURE, SUCCESS
import os, errno

def create(database, table, key, values):
    dir = os.getcwd()
    os.chdir("DataBases")
    try:
        if os.path.exists(database):
            os.chdir(database)
            if os.path.exists(table):
                os.chdir(table)
                keys_file = open("index.json", "r+")
                file_content = keys_file.read()
                json_keys = json.loads(file_content)
                if key in json_keys:
                    return json.dumps({"status": 409, "message": "Key already exists"})
                json_keys[key] = files_for_values(key, values)
                keys_file.seek(0)
                keys_file.write(json.dumps(json_keys))
                keys_file.truncate()
                keys_file.close()
            else:
                os.mkdir(table)
                os.chdir(table)
                values_array = files_for_values(key, values)
                keys_file = open("index.json", "w")
                keys_file.write(json.dumps({key: values_array}))
                keys_file.close()
        else:
            os.mkdir(database)
            os.chdir(database)
            os.mkdir(table)
            os.chdir(table)
            values_array = files_for_values(key, values)
            keys_file = open("index.json", "w")
            keys_file.write(json.dumps({key: values_array}))
            keys_file.close()
        return json.dumps({"status": 200, "message": "Success"})
    except Exception as exception:
        return json.dumps({"status": 500, "message": " Unexpected Error"})
    finally:
        os.chdir(dir)

def update(file_name, content):
    try:
        file = open(directory + "/" + file_name, "wb")
        file.write(content)
        file.close()
        return SUCCESS
    except Exception as exception:
        return FAILURE
def delete(file_name):
    try:
        if os.path.exists(directory + "/" + file_name):
            os.remove(directory + "/" + file_name)
            return "File deleted"
        return "File doesnt exist"
    except Exception as exception:
        return FAILURE

def read(file_name):
    try:
        file = open(directory + "/" + file_name, "rb")
        content = file.read()
        file.close()
        return content
    except Exception as exception:
        return FAILURE

def files_for_values(key, values):
    if(type(values) == str):
        values = values.split(",")
    print(values)
    print(type(values))
    value_count = 0
    values_array = list()
    for value in values:
        file_name = key + str(value_count) + ".txt"
        value_file = open(file_name, "w")
        value_file.write(value)
        value_file.close()
        values_array.append(file_name)
        value_count += 1
    return values_array