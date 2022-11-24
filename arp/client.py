
import json
import requests
url='http://ptsv2.com/t/3894f-1665744100/d/latest/json'
r=requests.get(url)
data=r.json()['FormValues']
for x in data:
  data[x] = data[x][0]
ip=input("Enter ip adddress:")
if ip in data.keys():
  print(data[ip])
else:
  print("ip address not found")
  mac=input("Enter corresponding mac address:")
  urlpost='http://ptsv2.com/t/3894f-1665744100/post'
  data[ip]=mac
  r=requests.post(urlpost,data=data)