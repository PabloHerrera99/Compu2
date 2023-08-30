#!/usr/bin/python3
import socket, os, threading

def th_server(sock):
    print("Launching thread...")
    
    while True:
        msg = sock.recv(1024)
        if msg.decode() == '\r\n':
            pass
        else:
            data = msg.decode()
            print("Received: %s" % data)
            if data == "exit\r\n":
                response = "\nBye\r\n".encode("utf-8")
                sock.send(response)
                print("The Client close the connection\r\n")
                sock.close()
                break
            else:
                msg = data.upper() + "\r\n"
                sock.send(msg.encode("utf-8"))

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# get local machine name
#host = socket.gethostname()
host = ""
port = 50001

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))

    msg = 'Thank you for connecting'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))
    th = threading.Thread(target=th_server, args=(clientsocket,))
    th.start()