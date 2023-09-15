# Usage: python3.7 ./echoserver-guest.py [port]
#
# This is a simple echo server that uses vsock. This script must run in the
# guest.
# e.g., ./echoserver-guest.py 1234
#
import socket
import threading
import time
import sys
import os

s = socket.socket(socket.AF_VSOCK, socket.SOCK_STREAM)
s.bind((socket.VMADDR_CID_ANY, int(sys.argv[1])))
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
