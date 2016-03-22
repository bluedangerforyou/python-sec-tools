from _winreg import *

def val2addr(val):
	addr=''
	for ch in val:
		addr+='%02x '%ord(ch)
	addr=addr.strip(' ').replace(' ',':')[0:17]
	return addr
def printNetworks():
	net= "SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
	key=OpenKey(HKEY_LOCAL_MACHINE,net,0,KEY_READ | KEY_WOW64_64KEY)
	print '\n[*] Networks that have been connected: '
	for i in range(100):
		try:
			guid=EnumKey(key,i)
			netKey=OpenKey(key,str(guid))
			(n,addr,t)=EnumValue(netKey,5)
			(n,name,t)=EnumValue(netKey,4)
			macAddr=val2addr(addr)
			netName=str(name)
			print '[+] '+netName+' '+macAddr
			CloseKey(netKey)
		except Exception,e:
			print e
			exit(0)
def main():
	printNetworks()

if __name__=='__main__':
	main()
