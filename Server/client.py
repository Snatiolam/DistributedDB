from shelve import DbfilenameShelf
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3337  # The port used by the server

class Connection():
    def __init__(self, sock, dbname):
        self.dbname = dbname
        self.sock = sock

    def close(self):
        self.sock.close()

    def get(self, tableName):
        table = Table(self.sock, self.dbname, tableName)
        return table

class Table(Connection):
    def __init__(self, sock, dbname, table):
        super().__init__(sock, dbname)
        self.table = table

    def put(self, key, value):
        json = {
            "dbname": self.dbname,
            "table": self.table,
            "type": "create",
            "key": key,
            "value": value
            } 
        jsonBytes = bytes(str(json), 'utf-8') 
        self.sock.sendall(jsonBytes)

    def get(self, key):
        json = {
            "dbname": self.dbname,
            "table": self.table,
            "type": "read",
            "key": key,
            } 
        jsonBytes = bytes(str(json), 'utf-8') 
        self.sock.sendall(jsonBytes)

    def delete(self, key, value):
        json = {
            "dbname": self.dbname,
            "table": self.table,
            "type": "delete",
            "key": key,
            "value": value,
            } 
        jsonBytes = bytes(str(json), 'utf-8') 
        self.sock.sendall(jsonBytes)

    def update(self, key, oldval, newval):
        json = {
            "dbname": self.dbname,
            "table": self.table,
            "type": "update",
            "key": key,
            "oldVal": oldval,
            "newVal": newval,
            } 
        jsonBytes = bytes(str(json), 'utf-8') 
        self.sock.sendall(jsonBytes)

def connect(host, db):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, PORT))
    connection = Connection(sock, db)
    return connection


# Ejemplo

myConnection = connect(HOST, 'MyDB')
myTable = myConnection.get("Tabla Prueba")
# myTable.put("key1", "algun dato simple o complejo")
# myTable.get("key1")
# myTable.delete("key1", "value 1")
myTable.update("key1", "old val", "new val")
myTable.close()
#print(f"Received {data!r}")
