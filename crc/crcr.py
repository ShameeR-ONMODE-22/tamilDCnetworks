#RECEIVER:


import socket

def xor(a, b):
 result = []

 for i in range(1, len(b)):
  if a[i] == b[i]:
   result.append('0')
  else:
   result.append('1')

 return ''.join(result)


def mod2div(divident, divisor):

 pick = len(divisor)

 tmp = divident[0: pick]

 while pick < len(divident):

  if tmp[0] == '1':
   tmp = xor(divisor, tmp) + divident[pick]

  else: 
   tmp = xor('0'*pick, tmp) + divident[pick]

	
  pick += 1


 if tmp[0] == '1':
  tmp = xor(divisor, tmp)
 else:
  tmp = xor('0'*pick, tmp)

 checkword = tmp
 return checkword




def decodeData(data, key):

 l_key = len(key)


 appended_data = data.decode() + '0'*(l_key-1)
 remainder = mod2div(appended_data, key)

 return remainder


s = socket.socket()
print("Socket successfully created")


port = 12345

s.bind(('', port))
print("socket binded to %s" % (port))

s.listen(5)
print("socket is listening")


while True:

 c, addr = s.accept()
 print('Got connection from', addr)


 data = c.recv(1024)

 print("Received encoded data in binary format :", data.decode())

 if not data:
  break
 dat = data.decode()
 key = input("Enter divisor :")

 ans = decodeData(data, key)
 print("Remainder after decoding is->"+ans)

 dat = list(dat)
 val = input("Do u want to intorduce error(1) : ")
 print(val)
 if val == "1":
  err = int(input("Error index : "))
  if dat[len(dat)-err] == "1":
   dat[len(dat)-err] = "0"
  else:
   dat[len(dat)-err] = "1"

 dat = "".join(dat)

 #temp = "0" * (len(key) - 1)
 if dat == data.decode():
  c.sendto(("THANK you Data ->"+dat+
    " Received No error FOUND").encode(), ('127.0.0.1', 12345))
 else:
  c.sendto(("Error in data->"+dat).encode(), ('127.0.0.1', 12345))

 c.close()