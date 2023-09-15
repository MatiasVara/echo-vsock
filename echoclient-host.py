# Usage: python3.7 ./echoclient-host.py [unix-sock path] [port] [samples] [name]
# Run this in the host to measure latency when communicating to guest.
#
import socket
import threading
import datetime
import sys
import statistics

max_latency = 0
values = []

for i in range(int(sys.argv[3])):
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.connect(str(sys.argv[1]))
    message = 'CONNECT ' + str(sys.argv[2]) +'\n'
    s.sendall(message.encode())
    # TODO: to check if is OK
    data = s.recv(1024).decode();
    a = datetime.datetime.now()
    s.send(b'abcdefghijklmn1234');
    data = s.recv(1024).decode();
    b = datetime.datetime.now()
    c = b - a;
    max_latency = max(max_latency, c.microseconds)
    values.append(c.microseconds)
    s.close();
f = open (sys.argv[4]+'.dat','w')
med = statistics.median(values);
for x in values:
    f.write(str((x - med) / med) + '\n');
f.close()
# plot using gnuplot
print("gnuplot -e \"set terminal png; set output '"+ sys.argv[4] + ".png';set xlabel 'latency, max=" + str(max_latency) + "us, median="+ str(med) + "us';set yzeroaxis;set boxwidth 0.05 absolute;set style fill solid 1.0 noborder;bin_width = 0.1;bin_number(x) = floor(x/bin_width);rounded(x) = bin_width * ( bin_number(x) + 0.5 ); show xlabel; set ylabel 'frecuency'; show ylabel; set title 'Latency in " + sys.argv[4] +  " (SOCKSTREAM)';set xrange [-3:3];set key off; plot '" + sys.argv[4] + ".dat' using (rounded(\$1)):(1) smooth frequency with boxes\"")
