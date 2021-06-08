import socket
import pickle 
import time 


ADDRESS = '127.0.0.1'
PORT = 5500


addrMainServer = ('127.0.0.1', 5551)


server = socket.socket()
server.bind((ADDRESS,PORT))


while(True):
    server.listen(10)

    cli, addr = server.accept()
    print("Client connected : " + str(addr))

    data = cli.recv(1024)
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
        ln = len(string)

        print("String Length is : " + str(ln))
        ln = "Length Of string is " + ln
        data = pickle.dumps(ln)
        cli.send(data)
        cli.close()
    else:
        msg = "In Valid token...."
        msg = pickle.dumps(msg)
        cli.send(msg)





