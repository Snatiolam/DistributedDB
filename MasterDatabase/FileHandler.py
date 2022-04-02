import json
import os

DIR = os.getcwd()

def create(database, table, key, values):
    os.chdir(DIR + "/DataBases")

    try:

        if os.path.exists(database):
            os.chdir(database)

            if os.path.exists(table):
                os.chdir(table)
                keys_file = open("index.json", "r+")
                file_content = keys_file.read()
                json_keys = json.loads(file_content)

                if key in json_keys:
                    os.chdir(DIR)
                    return {"status": 409, "message": "Key already exists"}

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

        os.chdir(DIR)
        return {"status": 200, "message": "Success"}
    except Exception as exception:
        os.chdir(DIR)
        return {"status": 500, "message": " Unexpected Error"}

def delete(database, table, key):
    os.chdir(DIR + "/DataBases")

    try:

        if os.path.exists(database):
            os.chdir(database)

            if os.path.exists(table):
                os.chdir(table)
                keys_file = open("index.json", "r+")
                file_content = keys_file.read()
                json_keys = json.loads(file_content)

                if key in json_keys:
                    for fileName in json_keys[key]:
                        os.remove(fileName) 
                    json_keys.pop(key)
                    keys_file.seek(0)
                    keys_file.write(json.dumps(json_keys))
                    keys_file.truncate()
                    keys_file.close()
                    os.chdir(DIR)
                    return {"status": 204, "message": "Resource Deleted"}

                os.chdir(DIR)
                return {"status": 404, "message": "Key Not Found"}

            os.chdir(DIR)
            return {"status": 404, "message": "Table Not Found"}

        os.chdir(DIR)
        return {"status": 404, "message": "Database Not Found"}
    except Exception as exception:
        os.chdir(DIR)
        return {"status": 500, "message": " Unexpected Error"}

def update(database, table, key, new_values):
    os.chdir(DIR + "/DataBases")

    try:

        if os.path.exists(database):
            os.chdir(database)

            if os.path.exists(table):
                os.chdir(table)
                keys_file = open("index.json", "r+")
                file_content = keys_file.read()
                json_keys = json.loads(file_content)

                if key in json_keys:
                    for fileName in json_keys[key]:
                        os.remove(fileName) 
                    json_keys[key] = files_for_values(key, new_values)
                    keys_file.seek(0)
                    keys_file.write(json.dumps(json_keys))
                    keys_file.truncate()
                    keys_file.close()
                    os.chdir(DIR)
                    return {"status": 201, "message": "Modification Successful"}

                os.chdir(DIR)
                return {"status": 404, "message": "Key Not Found"}
            os.chdir(DIR)
            return {"status": 404, "message": "Table Not Found"}
        os.chdir(DIR)
        return {"status": 404, "message": "Database Not Found"}
    except Exception as exception:
        os.chdir(DIR)
        return {"status": 500, "message": " Unexpected Error"}


def read(database, table, key):
    os.chdir(DIR + "/DataBases")

    try:

        if os.path.exists(database):
            os.chdir(database)

            if os.path.exists(table):
                os.chdir(table)
                keys_file = open("index.json", "r+")
                file_content = keys_file.read()
                json_keys = json.loads(file_content)

                if key in json_keys:
                    values_array = list()
                    for fileName in json_keys[key]:
                        file = open(fileName)
                        content = file.read()
                        values_array.append(content)
                        file.close()
                    keys_file.close()
                    os.chdir(DIR)
                    return {"status": 200, "message": "Succesfull", "values": values_array}

                os.chdir(DIR)
                return {"status": 404, "message": "Key Not Found"}

            os.chdir(DIR)
            return {"status": 404, "message": "Table Not Found"}

        os.chdir(DIR)
        return {"status": 404, "message": "Database Not Found"}
    except Exception as exception:
        os.chdir(DIR)
        return {"status": 500, "message": " Unexpected Error"}

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