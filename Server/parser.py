import configparser
import json
import socket
import random
import debug

from builtins import ConnectionRefusedError

PORT = 3338
INIFILE = "config.ini"

def parseConfig(iniFile, operationType):
    config = configparser.ConfigParser()
    config.read(iniFile)

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
    print(strRequest)
    jsonRequest = json.loads(strRequest)
    # print(jsonRequest)
    return jsonRequest
    
def getServers(jsonRequest, iniFile):
    requestType = jsonRequest["type"]
    
    if requestType == "create" or requestType == "update" or requestType == "delete":
        operationType = "WRITE"
        print('WRITING TO SERVERS')
    elif requestType == "read":
        operationType = "READ"
        print('READING FROM SERVERS')
    
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
        response = b''

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((serverIp, serverSock))
            debug.printSuccess(f"Connected to {serverIp, serverSock}")
            sock.sendall(request)
            response = sock.recv(1024)
            strResponse = response.decode('utf-8')
            jsonResponse = json.loads(strResponse)

            try:
                if jsonResponse["servers_errors"] == True:
                    failed_servers = jsonResponse["failed_servers"]

                    for server in failed_servers:
                        deleteServer(server)
                    print(failed_servers)
            except:
                debug.printError("Master server is not sending a valid response")

            sock.close()
            debug.printSuccess(f"Closed connection to {serverIp, serverSock}")
            break
        except ConnectionRefusedError:
            print("------------------------------------------")
            debug.printWarning(f"Warning: Server {serverIp, serverSock} is down")
            debug.printWarning("Trying connection with the other servers")
            print("------------------------------------------")
            servers.pop(randomServer)
            
    return response    

def deleteServer(server, iniFile=INIFILE):
    config = configparser.ConfigParser()
    config.read(iniFile)
    config.remove_option('Slaves', server)
    with open(iniFile, "w") as file:
        config.write(file)