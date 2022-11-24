
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('127.0.0.1',8000))

print("Waiting for client")

data,addr=s.recvfrom(1024)

print("The message is recieved from client and that is")

print(data.decode('utf-8'))
