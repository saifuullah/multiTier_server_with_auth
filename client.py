import socket
import pickle
import time


ADDRESS = '127.0.0.1'
PORT = 5551

cli = socket.socket()
cli.connect((ADDRESS,PORT))


while(True):
    
    
    uname = input("Enter your username : ")
    passw = input("Enter your password : ")

    print("\nSelect your service.....\n")
    print("1. For Echo your message")
    print("2. For Palendrome check")
    print("3. For LENGTH of string")

    choice = int(input("Choice :  ") )
    

    data = [uname, passw, choice]

    data = pickle.dumps(data)
    cli.send(data)
    
    time.sleep(2)

    data = cli.recv(1024)
    data = pickle.loads(data)

    if data[0] == False:
        print("Invalid user credientials....\n")
    elif data[0] == True:
        token = data[1]
        port = data[2]

        s = socket.socket()
        s.connect((ADDRESS, port))

        if choice == 1:
            msg = input("Enter your ECHO message : ")
        elif choice == 2:
            msg = input("Enter your string for palendrome check : ")
        elif choice == 3:
            msg = input("Enter string for checking its length : ")
        m = [token, msg]
        data = pickle.dumps(m)
        s.send(data)
        time.sleep(2)
        data = s.recv(1024)
        data = pickle.loads(data)

        print(data)

    break
