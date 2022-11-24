import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while(1):

 message=input("enter message to send to server: ")
 s.sendto(str.encode(message),('localhost',8000))
 if(message=="exit"):
   print("exited")
   break;
 print("message sent")
 data,address=s.recvfrom(1000)
#  if(data.decode()=="exit"):
#    print("exited")
#    break;
 print("Response from server side is: ",data.decode())
