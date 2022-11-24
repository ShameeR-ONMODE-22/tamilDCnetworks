import socket
import http.server
import socketserver

Handler = http.server.SimpleHTTPRequestHandler
http = socketserver.TCPServer(("", 8100), Handler)

print("serving at port", 8100)
http.serve_forever()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",8100))
s.sendall('POST /HTTP/1.1\r\nHost: http://127.0.0.1:5500/index.html\r\n\r\n')