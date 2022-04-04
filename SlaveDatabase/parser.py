import json
import debug

def parseRequest(request):
    strRequest = request.decode('utf-8')
    strRequest = strRequest.replace('\'', '\"')
    debug.printSuccess('\n------- Parsing request --------')
    print(strRequest)
    jsonRequest = json.loads(strRequest)
    return jsonRequest