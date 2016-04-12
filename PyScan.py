import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

print"""
Python Port scanner -
Will scan port 1 - 1025
To change port range, change the source
"""
remoteServer    = raw_input("Enter an IP to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)


print "8" * 30
print "Please wait, scanning remote host", remoteServerIP
print "8" * 30


t1 = datetime.now()
try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "It's dead Jim!"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved'
    sys.exit()

except socket.error:
    print "Problem connecting to host"
    sys.exit()


t2 = datetime.now()


total =  t2 - t1


print 'Scanning Completed in: ', total
