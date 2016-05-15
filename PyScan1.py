import socket
import subprocess
import sys
from datetime import datetime
import os

subprocess.call('clear', shell=True)

print"""
Python Port scanner -
Will scan common ports
To change port range, change the source in the list!
"""
remoteServer    = raw_input("Enter an IP to scan: ")# User input to select IP
remoteServerIP  = socket.gethostbyname(remoteServer)# Get host name
host = socket.gethostbyaddr(remoteServerIP)

print " " * 30
print "Please wait, scanning remote host", remoteServerIP
print " " * 30

pList = [15, 20, 21, 22, 23, 24, 25, 26, 53, 66, 67, 68, 80, 88, 109, 110, 118, 130, 131, 132, 135, 137, 138, 139, 464, 543, 545, 767,  8080, 443]
t1 = datetime.now()
try:
    for port in list(pList):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:            
            s=socket.socket()  
            s.connect((remoteServerIP,port))  
            banner = s.recv(1024)  
            print "**********************************************"
            print "Port {} is Open".format(port)
            print "Hostname is: ", host
            print "Service on port is: ", banner
            print "**********************************************"
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
