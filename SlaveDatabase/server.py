import slave
import socket
import selectors
import types
import parser
import debug

sel = selectors.DefaultSelector()

HOST = "127.0.0.1"
PORT = 3338

sel = selectors.DefaultSelector()

def accept_wrapper(sock):
    conn, addr = sock.accept()
    debug.printSuccess(f"Accepted connection from {addr}")
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data.outb += recv_data
        else:
            debug.printWarning(f"Closing connection to {data.addr}")
            sel.unregister(sock)
            sock.close()

    if mask & selectors.EVENT_WRITE:
        if data.outb:
            jsonRequest = parser.parseRequest(data.outb)
            if(jsonRequest["type"] == "create"):
                result = slave.create(jsonRequest)
            elif(jsonRequest["type"] == "read"):
                result = slave.read(jsonRequest)
            elif(jsonRequest["type"] == "update"):
                result = slave.update(jsonRequest)
            elif(jsonRequest["type"] == "delete"):
                result = slave.delete(jsonRequest)
            print(result)
            sock.send(bytes(str(result), 'utf-8'))
            data.outb = b""   


def main():
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind((HOST, PORT))
    lsock.listen()
    debug.printSuccess(f"Listening on {(HOST, PORT)}")
    sel.register(lsock, selectors.EVENT_READ, data=None)

    try:
        while True:
            events = sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    accept_wrapper(key.fileobj)
                else:
                    service_connection(key, mask)
    except KeyboardInterrupt:
        debug.printWarning("Caught keyboard interrupt, exiting")
    finally:
        sel.close()

if __name__=="__main__":
    main()