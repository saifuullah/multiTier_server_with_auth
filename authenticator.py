import socket
import pickle 
import random


ADDRESS = '127.0.0.1'
PORT = 5581

server = socket.socket()
server.bind((ADDRESS,PORT))

lst = [['saif', '123'], ['wisha', '321'], ['ali', '111']]

while(True):
    server.listen(10)

    cli, addr = server.accept()
    print("Client connected : " + str(addr))

    data = cli.recv(1024)
    data = pickle.loads(data)
    
    find = False
    for user in lst:
        if user[0] == data[0] and user[1] == data[1]:
            msg = "True"
            find = True
            token1 = random.randint(0, 898989)
            token2 = random.randint(0, 898989)
            token3 = random.randint(0, 898989)
            token4 = random.randint(0, 898989)
            token = token4 + token3 + token2 + token1
            d = [msg, token]
    if find == False:
        msg = "False"
        d = [msg]

    data = pickle.dumps(d)
    cli.send(data)
    cli.close()

