# Usage: python3.7 ./echoserver.py [unix-socket path] [cpu]
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
import os
from subprocess import call

devnull = open(os.devnull, 'w')

pid = os.getpid()

try:
    call(['taskset', '-pc', str(sys.argv[2]), str(pid)], stdout=devnull)
except OSError:
    print(f"Error when pinning! {str(sys.argv[5])} {str(pid)}") #.format(vcpuid, cpuid)

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# remove link if it exist
try:
    os.unlink(sys.argv[1])
except OSError:
    if os.path.exists(sys.argv[1]):
        raise

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
