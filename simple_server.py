from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try :
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5)
        while True:
            (clientsocket, _) = serversocket.accept()

            read_data = clientsocket.recv(5000).decode()
            splitted_data = read_data.split('\n')
            if (len(splitted_data) > 0):
                print(splitted_data[0])
            
            data = 'HTTP/1.1 200 OK\r\n'
            data += 'Content-Type: text/html; charset=utf-8\r\n'
            data += '\r\n'
            data += '<html><body>Hello World</body></html>\r\n'
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt :
        print('\nShutting down ...')
    except Exception as exc :
        print('Error:\n')
        print(exc)
    serversocket.close()

print('Access http://loclhost:9000')
createServer()