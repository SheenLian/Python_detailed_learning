import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9991


client_socket.connect((host, port))

while True:
    try:
        msg = client_socket.recv(1024)
        message = msg.decode('ascii')
        if message == 'stop':
            client_socket.close()
            break
        else:
            print('Message received: ', message)
        reply = input('Enter message: ')
        if reply == 'stop':
            client_socket.sendall(reply.encode('ascii'))
            client_socket.close()
            break
        else:
            client_socket.sendall(reply.encode('ascii'))

    except ConnectionResetError:
        print('Connection lost')










