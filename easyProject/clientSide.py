# Client side script
# Host: python 3.2

import socket 
ip = str(input('Type ip of connection'))
port = 7000 
addr = ((ip,port)) 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect(addr) 
mensagem = input('Type a message for to send at server').encode()
client_socket.send(mensagem) 
print('message sended') 
client_socket.close()