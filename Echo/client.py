import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',8001))
print("Requesting server to send date and time")
data=s.recv(1024)
print("date and time from server")
print(data.decode())
