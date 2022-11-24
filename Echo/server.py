import socket
from datetime import datetime
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8001))
s.listen(1)
print("waiting for client")
conn,addr=s.accept()
data=datetime.now()
print("sent date and time to client")
conn.sendall(str(data).encode())
s.close()
