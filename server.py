import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
print(host)
port = 9991
server_socket.bind((host,port))

server_socket.listen(2)
client_socket , addr = server_socket.accept()
print('Got a connection from %s' % str(addr))
while True:

    msg = input('Enter your message: ')
    client_socket.send(msg.encode('ascii'))
    re = client_socket.recv(1024)
    if re.decode('ascii') == 'stop':
        server_socket.close()
        break
    else:
        print('message received: ', re.decode('ascii'))



