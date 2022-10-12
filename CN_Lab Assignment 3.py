#Write an chatting application based on the following :
a. Connection oriented Client server applications with TCP.
b. Connectionless Client server applications with UDP.

#Server_1 TCP:

import socketserver

class Handler_TCPServer(socketserver.BaseRequestHandler):
   

    def handle(self):
        # self.request - TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} sent:".format(self.client_address[0]))
        print(self.data)
        # just send back ACK for data arrival confirmation
        self.request.sendall("ACK from TCP Server".encode())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Init the TCP server object, bind it to the localhost on 9999 port
    tcp_server = socketserver.TCPServer((HOST, PORT), Handler_TCPServer)

    # Activate the TCP server.
    # To abort the TCP server, press Ctrl-C.
    tcp_server.serve_forever()
    
#Client_1 TCP:
    
  import socket

host_ip, server_port = "127.0.0.1", 9999
data = " Hello how are you?\n"


tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  
    tcp_client.connect((host_ip, server_port))
    tcp_client.sendall(data.encode())

   
    received = tcp_client.recv(1024)
finally:
    tcp_client.close()

print ("Bytes Sent:     {}".format(data))
print ("Bytes Received: {}".format(received.decode()))
