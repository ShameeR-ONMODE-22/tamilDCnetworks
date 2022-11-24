from email import message
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',8000))
print("Waiting for client")
while(1):
 data,address=s.recvfrom(1024)
 if(data.decode()=="exit"):
   print("client exited")
   break;
 print("Message from client side: ",data.decode())
 data1=str(input("enter message to send to client: "))

 s.sendto(str.encode(data1),address)
#  if(data1=="exit"):
#    print("client exited")
#    break;
 print("message sent")
