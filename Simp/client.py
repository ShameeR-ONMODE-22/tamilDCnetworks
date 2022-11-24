
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
b=str.encode("Hi server")

s.sendto(b,('127.0.0.1',8000))
print("Message sent")
