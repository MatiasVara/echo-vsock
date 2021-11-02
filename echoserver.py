# Usage: python3.7 ./echoserver.py
# This is just an echo server
import socket
import threading
import time

s = socket.socket(socket.AF_VSOCK, socket.SOCK_STREAM)
s.bind((socket.VMADDR_CID_ANY, 1234))
s.listen();

try:
    while True:
        client, addr = s.accept()
        data = client.recv(1024)
        client.send(data)
        client.close
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    s.close()
