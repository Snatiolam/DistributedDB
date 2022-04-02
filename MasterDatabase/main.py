import configparser

FILE = "config.ini"

config = configparser.ConfigParser()
config.read(FILE)
config.remove_option('Slaves', "server2")
file = open(FILE, "w")
config.write(file)
file.close()

config2 = configparser.ConfigParser()
config2.read(FILE)
config2.remove_option('Slaves', "server4")
file = open(FILE, "w")
config2.write(file)
file.close()