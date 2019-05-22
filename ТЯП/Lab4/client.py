import socket

sock = socket.socket()
sock.connect(('localhost', 9000))

print('Дата и время: ', sock.recv(1024).decode())
