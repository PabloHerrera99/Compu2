#!/usr/bin/python3
import socket, os, sys
import signal


signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# get local machine name
#host = socket.gethostname()
host = ""
#port = int(sys.argv[1])
port = 50002

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()

    print("Connection from %s" % str(addr))

    msg = "Thank for connect"+ "\r\n"
    clientsocket.send(msg.encode('ascii'))
    try:
        child_pid = os.fork()
        if not child_pid:
            while True:
                msg = clientsocket.recv(1024)
                if not msg.decode():
                    break
                else:
                    data = msg.decode()
                    print("Received: %s" % data)
                    if data == "exit\r\n":
                        response = "\nBye\r\n".encode("utf-8")
                        clientsocket.send(response)
                        clientsocket.close()
                        print("The Client %s close the connection\r\n" % str(addr))
                        sys.exit(0)
                        
                    else:
                        msg = data.upper()+"\r\n"
                        clientsocket.send(msg.encode("utf-8"))

    except BrokenPipeError:
        print("The Client close the connection")

    clientsocket.close()