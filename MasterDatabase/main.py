import sys
from FileHandler import FileHandler 

def main():
    file = open(sys.argv[1], 'rb')
    image = file.read()
    file_handler = FileHandler("database")
    #result = file_handler.create_update("test1.jpeg", image)
    #result = file_handler.delete("test1.jpeg")
    print(file_handler.read("test1.jpeg"))
    #print(result)

if __name__ == "__main__":
    main()