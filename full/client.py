import socket
import time
import threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',8001))

def getmsg():
  while True:
    msg = client.recv(1000).decode('utf-8')
    if msg=="exit":
     exit(1)
    print("Server: ",msg)
    time.sleep(0.5)

def sendmsg():
  while True:
    msg = input("")
    if msg=="exit":
     exit(1)
    client.sendall(msg.encode())
    time.sleep(0.5)

thread2 = threading.Thread(target=sendmsg)
thread2.start()

thread1 = threading.Thread(target=getmsg)
thread1.start()
