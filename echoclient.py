# Usage: python3.7 ./echoclient.py [cid] [samples] [name]
#
# latency is calculated as the half of the time elapsed between the sending and the reception
# SOCKSTREAM is not the best for latency but SOCKDGRAM is not supported yet
# 
# CID '2' is always the host
# e.g., ./echoclient.py 4 10000 guesttohost
#
import socket
import threading
import datetime
import sys
import statistics

max_latency = 0
values = []

for i in range(int(sys.argv[2])):
    s = socket.socket(socket.AF_VSOCK, socket.SOCK_STREAM)
    s.connect((int(sys.argv[1]), 1234))
    a = datetime.datetime.now()
    s.send(b'abcdefghijklmn1234');
    data = s.recv(1024).decode();
    b = datetime.datetime.now()
    c = b - a;
    max_latency = max(max_latency, c.microseconds / 2)
    values.append(c.microseconds / 2)    
    s.close();
f = open (sys.argv[3]+'.dat','w')
med = statistics.median(values);
for x in values:
    f.write(str((x - med) / med) + '\n');
f.close()
# plot using gnuplot
print("gnuplot -e \"set terminal png; set output '"+ sys.argv[3] + ".png';set xlabel 'latency, max=" + str(max_latency) + "us, median="+ str(med) + "us';set yzeroaxis;set boxwidth 0.05 absolute;set style fill solid 1.0 noborder;bin_width = 0.1;bin_number(x) = floor(x/bin_width);rounded(x) = bin_width * ( bin_number(x) + 0.5 ); show xlabel; set ylabel 'frecuency'; show ylabel; set title 'Latency in " + sys.argv[3] +  " (SOCKSTREAM)';set xrange [-3:3];set key off; plot '" + sys.argv[3] + ".dat' using (rounded(\$1)):(1) smooth frequency with boxes\"")
