import socket
import pickle 
import time


ADDRESS = '127.0.0.1'
PORT = 5577

server = socket.socket()
server.bind((ADDRESS,PORT))

addrMainServer = ('127.0.0.1', 5551)

while(True):
    server.listen(10)

    cli, addr = server.accept()
    print("Client connected : " + str(addr))
    data = cli.recv(1024)
    usr = data
    data = pickle.loads(data)


    token = data[0]
    string = data[1]

    s = socket.socket()
    s.connect(addrMainServer)
    th = ['tokenValidation', token]
    tk = pickle.dumps(th)
    s.send(tk)

    time.sleep(1)
    data = s.recv(1024)
    data = pickle.loads(data)
    if data == True:
        cli.send(usr[1])
    else:
        print("Data recived : " + pickle.loads(data))
        msg = "In Valid token...."
        msg = pickle.dumps(msg)
        cli.send(msg)


