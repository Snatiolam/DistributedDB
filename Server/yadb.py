import socket

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
        data = self.sock.recv(1024)

    def get(self, key):
        json = {
            "dbname": self.dbname,
            "table": self.table,
            "type": "read",
            "key": key,
            } 
        jsonBytes = bytes(str(json), 'utf-8') 
        self.sock.sendall(jsonBytes)
        data = self.sock.recv(1024)

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
        data = self.sock.recv(1024)

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
        data = self.sock.recv(1024)

def connect(host, db):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, PORT))
    connection = Connection(sock, db)
    return connection