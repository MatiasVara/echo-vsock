# Usage: python3.7 ./echoserver.py [unix-socket path]
#
# This script just replies with the received content. Note
# that the socket path includes the port.
#
# e.g., ./echoserver.py /tmp/vm3.vsock_1234
#
import socket
import threading
import time
import sys

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.bind(sys.argv[1])
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
