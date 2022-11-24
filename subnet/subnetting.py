import ipaddress
ip = input("Enter the Ip address:")
mask = input("Enter the mask Address:")
result=ip+'/'+mask
print("Subnet mask:" ,result)
addr = ipaddress.ip_network(result,strict=False)
first,last=addr[0],addr[-1]
print("first address:" ,first)
print("last address:",last)
