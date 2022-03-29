from sre_constants import FAILURE, SUCCESS
import os, errno


class FileHandler:

    def __init__(self, directory):
        self.directory = directory
    
    def create_update(self, file_name, content):
        try:
            file = open(self.directory + "/" + file_name, "wb")
            file.write(content)
            file.close()
            return SUCCESS
        except Exception as exception:
            return FAILURE

    def delete(self, file_name):
        try:
            if os.path.exists(self.directory + "/" + file_name):
                os.remove(self.directory + "/" + file_name)
                return "File deleted"
            return "File doesnt exist"
        except Exception as exception:
            return FAILURE

    def read(self, file_name):
        try:
            file = open(self.directory + "/" + file_name, "rb")
            content = file.read()
            file.close()
            return content
        except Exception as exception:
            return FAILURE
