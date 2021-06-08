import socket
import pickle 
import time


addrMainServer = ('127.0.0.1', 5551)



ADDRESS = '127.0.0.1'
PORT = 5578

server = socket.socket()
server.bind((ADDRESS,PORT))


def isPalindrome(s):
    my_str = s

    # make it suitable for caseless comparison
    my_str = my_str.casefold()

    # reverse the string
    rev_str = reversed(my_str)

    # check if the string is equal to its reverse
    if list(my_str) == list(rev_str):
        return "The string is a palindrome."
    else:
        return "The string is not a palindrome."

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
        msg = isPalindrome(string)
        data = pickle.dumps(msg)
        cli.send(data)
        cli.close()

    else:
        msg = "In Valid token...."
        msg = pickle.dumps(msg)
        cli.send(msg)



