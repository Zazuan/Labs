import socket
from time import localtime, strftime

sock = socket.socket()

sock.bind(('', 9000))
sock.listen(1)
conn, addr = sock.accept()

print("connected", addr)


def time():
    return strftime("%d.%m.%Y %H:%M:%S", localtime())


conn.send(str(time()).encode())
