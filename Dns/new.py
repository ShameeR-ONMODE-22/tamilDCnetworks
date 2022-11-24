import socket
dnsDomain={
    '35.230.7.49':'ysyouthgct.in'
}

while True:
    print("\n1.-->To Find IP address by Url\n2.-->To Find Domain name by IP Address\nEnter Your Selection: ")
    option=eval(input())
    if option == 1:
        url=input("\nEnter the Url: ")
        ipname=socket.gethostbyname(url)
        print("The IP address for Requested URL is: ",ipname)
        dnsDomain.update({ipname:url})

    elif option == 2:
        ip=input("\nEnter the Ip address: ")
        host=socket.gethostbyaddr(ip)
        if host[2][0] in dnsDomain.keys():
            print("Dns Domain Name for the requested IP Address is: ",dnsDomain[host[2][0]])
    else :
        print("\n*-*-*-*End*-*-*-*")
        break