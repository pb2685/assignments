from socket import *
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("localhost", port))
    serverSocket.listen(1)

    while True:
        connectionSocket, addr = serverSocket.accept()

        try:

            try:
                message = connectionSocket.recv(5000).decode()
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = "HTTP/1.1 200 OK\r\n"
                connectionSocket.sendall(outputdata.encode())
                fcontent = f.read()
                f.close()
                outputdata = fcontent
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                errordata = "HTTP/1.1 404 Not Found\r\n"
                connectionSocket.sendall(errordata.encode())
                connectionSocket.close()
        except (ConnectionResetError, BrokenPipeError):
            pass
    serverSocket.close()
    sys.exit()


if __name__ == "__main__":
    webServer(13331)
