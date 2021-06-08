from math import trunc
from random import choice
import socket
import pickle
from sys import flags
import time




ADDRESS = '127.0.0.1'
PORT = 5551

server = socket.socket()
server.bind((ADDRESS,PORT))

server1 = (ADDRESS , 5577)
server2 = (ADDRESS , 5578)
server3 = (ADDRESS , 5500)
server4 = (ADDRESS , 5581)

TOKENS = []

server.listen(10)
print("Listening.........")

while (True):
    
    cli, addr = server.accept()
    print("Client connected on: ", addr)


    user = cli.recv(1024)
    data = pickle.loads(user)
    if data[0] == 'tokenValidation':
        token = data[1]
        if token in TOKENS:
            msg = True
        else:
            msg = False
        msg = pickle.dumps(msg)
        cli.send(msg)
    else:
        uname = data[0]
        passw = data[1]
        choice = data[2]

        s4 = socket.socket()
        s4.connect(server4)
        s4.send(user)

        data = s4.recv(1024)
        data = pickle.loads(data)

        if data[0] == "False":
            flag = False
            msg = "In valid User Credientials"
            lst = [flag, msg]

            data = pickle.dumps(lst)
            cli.send(data)

        elif data[0] == "True":
            TOKENS.append(data[1])
            if choice == 1:
                port = 5577
            elif choice == 2:
                port = 5578
            elif choice == 3:
                port = 5500

            flag = True
            lst = [flag, data[1], port]
            data = pickle.dumps(lst)
            cli.send(data)