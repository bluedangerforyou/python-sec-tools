import os
import optparse
import mechanize
import urllib
import re
import urlparse
from _winreg import *

def val2addr(val):
	addr = ''
	for ch in val:
		addr += '%02x '% ord(ch)
	addr = addr.strip(' ').replace(' ', ':')[0:17]
	return addr
def wiglePrint(username, password, netid):
	browser = mechanize.Browser()
	browser.open('http://wigle.net')
	reqData = urllib.urlencode({'credential_0': username, 'credential_1': password})
	browser.open("https://wiglenet.net//gps/gps/main/login", reqData)
	params = {}
	params['netid'] = netid
	reqParams = urllib.urlencode(params)
	respURL = 'http://wigle.net/gps/gps/main/confirmquery/'
	resp = browser.open(respURL, reqParams).read()
	mapLat = 'N/A'
	mapLon = 'N/A'
	rLat = re.findall(r'maplat=.*\&', resp)
	if rLat:
		mapLat = rLat[0].split('&')[0].split('=')[1]
	rLon = re.findall(r'maplon=.*\&', resp)
	if rLon:
		mapLon = rLon[0].split
		print '[-] Lat: ' + mapLat + ', Lon: ' + mapLon
				
def printNets():
	net = "SOFTWARE\MICROSOFT\WINDOWS NT\CurrentVersion"+\
		"\NetworkList\Signatures\Unmanaged"
	key = OpenKey(HKEY_LOCAL_MACHINE, net)
	print '\n[-] Wifi Networks Joined:'
	for i in range(100):
		try:
			guid = EnumKey(key, i)
			netkey = OpenKey(key, str(guid))
			(n, addr, t) = EnumValue(netKey, 5)
			(n, name, t) = EnumValue(netKey, 4)
			macAddr = val2addr(addr)
			netName = str(name)
			print '[+] ' + netName + ' ' + macAddr
			CloseKey(netKey)
		except:
			break
def main():
	printNets()
if __name__ == "__main__":
	main()
