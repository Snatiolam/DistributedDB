import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3337  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    json = {
        "type": "create",
        "key": "ciudad",
        "value": "New York"
        }  
    json = bytes(str(json), 'utf-8') 
    s.sendall(json)
    #data = s.recv(1024)

#print(f"Received {data!r}")