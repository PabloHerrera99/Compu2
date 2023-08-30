#!/usr/bin/python3
import socket, os, multiprocessing, sys

def mp_server(c):
    print("Launching proc...\n")
    sock, addr = c

    while True:
        msg = sock.recv(1024)
        if msg.decode() == '\r\n':
            pass
        else:
            data = msg.decode()
            print("Received: %s de %s" % (msg, addr))
            if data == "exit\r\n":
                response = "\nBye\r\n".encode("utf-8")
                sock.send(response)
                print("The Client %s close the connection\r\n" % str(addr))
                break
            else:
                msg = data.upper() + "\r\n"
                sock.send(msg.encode("utf-8"))

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# get local machine name
host = ""
port = 50001

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    cliente = serversocket.accept()

    clientsocket, addr = cliente

    print("Got a connection from %s" % str(addr))

    msg = 'Thank you for connecting' + "\r\n"
    clientsocket.send(msg.encode('ascii'))
    child = multiprocessing.Process(target=mp_server, args=(cliente,))
    child.start()

    clientsocket.close()