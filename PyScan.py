import optparse
from socket import *
from threading import *
screenLock = Semaphore(value=1)
def connectScan(tgtHost, tgtPort):
	try:
		connectSocket = socket(AF_INET, SOCK_STREAM)
		connectSocket.connect((tgtHost, tgtPort))
		connectSocket.send('connect\r\n')
		results = connectSocket.recv(100)
		screenLock.acquire()
		print '[+]%d/tcp port open'% tgtPort
		print '[+] ' + str(results)
	except:
		screenLock.acquire()
		print '[-]%d/tcp port closed'% tgtPort
	finally:
		screenLock.release()
		connectSocket.close()
def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "[-] Unable to resolve '%s': Unknown host"%tgtHost
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print '\n[+] Scanned results for: ' + tgtName[0]
	except:
		print '\n[+] Scanned results for: ' + tgtIP
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connectScan, args=(tgtHost, int(tgtPort)))
		t.start()
def main():
	parser = optparse.OptionParser('usage PyScan.py ' + ' -H <target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', \
		help='Specify target host!')
	parser.add_option('-p', dest='tgtPort', type='string', \
		help='Specify target port or ports seperated by a comma')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(', ')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)
	portScan(tgtHost, tgtPorts)
if __name__ == "__main__":
	main()

