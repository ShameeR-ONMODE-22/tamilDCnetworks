import socket
dnsDomain={
    '35.230.7.49':'ysyouthgct.in'
}

while True:
    print("Enter your choice\n1.For ip address by name\n2.Domain name by ipAddress")
    choice=eval(input())
    if choice == 1:
        url=input("\nEnter the Url: ")
        ipname=socket.gethostbyname(url)
        print("Ip address :",ipname)
        dnsDomain.update({ipname:url})

    elif choice == 2:
        ip=input("\nEnter the Ip address: ")
        host=socket.gethostbyaddr(ip)
        # if host[3] in dnsDomain.keys():
        # print(dnsDomain[host[1]])
        # hostName=host[2]
        if host[2][0] in dnsDomain.keys():
            print("Dns Domain Name : ",dnsDomain[host[2][0]])
    else :
        print("\n********* Exiting the Program *********")
        break
