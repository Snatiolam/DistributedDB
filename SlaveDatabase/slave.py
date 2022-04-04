import json
import database_handler as database

def create(variables_dict):
    response = database.create(variables_dict["dbname"], variables_dict["table"], variables_dict["key"], variables_dict["values"])
    return json.dumps(response) 

def read(variables_dict):
    response = database.read(variables_dict["dbname"], variables_dict["table"], variables_dict["key"])
    response["server"] = "127.0.0.1:3338 (Slave1)"
    return json.dumps(response)    
def update(variables_dict):
    response = database.update(variables_dict["dbname"], variables_dict["table"], variables_dict["key"], variables_dict["new_values"])
    return json.dumps(response) 

def delete(variables_dict):
    response = database.delete(variables_dict["dbname"], variables_dict["table"], variables_dict["key"])
    return json.dumps(response) 
