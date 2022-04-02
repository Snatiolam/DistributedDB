import configparser
import json
import socket
import random
import debug
from builtins import ConnectionRefusedError
import os

PORT = 3338

FILE = "config.ini"

def parseRequest(request):
    # print('\n------- Parsing request --------')
    strRequest = request.decode('utf-8')
    strRequest = strRequest.replace('\'', '\"')
    print(strRequest)
    jsonRequest = json.loads(strRequest)
    # print(jsonRequest)
    return jsonRequest

def getSlavesServers():
    config = configparser.ConfigParser()
    config.read(FILE)
    servers = dict(config.items('Slaves'))
    return servers

def connectToServer(request):
    request = bytes(str(request), 'utf-8') 
    servers = getSlavesServers()
    servers_errors = False
    failed_servers = list()
    for key, server in servers.items():
        serverIp, serverSock = server.split(',')
        serverSock = int(serverSock)
        response = b''

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((serverIp, serverSock))
            debug.printSuccess(f"Connected to {serverIp, serverSock}")
            sock.sendall(request)
            response = sock.recv(1024)
            print("Response:", response)
            sock.close()
            debug.printSuccess(f"Closed connection to {serverIp, serverSock}")

        except ConnectionRefusedError:
            servers_errors = True
            failed_servers.append(key)
            deleteServer(key)
            debug.printError(f"Connection refused to {key, serverIp, serverSock}")
            
    return servers_errors, failed_servers

def deleteServer(server):
    config = configparser.ConfigParser()
    config.read(FILE)
    config.remove_option('Slaves', server)
    file = open(FILE, "w")
    config.write(file)
    file.close()