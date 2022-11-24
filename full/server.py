import socket 
import time
import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',8001))
server.listen(1)
print("Server Up and Running")
conn,addr = server.accept()

print("Connection Accepted",addr)

def getmsg():
  while True:
    msg = conn.recv(1000).decode('utf-8')
    if msg=="exit":
     exit(1)
    print("Client: ",msg)
    time.sleep(0.5)

def sendmsg():
  while True:
    msg = input("")
    if msg=="exit":
     exit(1)
    conn.sendall(msg.encode())
    time.sleep(0.5)

thread1 = threading.Thread(target=getmsg)
thread1.start()

thread2 = threading.Thread(target=sendmsg)
thread2.start()
