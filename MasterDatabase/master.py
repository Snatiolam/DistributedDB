import parser
import json
import database_handler as database

def create(variables_dict):
    servers_errors, failed_servers = parser.connectToServer(variables_dict)
    response = database.create(variables_dict["dbname"], variables_dict["table"], variables_dict["key"], variables_dict["values"])
    response["failed_servers"] = failed_servers
    response["servers_errors"] = servers_errors
    return json.dumps(response) 

def read(variables_dict):
    response = database.read(variables_dict["dbname"], variables_dict["table"], variables_dict["key"])
    response["server"] = "127.0.0.1:3340 (Master)"
    return json.dumps(response)
    
def update(variables_dict):
    servers_errors, failed_servers = parser.connectToServer(variables_dict)
    response = database.update(variables_dict["dbname"], variables_dict["table"], variables_dict["key"], variables_dict["new_values"])
    response["failed_servers"] = failed_servers
    response["servers_errors"] = servers_errors
    return json.dumps(response) 

def delete(variables_dict):
    servers_errors, failed_servers = parser.connectToServer(variables_dict)
    response = database.delete(variables_dict["dbname"], variables_dict["table"], variables_dict["key"])
    response["failed_servers"] = failed_servers
    response["servers_errors"] = servers_errors
    return json.dumps(response) 
