import FileHandler as file_handler

def process_request(variables_dict):
    if(variables_dict["type"] == "create"):
        response = create(variables_dict)
    elif(variables_dict["type"] == "read"):
        response = read(variables_dict)
    elif(variables_dict["type"] == "update"):
        response = update(variables_dict)
    elif(variables_dict["type"] == "delete"):
        response = delete(variables_dict)
    return response

def create(variables_dict):
    return file_handler.create(variables_dict["dbname"], variables_dict["table"], variables_dict["key"], variables_dict["values"])
    
def read(variables_dict):
    pass

def update(variables_dict):
    return file_handler.update(variables_dict["dbname"], variables_dict["table"], variables_dict["key"], variables_dict["new_values"])

def delete(variables_dict):
    return file_handler.delete(variables_dict["dbname"], variables_dict["table"], variables_dict["key"])
    