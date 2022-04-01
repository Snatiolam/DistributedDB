#!/bin/env python3

import configparser
import json
import socket
import random
from colorama import Fore

from builtins import ConnectionRefusedError

PORT = 3338

def parseConfig(iniFile, operationType):
    config = configparser.ConfigParser()
    config.read(iniFile)
    # print("\n------ Parsing configurations file ------")
    if operationType == 'WRITE':
        sectionItems = dict(config.items('Master'))
    elif operationType == 'READ':
        sectionItems = dict(config.items('Master'))
        sectionItems.update(dict(config.items('Slaves')))
    else:
        return None            
    return sectionItems

def parseRequest(request):
    # print('\n------- Parsing request --------')
    strRequest = request.decode('utf-8')
    strRequest = strRequest.replace('\'', '\"')
    jsonRequest = json.loads(strRequest)
    # print(jsonRequest)
    return jsonRequest
    
def getServers(jsonRequest, iniFile):
    requestType = jsonRequest["type"]
    # print("Request type:", requestType)
    if requestType == "create" or requestType == "update" or requestType == "delete":
        operationType = "WRITE"
        print('WRITING TO SERVERS')
    elif requestType == "read":
        operationType = "READ"
        print('READING FROM SERVERS')
    # print("Operation type:", operationType)
    servers = parseConfig(iniFile, operationType)
    return servers

def getRandomServer(servers):
    serverNames = list(servers)
    return random.choice(serverNames)

def connectToServer(request, servers):
    while len(servers) > 0:
        randomServer = getRandomServer(servers)
        server = servers[randomServer]
        serverIp, serverSock = server.split(',')
        serverSock = int(serverSock)
        print(f"Connecting to {serverIp, serverSock}")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((serverIp, serverSock))
            sock.sendall(request)
            data = sock.recv(1024)
            sock.close()
            print(f"Closed connection to {serverIp, serverSock}")
            return data
        except ConnectionRefusedError:
            print("------------------------------------------")
            print(Fore.YELLOW + f"Warning: Server {serverIp, serverSock} is down")
            print(Fore.YELLOW + "Retrying connection with the other servers" + Fore.WHITE)
            print("------------------------------------------")
            servers.pop(randomServer)
    return None    